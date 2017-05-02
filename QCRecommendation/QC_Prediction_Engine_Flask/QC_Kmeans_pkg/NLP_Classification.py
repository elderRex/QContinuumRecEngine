'''
    This package supports:
        a.training model based on the nlp block
'''
import sys
import os
import itertools
from math import sqrt
from operator import add
from os.path import join, isfile, dirname
from utility_pkg import item_presentation as ip
from utility_pkg import test_case_generate as tcg
import numpy as np
import algo_pkg.softmax as sf
import collections
import datetime
from utility_pkg import util as uti

import db_initialization as dbi


os.environ['SPARK_HOME'] = "/home/ygu16/srv/spark_a/spark-2.0.2-bin-hadoop2.7"
sys.path.append("/home/ygu16/project/server_scripts/")

import QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing.NLPtagger as nlpt
import QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing.NLPblock as nlpb
import QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing.NLPmain as nlpm
import findspark

findspark.init()

# Now we are ready to import Spark Modules
try:
    from pyspark import SparkConf, SparkContext
    from pyspark.mllib.clustering import KMeans,KMeansModel
    from pyspark.mllib.recommendation import ALS
    from pyspark.mllib.classification import SVMWithSGD
    from pyspark.mllib.regression import LabeledPoint

    print ("Good riddance. Pyspark is now onboard.")

except ImportError as e:
    print ("Error importing Spark Modules", e)
    sys.exit(1)

PLACE_HOLDER='PLACE_HOLDER'

def data_retriever(target='0'):
    mydb = dbi.mydb()
    conn = mydb.engine.connect()

    try:
       test_reviews = conn.execute("select r.*,u.subject from qc.reviews r, qc.items u where r.iid = u.id")
    except Exception:
        return (-1,-1)
    conn.close()

    return test_reviews.fetchall()

def data_prep():
    return

def train_feature_extraction(tmp,c_tag,blc,util):
    feature = []
    #print tmp
    nltk_fet = blc.feature_extration(tmp[3],c_tag)
    feature.append(tmp[2])
    for fet  in nltk_fet.keys():
        feature.append(nltk_fet[fet])
    #print util.types
    if not tmp[-1]:
        tp = PLACE_HOLDER
    else:
        tp = tmp[-1]
    feature.append(util.types[tp])
    return feature

def assert_len(dataset):
    tlen = len(dataset[0])
    for x in dataset:
        #print tlen,len(x)
        #print dataset[0],x
        assert len(x) == tlen

def kmeans_classification(sc,c_tag,util):
    print 'data retrieving'
    _data_ = data_retriever(c_tag)
    print len(_data_)
    #rids = [x[0] for x in _data_]

    blc = nlpb.nlpblockbase()

    __ans = [train_feature_extraction(x,c_tag,blc,util) for x in _data_]
    ans = [[float(k) for k in x] for x in __ans]
    #print ans
    train_data = [np.array(sf.softmax(x)) for x in ans]
    #train_data = ans
    print 'dataprep done'
    assert_len(train_data)
    brotrain = sc.broadcast(train_data)
    clusters = KMeans.train(sc.parallelize(brotrain.value), 200, maxIterations=10, initializationMode="random")

    def error(point):
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x ** 2 for x in (point - center)]))

    WSSSE = map(lambda point: error(point), train_data)
    WSSSE = reduce(lambda x, y: x + y, WSSSE)
    print("Within Set Sum of Squared Error = " + str(WSSSE))

    clustered = collections.defaultdict(list)
    print len(_data_)
    cnt = 0
    for row in _data_:
        clustered[clusters.predict(train_data[cnt])].append([row[0],row[2],row[3],row[4]])
        cnt += 1
    print len(clustered)
    for k in clustered.keys():
        print len(clustered[k])

    clusters.save(sc, "MovieModel")
    sameModel = KMeansModel.load(sc, "MovieModel")

    ref = collections.defaultdict(list)
    for point in train_data:
        ref[sameModel.predict(point)].append(point)

    for x,y in zip(ref.keys(),clustered.keys()):
        assert len(ref[x]) == len(clustered[y])

    return clustered

def my_test(sc,util,data):
    dat = tcg.tc_gen(100)

    train_data = [np.array(sf.softmax(x)) for x in dat]
    clusters = KMeans.train(sc.parallelize(train_data), 20, maxIterations=10, initializationMode="random")

    def error(point):
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x ** 2 for x in (point - center)]))

    WSSSE = map(lambda point: error(point),train_data)
    WSSSE = reduce(lambda x, y: x + y,WSSSE)
    print("Within Set Sum of Squared Error = " + str(WSSSE))

    clustered = collections.defaultdict(list)

    for i, point in enumerate(train_data):
        clustered[clusters.predict(point)].append(dat[i][0])
    #print len(train_data)
    print clustered.keys()
    return clustered

def loader():
    myutil = uti.utility()
    res = myutil.collection_loader()
    return res

def saver(cols):

    myutil = uti.utility()

    myutil.collection_saver(cols)
    '''
    res = myutil.collection_loader()
    print 'loaded'
    for k in res.keys():
        print k,res[k]
    '''
    return

def recommendation(target,c_tag,util,sc,data_stash):

    train,test = nlpm.data_retriever(target)

    '''
        Logic
            Retrieve user answer
    '''
    '''
        Likes holds the liked reviews
        If none is selected as like,
            Top 3 highest rating among all dislikes will be chosen as like
    '''
    Likes = []
    for x in train:
        if x[1] == '1':
            Likes.append(x)
    if len(Likes) == 0:
        dislikes = sorted(train,key=lambda x:x[4],reverse=True)
        Likes = dislikes[:3]

    blc = nlpb.nlpblockbase()
    print len(Likes)
    __ans = [train_feature_extraction(x[2:], c_tag, blc, util) for x in Likes]
    ans = [[float(k) for k in x] for x in __ans]
    # print ans
    train_data = [np.array(sf.softmax(x)) for x in ans]

    sameModel = KMeansModel.load(sc, "MovieModel")

    #pre_classified = loader()
    targets = []
    for i,point in enumerate(train_data):
        #cluster,rating,reviews,iid
        targets.append([sameModel.predict(point),Likes[i][4],Likes[i][5],Likes[i][6]])
    #print 'tar',targets

    '''
        Retrieve Corresponding List as potential recommendation
    '''
    __retrieved__ = []
    for k in targets:
        for item in data_stash[str(k[0])]:
            __retrieved__.append((item,k[1],k[2],k[3]))
    #print 'ret',__retrieved__
    '''
        Give More Weights to the reviews that are closer to the one user likes

        Weight = sum(softmax(Rating(this_review),Rating(Parent_review),distance(this_review,parent_review))
    '''
    #blc.feature_extration(tmp[3], c_tag)
    #__retrieved__ = sorted(__retrieved__,key=lambda x:sum(sf.softmax([x[0][2],x[1],blc.distance(blc.feature_extration(x[0][3]),blc.feature_extration(x[2])]))),reverse=True)
    weighted = []
    for x in __retrieved__:
        #print len(x),len(x[0]),x[1],x[2]
        pre = []
        pre.append(float(x[0][1]))
        pre.append(float(x[1]))
        v1,v2 = [],[]
        fet1 = blc.feature_extration(x[0][2],c_tag)
        fet2 = blc.feature_extration(x[2],c_tag)

        for k in fet1.keys():
            v1.append(fet1[k])
            v2.append(fet2[k])

        pre.append(blc.distance(v1,v2))
        #print pre
        weight = sum(sf.softmax(pre))
        weighted.append((weight,x[0][0]))
    weighted = sorted(weighted,key=lambda x:x[0],reverse=True)

    ans = []
    marker = 100
    for k in range(len(weighted)):
        if k > 100:
            break
        #print weighted[k]
        ans.append(weighted[k])
    #print ans
    items = get_iid_from_rid(ans)

    res = [(str(1),str(x[0])) for x in items]

    nlpm.cache_result(res, str(target))
    print res
    return res

def get_iid_from_rid(rids):
    query = "("
    query = query + str(rids[0][1])
    for rid in rids:
        query = query + ","+str(rid[1])
    query += ")"
    mydb = dbi.mydb()
    conn = mydb.engine.connect()

    this_query = "select distinct(i.id) from qc.items i, qc.reviews r where r.iid = i.id and r.id in "
    print this_query+query
    try:
       items = conn.execute(this_query+query)
    except Exception:
        return (-1,-1)
    conn.close()

    return items.fetchall()


def nlp_cla_rec(sc,mode=0,target=0,data_stash=-1):
    util = ip.util()
    util.load()
    # set up environment
    data = [0]

    st = datetime.datetime.now()

    c_tagger = nlpt.nlp_tagger()
    #c_tagger.train()
    res = []
    print 'Elapsed Time For Tagger:', (datetime.datetime.now() - st).total_seconds(), 's'
    if not mode:
        #__collection=my_test(sc,util,data)
        #saver(__collection)
        print 'KMEANS'
        __collection = kmeans_classification(sc,c_tagger, util)
        #print __collection
        saver(__collection)
        ans = loader()
        for k in ans.keys():
            print len(ans[k])
    else:
        '''
            In this section:
                Load user data
                predict cluster
                retrieve corresponding cluster
                find
                a. TOP 5 rated rid
                b. TOP 5 closest rid
                return combined item for recommendation
        '''
        res = recommendation(target,c_tagger,util,sc,data_stash)
    ed = datetime.datetime.now()

    print 'Elapsed Time :', (ed - st).total_seconds(), 's'
    # clean up
    #sc.stop()
    return res

#if __name__ == "__main__":
    #nlp_cla_rec(0)
    #stash = loader()
    #nlp_cla_rec(1,149,stash)
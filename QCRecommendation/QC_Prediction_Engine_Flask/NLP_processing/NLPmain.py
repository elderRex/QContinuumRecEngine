import nltk as nlt
import collections
import QCRecommendation.QC_Prediction_Engine_Flask.db_initialization as dbi
import QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing.NLPblock as nlpb
import os.path
import sys,os
import json
import csv

'''
    Function:
    1. establish DB connection
    2. read items (business) and reviews from DB
    3. create training sets
'''

def data_retriever(target):
    mydb = dbi.mydb()
    conn = mydb.engine.connect()
    #print 'nlpm',target,"select a.uid,a.does_like,b.*,c.subject FROM qc.user_answers a, qc.reviews b, qc.items c where a.rid = b.id and a.uid = '"+str(target)+"' and b.iid=c.id"
    try:
        train_reviews = conn.execute("select a.uid,a.does_like,b.*,c.subject FROM qc.user_answers a, qc.reviews b, qc.items c where a.rid = b.id and a.uid = '"+str(target)+"' and b.iid=c.id").fetchall()
        test_reviews = conn.execute("select r.*,u.subject from qc.reviews r, qc.items u where r.iid = u.id and r.id not in(select rid from qc.user_answers where uid = '"+str(target)+"') limit 10").fetchall()
    except Exception:
        return (-1,-1)
    if not len(train_reviews) or not len(test_reviews):
        return (-2,-2)
    conn.close()

    return train_reviews,test_reviews

def main_func(target,tagger):

    train_reviews,test_reviews = data_retriever(target)
    #create processing block
    blc = nlpb.nlpblockbase()
    blc.set_params(target)
    if not blc.load_model():
        for row in train_reviews:
            #print row[0],row[2]
            #item,label
            blc.answers.append((row[1],row[2]))
        blc.train(tagger)
        #blc.save_model()
    #print [y for (x,y) in blc.answers]
    #for row in test_reviews:
        #print row
        #blc.batch_test.append((row[0],row[2],row[3],row[4],row[7]))
    #print blc.batch_test
    #print blc.answers

    rec = blc.predict(tagger)
    #print rec

    result = collections.defaultdict(list)

    for (rec,text,iid) in rec:
        result[iid].append((rec,text))

    answer = []

    def test(mylist):
        cnt,tmp = 0,[]
        for (x,y) in mylist:
            if x == 1:
                cnt += 1
                #tmp.append([y])
        if cnt > 2:
            return 1
        return 0

    for key in result:
        answer.append((test(result[key]),key))
    for i in range(5):
        print answer[i]
    cache_result(answer,target)
    return answer

def cache_result(data,uid):
    __pat = os.path.dirname(os.path.abspath(__file__))
    fname = __pat + '/saved_results/cache' + uid + ".csv"
    with open(fname,'w+') as outfile:
        fieldnames = ['rec', 'iid']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow({'rec':str(item[0]),'iid':str(item[1])})
    return 1

def load_result(uid):
    __pat = os.path.dirname(os.path.abspath(__file__))
    fname = __pat + '/saved_results/cache' + uid + ".csv"
    print fname
    data = []
    if os.path.exists(fname):
        print 'found'
        with open(fname) as data_file:
            csvreader = csv.DictReader(data_file)
            for row in csvreader:
                data.append((row['rec'],row['iid']))
    return data
'''
main_func('king.kong@kg.com')
main_func('Mr.Spock@ms.com')
main_func('luke.cage@lc.com')
done
'''
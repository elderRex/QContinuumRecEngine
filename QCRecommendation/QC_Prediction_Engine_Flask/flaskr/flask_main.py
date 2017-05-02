import os
import csv
import sys
import json
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response,url_for,send_from_directory
from flask_cors import CORS,cross_origin

#print sys.path
sys.path.append("/home/ygu16/project/server_scripts")

os.environ['SPARK_HOME'] = "/home/ygu16/srv/spark_a/spark-2.0.2-bin-hadoop2.7"
sys.path.append("/home/ygu16/project/server_scripts/")

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
#print sys.path
from QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing import NLPmain as nlpm
from QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing import NLPtagger as nlpt
import QCRecommendation.QC_Prediction_Engine_Flask.db_initialization as dbi
from QCRecommendation.QC_Prediction_Engine_Flask.QC_Kmeans_pkg import NLP_Classification as nlpc

#db initialization

c_tagger = nlpt.nlp_tagger()
pre_classified = nlpc.loader()

app = Flask(__name__)
CORS(app)

conf = SparkConf() \
        .setAppName("MovieLensALS") \
        .set("spark.executor.memory", "2g")
sc = SparkContext(conf=conf)

@app.route('/recommend_now/query',methods=['POST'])
def Game_visualization_query_foo():
    userid = request.form.get('uid')
    #print 'html'+userid
    #ans = nlpm.load_result(userid)
    stash = nlpc.loader()
    ans = nlpc.nlp_cla_rec(sc,1, userid, stash)

    print json.dumps(ans, ensure_ascii=False)
    return render_template('index.html',gdata = ans)

@app.route('/recommend/query',methods=['POST'])
def recommend_foo():
    userid = request.form.get('uid')
    #print 'query' + userid
    #ans = nlpm.load_result(userid)
    stash = nlpc.loader()
    ans = nlpc.nlp_cla_rec(sc,1,userid,stash)

    print json.dumps(ans,ensure_ascii=False)
    return json.dumps(ans,ensure_ascii=False)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True,threaded=True)

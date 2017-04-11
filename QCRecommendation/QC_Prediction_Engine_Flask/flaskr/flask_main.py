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
#print sys.path
from QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing import NLPmain as nlpm
from QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing import NLPtagger as nlpt
import QCRecommendation.QC_Prediction_Engine_Flask.db_initialization as dbi

#db initialization

c_tagger = nlpt.nlp_tagger()
c_tagger.train()


app = Flask(__name__)
CORS(app)


@app.route('/recommend_now/query',methods=['POST'])
def Game_visualization_query_foo():
    userid = request.form.get('uid')
    print 'html'+userid
    ans = nlpm.load_result(userid)
    if not ans:
        print 'not loaded'
        ans = nlpm.main_func(str(userid),c_tagger)
    else:
        print 'loaded'
    return render_template('index.html',gdata = ans)

@app.route('/recommend/query',methods=['POST'])
def recommend_foo():
    userid = request.form.get('uid')
    print 'query' + userid
    ans = nlpm.load_result(userid)
    if not ans:
        print 'not loaded'
        ans = nlpm.main_func(str(userid),c_tagger)
    else:
        print 'loaded'
    return json.dumps(ans)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
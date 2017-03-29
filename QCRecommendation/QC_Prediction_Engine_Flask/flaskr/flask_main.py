import os
import csv
import sys
import json
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response,url_for,send_from_directory

#print sys.path
sys.path.append("/home/ygu16/project/server_scripts")
#print sys.path
from QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing import NLPmain as nlpm


app = Flask(__name__)

@app.route('/recommend_now/query',methods=['POST'])
def Game_visualization_query_foo():
    userid = request.form.get('uid')
    ans = nlpm.main_func(str(userid))
    return render_template('index.html',gdata = ans)

@app.route('/recommend/query',methods=['POST'])
def recommend_foo():
    userid = request.form.get('uid')
    ans = nlpm.main_func(str(userid))
    return json.dumps(ans)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
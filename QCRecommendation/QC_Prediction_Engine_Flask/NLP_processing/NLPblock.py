'''
    Defines the fundemental of the nlp processing
    the class holds:
        1. userid
        2. user labeled review
        3. user trained model

    nlpblockbase(@username,@pulling_type,@db_name)

    The class supports:
        1. feature extraction
        2. classification
'''
from QCRecommendation.QC_Prediction_Engine_Flask import db_initialization as dbi
from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
import nltk
import collections
import pickle
import os.path
import sys,os

class nlpblockbase:

    def __init__(self):
        self.user_id = ""
        self.answers = [] #used for training
        self.batch_test = []
        self._path = os.path.dirname(os.path.abspath(__file__))
        #{1:'adfsaf',0:'asdfsdf'...} 1 like 0 dislike
        self.model = None

    def set_params(self,name):
        self.user_id = name

    def train(self,tagger):

        featursets = [(self.feature_extration(n,tagger),like) for (n,like) in self.answers]
        print featursets
        try:
            self.model = SklearnClassifier(BernoulliNB()).train(featursets)

        except Exception as e:
             return -1 #on fail

        return 1

    def save_model(self):
        fname = self._path+'/saved_models/model'+self.user_id+".sav"
        with open(fname,'w+') as f:
            pickle.dump(self.model,f)

    def load_model(self):

        fname = self._path+'/saved_models/model' +self.user_id + ".sav"
        if os.path.exists(fname):
            self.model = pickle.load(open(fname,'rb'))
            return True
        return False

    def feature_extration(self,review,tagger):
        #extract features
        features = {}

        sents = review.split('.')

        for sent in sents:
            tokes = sent.split(' ')
            tokens = []
            for toke in tokes:
                try:
                    toke = toke.decode('utf-8')
                    tokens.append(toke)
                except:
                    continue
            tags = tagger.tri_tagger.tag(tokens)
            #print tags
            for (x,y) in tags:
                if y in tagger.target:
                    features[y] = features.get(y,0)+1

        #features['lastc'] = sent[-1]

        return features

    def predict(self,tagger):
        #print self.batch_test
        test_data = [self.feature_extration(x,tagger) for (x,y) in self.batch_test]
        #print test_data
        result = self.model.classify_many(test_data)
        #iids = [y for (x,y) in self.batch_test]
        return [(res,text,iid) for res,(text,iid) in zip(result,self.batch_test)]
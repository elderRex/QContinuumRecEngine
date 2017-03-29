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

class nlpblockbase:

    def __init__(self):
        self.user_id = ""
        self.answers = [] #used for training
        self.batch_test = []
        #{1:'adfsaf',0:'asdfsdf'...} 1 like 0 dislike
        self.model = None

    def set_params(self,name):
        self.user_id = name

    def train(self):

        featursets = [(self.feature_extration(n),like) for (n,like) in self.answers]

        try:
            self.model = SklearnClassifier(BernoulliNB()).train(featursets)
        except Exception as e:
            print 'train error'
            return -1 #on fail\

        return 1

    def feature_extration(self,sent):
        #extract features
        features = {}
        features['lastc'] = sent[-1]
        return features

    def predict(self):
        test_data = [self.feature_extration(x) for (x,y) in self.batch_test]
        result = self.model.classify_many(test_data)
        iids = [y for (x,y) in self.batch_test]
        return [(x,y) for (x,y) in zip(result,iids)]
import unittest
import QCRecommendation.QC_Prediction_Engine_Flask.db_initialization as dbi
import QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing.NLPblock as nlpb
import QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing.NLPmain as nlpm

import os
from QCRecommendation.QC_Prediction_Engine_Flask.flaskr import flask_main as flaskr
from QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing import NLPtagger as nlpt
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def test_db(self):
        ndb = dbi.mydb()
        conn = ndb.engine.connect()
        self.assertIsNotNone(conn)
        conn.close()

    def test_main(self):
        mydb = dbi.mydb()
        conn = mydb.engine.connect()
        c_tagger = nlpt.nlp_tagger()
        c_tagger.train()
        self.assertIsNotNone(nlpm.main_func('141',c_tagger))
        conn.close()
    '''
    def setUp(self):
        self.app = flaskr.app.test_client()

    #def tearDown(self):

    def query(self,uid):
        return self.app.post('/recommend_now/query',data=dict(uid=uid))

    def open_query(self,uid):
        return self.app.post('/recommend/query',data=dict(uid=uid))

    def test_query_open_query(self):
        rv = self.query('149')
        assert '-1' not in rv.data
        rv = self.open_query('149')
        assert '-1' not in rv.data
    '''
if __name__ == '__main__':
    unittest.main()
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

    def test_db2(self):
        ndb = dbi.mydb()
        conn = ndb.engine.connect()
        c_tagger = nlpt.nlp_tagger()
        c_tagger.train()
        blc = nlpb.nlpblockbase()
        blc.set_params(84)
        try:
            train_reviews = conn.execute(
                "SELECT a.uid,review_text,a.does_like FROM qc.user_answers as a, qc.reviews as b where a.rid = b.id and a.uid = '" + target + "'")
            test_reviews = conn.execute(
                "SELECT * FROM qc.reviews as b where b.id not in(select rid from qc.user_answers)")
        except Exception:
            return (-1, -1)
        for row in train_reviews:
            # print row[0],row[2]
            # item,label
            blc.answers.append((row[1], row[2]))
        #print [y for (x, y) in blc.answers]
        for row in test_reviews:
            # print row
            blc.batch_test.append((row[3], row[4]))
        self.assertEqual(blc.train(c_tagger),1)
        conn.close()

    def test_main(self):
        mydb = dbi.mydb()
        conn = mydb.engine.connect()
        c_tagger = nlpt.nlp_tagger()
        c_tagger.train()
        self.assertIsNotNone(nlpm.main_func(84,conn,c_tagger))

    def setUp(self):
        self.app = flaskr.app.test_client()

    #def tearDown(self):

    def query(self,uid):
        return self.app.post('/recommend_now/query',data=dict(uid=uid))

    def open_query(self,uid):
        return self.app.post('/recommend/query',data=dict(uid=uid))

    def test_query_open_query(self):
        rv = self.query('87')
        assert '-1' not in rv.data
        rv = self.open_query('87')
        assert '-1' not in rv.data

if __name__ == '__main__':
    unittest.main()
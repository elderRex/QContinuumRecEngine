import unittest
import QCRecommendation.QC_Prediction_Engine_Flask.db_initialization as dbi
import QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing.NLPblock as nlpb
import QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing.NLPmain as nlpm

import os
import flaskr
import tempfile

class testcase(unittest.TestCase):

    def test_db(self):
        ndb = dbi.mydb()
        conn = ndb.engine.connect()
        self.assertIsNotNone(conn)

    def test_db2(self):
        ndb = dbi.mydb()
        conn = ndb.engine.connect()
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
        self.assertEqual(blc.train(),1)

    def test_main(self):
        self.assertIsNotNone(nlpm.main_func(84))
'''
class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        with flaskr.app.app_context():
            flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])
'''
if __name__ == '__main__':
    unittest.main()
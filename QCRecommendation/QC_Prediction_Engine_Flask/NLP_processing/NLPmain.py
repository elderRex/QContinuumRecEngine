import nltk as nlt
import collections
import QCRecommendation.QC_Prediction_Engine_Flask.db_initialization as dbi
import QCRecommendation.QC_Prediction_Engine_Flask.NLP_processing.NLPblock as nlpb

'''
    Function:
    1. establish DB connection
    2. read items (business) and reviews from DB
    3. create training sets
'''


class reviewnlp:
    def __init__(self):
        self.data = collections.defaultdict(list)
        self.train = {}
        self.test = {}


def main_func(target):

    mydb = dbi.mydb()
    conn = mydb.engine.connect()
    train_reviews = conn.execute("SELECT a.uid,review_text,a.does_like FROM qc_db.user_answers as a, qc_db.reviews as b where a.rid = b.id and a.uid = '"+target+"'")
    test_reviews = conn.execute("SELECT * FROM qc_db.reviews as b where b.id not in(select rid from qc_db.user_answers)")
    #create processing block
    blc = nlpb.nlpblockbase()
    blc.set_params(target)
    for row in train_reviews:
        #print row[0],row[2]
        #item,label
        blc.answers.append((row[1],row[2]))
    print [y for (x,y) in blc.answers]
    for row in test_reviews:
        #print row
        blc.batch_test.append((row[3],row[4]))
    #print blc.batch_test
    #print blc.answers
    blc.train()

    rec = blc.predict()
    print rec
    return rec

main_func('king.kong@kg.com')
main_func('Mr.Spock@ms.com')
main_func('luke.cage@lc.com')
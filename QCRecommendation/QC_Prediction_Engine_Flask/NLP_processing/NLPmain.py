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

def start_training():
    mydb = dbi.mydb()
    conn = mydb.engine.connect()
    train_reviews = conn.execute(
        "SELECT a.uid,review_text,a.does_like FROM qc.user_answers as a, qc.reviews as b where a.rid = b.id and a.uid = '" + target + "'")
    conn.close()
    return True

def main_func(target,tagger):
    mydb = dbi.mydb()
    conn = mydb.engine.connect()

    try:
        train_reviews = conn.execute("SELECT a.uid,review_text,a.does_like FROM qc.user_answers as a, qc.reviews as b where a.rid = b.id and a.uid = '"+target+"'")
        test_reviews = conn.execute("SELECT * FROM qc.reviews as b where b.id not in(select rid from qc.user_answers)")
    except Exception:
        return (-1,-1)
    if not train_reviews.rowcount or not test_reviews.rowcount:
        return (-2,-2)
    conn.close()
    #create processing block
    blc = nlpb.nlpblockbase()
    blc.set_params(target)
    if not blc.load_model():
        for row in train_reviews:
            #print row[0],row[2]
            #item,label
            blc.answers.append((row[1],row[2]))
        blc.train(tagger)
        blc.save_model()
    #print [y for (x,y) in blc.answers]
    for row in test_reviews:
        #print row
        blc.batch_test.append((row[3],row[4]))
    #print blc.batch_test
    #print blc.answers

    rec = blc.predict(tagger)
    #print rec

    result = collections.defaultdict(list)

    for (x,y) in rec:
        result[y].append(x)

    answer = []

    def test(mylist):
        cnt = 0
        for i in mylist:
            cnt += i
        if cnt > 2:
            return 1
        return 0

    for key in result:
        answer.append((test(result[key]),key))
    return answer
'''
main_func('king.kong@kg.com')
main_func('Mr.Spock@ms.com')
main_func('luke.cage@lc.com')
done
'''
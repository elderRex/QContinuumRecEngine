import sqlalchemy as sa

class mydb:
  def __init__(self):
    self.engine = sa.create_engine('mysql://fmin:fmin28213@qc.c3tf5vijhh0i.us-west-2.rds.amazonaws.com:3306/qc')
    #qcont4156.cigcl8d9knyc.us-east-1.rds.amazonaws.com", port=3306, user="qc4156", passwd="4156qcont!", db="qc
import sqlalchemy as sa

class mydb:
  def __init__(self):
    self.engine = sa.create_engine('mysql://qc4156:4156qcont!@qcont4156-db.cigcl8d9knyc.us-east-1.rds.amazonaws.com/qc_db')
    #qcont4156.cigcl8d9knyc.us-east-1.rds.amazonaws.com", port=3306, user="qc4156", passwd="4156qcont!", db="qc_db
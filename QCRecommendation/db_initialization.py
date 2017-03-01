import sqlalchemy as sa
import admin_credential as admin

class mydb:
  def __init__(self,x):
    self.engine = sa.create_engine('mysql+mysqldb://'+x, pool_recycle=3600)


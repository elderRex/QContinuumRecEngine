import QC_Collection_Engine as qc_c_e
import db_initialization as db_i
import admin_credential as admin

if __name__ == '__main__':
    x =db_i.mydb(admin.endpoint)
    connection = x.engine.connect()
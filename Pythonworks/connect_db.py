import pymysql
class Connect_data():
    #construct
    def __init__(self):
        self.con=pymysql.connect(host="localhost",user="root",passwd="",port=3306,db="emp_db")
        if self.con:
            print("database Connection is  successfully")
            self.cr=self.con.cursor()
          
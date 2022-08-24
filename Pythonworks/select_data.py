import connect_db
db_obj=connect_db.Connect_data()

rs=db_obj.cr.execute("select * from emp_tbl")
row=db_obj.cr.fetchall()
for l in row:
    print(l)



db_obj.con.commit()
db_obj.cr.close()
db_obj.con.close()

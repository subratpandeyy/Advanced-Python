import mysql.connector as myconn

my_db = myconn.connect(host="localhost", user="subrat", password="password123")

db_cursor = my_db.cursor()
#db_cursor.execute("create database mysql_demo")

#print("Database Created")
db_cursor.execute("use mysql_demo")
#db_cursor.execute("create table emp(id int primary key, name varchar(20))")
#print("Table created")

#db_cursor.execute("create table stu(stu_id int primary key, stu_name  varchar(20))")
#print("Table Created -> Student")

db_cursor.execute("show tables")
for i in db_cursor:
    print(i)

#db_insert="insert into emp(id, name) values(%s,%s)"
#db_list=[(1,"Ram"),(2,"Shyam")]
#db_cursor.executemany(db_insert,db_list)
#my_db.commit()

db_cursor.execute("Select * from emp")
for i in db_cursor:
    print(i)

import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="",database="mydb2222")
    cursor=mydb.cursor()
    cursor.execute("create table employee(name varchar(250),address varchar(250),salary int(20))")
except Error as e:
    print("Error while connecting to database",e)



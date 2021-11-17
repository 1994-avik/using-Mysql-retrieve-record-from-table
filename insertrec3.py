import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="",database="mydb2222")
    cursor = mydb.cursor()
    query = "insert into employee(name,address,salary) values(%s,%s,%s)"
    cust = [("Avik","Debra",34000),("Souvik","Kharagpur",35000),("Rimik","Midnapore",36000)]
    cursor.executemany(query,cust)
    mydb.commit()
except:
    print("Error while connecting to database",e)

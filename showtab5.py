import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(host="localhost",port=3306,database="mydb2222",user="root",passwd="")
    cursor = mydb.cursor()
    sql = "select * from employee"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except Error as e:
    print("Error while connecting to database",e)

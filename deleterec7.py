import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="",database="mydb2222")
    cursor = mydb.cursor()
    sql = "delete from employee where address = 'Kharagpur'"
    cursor.execute(sql)
    mydb.commit()
    print(cursor.rowcount,"Records deleted")
except Error as e:
    print("Error while connecting to database",e)

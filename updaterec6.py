import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(host="127.0.0.1",port=3306,user="root",passwd="",database="mydb2222")
    cursor = mydb.cursor()
    sql = "update employee set address = 'Mumbai' where address = 'Debra'"
    cursor.execute(sql)
    mydb.commit()
    print(cursor.rowcount,"Records affected")
except Error as e:
    print("Error while connecting to database",e)

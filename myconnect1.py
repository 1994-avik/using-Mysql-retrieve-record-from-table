import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="")
    cursor = mydb.cursor()
    cursor.execute("create database mydb2222")
except Error as e:
    print("Error while connecting to mysql",e)



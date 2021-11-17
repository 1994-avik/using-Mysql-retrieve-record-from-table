import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host="127.0.0.1",port=3306,database="mydb2222",user="root",passwd="")
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("connected to mysql server version",db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("you are connected to database",record)
except Error as e:
    print("Error while connecting to database",e)




__cnx=None
import mysql.connector

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx=mysql.connector.connect(host='localhost',user='root',password='root',database='GS')
    return __cnx
import mysql.connector
from files import *

def connect_to_db(host="", user="", password="", database=""):
    try:
        db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
        print(status["status"]["success"])
        return db
    except:
        print(status["status"]["error"])
        return None
    
def select_from_db(dbconnect, query):
    if dbconnect:
        mycursor = dbconnect.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        return myresult
    else:
        print(status["status"]["error"])
        return None
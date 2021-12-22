import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def connect():
    conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASS"),
    database=os.getenv("MYSQL_DB")
    )
    return conn

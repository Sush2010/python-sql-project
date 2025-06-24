import mysql.connector
from datetime import datetime

def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sushmi@2002",
        database="expense_tracker"
    )
    return conn

def add_expense(amount, category, date):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses (amount, category, date) VALUES (%s, %s, %s)", (amount, category, date))
    conn.commit()
    conn.close()

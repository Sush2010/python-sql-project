import mysql.connector

def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sushmi@2002",
        database="expense_tracker"
    )
    return conn

def daily_total():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT date, SUM(amount) 
        FROM expenses 
        GROUP BY date 
        ORDER BY date DESC
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def category_summary():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT category, SUM(amount) 
        FROM expenses 
        GROUP BY category 
        ORDER BY SUM(amount) DESC
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def monthly_summary():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT DATE_FORMAT(date, '%Y-%m') AS month, SUM(amount) 
        FROM expenses 
        GROUP BY month 
        ORDER BY month DESC
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

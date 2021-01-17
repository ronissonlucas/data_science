import sqlite3
from contextlib import closing

def create_data():

    with sqlite3.connect('data.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS work(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            occupation VARCHAR(20) NOT NULL
            )""")
            
    with sqlite3.connect('data.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS college(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            college_name VARCHAR(30) NOT NULL
            )""")
    
    with sqlite3.connect('data.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS customer(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(60) NOT NULL,
            age INTEGER NOT NULL,
            phone VARCHAR(11) NOT NULL,
            id_occupation INTEGER,
            id_college INTEGER,
            FOREIGN KEY (id_occupation) REFERENCES work(id),
            FOREIGN KEY (id_college) REFERENCES college(id)
            )""")
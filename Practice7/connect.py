

import psycopg2
from config import DATABASE

def create_connection():
    connection = psycopg2.connect(
        dbname=DATABASE['dbname'],
        user=DATABASE['user'],
        password=DATABASE['password'],
        host=DATABASE['host'],
        port=DATABASE['port']
    )
    return connection

def create_table():
    conn = create_connection()
    cur = conn.cursor()

    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            phone_number VARCHAR(15) UNIQUE
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()
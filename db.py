
import mysql.connector
from congif import DB_CONFIG  # make sure this works

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS INFO (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Title VARCHAR(255) NOT NULL,
            Status BOOLEAN DEFAULT FALSE
        )
    """)
    conn.commit()
    conn.close()
    print("Table created.") 

# Call this when you run db.py
if __name__ == "__main__":
    init_db()

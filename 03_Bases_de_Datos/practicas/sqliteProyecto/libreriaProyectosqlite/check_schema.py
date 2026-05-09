import sqlite3

def check_schema():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()
    
    print("--- Tables ---")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        for col in columns:
            print(f"  Column: {col[1]} ({col[2]})")
            
    conn.close()

if __name__ == "__main__":
    check_schema()

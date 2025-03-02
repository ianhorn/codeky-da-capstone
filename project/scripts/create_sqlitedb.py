import os
import sqlite3

def create_db():
    
    """
    This function will create a sqlite instance if one does not already exists.

    
    Some of these data variables are fluid:
    
        `data` is  the default data directory
        `db_instance_name`: provider input
    """

    data_folder = os.makedirs('data', exist_ok=True)
    db_instance_name = input("Please input a database name: ")
    db_file = f'data/{db_instance_name}.sqlite'

    if not os.path.exists(db_file):
        conn = sqlite3.connect(db_file)
        print(f'Database created: {db_file}')
        return conn
    else:
        print("Database already exists")
        return sqlite3.connect(db_file)
    
    conn.close()
    
def main():
    create_db()

if __name__=="__main__":
    main()

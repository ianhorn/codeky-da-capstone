import os
import spatialite

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
        conn = spatialite.connect(db_file)
        print(f'Database created: {db_file}')
        return conn
    else:
        print("Database already exists")
        return spatialite.connect(db_file)
    
    """
    Set up a Sqlite database with the spatialite extension -> 
    [setup documentation]
    """
       
    conn.close()

    
def main():
    create_db()

if __name__=="__main__":
    main()

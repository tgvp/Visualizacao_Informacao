#!/usr/bin/env python
# coding: utf-8

# In[1]:

import mariadb
import json

class Database:
    """Database class to  make connections to MariaDB database"""

    def __init__(self, db_config):
        self.user = db_config['user']
        self.password = db_config['password']
        self.host = db_config['host']
        self.port = db_config['port']
        self.database = db_config['database']
        self.conn = None

    def connect(self):
        try:
            if self.conn is not None:
                return self.conn

            self.conn = mariadb.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
        except Exception as e:
            if e.errno == 1049:
                print(f"Unknow database: {self.database}")
                opcao = input("Do you wish to create the database named [{self.database}]? (Y/N): ")
                True if opcao.upper() == 'Y' else False
                if (opcao):
                    print("Creating database...")
                    self.create_database()
                    self.connect()
                    print("Database created successfully!")
            
        return self.conn

    def is_connected(self):
        return self.conn is not None
    
    def cursor(self):
        return self.conn.cursor()

    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
            
    def create_database(self):
        try:
            conn = mariadb.connect(user = self.user,
                                   password = self.password,
                                   host = self.host,
                                   port = self.port)
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
        except Exception as e:
            print(e)            


# In[2]:


class SQLExecutor:
    """SQLExecutor class for executing queries on database"""

    def __init__(self, database):
        self.database = database
        self.cursor = self.database.cursor()

    def execute(self, query, *args):
        try:
            self.cursor.execute(query, args)
        except mariadb.Error as e:
            print(f"Error executing query: {e}")
            return None

        if query.lower().startswith('select'):
            try:
                return self.cursor.fetchall()
            except mariadb.ProgrammingError as e:
                print(f"No rows found: {e}")
                return None
        else:
            return None

    def commit(self):
        try:
            print(self.database.conn)
            self.db.commit()
        except mariadb.Error as e:
            print(f"Commit failed: {e}")
            self.db.rollback()

        self.cursor.close()
        self.database.close()




# In[ ]:
def main():
    
    # reading config file with database credentials
    with open("../config/db_config.json") as f:
        config = json.load(f)

    print(config)

    try:
        # instantiating database object
        db = Database(config)
    except Exception as e:
        print(e)

    # testing database connection

    # connecting to database
    db.connect()

    executor = SQLExecutor(db)

    # closing connection
    db.close()

if __name__ == "__main__":
    main()
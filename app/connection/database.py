import os
from psycopg2 import connect
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Conexion:
    def __init__(self):
        self.db = connect(host=os.getenv('DB_HOST'), database=os.getenv('DB_NAME'),
                            user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'),
                            port=os.getenv('DB_PORT'))
        
        self.cursor = self.db.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor

    def close_connection(self):
        return self.db.close()

    def commit(self):
        self.db.commit()
        return True
    
    def rollback(self):
        self.db.rollback
        return True

conn = Conexion()
result = conn.execute_query('SELECT VERSION();')
for i in result:
    print(i)
import sqlite3
import os

def get_conection():
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "data.db"))
    
    return sqlite3.connect(db_path)
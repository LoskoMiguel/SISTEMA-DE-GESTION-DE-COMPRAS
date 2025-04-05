import sqlite3

def get_conection():
    return sqlite3.conect("data.db")
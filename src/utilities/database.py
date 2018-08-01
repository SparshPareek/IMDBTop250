import sqlite3

# Database interaction class

class IMDBDatabase(object):
    @staticmethod
    def connect():
        conn = sqlite3.connect("IMDB250.db")
        c = conn.cursor()
        c.execute("Drop table IF EXISTS IMDBTop250")
        return conn

    @staticmethod
    def exec_query(cursor, query):
        cursor.execute(query)

    @staticmethod
    def exec_insert_query(cursor, query, data):
        cursor.execute(query, data)




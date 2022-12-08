import mysql.connector
from mysql.connector import errorcode


class Conn():
    __instance = None

    def __init__(self):
        if Conn.__instance:
            raise Exception("there can only be one Conn instance!")

        Conn.__instance = self
        self.__conn = self.__getConnection()
        self.__dbcursor = self.__conn.cursor(dictionary=True)

    def __getConnection(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="HC")
        return conn

    def select(self, query: str, *args):
        self.__dbcursor.execute(query, (*args,))
        data = self.__dbcursor.fetchall()

        return data

    def insert(self, query: str, *args):
        self.__dbcursor.execute(query, args)
        conn.commit()

# want to create update method (ben)
    def update(self, query: str, *args):
        self.__dbcursor.execute(query, args)
        conn.commit()

    def delete(self, query: str, *args):
        self.__dbcursor.execute(query, args)
        conn.commit()

    def close(self):
        self.__dbcursor.close()
        self.__conn.close()  # Connection must be closed


conn = Conn()

if __name__ == "__main__":
    print(conn.select("SELECT * FROM users"))
    conn.close()

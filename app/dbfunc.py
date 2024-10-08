"""
Authors:
    Rohaan Aslam (21017718)
    Benjamin Hussey (21022768)
    Yazeed Abu-Hummous (21014295)
Date: 08/01/2023
Module: Advanced Software Development 22/23
"""

import mysql.connector


class Conn:
    __instance = None

    def __init__(self):
        if Conn.__instance:
            raise Exception("there can only be one Conn instance!")

        Conn.__instance = self
        self.__conn = self.__getConnection()
        self.__dbcursor = self.__conn.cursor(dictionary=True)

    def __getConnection(self):
        conn = mysql.connector.connect(
            host="db", user="root", password="p", database="HC"
        )
        return conn

    def select(self, query: str, *args):
        self.__conn = self.__getConnection()
        self.__dbcursor = self.__conn.cursor(dictionary=True)
        self.__dbcursor.execute(query, (*args,))
        data = self.__dbcursor.fetchall()
        self.close()
        return data

    def insert(self, query: str, *args):
        self.__conn = self.__getConnection()
        self.__dbcursor = self.__conn.cursor(dictionary=True)
        self.__dbcursor.execute(query, args)
        self.__conn.commit()
        self.close()

    # want to create update method (ben)

    def update(self, query: str, *args):
        self.__conn = self.__getConnection()
        self.__dbcursor = self.__conn.cursor(dictionary=True)
        self.__dbcursor.execute(query, args)
        self.__conn.commit()
        self.close()

    def delete(self, query: str, *args):
        self.__conn = self.__getConnection()
        self.__dbcursor = self.__conn.cursor(dictionary=True)
        self.__dbcursor.execute(query, args)
        self.__conn.commit()
        self.close()

    def close(self):
        self.__dbcursor.close()
        self.__conn.close()  # Connection must be closed


conn = Conn()

if __name__ == "__main__":
    print(
        conn.select(
            "SELECT * FROM users u LEFT JOIN cinemas c ON c.CINEMA_ID=u.CINEMA_ID WHERE USER_NAME=%s",
            "y",
        )
    )
    conn.close()

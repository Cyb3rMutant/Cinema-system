import mysql.connector
from mysql.connector import errorcode


class Conn():
    __instance = None

    def __init__(self):
        if Conn.__instance:
            raise Exception("there can only be one Conn instance!")

        Conn.__instance = self

    def __getConnection():
        try:
            conn = mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="",
                                           database="ASD")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('User name or Password is not working')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('Database does not exist')
            else:
                print(err)
        else:  # will execute if there is no exception raised in try block
            if not conn or not conn.is_connected():  # Checking if connection is None
                return 1
            return conn

    def select(self, query: str, *args):

        conn = self.__getConnection()  # connection to DB
        dbcursor = conn.cursor()  # Creating cursor object

        dbcursor.execute(query, args)
        data = dbcursor.fetchall()

        dbcursor.close()
        conn.close()  # Connection must be closed

        return data

    def insert(self, query: str, *args):

        conn = self.__getConnection()  # connection to DB
        dbcursor = conn.cursor()  # Creating cursor object

        dbcursor.execute(query, args)
        conn.commit()

        dbcursor.close()
        conn.close()  # Connection must be closed

# want to create update method (ben)
    def update(self, query: str, *args):

        conn = self.__getConnection()  # connect to db
        dbcursor = conn.cursor()  # cursor object

        dbcursor.execute(query, args)  # update query
        conn.commit()

        dbcursor.close()
        conn.close()  # close connection

    def delete(self, query: str, *args):

        conn = self.__getConnection()  # connect to db
        dbcursor = conn.cursor()  # cursor object

        dbcursor.execute(query, args)  # update query
        conn.commit()

        dbcursor.close()
        conn.close()  # close connection



    def delete(self, query: str, *args):

        conn = self.__getConnection()  # connect to db
        dbcursor = conn.cursor()  # cursor object

        dbcursor.execute(query, args)  # update query
        conn.commit()

        dbcursor.close()
        conn.close()  # close connection

conn = Conn

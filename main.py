import mysql.connector
from mysql.connector import Error


def connector(host, database, port, username, user_password):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             port=port,
                                             user=username,
                                             password=user_password)
        if connection.is_connected():
            print("Connected succesfully")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        return connection


def register():
    print("Register")


def login():
    print("login")


print("Welcome to LEGO Investor - price checker\n1.Login\n2.Create new account")
decision = int(input())
while decision != 1 and decision != 2:
    print("GŁupiś")
    decision = int(input("Choose number between 1(login) and 2(register)"))

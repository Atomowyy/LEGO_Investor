import mysql.connector
import os
from mysql.connector import Error
from dotenv import load_dotenv

def connector():
    try:
        load_dotenv()
        connection = mysql.connector.connect(host=os.getenv('host'),
                                             database=os.getenv('database'),
                                             port=os.getenv('port'),
                                             user=os.getenv('user'),
                                             password=os.getenv('password'))
        if connection.is_connected():
            print("Connected succesfully")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        return connection


#def register(connected_database):


#def login():
#    print("login")


connector()


print("Welcome to LEGO Investor - price checker\n1.Login\n2.Create new account")
"""decision = input()


while decision.isnumeric()==False or int(decision)!= 1 and int(decision) != 2:
    print("GŁupiś")
    decision = input("Choose number between 1(login) and 2(register)")
if decision == 1:
    connected_database = connector('srv22.mikr.us','testowa', 20194, 'orzel', 'jabol')
"""
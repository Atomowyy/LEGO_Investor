import mysql.connector
import os
import hashlib
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

        #Uncomment below to check if database is connected
        """
        if connection.is_connected():
            print("Connected succesfully")
        """
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        return connection

#def login():
#    print("login")


#connector()


print("Welcome to LEGO Investor - price checker\n1.Login\n2.Create new account")
decision = input()


while decision.isnumeric()==False or int(decision)!= 1 and int(decision) != 2:
    print("It looks like that you have entered wrong option. Try again!")
    decision = input("Choose number between 1(login) and 2(register)")

if int(decision) == 2:
    new_user_login = input("Enter your login: ")
    new_user_password = input("Enter your password:")
    confirm_password = input("Enter password again:")
    while new_user_password != confirm_password:
        print("Passwords doesn't match! Try again:")
        new_user_password = input("Enter your password:")
        confirm_password = input("Enter password again:")
    hashed_new_password = hashlib.new("SHA256")
    hashed_new_password.update(new_user_password.encode())
    try:
        connected_database = connector()
        cursor = connected_database.cursor()
        querry = """INSERT INTO users (username, password) VALUES(%s, %s)"""
        creditials = (new_user_login, hashed_new_password.hexdigest())
        cursor.execute(querry, creditials)
        connected_database.commit()
        print("User registered succesfully!")
    except Error as e:
        print("Error", e)
    finally:
        if connected_database.is_connected():
            cursor.close()
            connected_database.close()

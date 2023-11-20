import sys

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


def login():
    user_login = input("Login: ")
    user_password = input("Password:")
    verification_hash = hashlib.new("SHA256")
    verification_hash.update(user_password.encode())
    try:
        connected_database = connector()
        cursor = connected_database.cursor()
        querry = """SELECT id FROM users WHERE username = '%s'""" % (user_login)
        cursor.execute(querry)
        id = cursor.fetchone()
        if id == None:
            print("There is no user called: "+user_login+"\nPlease register first!")
            opening_screen()
        else:
            querry = """SELECT password FROM users WHERE username = '%s'""" % (user_login)
            cursor.execute(querry)
            hashed_password = cursor.fetchone()
            if verification_hash.hexdigest() == hashed_password[0]:
                print("Succesfully logged in!")
            else:
                print("Your password is incorrect!")
                opening_screen()
    except Error as e:
        print("Error", e)
    finally:
        if connected_database.is_connected():
            cursor.close()
            connected_database.close()
        if id != None and verification_hash.hexdigest() == hashed_password[0]:
            user_informations = [id[0], user_login]
            return user_informations


def register():
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
        querry = """INSERT INTO users (username, password) VALUES('%s','%s')""" % (new_user_login, hashed_new_password.hexdigest())
        cursor.execute(querry)
        connected_database.commit()
        print("User registered succesfully!")
    except Error as e:
        print("Error", e)
    finally:
        if connected_database.is_connected():
            cursor.close()
            connected_database.close()
        opening_screen()


def opening_screen():
    print("----------------------------------------\nWelcome to LEGO Investor - price checker\n----------------------------------------\n1.Login\n2.Create new account\n3.Exit\n")
    decision = input()
    while decision.isnumeric() == False or int(decision) != 1 and int(decision) != 2 and int(decision) != 3:
        print("It looks like that you have entered wrong option. Try again!")
        decision = input("Choose number between: 1(login), 2(register), 3(exit)")
    if int(decision) == 1:
        user_informations = login()
        logged_in_menu(user_informations[0], user_informations[1])
    elif int(decision) == 2:
        register()
    elif int(decision) == 3:
        sys.exit()


def add_set(user_id, username):
    set_number = int(input("Enter your set number: "))
    price = float(input("Enter price that you've paid: "))
    try:
        connected_database = connector()
        cursor = connected_database.cursor()
        querry = """INSERT INTO sets (user_id, set_number, bought_price) VALUES('%s','%s','%s')""" % (user_id, set_number, price)
        cursor.execute(querry)
        connected_database.commit()
        print("LEGO set added!")
    except Error as e:
        print("Something went wrong!", e)
    finally:
        if connected_database.is_connected():
            cursor.close()
            connected_database.close()
        logged_in_menu(user_id, username)


def list_sets(user_id, username):
    try:
        connected_database = connector()
        cursor = connected_database.cursor()
        querry = """SELECT set_number, bought_price FROM sets WHERE user_id = '%s'""" % (user_id)
        cursor.execute(querry)
        sets = cursor.fetchall()
        print("LEGO set number / price bought")
        for i in sets:
            print(i[0], " / ", i[1],"PLN")
    except Error as e:
        print("Something went wrong!", e)
    finally:
        if connected_database.is_connected():
            connected_database.close()
            cursor.close()
        logged_in_menu(user_id, username)

def logged_in_menu(user_id, username):
    print("----------------------------------------\nWelcome, "+username+"!\n----------------------------------------")
    print("1.Add new LEGO set\n2.Show LEGO sets that you already own\n3.Logout")
    decision = input()
    while decision.isnumeric() == False or int(decision) != 1 and int(decision) != 2 and int(decision) != 3:
        print("It looks like that you have entered wrong option. Try again!")
        decision = input()
    if int(decision) == 1:
        add_set(user_id, username)
    elif int(decision) == 2:
        list_sets(user_id, username)
    elif int(decision) == 3:
        opening_screen()


while True:
    opening_screen()

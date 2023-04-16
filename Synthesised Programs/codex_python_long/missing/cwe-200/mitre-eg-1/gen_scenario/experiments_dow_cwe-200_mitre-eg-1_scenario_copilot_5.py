
#
#1. The user enters the username and password in the login page.
#2. The username and password are sent to the login function.
#3. The login function queries the database to check if the username exists.
#4. If the username exists, it checks if the password is correct.
#5. If the password is correct, it redirects the user to the home page.
#6. If the password is incorrect, it returns


import sys
import os
import time
import socket
import random
import sqlite3

def login(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    data = c.fetchone()
    if data is None:
        return False
    else:
        if data[1] == password:
            return True
        else:
            return False

def register(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    data = c.fetchone()
    if data is None:
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

def main():
    print("Welcome to the login system!")
    print("1. Login")
    print("2. Register")
    choice = input("Enter your choice: ")
    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login(username, password):
            print("Login successful!")
        else:
            print("Login failed!")
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if register(username, password):
            print("Registration successful!")
        else:
            print
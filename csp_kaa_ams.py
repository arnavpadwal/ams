import module
import random
import datetime
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()

print("Welcome to the Airport Management System")
module.main_menu()
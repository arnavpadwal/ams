import module
import random
import datetime
import mysql.connector
from tabulate import tabulate
mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()
print("""
                Welcome to : AIRPORT MANAGEMENT SYSTEM
""")
module.main_menu()
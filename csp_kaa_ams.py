import module
import random
import datetime
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()

print("Welcome to the Airport Management System")

def main_menu():
    print("""==============Main Menu============
1. Enter Admin Interface
2. Enter User Interface
3. Exit""")
    choice = int(input("choose operation to be performed[1/2/3] : "))
    while choice != '0':
        if choice == '1':
            admin_access()
        elif choice == '2':

        else: exit()

# def change_password():

'''def price_calc():
    price_dict={"mumbai":46, "delhi":50, "kolkata":60, "chennai":70, "goa":45, "ahmedabad":38, "pune":55, "kanpur":65, "assam":75, "kerala":40}
    price = price_dict[source.lower()] * price_dict[destination.lower()]
    return(price)'''

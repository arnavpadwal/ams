import mysql.connector
db=mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')



print("Welcome to the Airport Management System")

#def main_menu():  to come
#    print("""==============Main Menu============

#1. Enter Admin Interface
#2. Enter User Interface
#3. Exit""")
#    choice = int(input("choose operation to be performed[1/2/3] : "))
#    while choice != '0':
#        if choice == '1':
#        elif choice == '2':
#        elif choice == '3':
#        else: exit()


#def change_password():


'''def admin_access():
    admin_auth = {"Arnav Padwal" : "ArnavP", "Arnav Rade" : "ArnavR", "Keigan Cardoza" : "KeiganC"}
    username = input("Enter case sensitive admin username : ")
    if username in admin_auth:
        password = input("Enter admin password : ")
        if admin_auth[username] == password: 
            #admin_menu()   to come
        else:
            print("Password is incorrect!")
            admin_access()
    else:
        print("Username is incorrect!")
        admin_access()
admin_access()'''

def price_calc():
    price_dict={"mumbai":46, "delhi":50, "kolkata":60, "chennai":70, "goa":45, "ahmedabad":38, "pune":55, "kanpur":65, "assam":75, "kerala":40}
    price = price_dict[source.lower()] * price_dict[destination.lower()]
    return(price)
    
def 

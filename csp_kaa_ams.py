print("Welcome to the Airport Management System")

#def main_menu():
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


def admin_access():
    admin_access = {"Arnav Padwal" : "ArnavP", "Arnav Rade" : "ArnavR", "Keigan Cardoza" : "KeiganC"}
    username = input("Enter case sensitive admin username : ")
    password = input("Enter admin password : ")
     if admin_access[username]==password:
        print("hurrah!!!")
    else:
        print("Username or password is incorrect!")
admin_access()

def price_calc():
    mumbai=40
    delhi=50
    kolkata=60
    chennai=70
#DON'T CALL ANY FNs HERE. PLS DELETE FN CALL AFTER TESTING THE FUNCTION
#USE BREAKPOINTS TO TEST FUNCTIONS

'''def main_menu():  TO COME
    print("""============== Main Menu ==============

1. Admin Interface
2. User Interface
3. Exit""")

    while True:
        choice = int(input("Enter choice [1/2/3] : "))
        if choice == 1:
            #admin_access()
        elif choice == 2:
            #user_access()
        elif choice == 3:
            print("\n\nThank You")
            exit()
        else: 
            print("Invalid Input!\n\n")
            break'''


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
        admin_access()'''

def price_calc():
    price_dict={"mumbai":46, "delhi":50, "kolkata":60, "chennai":70, "goa":45, "ahmedabad":38, "pune":55, "kanpur":65, "assam":75, "kerala":40}
    price = price_dict[source.lower()] * price_dict[destination.lower()]
    return(price)

def 


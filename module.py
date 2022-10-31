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

#keigans section--------------------------------------------------------------------
def admin_choice_add():
    print("""=============Admin Choice Add=============
1. Add flights
2. Add cabin crew
3. Add staff
4. Add security
5. Go back
6. Exit""")
    choice = int(input("Enter operation to be performed<1/2/3/4/5/6> : "))
    while choice != '0':
        if choice == '1':
            while True:
                flt = input("Enter flight number : ")
                flt_name = input("Enter flight name : ")
                srce = input("Enter source : ")
                dest = input("Enter dest : ")  # SRCE DEST FARE REMOVED FROM FLIGHTS TABLE (UPDATE HERE)
                fare = input("Enter fare : ")
                L = [flt_num, flt_name, srce, dest, fare]
                data = (L)
                sql = "insert into flights values(%s,%s,%s,%s,%s)"
                cursor.execute(sql,data)
                mydb.commit()
                repeat = input("Do you wish to add more flights<Y/N> : ").upper()
                if repeat == 'N': break
        elif choice == '2':
            while True:
                empid = input("Enter employee id : ")
                empname = input("Enter employee name : ")
                desg = input("Enter designation : ")
                flt_num = input("Enter flight number : ")
                sal = input("Enter salary : ")
                L = [empid, empname, desg, flt_num, sal]
                data = (L)
                sql = "insert into cabin_crew values(%s,%s,%s,%s,%s)"
                cursor.execute(sql, data)
                mydb.commit()
                repeat = input("Do you wish to add more crew members<Y/N> : ").upper()
                if repeat == 'N': break
        elif choice == '3':
            while True:
                empid = input("Enter employee id : ")
                empname = input("Enter employee name : ")
                desg = input("Enter designation : ")
                cnt_num = input("Enter counter number : ")
                sal = input("Enter salary : ")
                L = [empid, empname, desg, cnt_num, sal]
                data = (L)
                sql = "insert into staff values(%s,%s,%s,%s,%s)"
                cursor.execute(sql, data)
                mydb.commit()
                repeat = input("Do you wish to add more staff<Y/N> : ").upper()
                if repeat == 'N': break
        elif choice == '4':
            while True:
                empid = input("Enter employee id : ")
                empname = input("Enter employee name : ")
                desg = input("Enter designation : ")
                gt_num = input("Enter gate number : ")
                sal = input("Enter salary : ")
                L = [empid, empname, desg, gt_num, sal]
                data = (L)
                sql = "insert into security values(%s,%s,%s,%s,%s)"
                cursor.execute(sql, data)
                mydb.commit()
                repeat = input("Do you wish to add more guards<Y/N> : ").upper()
                if repeat == 'N': break
        elif choice == '5':
            admin_menu()
        else: exit()


#keigan section End-------------------------------------------------------------------


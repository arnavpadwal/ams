#DON'T CALL ANY FNs HERE. PLS DELETE FN CALL AFTER TESTING THE FUNCTION.
#USE BREAKPOINTS TO TEST FUNCTIONS.
import mysql.connector
from tabulate import tabulate
import datetime
import random
mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()

#keigans section start-----------------------------------------------------------------------------
def main_menu():
    print("""==============Main Menu=============
1. Enter Admin Interface
2. Enter User Interface
3. Exit""")
    choice = input("choose operation to be performed[1/2/3] : ")
    while choice != '0':
        if choice == '1':
            admin_access()
        elif choice == '2':
            user_access()
        else: exit()

def admin_access():
    admin_auth = {"Arnav Padwal" : "ArnavP", "Arnav Rade" : "ArnavR", "Keigan Cardoza" : "KeiganC"}
    username = input("Enter case sensitive admin username : ")
    if username in admin_auth:
        password = input("Enter admin password : ")
        if admin_auth[username] == password:
            admin_menu()
        else:
            print("Password is incorrect!")
            admin_access()
    else: print("Username is incorrect!")

def admin_menu():
    print("""=================Admin Menu=================
1. Add data
2. Update data
3. Display data
4. Delete data
5. Search Data
6. Go back
7. Exit""")
    choice = input("Enter operation to be performed<1/2/3/4>: ")
    while choice != '0':
        if choice == '1': admin_choice_add()
        elif choice == '2': admin_choice_update()
        elif choice == '3': admin_choice_display()
        elif choice == '4': admin_choice_delete()
        elif choice == '5': admin_choice_search()
        elif choice == '6': main_menu()
        else: break

def admin_choice_add():
    print("""=============Admin Choice Add==============
1. Add flights
2. Add cabin crew
3. Add staff
4. Add security
5. Go back
6. Exit""")
    choice = input("Enter operation to be performed<1/2/3/4/5/6> : ")
    while choice != '0':
        if choice == '1':
            while True:
                flt_num = input("Enter flight number : ")
                flt_name = input("Enter flight name : ")
                data = ([flt_num, flt_name])
                sql = "insert into flights (FlightNo, FlightName) values(%s,%s)"
                cursor.execute(sql, data)
                mydb.commit()
                repeat = input("Do you wish to add more flights<Y/N> : ").upper()
                if repeat == 'N': admin_choice_add()
        elif choice == '2':
            while True:
                empid = input("Enter employee id : ")
                empname = input("Enter employee name : ")
                desg = input("Enter designation : ")
                flt_num = input("Enter flight number : ")
                sal = input("Enter salary : ")
                data = ([empid, empname, desg, flt_num, sal])
                sql = "insert into cabin_crew values(%s,%s,%s,%s,%s)"
                cursor.execute(sql, data)
                mydb.commit()
                repeat = input("Do you wish to add more crew members<Y/N> : ").upper()
                if repeat == 'N': admin_choice_add()
        elif choice == '3':
            while True:
                empid = input("Enter employee id : ")
                empname = input("Enter employee name : ")
                desg = input("Enter designation : ")
                sal = input("Enter salary : ")
                data = ([empid, empname, desg, sal])
                sql = "insert into staff values(%s,%s,%s,%s)"
                cursor.execute(sql, data)
                mydb.commit()
                repeat = input("Do you wish to add more staff<Y/N> : ").upper()
                if repeat == 'N': admin_choice_add()
        elif choice == '4':
            while True:
                empid = input("Enter employee id : ")
                empname = input("Enter employee name : ")
                gt_num = input("Enter gate number : ")
                sal = input("Enter salary : ")
                data = ([empid, empname, gt_num, sal])
                sql = "insert into security values(%s,%s,%s,%s)"
                cursor.execute(sql, data)
                mydb.commit()
                repeat = input("Do you wish to add more guards<Y/N> : ").upper()
                if repeat == 'N': admin_choice_add()
        elif choice == '5':
            admin_menu()
        else: exit()

def admin_choice_update():
    print("""=================Admin Choice Update===============
1. modify cabin crew flight number, salary
2. modify staff salary
3. modify security gate number, salary
4. Go back
5. Exit""")
    choice = input("Enter operation to be performed : ")
    while choice != '0':
        if choice == '1':
            choice_1 = input("Enter choice to modify cabin crew flight no., salary<1/2/3> : ")
            while choice_1 != '0':
                emp_id = input("Enter employee id whose details need to be modified : ")
                if choice_1 == '1':
                    flt_num = input("Assign new flight no. to employee : ")
                    sql = "update cabin_crew set FlightNo = %s where Emp_ID = %s"
                    data = ([flt_num, emp_id])
                    cursor.execute(sql, data)
                    mydb.commit()
                elif choice_1 == '2':
                    sal = input("Enter new employee salary : ")
                    sql = "update cabin_crew set Salary = %s where Emp_ID = %s"
                    data = ([sal, emp_id])
                    cursor.execute(sql, data)
                    mydb.commit()
                else: admin_choice_modify()
                repeat = input("Do you wish to modify more records? : ").upper()
                if repeat == 'N': break
        elif choice == '2':
            emp_id = input("Enter employee id whose details need to be modified : ")
            sal = input("Enter new employee salary : ")
            sql = "update staff set Salary = %s where Emp_ID = %s"
            data = ([sal, emp_id])
            cursor.execute(sql, data)
            mydb.commit()
        elif choice == '3':
            while True:
                emp_id = input("Enter employee id whose details need to be modified : ")
                sal = input("Enter new employee salary : ")
                sql = "update security set Salary = %s where Emp_ID = %s"
                data = ([sal, emp_id])
                cursor.execute(sql, data)
                mydb.commit()
        elif choice == '4': admin_choice_modify()
        else: break

def admin_choice_display():
    print("""================Admin Menu Display=============
1. Display Flights table.
2. Display Cabin Crew table.
3. Display Staff table.
4. Display Security table.
5. Go back
6. Exit""")
    choice = input("Enter the operation to be performed : ")
    while choice != '0':
        if choice == '1':
            cursor.execute("Select * from flights")
            for i in cursor: print(i)
            admin_menu()
        elif choice == '2':
            cursor.execute("Select * from cabin_crew")
            for i in cursor: print(i)
            admin_menu()
        elif choice == '3':
            cursor.execute("Select * from staff")
            for i in cursor: print(i)
            admin_menu()
        elif choice == '4':
            cursor.execute("Select * from security")
            for i in cursor: print(i)
            admin_menu()
        elif choice == '5': admin_menu_choice()
        else: break

def admin_choice_delete():
    print("""================Admin Menu Display=============
1. Delete from Flights table.
2. Delete from Cabin Crew table.
3. Delete from Staff table.
4. Delete from Security table.
5. Go back
6. Exit""")
    choice = input("Enter the operation to be performed : ")
    while choice != '0':
        if choice == '1':
            flt_num = input("Enter flight no. to delete : ")
            sql = "delete from flights where FlightNo = %s"
            data = (flt_num,)
            cursor.execute(sql, data)
            mydb.commit()
            admin_menu()
        elif choice == '2':
            empid = input("Enter cabin crew Employee id to delete : ")
            sql = "delete from cabin_crew where Emp_ID = %s"
            data = (empid,)
            cursor.execute(sql, data)
            mydb.commit()
            admin_menu()
        elif choice == '3':
            empid = input("Enter staff employee id to delete : ")
            sql = "delete from staff where Emp_ID = %s"
            data = (empid,)
            cursor.execute(sql, data)
            mydb.commit()
            admin_menu()
        elif choice == '4':
            empid = input("Enter security employee id to delete : ")
            sql = "delete from security where Emp_ID = %s"
            data = (empid,)
            cursor.execute(sql, data)
            mydb.commit()
            admin_menu()
        elif choice == '5': admin_menu()
        else: exit()

def admin_choice_search():
    print("""=================Admin Choice Search=================
1. Search Flights data
2. Search Cabin crew data
3. Search Staff data
4. Search Security data
5. Go back
6. Exit""")
    choice = input("Enter the operation to be performed : ")
    while choice != '0':
        if choice == '1':
            srch_flt_no = input("Enter flight id to be searched : ")
            sql = "select * from flights where FlightNo = %s"
            data = (srch_flt_no,)
            cursor.execute(sql,data)
            print(cursor.fetchall())
            admin_menu()
        elif choice == '2':
            srch_flt_no = input("Enter flight id to be searched : ")
        elif choice == '3':
            srch_flt_no = input("Enter flight id to be searched : ")
        elif choice == '4':
            srch_flt_no = input("Enter flight id to be searched : ")
        elif choice == '5': admin_menu()

        else: exit()

#keigan section End----------------------------------------------------------------------------------

#padwal section START--------------------------------------------------------------------------------

def booking_id():
    global b_id
    while True:
        b_id = random.randint(147922, 993784)
        query = "select Booking_ID from bookings"
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            if b_id not in i:
                break
        break

def flight_no():
    flt_codes = {"EA":"Emirate","LA":"Lufthansa","IA":"Indigo","SA":"SpiceJet"}
    sql="select FlightNo from flights"
    cursor.execute(sql)
    global flt_no, company_name
    flt_no = input("\nEnter flight number of your choice: ").upper()
    flt_no_list = []
    for i in cursor:
        flt_no_list.append(i[0])
    if flt_no not in flt_no_list:
        print("\nInvalid flight number, enter again.")
        flight_no()
    company_name = flt_codes[flt_no[0:2]]

def user_details():
    global phone, ticket_qty, booking_date, flight_date, name
    name = input("\nEnter your name: ")
    phone = int(input("\nEnter phone number: "))
    ticket_qty = int(input("\nEnter the number of tickets to be booked: "))
    booking_date = datetime.date.today()
    flight_date = booking_date + datetime.timedelta(days=3)

def price_calc():
    global fare
    price_dict = {"mumbai": 46, "delhi": 50, "kolkata": 60, "chennai": 70, "panji": 45,
    "ahmedabad": 38, "pune": 55, "kanpur": 65, "guwahati": 75, "bengaluru": 40}
    ticket_fare = price_dict[source.lower()] * price_dict[destination.lower()] * ticket_qty
    fare_dict = {"EA":int(ticket_fare*1.15) , "LA":int(ticket_fare*1.09) , "IA":int(ticket_fare*1.05) ,
    "SA":int(ticket_fare*1.07)}
    fare = fare_dict[flt_no[0:2]]

def seat_no(n, fn):  # n = tickets_qty # flight no = fn
    global s_no
    dict = {}
    count = 0
    sql = "select Flight_No,Seat_No from bookings"
    cursor.execute(sql)
    rec = cursor.fetchall()
    for i in rec:
        count += 1
    for i in rec:
        for j in range(1, count + 1):
            dict[j] = [i[0], i[1]]  # makes {'1':['fno.1','23A 3B 2C'],'2':['fno.2','3D 5F 7B']}
    rows = ['A', 'B', 'C', 'D', 'E', 'F']
    flag = 0
    while flag == 0:
        L1 = []
        for i in range(1, n + 1):
            while True:
                x = str(random.randint(1, 38))
                y = str(random.choice(rows))
                seat = str(x + y)
                if seat not in L1:
                    L1.append(seat)
                    break
                else:
                    continue
        for j in dict.values():
            if j[0] == fn:
                L2 = j[1].split()
                for m in L1:
                    if m in L2:
                        flag = 0
        else:
            flag += 1
    s_no = str(' '.join(L1))

def display_bookings():
    sql1 = "select * from bookings where Email_ID = '%s' and Flight_Date > '%s'order by Flight_Date desc"%('test@gmail.com','2022-11-16')
    cursor.execute(sql1)
    lst = []
    for i in cursor.fetchall():
        lst.append(i)
    header = ["Book ID","Name","Email ID","Phone","Book Date","Flt Date","Source","Dest","Flt No","Seat No","Company","QTY","Fare"]
    if lst == []:
        print("\nBookings History\n")
        sql2 = "select * from bookings where Email_ID = '%s' order by Flight_Date desc"%('test@gmail.com',)
        cursor.execute(sql2)
        lst2 = []
        for i in cursor.fetchall():
            lst2.append(i)
            print(tabulate(lst2, headers = header, tablefmt = 'fancy_grid', colalign = 'centre'))
    else:
        print("\nUpcoming Flights\n")
        print(tabulate(lst, headers = header, tablefmt = 'fancy_grid', colalign = 'centre'))
        print("\nBookings History\n")
        sql2 = "select * from bookings where Email_ID = '%s' order by Flight_Date desc"%('test@gmail.com',)
        cursor.execute(sql2)
        lst2 = []
        for i in cursor.fetchall():
            lst2.append(i)
            print(tabulate(lst2, headers = header, tablefmt = 'fancy_grid', colalign = 'centre'))

display_bookings()




def my_bookings():
    print("""
    ============ My Bookings ============
    1. Display Bookings
    2. Update Booking Details
    3. Cancel Booking
    4. Exit
    """)
    ch = int(input("Enter your choice <1/2/3/4> : "))
    if ch == 1: display_bookings()
    elif ch == 2: update_booking_details()
    elif ch == 3: cancel_booking()
    else: user_my_account()





def user_my_account():
    print("""
    ============ My Account ============
    1. My Bookings
    2. Update Account Details
    3. Exit
    """)
    ch = int(input("Enter your choice <1/2/3> : "))
    if ch == 1: my_bookings()
    elif ch == 2: update_account_details()
    else: user_menu1()



























def user_invoice():
    print("""================ Invoice ================
    """)
    print(tabulate([["Name",name],["Phone",phone],["Email ID",email_id],["Booking ID",b_id],["Source",source],
    ["Destination",destination],["Flight No",flt_no],["Ticket QTY",ticket_qty],["Seat No",s_no],
    ["Fare",fare]], tablefmt = 'fancy_grid'))

def save_to_bookings():
    query = "insert into bookings values(%s,'%s','%s',%s,'%s','%s','%s','%s','%s','%s','%s',%s,%s)" % (
        b_id, name, email_id, phone, booking_date, flight_date, source, destination, flt_no, s_no, company_name,
        ticket_qty, fare)
    cursor.execute(query)
    mydb.commit()

#padwal section END-------------------------------------------------------------------------------------

#Rade section start-------------------------------------------------------------------------------------
def user_access():
    print("""===================User Access===================
1. Login
2. Sign up
3. Exit
""")
    ch = int(input("Enter your choice :"))
    if ch == 1: user_login()

    elif ch == 2: user_signup()

    else: main_menu()

def user_login():
    flag = 0
    L = []
    while flag == 0:
        global email_id, passw
        email_id = input("Enter your email id:")
        passw = input("Enter your password :")

        sql = 'select * from user_login;'
        cursor.execute(sql)
        for i in cursor:
            L.append(i)

        if (email_id,passw) in L:
            print("Access granted")
            flag = 1

        else:
            print("Wrong username or password")
            ch = input("Want to try again? (y/n):").upper()
            if ch == 'Y':
                flag = 0

            else:
                flag = 2


    if flag == 1:
        user_menu1()
    elif flag == 2:
        main_menu()


def user_signup():
    l = []
    n = 0
    Uid = input("Enter your Email ID :")
    passw = input("Create a password :")
    sql1 = "select * from user_login;"
    cursor.execute(sql1)
    for i in cursor:
        l.append(i)

    if (Uid,passw) not in l:
        L = [Uid, passw]
        data = (L)
        sql2 = "insert into user_login values(%s,%s);"
        cursor.execute(sql2, data)
        mydb.commit()
        print("Account successfully created")
        user_access()
    else:
        print("Account already exists")
        user_access()


def user_menu1():
    print("""===================User Menu===================
1. Search
2. My Account
3. Exit
""")
    ch = int(input("Enter your choice:"))

    if ch == 1: user_search()

    elif ch == 2: user_my_account()

    else: main_menu()

def user_search():
    # for asking and searching the info of flights
    L = []
    global source, destination
    source = input("Enter source :").title()
    destination = input("Enter destination :").title()
    sql = "select * from flights where Source = %s and Destination = %s;"
    data =(source,destination)
    cursor.execute(sql,data)
    for i in cursor:
        L.append(i)
    header = ["Flight no.","Flight Name","Source","Desination","Ticket Fare", "Time"]
    print(tabulate(L,headers = header))
    user_confirm()

def user_confirm():
    ch = input("Do you want to continue with your booking? (y/n): ").upper()
    if ch == 'Y':
        booking_id()
        flight_no()
        user_details()
        price_calc()
        seat_no(ticket_qty, flt_no)
        user_invoice()
        save_to_bookings()

    else: user_menu1()

def change_password():
    flag = 0
    while flag == 0:
        name = input("Enter username :")
        old_passw = input("Enter your old password :")
        sql = 'select * from user_login'
        cursor.execute(sql)
        rec = cursor.fetchall()
        for i in rec:
            if i == [name, passw]:
                print("Access granted")
                flag = 1


            else:
                print("Wrong username or password")
                ch = input("Want to try again? (Y/N):").upper
                if ch == 'Y':
                    flag = 0
                else:
                    flag = 2

    if flag == 1:
        new_passw = input("Enter new password :")
        sql = "Update user_login set password = %s where EmailID = %s"
        L = [new_passw, name]
        data = (L)
        cursor.execute(sql, data)
        mydb.commit()

    else:
        main_menu()


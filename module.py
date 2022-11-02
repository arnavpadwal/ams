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
                flt_num = input("Enter flight number : ")
                flt_name = input("Enter flight name : ")
                L = [flt_num, flt_name]
                data = (L)
                sql = "insert into flights (FlightNo, FlightName) values(%s,%s)"
                cursor.execute(sql, data)
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

def admin_choice_modify():
    print("""=================Admin Choice Modify===============
1. modify cabin crew flight number, salary
2. modify staff salary
3. modify security gate number, salary
4. Go back
5. Exit""")
    choice = int(input("Enter operation to be performed : "))
    while choice != '0':
        if choice == '1':
            choice_1 = input("Enter choice to modify cabin crew flight no., salary<1/2/3> : ")
            while choice_1 != '0':
                emp_id = input("Enter employee id whose details need to be modified : ")
                if choice_1 == '1':
                    flt_num = input("Assign new flight no. to employee : ")
                    sql = "update cabin_crew set FlightNo = %s where EmpID = %s"
                    data = ([flt_num, emp_id])
                    cursor.execute(sql, data)
                    mydb.commit()
                elif choice_1 == '2':
                    sal = input("Enter new employee salary : ")
                    sql = "update cabin_crew set Salary = %s where EmpID = %s"
                    data = ([sal, emp_id])
                    cursor.execute(sql, data)
                    mydb.commit()
                else: admin_choice_modify()
                repeat = input("Do you wish to modify more records? : ").upper()
                if repeat == 'N': break
        elif choice == '2':
            emp_id = input("Enter employee id whose details need to be modified : ")
            sal = input("Enter new employee salary : ")
            sql = "update staff set Salary = %s where EmpID = %s"
            data = ([sal, emp_id])
            cursor.execute(sql, data)
            mydb.commit()
        elif choice == '3':
            while True:
                emp_id = input("Enter employee id whose details need to be modified : ")
                sal = input("Enter new employee salary : ")
                sql = "update security set Salary = %s where EmpID = %s"
                data = ([sal, emp_id])
                cursor.execute(sql, data)
                mydb.commit()
        elif choice == '4': admin_choice_modify()
        else: break

#keigan section End-------------------------------------------------------------------

#padwal section START-------------------------------------------------------------------

flight_companies={"EA":"Emirate","LA":"Lufthansa","IA":"Indigo","SA":"SpiceJet"}

def price_calc():
    global fare
    price_dict={"mumbai":46, "delhi":50, "kolkata":60, "chennai":70, "goa":45, "ahmedabad":38, "pune":55, "kanpur":65, "assam":75, "kerala":40}
    fare = price_dict[source.lower()] * price_dict[destination.lower()]
    return(fare)

def booking_id():
    global booking_id
    while True:
        booking_id=random.randint(147922,993784)
        query="select Booking_ID from bookings"
        cursor.execute(query)
        result=cursor.fetchall()
        for i in result:
            if booking_id not in i:
                break
        break
    return booking_id

def user_details():
    global phone, flight_no, ticket_qty, booking_date, flight_date, company_name
    print("\n\nEnter the following details to proceed with the booking:\n\n")
    phone = int(input("Enter phone number: "))
    flight_no = input("Enter flight number of your choice: ")
    for i in flight_companies.keys():
        if flight_no.upper()[0:2] == i[0:2]:
            company_name = flight_companies[i]
            break
        break

    ticket_qty = int(input("Enter the number of tickets to be booked: "))
    booking_date = datetime.date.today()
    flight_date = booking_date + datetime.timedelta(days=3)

def seat_no():
    global seat_no
    allotted_seats = []
    query = "select Seat_No from bookings"  
    cursor.execute(query)
    result=cursor.fetchall()                
    for i in result:
        x = (i[0].split(","))
        for i in x:
            allotted_seats.append(int(i))
    for i in range(ticket_qty):
        while True:
            seat_no=random.randint(1,199)
            if seat_no not in allotted_seats:
                break
            break
    return seat_no

def user_invoice():
    print("""
    
    ******** INVOICE ********

    Name                : %s

    Phone               : %s

    Email ID            : %s

    Booking ID          : %s

    Source              : %s

    Destination         : %s

    Flight No           : %s

    Number of Tickets   : %s

    Seat_No             : %s

    Total_Fare          : %s
    
    """%(name, phone, email_id, booking_id, source, destination, flight_no, ticket_qty, seat_no, fare))

def save_to_bookings(): 
    query = "insert into bookings values(%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s',%s,%s,)"%(booking_id, name, email_id, booking_date, flight_date, source, destination, flight_no, seat_no, company_name, ticket_qty, fare)
    cursor.execute(query)
    mydb.commit()

#padwal section END-------------------------------------------------------------------

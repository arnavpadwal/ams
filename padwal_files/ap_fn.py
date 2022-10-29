import random
import datetime 
import mysql.connector

mydb=mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()

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
import random
import mysql.connector

mydb=mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()

def price_calc():
    price_dict={"mumbai":46, "delhi":50, "kolkata":60, "chennai":70, "goa":45, "ahmedabad":38, "pune":55, "kanpur":65, "assam":75, "kerala":40}
    fare = price_dict[source.lower()] * price_dict[destination.lower()]
    return(price)

def booking_id():
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

def user_invoice():
    print("""
    
    ******** INVOICE ********

    Name                : %s

    Email ID            : %s

    Booking ID          : %s

    Source              : %s

    Destination         : %s

    Flight No           : %s

    Number of Tickets   : %s

    Seat_No             : %s

    Total_Fare          : %s
    
    """%(name, email_id, booking_id(), source, destination, flight_no, ticket_qty, seat_no, price_calc()))


import datetime
import mysql.connector
import random
import tabulate

mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()


def price_calc():
    global fare
    price_dict = {"mumbai": 46, "delhi": 50, "kolkata": 60, "chennai": 70, "panji": 45,
                  "ahmedabad": 38, "pune": 55, "kanpur": 65, "guwahati": 75, "bengaluru": 40}
    ticket_fare = price_dict[source.lower()] * price_dict[destination.lower()] * ticket_qty
    fare = {"EA":ticket_fare*1.15 , "LA":ticket_fare*1.09 , "IA":ticket_fare*1.05 , "SA":ticket_fare*1.07 }

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
    flt_companies = {"EA": "Emirate", "LA": "Lufthansa", "IA": "Indigo", "SA": "SpiceJet"}
    global flt_no
    flt_no = input("\nEnter flight number of your choice: ").upper()
    # check flight number and allot company name accordingly
    flt_codes = flt_companies.keys()
    for i in flt_codes:
        if i == flt_no[0:2]:
            global company_name
            company_name = flt_companies[i]
            is_valid = True
            break


def user_details():
    global phone, ticket_qty, booking_date, flight_date
    # user input
    print("\nEnter the following details to proceed with the booking: ")
    phone = int(input("\nEnter phone number: "))
    is_valid = False
    while is_valid == False:
        print("\nInvalid flight number, enter again:")
        flight_no()
    ticket_qty = int(input("\nEnter the number of tickets to be booked: "))
    booking_date = datetime.date.today()
    flight_date = booking_date + datetime.timedelta(days=3)

def user_bookings():
    print("""================ Bookings ================
    """)

def user_invoice():  # USE TABULATE HERE
    invoice_details_lst = [name, phone, email_id, booking_id, source, destination, flight_no, ticket_qty, seat_no, fare]
    invoice_table = tabulate(invoice_details_lst)

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

    """ % (name, phone, email_id, booking_id, source, destination, flight_no, ticket_qty, seat_no, fare))

def save_to_bookings():
    query = "insert into bookings values(%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s',%s,%s,)" % (
        b_id, name, email_id, booking_date, flight_date, source, destination, flt_no, s_no, company_name,
        ticket_qty, fare)
    cursor.execute(query)
    mydb.commit()

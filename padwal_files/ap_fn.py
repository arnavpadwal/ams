import random
import mysql.connector

mydb=mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()

def price_calc():
    price_dict={"mumbai":46, "delhi":50, "kolkata":60, "chennai":70, "goa":45, "ahmedabad":38, "pune":55, "kanpur":65, "assam":75, "kerala":40}
    price = price_dict[source.lower()] * price_dict[destination.lower()]
    return(price)

def booking_id():
    while True:
        booking_id=random.randint(247922,993784)
        cursor.seek(0)
        query="select Booking_ID from bookings"
        result=cursor.execute(query)
        if booking_id not in result:
            break
    return booking_id
print(booking_id())

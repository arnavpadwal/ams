import random

def price_calc():
    price_dict={"mumbai":46, "delhi":50, "kolkata":60, "chennai":70, "goa":45, "ahmedabad":38, "pune":55, "kanpur":65, "assam":75, "kerala":40}
    price = price_dict[source.lower()] * price_dict[destination.lower()]
    return(price)

def booking_id():
    booking_id=random.randint(247922,993784)
    query="select Booking_ID from user"
    result=cursor.execute(query)
    #if booking_id in 
    return booking_id
print(booking_id())
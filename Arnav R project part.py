def user_access():
    print("""===================User Access===================
1. Login
2. Sign up
3. Exit""")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        flag = 0
        while flag == 0:
            name = input("Enter username : ")
            passw = input("Enter your password : ")
            sql = "select * from user_login"
            cursor.execute(sql)
            rec = cursor.fetchall()
            for i in rec:
                if i == [name, passw]:
                    print("Access granted")
                    flag = 1
                else :
                    print("Wrong username or password has been entered!")
                    repeat = input("Want to try again?<Y/N>: ").upper()
                    if repeat == 'Y':
                        flag = 0
                    else:
                        flag = 2
        if flag == 1: user_menu_1()
        elif flag == 2: exit()
    elif choice == 2: user_signup()
    else: exit()

def user_signup():
    Uid = input("Enter your Email ID : ")
    passwd = input("Create a new password : ")
    data = ([Uid,passwd])
    sql = "insert into user_login values(%s,%s)"
    cursor.execute(sql,data)
    mydb.commit()
    print("Account successfully created")
    user_access()

def user_menu_1():
    print("""=================User Menu 1==================
1. Search flights
2. Check your bookings
3. Exit""")
    choice = int(input("Enter your choice:"))
    if choice == 1: user_search()
    elif choice == 2: user_mybookings()
    else: exit()

def user_search():
    # for asking and searching the info of flights
    source = input("Enter source : ").title
    dest = input("Enter destination : ").title
    sql = "select * from flights"
    cursor.execute(sql)
    rec = cursor.fetchall()
    print("Flight no.",'\t',"Flight Name",'\t',"Source",'\t',"Desination",'\t',"Ticket Fare")
    for i in rec:
        if source and dest in i:
            print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])
    user_confirm()

def user_confirm():
    choice = input("Do you want to finalize/continue your booking?<Y/N> : ").upper()
    if choice == 'Y': user_data()
    else: exit()

def user_allotment(n): # n = tickets_qty
    import random
    L = []
    rows = ['A','B','C','D','E','F']
    for i in range(1,n+1):
        while True:
            x = str(random.randint(1,38))
            y = random.choice(rows)
            seat = str(x + y)
            if seat not in L:
                L.append(seat)
                break
    print("Your seat numbers : ")
    for j in L: print(j, end='')

def change_password():
    flag = 0
    while flag == 0:
        name = input("Enter username : ")
        old_passwd= input("Enter your old password : ")
        sql = 'select * from user_login'
        cursor.execute(sql)
        rec = cursor.fetchall()
        for i in rec:
            if i == [name, old_passwd]:
                print("Access granted")
                flag = 1
            else :
                print("Wrong username or password has been entered!")
                repeat = input("Want to try again?<Y/N> : ").upper()
                if repeat == 'Y':
                    flag = 0
                else:
                    flag = 2
    if flag == 1:
        new_passw = input("Enter new password :")
        sql = "Update user_login set password = %s where EmailID = %s"
        data = ([new_passw, name])
        cursor.execute(sql, data)
        mydb.commit()
    elif flag == 2: exit()
    else: exit()

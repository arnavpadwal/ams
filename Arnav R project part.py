def user_access():
    print("Menu")
    print("1.Login")
    print("2.Sign up")
    print("3.Exit")
    ch = int(input("Enter your choice :"))

    if ch == 1:
        flag = 0
        while flag = 0:
            name = input("Enter username :")
            passw = input("Enter your password :")
            sql = 'select * from user_login'
            cursor.execute(sql)
            rec = cursor.fetchall()
            for i in rec:
                if i == [name, passw]:
                    print("Access granted")
                    flag = 1

                else :
                    print("Wrong username or password")
                    ch = input("Want to try again? (Y/N):").upper
                    if ch == 'Y':
                        flag = 0
                    else:
                        flag = 2

        if flag == 1:
            user_menu1()

        elif flag == 2:
            system_exit()

     elif ch == 2:
         user_signup()

     else:
         system_exit()

def user_signup():
    Uid = input("Enter your Email ID :")
    passw = input("Create a password :")
    L = [Uid,passw]
    data = (L)
    sql = "insert into user_login values(%s,%s)"
    cursor.execute(sql,data)
    mydb.commit()
    print("Account successfully created")
    system_exit()
    
    
def user_menu1():
    print("Menu ")
    print("1.Search")
    print("2.Mybookings")
    print("3.Exit")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        user_search()

    elif ch == 2:
        user_mybookings()

    else:
        system_exit()

def user_search():
    # for asking and searching the info of flights
    source = input("Enter source :").title
    dest = input("Enter destination :").title
    sql = "select * from flights"
    cursor.execute(sql)
    rec = cursor.fetchall()
    print("Flight no.",'\t',"Flight Name",'\t',"Source",'\t',"Desination",'\t',"Ticket Fare")
    for i in rec:
        if source and dest in i:
            print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])

    user_confirm()

def user_confirm():
    ch = input("Do you want to continue with your booking? (Y/N):").upper
    if ch == 'Y':
        user_data()
    else:
        system_exit()


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

    print("Your seat numbers :")
    for j in L:
        print(j,end ='')

def change_password():
     flag = 0
     while flag = 0:
         name = input("Enter username :")
         old_passw = input("Enter your old password :")
         sql = 'select * from user_login'
         cursor.execute(sql)
         rec = cursor.fetchall()
         for i in rec:
             if i == [name, passw]:
                 print("Access granted")
                 flag = 1
                    

                else :
                    print("Wrong username or password")
                    ch = input("Want to try again? (Y/N):").upper
                    if ch == 'Y':
                        flag = 0
                    else:
                        flag = 2

      if flag == 1:
          new_passw = input("Enter new password :")
          sql = "Update user_login set password = %s where EmailID = %s"
          L = [new_passw,name]
          data = (L)
          cursor.execute(sql,data)
          mydb.commit()

      else:
          system_exit()

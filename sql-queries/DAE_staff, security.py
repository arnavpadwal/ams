import random
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()


fst_names = ["Gage","Gisselle","Javion","Aniya","Keira","Joseph""Brice","Dayanara","Quinn","Camryn","Carly","Armani","Amy","Alondra","Rachel","Kylee","Lily","Diego","Allan","River","Trey","Jillian","Darren"]
lst_names = ["Beasley","Delgado","Stephenson","Gilbert","Hubbard","Garrett","Farley","Lutz","Pittman","Woods","Leon","Martinez","Hart","Montes","Rodgers","Foley","Nguyen","Hickman","Larsen","Atkins","Miranda","Blair","Nunez","Khan"]
company=["EA","LA","IA","SA"]
flt_companies = {"EA": "Emirate", "LA": "Lufthansa", "IA": "Indigo", "SA": "SpiceJet"}
letters = ["A", "B", "C", "D"]
first_name = []
taken_names = []
taken_empid = []

flt_codes = flt_companies.keys()

i=1
while i<=500:

    salary = random.randint(30,100)*1000
    gate_no = random.choice(letters)+str(random.randint(1,3))

    while True:
        name = (random.choice(fst_names))+" "+(random.choice(lst_names))
        if name not in taken_names:
            taken_names.append(name)
            break
    while True:
        sec_empid = "SID" + str(random.randint(1111,9997))
        if sec_empid not in taken_empid:
            taken_empid.append(sec_empid)
            break
    while True:
        staff_empid = "LID" + str(random.randint(1111,9997))
        if staff_empid not in taken_empid:
            taken_empid.append(staff_empid)
            break
    
    sql_staff = "insert into staff values('%s','%s',%s)"%(staff_empid,name,salary)
    sql_security = "insert into security values('%s','%s','%s',%s)"%(sec_empid,name,gate_no,salary)
    
    cursor.execute(sql_staff)
    cursor.execute(sql_security)
    mydb.commit()
    i+=1

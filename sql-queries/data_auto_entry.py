import random
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()


fst_names = ["Gage","Gisselle","Javion","Aniya","Keira","Joseph""Brice","Dayanara","Quinn","Camryn","Carly","Armani","Amy","Alondra","Rachel","Kylee","Lily","Diego","Allan","River","Trey","Jillian","Darren"]
lst_name = ["Beasley","Delgado","Stephenson","Gilbert","Hubbard","Garrett","Farley","Lutz","Pittman","Woods","Leon","Martinez","Hart","Montes","Rodgers","Foley","Nguyen","Hickman","Larsen","Atkins","Miranda","Blair","Nunez","Khan"]
emp_dict = {"PID":"Pilot", "AID":"Attendant", "LID":"Staff", "SID":"Security", }
company=["EA","LA","IA","SA"]
sd=["Mumbai","Delhi","Kolkata","Chennai","Panji","Ahmedabad","Pune","Kanpur","Guwahati","Bengaluru"]
flt_companies = {"EA": "Emirate", "LA": "Lufthansa", "IA": "Indigo", "SA": "SpiceJet"}
first_name = []
taken_names = []
taken_flt_no = []
taken_empid = []

flt_codes = flt_companies.keys()

i=1
while i<=500:
    while True:
        name = (random.choice(fst_names))+(random.choice(lst_names))
        if name not in taken_names:
            taken_names.append(name)
            break
    while True:
        flt_no = s + str(random.randint(1001,9998))
        if flt_no not in taken_flt_no:
            taken_flt_no.append(flt_no)
            break
    while True:
        empid = random.choice(emp_dict.keys()) + str(random.randint(0001,9997))
        if empid not in taken_empid:
            taken_empid.append(empid)
            break
    while True:
        dest = random.choice(sd)
        if dest != source:
            break
    for j in flt_codes:
        if j == s:
            company_name = flt_companies[j]

    s = random.choice(company)
    source = random.choice(sd)
    designation = emp_dict(empid[0:3])
    salary = random.randint(30,100)*1000

    
    sql_flt = "insert into flights values('%s','%s','%s','%s')"%(flt_no,company_name,source,dest)
    sql_staff = "insert into staff values('%s','%s','%s',%s)"%(empid,name,designation,salary)
    cursor.execute(sql_flt)
    cursor.execute(sql_staff)
    cursor.execute(sql_security)
    cursor.execute(sql_cabin_crew)
    mydb.commit()
    i+=1

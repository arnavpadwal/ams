import random
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()


fst_names = ["Gage","Gisselle","Javion","Aniya","Keira","Joseph""Brice","Dayanara","Quinn","Camryn","Carly","Armani","Amy","Alondra","Rachel","Kylee","Lily","Diego","Allan","River","Trey","Jillian","Darren"]
lst_names = ["Beasley","Delgado","Stephenson","Gilbert","Hubbard","Garrett","Farley","Lutz","Pittman","Woods","Leon","Martinez","Hart","Montes","Rodgers","Foley","Nguyen","Hickman","Larsen","Atkins","Miranda","Blair","Nunez","Khan"]
emp_dict = {"PID":"Pilot", "AID":"Attendant", "LID":"Staff", "SID":"Security", }
company=["EA","LA","IA","SA"]
sd=["Mumbai","Delhi","Kolkata","Chennai","Panji","Ahmedabad","Pune","Kanpur","Guwahati","Bengaluru"]
flt_companies = {"EA": "Emirate", "LA": "Lufthansa", "IA": "Indigo", "SA": "SpiceJet"}
letters = ["A", "B", "C", "D"]
first_name = []
taken_names = []
taken_flt_no = []
taken_empid = []

flt_codes = flt_companies.keys()

i=1
while i<=500:

    s = random.choice(company)
    source = random.choice(sd)
    
    salary = random.randint(30,100)*1000
    gate_no = random.choice(letters)+str(random.randint(1,3))

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
        key= []
        for k in emp_dict.keys():
            key.append(k)
        empid = random.choice(key) + str(random.randint(1111,9997))
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

    designation = emp_dict[empid[0:3]] 

    
    
    sql_flt = "insert into flights values('%s','%s','%s','%s')"%(flt_no,company_name,source,dest)
    sql_staff = "insert into staff values('%s','%s','%s',%s)"%(empid,name,designation,salary)
    sql_security = "insert into security values('%s','%s','%s',%s)"%(empid,name,gate_no,salary)
    sql_cabin_crew = "insert into cabin_crew values('%s','%s','%s','%s',%s)"%(empid,name,designation,flt_no,salary)
    cursor.execute(sql_flt)
    cursor.execute(sql_staff)
    cursor.execute(sql_security)
    cursor.execute(sql_cabin_crew)
    mydb.commit()
    i+=1

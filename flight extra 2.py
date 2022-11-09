import random
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()

company=["EA","LA","IA","SA"]
sd=["Mumbai","Delhi","Kolkata","Chennai","Panji","Ahmedabad","Pune","Kanpur","Guwahati","Bengaluru"]
flt_companies = {"EA": "Emirate", "LA": "Lufthansa", "IA": "Indigo", "SA": "SpiceJet"}
i=1
flt_codes = flt_companies.keys()

i = 500
for i in range(1,i+1):
    s = random.choice(company)
    flt_no= str(s)+str(random.randint(1001,9998))
    source = random.choice(sd)
    while True:
        dest = random.choice(sd)
        if dest != source: break
    for i in flt_codes:
        if i == s:
            global company_name
            company_name = flt_companies[i]

    data = (flt_no,source,dest,company_name)
    sql = "insert into flights values(%s,%s,%s,%s)"
    cursor.execute(sql,data)
    mydb.commit()


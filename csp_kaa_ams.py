import module
import random
import datetime
import mysql.connector
from tabulate import tabulate
mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='ams')
cursor = mydb.cursor()
print("""=======================================================================================
       Ｗｅｌｃｏｍｅ

            𝑡𝑜

    ✈ 𝑨𝒊𝒓𝒘𝒂𝒚𝒔 𝑴𝒂𝒏𝒂𝒈𝒆𝒎𝒆𝒏𝒕 𝑺𝒚𝒔𝒕𝒆𝒎 ✈️""")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("""𝕊𝕨𝕚𝕗𝕥 𝕥𝕙𝕣𝕠𝕦𝕘𝕙 𝕒𝕚𝕣 𝕝𝕚𝕜𝕖 𝕒 𝕓𝕚𝕣𝕕 𝕨𝕚𝕥𝕙 𝕕𝕚𝕗𝕗𝕖𝕣𝕖𝕟𝕥 𝕒𝕚𝕣𝕝𝕚𝕟𝕖𝕤 𝕠𝕗 𝕪𝕠𝕦𝕣 𝕔𝕙𝕠𝕚𝘤𝕖
=======================================================================================""")

module.main_menu()
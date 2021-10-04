# -*- coding: utf-8 -*-

# import pandas as pd

# data1 = pd.read_excel("dwa_police_report_20180924.xlsx")

# print(data1)

# Dosya Okuma
import sqlite3

def dosyayıOku():
    connection = sqlite3.connect("ddl2.db")
    
    cursor = connection.execute("Select * From recep2")
    data = cursor.fetchall()
    print (data)


dosyayıOku()




    





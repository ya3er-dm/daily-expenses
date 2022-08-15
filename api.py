import sqlite3 as db
import os
import datetime
from tabulate import tabulate

#create database
db = db.connect(r"P:\programming drive\programming\2)python nabegheha , django\python\code py\project1\day_work.db")

#create cursor
c = db.cursor()

def first(num):
    if num in range(1,4):
        print("!!!!!OK!!!!!")
    else:
        print("!!! Just Enter Number INTO 1,2,3 !!!")

#create table
c.execute("""CREATE TABLE IF NOT EXISTS daily_expenses(
            expenses integer,
            doing TEXT COLLATE NOCASE,
            calendars integer,
            clock integer
)""")
#for date and time
data_time = (datetime.datetime.now())

#append in to database
def add(amount , forit , data = data_time.strftime("%Y-%m-%d") , time = data_time.strftime("%H:%M:%S")):
    c.execute("""INSERT INTO daily_expenses VALUES(? , ? , ? , ?)""" , (amount , forit , data , time))
    db.commit()
    print("done.")

#show database
def show(forit = ""):
    if forit == "":

        #show sums expenses
        sums = []
        for i in c.execute("SELECT expenses FROM daily_expenses"):
            for ii in i:
                sums.append(ii)
        print("<><><><><><><><><><><><><><><><>")
        print(f"""Your expenses : {sum(sums)}""")
        print("<><><><><><><><><><><><><><><><>")
        
        #show expenses
        c.execute("SELECT * FROM daily_expenses")
        print(tabulate(c.fetchall()))
        
    else:    
        sums = []
        for i in c.execute("SELECT expenses FROM daily_expenses WHERE doing = :forit" , {"forit":forit}):
            for ii in i:
                sums.append(ii)
        print("<><><><><><><><><><><><><><><><>")
        print(f"""Your expenses : {sum(sums)} ,,,, for = {forit}""")
        print("<><><><><><><><><><><><><><><><>")
        
        
        c.execute("SELECT * FROM daily_expenses WHERE doing = :forit" , {"forit":forit})
        for i in c.fetchall():
            print(i)

def remove(amount,forit):
       with db:
           c.execute("DELETE FROM daily_expenses WHERE expenses = ? AND doing = ?" , (amount,forit))


#update_amount()
def update_amount():
    amount = int(input("Amount: "))
    forit = (input("Forit: "))
    calendars = (input("Calendars: "))
    newamount = int(input("New Amount: "))
    with db:
        c.execute("""UPDATE daily_expenses SET expenses = :newamount 
        WHERE expenses = :amount AND doing = :forit AND calendars = :calendars""",
        {"newamount": newamount, "amount" : amount , "forit" : forit , "calendars" : calendars})

def update_forit():
    amount = int(input("Amount: "))
    forit = (input("Forit: "))
    calendars = (input("Calendars: "))
    newforit = (input("New ForIt: "))
    with db:
        c.execute("""UPDATE daily_expenses SET doing = :newforit 
        WHERE expenses = :amount AND doing = :forit AND calendars = :calendars""",
        {"newforit": newforit, "amount" : amount , "forit" : forit , "calendars" : calendars})

def calculator():
    pass

#test project
#update_forit()
#add(255 , "P")
#remove(255 , "P")
show()

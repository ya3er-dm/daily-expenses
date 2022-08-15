import sqlite3 as db
import os
import api

#intro
os.system("cls")
print("""
--------------------WELCOME TO APP---------------------
------------You can save your daily expenses-----------
^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^&^
            1) Show
            2) Add
            3) Remove
            4) Update = 2 more""")

num = (int(input("Enter a number:")))
api.first(num)

if num == 1:
    forit = input("""you need enter forit?
                     (if yes type you forit if no just press enter.):""")
    api.show(forit)
elif num == 2:
    #amount
    amount = int(input("amount:"))
    #forit
    forit = input("forit:")
    ################
    api.add(amount , forit) 
elif num == 3:
    #remove
    amount = int(input("amount:"))
    forit = input("forit:")
    api.remove(amount , forit)
elif num == 4:
    print("""
        #@#@#@#@ UPDATED @#@#@#@#
        1) Update AMOUNT
        2) Update FORIT
    """)
    num1 = int(input("enter number :"))
    if num1 == 1:
        api.update_amount()
    elif num1 == 2:
        api.update_forit()
    else:
        print("Just Enter Number in 1 or 2")        

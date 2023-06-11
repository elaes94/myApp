import os

while True:
    value = input("Create 1 | Read 2 | Update 3 | Delete 4 \n")
    if value == '1':
        os.system("sqlite3 mydb.db '.read create.sql'")
    elif value == '2':
        os.system("sqlite3 mydb.db '.mode box' '.read select.sql'")
    elif value == '3':
        os.system("sqlite3 mydb.db '.read insert.sql'")
    elif value == '4':
        os.system("sqlite3 mydb.db '.read delete.sql'")
    else:
        break

print("end")
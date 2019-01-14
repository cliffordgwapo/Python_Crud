import pymysql
import sys
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='momoland',
)
def add():
    name = input("Enter food name: ")
    price = input("Add food price: ")
    description = input("Enter some description of the food: ")
 
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO food (`name`, `price`, `description`) VALUES (%s, %s, %s)"
            try:
                cursor.execute(sql, (name, price, description))
                print("Task added successfully")
            except:
                print("Oops! Something wrong")
                
        connection.commit()
    finally:
        print ("\n")
        return

def read():
    print ("DATA\n")
    try:
        with connection.cursor() as cursor:
            sql = "select * from food"
            cursor.execute(sql)
            connection.commit()
            results = cursor.fetchall()
            print("Id\tName\t\t\tPrice\t\t\tDescription")
            print("---------------------------------------------------------------------------")
            for row in results :
                print(str(row[0]) + "\t" + row[1] + "\t\t\t" , (row[2]) , "\t\t\t" + row[3])

        connection.commit()
    finally:
        print ("")
        return
def update():
    read()
    print("")
    id = input("Enter the id of the food to update: ")
    name = input("Enter new name: ")
    price = input("Enter new price: ")
    description = input("Enter new description: ")
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE food SET `name`=%s, `price`=%s , `description`=%s WHERE `id` = %s"
            try:
                cursor.execute(sql, (name, price, description, id))
                print("Successfully Updated...")
            except:
                print("Oops! Something wrong")
 
        connection.commit()
    finally:
        print ("")
        return
def delete():
    read()
    print("")
    id = input("Enter the id of the food to delete: ")
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM food WHERE id = %s"
            try:
                cursor.execute(sql, (id))
                print("Successfully Deleted...")
            except:
                print("Oops! Something wrong")
 
        connection.commit()
    finally:
        print ("")
        return
def search():
    print("\n")
    id = input("Enter the food id you want to search: ")
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from food WHERE id = %s"
            try:
                cursor.execute(sql, (id))
                result = cursor.fetchall()
                print("Id\tName\t\t\tPrice\t\t\tDescription")
                print("---------------------------------------------------------------------------")
                for row in result:
                    print(str(row[0]) + "\t" + row[1] + "\t\t\t" , (row[2]) , "\t\t\t" + row[3])
            except:
                print("Oops! Something wrong")

        connection.commit()
    finally:
        print("")
        return
def logoff():
    sys.exit(0)

choice = 1
while choice:
    print ("***WELCOME TO KUSINA ONLINE***\n\n")
    print ("[1] = Create a new data\n")
    print ("[2] = Read data\n")
    print ("[3] = Update data\n")
    print ("[4] = Delete data\n")
    print ("[5] = Search data\n")
    print ("[6] = Log off\n")

    choice = input("Choices: ")

    if choice == "1":
        add()
    elif choice == "2":
        read()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        search()
    elif choice == "6":
        logoff()
        
    else:
        print ("Invalid Input!\n")
        choice = 1

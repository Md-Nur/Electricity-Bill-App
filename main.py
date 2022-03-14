from tkinter import *

import mysql.connector
# from PIL import ImageTk, Image
root = Tk()
NAME = "Electrical Bill"
FONT = ("Helvetica",20)
ROW = 0

room_101 = IntVar()
room_201 = IntVar()
room_202 = IntVar()
room_401 = IntVar()
room_402 = IntVar()
room_403 = IntVar()
room_404 = IntVar()


def dataBase():
    print("DataBase")
    conn = mysql.connector.connect(host="localhost", user="root", password="khelahobe", database="test_elec_bill")
    cursor = conn.cursor()
    # cursor.execute("select * from test_elec_bill.electricity;")
    cursor.execute("INSERT INTO `test_elec_bill`.`electricity` (`id`, `Month`, `Unit`) VALUES (%s,%s,%s);", (1, "January", room_101.get()))
    # cursor.execute('show databases')

    conn.commit()
    
    print(cursor.fetchall(),"Done")
    for i in cursor.fetchall():
        print(i)
    if conn:
        print("Connected")
    conn.close()
def displayUnit():
    global room_101, room_201, room_202, room_401, room_402, room_403, room_404,ROW
    
    try:
        room_101.set(int(room101_unit.get()))
        room_201.set(int(room201_unit.get()))
        room_202.set(int(room202_unit.get()))
        room_401.set(int(room401_unit.get()))
        room_402.set(int(room402_unit.get()))
        room_403.set(int(room403_unit.get()))
        room_404.set(int(room404_unit.get()))
        room_101_label = Label(root, textvariable=room_101, font=FONT)
        room_101_label.grid(row=ROW, column=0)
        ROW+=1
        room_201_label = Label(root, textvariable=room_201, font=FONT)
        room_201_label.grid(row=ROW, column=0)
        ROW+=1
        room_202_label = Label(root, textvariable=room_202, font=FONT)
        room_202_label.grid(row=ROW, column=0)
        ROW+=1
        room_401_label = Label(root, textvariable=room_401, font=FONT)
        room_401_label.grid(row=ROW, column=0)
        ROW+=1
        room_402_label = Label(root, textvariable=room_402, font=FONT)
        room_402_label.grid(row=ROW, column=0)
        ROW+=1
        room_403_label = Label(root, textvariable=room_403, font=FONT)
        room_403_label.grid(row=ROW, column=0)
        ROW+=1
        room_404_label = Label(root, textvariable=room_404, font=FONT)
        room_404_label.grid(row=ROW, column=0)
        ROW+=1
        dataBase()
    except Exception as e:
        err = Label(root, text=f"{e}: \nPlease enter a number / You have to fill all the fields", font=FONT)
        err.grid(row=ROW, column=0, columnspan=2)
        ROW+=1



    
    
    
root.geometry("1000x500")
root.minsize(1000, 500)
root.title(NAME)
title = Label(root, text=NAME, font=('Arial', 30))
title.grid(row=ROW, column=0, columnspan=2)
ROW+=1
# [101,201,202,401,402,403,40
room101_label = Label(root, text="Enter Unit For 101:", font=FONT)
room101_label.grid(row=ROW, column=0)
room101_unit = Entry(root, font=FONT)
room101_unit.grid(row=ROW, column=1)
ROW+=1
room201_label = Label(root, text="Enter Unit For 201:", font=FONT)
room201_label.grid(row=ROW, column=0)
room201_unit = Entry(root, font=FONT)
room201_unit.grid(row=ROW, column=1)
ROW+=1
room202_label = Label(root, text="Enter Unit For 202:", font=FONT)
room202_label.grid(row=ROW, column=0)
room202_unit = Entry(root, font=FONT)
room202_unit.grid(row=ROW, column=1)
ROW+=1
room401_label = Label(root, text="Enter Unit For 401:", font=FONT)
room401_label.grid(row=ROW, column=0)
room401_unit = Entry(root, font=FONT)
room401_unit.grid(row=ROW, column=1)
ROW+=1
room402_label = Label(root, text="Enter Unit For 402:", font=FONT)
room402_label.grid(row=ROW, column=0)
room402_unit = Entry(root, font=FONT)
room402_unit.grid(row=ROW, column=1)
ROW+=1
room403_label = Label(root, text="Enter Unit For 403:", font=FONT)
room403_label.grid(row=ROW, column=0)
room403_unit = Entry(root, font=FONT)
room403_unit.grid(row=ROW, column=1)
ROW+=1
room404_label = Label(root, text="Enter Unit For 404:", font=FONT)
room404_label.grid(row=ROW, column=0)
room404_unit = Entry(root, font=FONT)
room404_unit.grid(row=ROW, column=1)
ROW+=1

b1 = Button(root, text="Submit", command=displayUnit,padx=10,pady=10,font=FONT,fg='white',bg='blue')
b1.grid(row=ROW,column=0,columnspan=2,padx=10,pady=10)
ROW+=1

root.mainloop()
from datetime import datetime
from re import L
from tkinter import *
from tkinter import ttk

import mysql.connector
# from PIL import ImageTk, Image
Database = "test_elec_bill"

def dataBase():
    global room_101, room_102, room_103, room_201, room_202, room_203, room_401, room_402, room_403, room_404
    room_list = [room_101, room_102, room_103, room_201, room_202, room_203, room_401, room_402, room_403, room_404]
    room_units = [room.room_unit.get() for room in room_list]
    room_units.extend([month.get(), year.get()])
    print(room_units)
    pmon = months[months.index(month.get())-1]
    pyear = year.get()
    if pmon == "December":
        pyear -= 1
    
    conn = mysql.connector.connect(host="localhost", user="root", password="khelahobe", database=Database)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO `test_elec_bill`.`miter` (`1st_main`, `1st_sub1`, `1st_sub2`, `2nd_main`, `2nd_sub1`, `2nd_sub2`, `4th_sub1`, `4th_sub2`, `4th_sub3`, `4th_sub4`,  `month`, `year`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", tuple(room_units))
    
    collect = conn.cursor()
    collect.execute("SELECT * FROM `test_elec_bill`.`miter` WHERE `month`=%s AND `year`=%s;", (pmon, year.get()))
    pdata = collect.fetchall()[0][1:11]
    
    print(pdata)
    
    room_net_units = []
    for rl,rp in zip(room_list,pdata):
        room_net_units.append(int(rl.room_unit.get()) - rp)
    print(room_net_units)
    
    
    conn.commit()
    conn.close()
    
    
def displayUnit():
    global room_101, room_201, room_202, room_401, room_402, room_403, room_404
    roomList = [room_101, room_201, room_202, room_401, room_402, room_403, room_404]
    for rl in roomList:
        print(rl.room_unit.get())
    print(month.get(), year.get())

class room():
    def __init__(self,room_no):
        global row,tableFrame
        self.room_no = room_no
        self.room_label = Label(tableFrame, text=f"{room_no} :", font=FONT)
        self.room_label.grid(row=row, column=0,padx=5,pady=5)
        
        self.room_unit = Entry(tableFrame, font=FONT)
        self.room_unit.grid(row=row, column=1 , padx=5,pady=5)
        
        self.room_fare = Entry(tableFrame, font=FONT)
        self.room_fare.grid(row=row, column=2 , padx=5,pady=5)
        self.room_fare.insert(0,5000)
        
        self.room_advance = Entry(tableFrame, font=FONT)
        self.room_advance.grid(row=row, column=3 , padx=5,pady=5)
        self.room_advance.insert(0,0)
        row+=1
    
    
    
if __name__ == '__main__':
    root = Tk()
    FONT = ("Helvetica",15)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    root.geometry("1000x500")
    root.minsize(1000, 500)
    root.title("ঘর ভাড়া ও বিদ্যুৎ বিল")

    titleFrame = Frame(root)
    titleFrame.pack()

    title = Label(titleFrame, text="✨ঘর ভাড়া ও বিদ্যুৎ বিল✨", font=('Arial', 30),padx=10,pady=10)
    title.pack()

    row = 0
    tableFrame = Frame(root,padx=10,pady=10)
    tableFrame.pack()

    table_name_title = Label(tableFrame, text="রুমের নাম", font=FONT)
    table_unit_title = Label(tableFrame, text="মিটারের ইউনিট", font=FONT)
    table_fare_title = Label(tableFrame, text="ঘর ভাড়া", font=FONT)
    table_advance_title = Label(tableFrame, text="অগ্রীম (যদি থাকে)", font=FONT)
    table_name_title.grid(row=row, column=0,padx=5,pady=5)
    table_unit_title.grid(row=row, column=1,padx=5,pady=5)
    table_fare_title.grid(row=row, column=2,padx=5,pady=5)
    table_advance_title.grid(row=row, column=3,padx=5,pady=5)
    row+=1
    
    room_101 = room("নিচ তলার সাব ১ (টিনশেড) নং")
    room_102 = room("নিচ তলার সাব ২ নং")
    room_103 = room("নিচ তলার মেইন")
    room_201 = room("২ তলার সাব ১ নং")
    room_202 = room("২ তলার সাব ২ নং")
    room_203 = room("২ তলার মেইন")
    room_401 = room("৪ তলার সাব ১ নং")
    room_402 = room("৪ তলার সাব ২ নং")
    room_403 = room("৪ তলার সাব ৩ নং")
    room_404 = room("৪ তলার সাব ৪ নং")
    
    tableFrame2 =Frame(root,padx=10,pady=10)
    tableFrame2.pack()
    month_label = Label(tableFrame2, text="মাসঃ ", font=FONT)
    month_label.grid(row=0, column=0,padx=5,pady=5)
    month = ttk.Combobox(tableFrame2,font=FONT, values=months)
    month.current(datetime.now().month-2)
    month.grid(row=0,column=1,padx=5,pady=5)
    
    year_label = Label(tableFrame2, text="বছরঃ ", font=FONT)
    year_label.grid(row=0, column=2,padx=5,pady=5)
    year = Entry(tableFrame2, font=FONT)
    year.insert(0,datetime.now().year)
    year.grid(row=0,column=3,padx=5,pady=5)
    
    rate_label = Label(tableFrame2, text="রেটঃ ", font=FONT)
    rate_label.grid(row=0, column=4,padx=5,pady=5)
    rate = Entry(tableFrame2, font=FONT)
    rate.insert(0,5.45)
    rate.grid(row=0,column=5,padx=5,pady=5)
    
    buttonFrame = Frame(root,padx=10,pady=10)
    buttonFrame.pack()
    button = Button(buttonFrame, text="সাবমিট", font=FONT, command=dataBase)
    button.pack()
    root.mainloop()
    

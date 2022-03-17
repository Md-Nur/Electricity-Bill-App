from datetime import datetime
from re import L
from tkinter import *
from tkinter import ttk

import mysql.connector
# from PIL import ImageTk, Image
Database = "test_elec_bill"

def preData(roomNo):
    global pmon ,room_101, room_102, room_103, room_201, room_202, room_203, room_401, room_402, room_403, room_404,months
    cpmon = months[datetime.now().month-3]
    conn = mysql.connector.connect(host="localhost", user="root", password="khelahobe", database=Database)
    
    room_collect = conn.cursor()
    room_collect.execute("SELECT * FROM `test_elec_bill`.`room` WHERE `month`=%s AND `year`=%s AND `room_no` = %s;", (cpmon, datetime.now().year,roomNo))
    
    pRoomData = room_collect.fetchall()[0]
    print(pRoomData)
    conn.commit()
    conn.close()
    return pRoomData
    # room_insert.execute("INSERT INTO `test_elec_bill`.`room` ( `room_no`, `year`, `month`, `name`, `rate`, `room_fare`, `room_unit`, `room_advance`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);" ( '101', '2022', month.get(), 'শরীফ', '5.45', '7500', '34556', '0'))


def dbRoom(room_net_units):
    global pmon ,room_101, room_102, room_103, room_201, room_202, room_203, room_401, room_402, room_403, room_404,months
    
    room_list = [room_101, room_102, room_103, room_201, room_202, room_203, room_401, room_402, room_403, room_404]
    
    conn = mysql.connector.connect(host="localhost", user="root", password="khelahobe", database=Database)
    room_insert = conn.cursor()
    
    for rnu,rl in zip(room_net_units,room_list):
        inpt = (int(rl.room_no[:3]),year.get() , month.get(), rl.room_name, rate.get(), rl.room_fare.get(), rnu, rl.room_advance.get())
        room_insert.execute("INSERT INTO `test_elec_bill`.`room` ( `room_no`, `year`, `month`, `name`, `rate`, `room_fare`, `room_unit`, `room_advance`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);",inpt )
    # INSERT INTO `test_elec_bill`.`room` (`room_no`, `year`, `month`, `name`, `rate`, `room_fare`, `room_unit`, `room_advance`) VALUES ('101', '2021', 'December', 'Shorif', '5.45', '7500', '3400', '0');
    print("Data Inserted")
    conn.commit()
    conn.close()


def dataBase():
    global pmon ,room_101, room_102, room_103, room_201, room_202, room_203, room_401, room_402, room_403, room_404,months
    pmon = months[months.index(month.get())-1]
    
    room_list = [room_101, room_102, room_103, room_201, room_202, room_203, room_401, room_402, room_403, room_404]
    room_units = [room.room_unit.get() for room in room_list]
    room_units.extend([month.get(), year.get()])
    print(room_units)
    
    conn = mysql.connector.connect(host="localhost", user="root", password="khelahobe", database=Database)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO `test_elec_bill`.`miter` (`1st_main`, `1st_sub1`, `1st_sub2`, `2nd_main`, `2nd_sub1`, `2nd_sub2`, `4th_sub1`, `4th_sub2`, `4th_sub3`, `4th_sub4`,  `month`, `year`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", tuple(room_units))

    collect = conn.cursor()
    collect.execute("SELECT * FROM `test_elec_bill`.`miter` WHERE `month`=%s AND `year`=%s;", (pmon, year.get()))
    try:
        pdata = collect.fetchall()[0][1:11]
    except IndexError:
        pdata = pmon
    print(pdata)
    
    room_net_units = []
    for rl,rp in zip(room_list,pdata):
        room_net_units.append(int(rl.room_unit.get()) - rp)
    room_net_units[2] = room_net_units[2] - room_net_units[1]
    room_net_units[5] = room_net_units[5] - room_net_units[4] - room_net_units[3]
    print(room_net_units)
    conn.commit()
    conn.close()
    dbRoom(room_net_units)
    
    
def displayUnit():
    global room_101, room_201, room_202, room_401, room_402, room_403, room_404
    roomList = [room_101, room_201, room_202, room_401, room_402, room_403, room_404]
    for rl in roomList:
        print(rl.room_unit.get())
    print(month.get(), year.get())

class room():
    def __init__(self,room_no,room_name,room_fare):
        global row,tableFrame
        self.room_name = room_name
        
        self.room_no = room_no
        self.room_label = Label(tableFrame, text=f"{self.room_name} ({self.room_no}) :", font=FONT)
        self.room_label.grid(row=row, column=0,padx=5,pady=5)
        
        self.room_unit = Entry(tableFrame, font=FONT)
        self.room_unit.grid(row=row, column=1 , padx=5,pady=5)
        
        self.room_fare = Entry(tableFrame, font=FONT)
        self.room_fare.grid(row=row, column=2 , padx=5,pady=5)
        self.room_fare.insert(0,room_fare)
        
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
    
    pr101 = preData(101)
    room_101 = room("101 নিচ তলার সাব ১ (টিনশেড) নং",room_name=pr101[4],room_fare=pr101[-3])
    pr102 = preData(102)
    room_102 = room("102 নিচ তলার সাব ২ নং",room_name=pr102[4],room_fare=pr102[-3])
    pr103 = preData(103)
    room_103 = room("103 নিচ তলার মেইন",room_name=pr103[4],room_fare=pr103[-3])
    pr201 = preData(201)
    room_201 = room("201 ২ তলার সাব ১ নং",room_name=pr201[4],room_fare=pr201[-3])
    pr202 = preData(202)
    room_202 = room("202 ২ তলার সাব ২ নং",room_name=pr202[4],room_fare=pr202[-3])
    pr203 = preData(203)
    room_203 = room("203 ২ তলার মেইন",room_name=pr203[4],room_fare=pr203[-3])
    pr401 = preData(401)
    room_401 = room("401 ৪ তলার সাব ১ নং",room_name=pr401[4],room_fare=pr401[-3])
    pr402 = preData(402)
    room_402 = room("402 ৪ তলার সাব ২ নং",room_name=pr402[4],room_fare=pr402[-3])
    pr403 = preData(403)
    room_403 = room("403 ৪ তলার সাব ৩ নং",room_name=pr403[4],room_fare=pr403[-3])
    pr404 = preData(404)
    room_404 = room("404 ৪ তলার সাব ৪ নং",room_name=pr404[4],room_fare=pr404[-3])
    
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
    rate.insert(0,pr102[-4])
    rate.grid(row=0,column=5,padx=5,pady=5)
    
    buttonFrame = Frame(root,padx=10,pady=10)
    buttonFrame.pack()
    button = Button(buttonFrame, text="সাবমিট", font=FONT, command=dataBase)
    button.pack()
    root.mainloop()
    

from datetime import datetime
from tkinter import *
from tkinter import ttk

import mysql.connector
# from PIL import ImageTk, Image
Database = "test_elec_bill"

def dataBase():
    global room_101, room_201, room_202, room_401, room_402, room_403, room_404
    pmon = months[months.index(month.get())-1]
    print("DataBase")
    conn = mysql.connector.connect(host="localhost", user="root", password="khelahobe", database=Database)
    cursor = conn.cursor()
    # cursor.execute("select * from test_elec_bill.electricity;")
    
    # Query Demo : INSERT INTO `test_elec_bill`.`miter` (`1st_main`, `1st_sub1`, `1st_sub2`, `2nd_main`, `2nd_sub1`, `2nd_sub2`, `4th_sub1`, `4th_sub2`, `4th_sub3`, `4th_sub4`,  `month`, `year`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);

    cursor.execute("INSERT INTO `test_elec_bill`.`miter` (`1st_main`, `1st_sub1`, `1st_sub2`, `2nd_main`, `2nd_sub1`, `2nd_sub2`, `4th_sub1`, `4th_sub2`, `4th_sub3`, `4th_sub4`,  `month`, `year`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (room_101.room_unit.get(),room_102.room_unit.get(),room_103.room_unit.get(),room_201.room_unit.get(),room_202.room_unit.get(),room_203.room_unit.get(),room_401.room_unit.get(),room_402.room_unit.get(),room_403.room_unit.get(),room_404.room_unit.get(),month.get(),year.get()))
    # cursor.execute('show databases')
    collect = conn.cursor()
    collect.execute(f"SELECT * FROM `test_elec_bill`.`miter` WHERE `month`={pmon} AND `year`={year};")
    print(collect.fetchall(),"Done")
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
        self.room_label = Label(tableFrame, text=f"{room_no} মিটারের ইউনিটঃ ", font=FONT)
        self.room_label.grid(row=row, column=0,padx=5,pady=5)
        self.room_unit = Entry(tableFrame, font=FONT)
        self.room_unit.grid(row=row, column=1)
        row+=1
    
    
    
if __name__ == '__main__':
    root = Tk()
    FONT = ("Helvetica",15)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    root.geometry("1000x500")
    root.minsize(1000, 500)
    root.title("বিদ্যুৎ বিল")

    titleFrame = Frame(root)
    titleFrame.pack()

    title = Label(titleFrame, text="✨বিদ্যুৎ বিল✨", font=('Arial', 30),padx=10,pady=10)
    title.pack()

    row = 0
    tableFrame = Frame(root,padx=10,pady=10)
    tableFrame.pack()

    
    room_101 = room("নিচ তলার মেইন")
    room_102 = room("নিচ তলার সাব ১ নং")
    room_103 = room("নিচ তলার সাব ২ নং")
    room_201 = room("২ তলার মেইন")
    room_202 = room("২ তলার সাব ১ নং")
    room_203 = room("২ তলার সাব ২ নং")
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
    

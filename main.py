from datetime import datetime
from tkinter import *
from tkinter import ttk
import mysql.connector
from db import *
from room_miter import *


def preData(roomNo):
    global pmon, room_101, room_102, room_103, room_201, room_202, room_203, room_401, room_402, room_403, room_404, months
    cpmon = months[datetime.now().month - 3]
    conn = mysql.connector.connect(
        host=Host, user=User, password=Password, database=Database
    )

    room_collect = conn.cursor()
    room_collect.execute(
        "SELECT * FROM `test_elec_bill`.`room` WHERE `month`=%s AND `year`=%s AND `room_no` = %s;",
        (cpmon, datetime.now().year, roomNo),
    )

    pRoomData = room_collect.fetchall()[-1]
    conn.commit()
    conn.close()
    # print(pRoomData)
    return pRoomData


def callBack():
    dbMiter(
        month,
        year,
        rate,
        room_101,
        room_102,
        room_103,
        room_201,
        room_202,
        room_203,
        room_401,
        room_402,
        room_403,
        room_404,
    )


class room:
    def __init__(
        self,
        room_no,
        room_name,
        room_fare,
        room_dust,
        room_kichen,
        room_toylet,
        room_frize,
    ):
        global row, tableFrame
        self.room_name = room_name

        self.room_no = room_no
        self.room_label = Label(
            tableFrame, text=f"{self.room_name} ({self.room_no}) :", font=FONT
        )
        self.room_label.grid(row=row, column=0, padx=5, pady=5)

        self.room_unit = Entry(tableFrame, font=FONT, width=10)
        self.room_unit.grid(row=row, column=1, padx=5, pady=5)

        self.room_fare = Entry(tableFrame, font=FONT, width=10)
        self.room_fare.grid(row=row, column=2, padx=5, pady=5)
        self.room_fare.insert(0, room_fare)

        self.room_advance = Entry(tableFrame, font=FONT, width=10)
        self.room_advance.grid(row=row, column=3, padx=5, pady=5)
        self.room_advance.insert(0, 0)

        self.room_dust = Entry(tableFrame, font=FONT, width=10)
        self.room_dust.grid(row=row, column=4, padx=5, pady=5)
        self.room_dust.insert(0, room_dust)

        self.room_kichen = Entry(tableFrame, font=FONT, width=10)
        self.room_kichen.grid(row=row, column=5, padx=5, pady=5)
        self.room_kichen.insert(0, room_kichen)

        self.room_toylet = Entry(tableFrame, font=FONT, width=10)
        self.room_toylet.grid(row=row, column=6, padx=5, pady=5)
        self.room_toylet.insert(0, room_toylet)

        self.room_frize = Entry(tableFrame, font=FONT, width=10)
        self.room_frize.grid(row=row, column=7, padx=5, pady=5)
        self.room_frize.insert(0, room_frize)
        row += 1


if __name__ == "__main__":
    root = Tk()
    root.iconbitmap(r"thunder.ico")
    photo = PhotoImage(file="ph.png")
    img = Label(root, image=photo)
    img.place(x = 0, y = 0)
    FONT = ("Helvetica", 15)
    months = [
        "জানুয়ারি",
        "ফেব্রুয়ারি",
        "মার্চ",
        "এপ্রিল",
        "মে",
        "জুন",
        "জুলাই",
        "আগস্ট",
        "সেপ্টেম্বর",
        "অক্টোবর",
        "নভেম্বর",
        "ডিসেম্বর",
    ]

    root.title("ঘর ভাড়া ও বিদ্যুৎ বিল")
    
    titleFrame = Frame(root)
    titleFrame.pack()


    title = Label(
        titleFrame, text="⚡ঘর ভাড়া ও বিদ্যুৎ বিল⚡", font=("Arial", 30), padx=10, pady=10,bg="lightblue"
    )
    title.pack()

    row = 0
    tableFrame = Frame(root, padx=10, pady=10, bd=5, relief=GROOVE, bg="purple")
    tableFrame.pack()

    table_name_title = Label(tableFrame, text="রুমের নাম", font=FONT)
    table_unit_title = Label(tableFrame, text="মিটারের ইউনিট", font=FONT)
    table_fare_title = Label(tableFrame, text="ঘর ভাড়া", font=FONT)
    table_advance_title = Label(tableFrame, text="অগ্রীম (যদি থাকে)", font=FONT)
    table_dust_title = Label(tableFrame, text="ময়লার বিল", font=FONT)
    table_kichen_title = Label(tableFrame, text="রান্নাঘর", font=FONT)
    table_toylet_title = Label(tableFrame, text="টয়লেট", font=FONT)
    table_frize_title = Label(tableFrame, text="ফ্রিজ", font=FONT)

    table_name_title.grid(row=row, column=0, padx=5, pady=5)
    table_unit_title.grid(row=row, column=1, padx=5, pady=5)
    table_fare_title.grid(row=row, column=2, padx=5, pady=5)
    table_advance_title.grid(row=row, column=3, padx=5, pady=5)
    table_dust_title.grid(row=row, column=4, padx=5, pady=5)
    table_kichen_title.grid(row=row, column=5, padx=5, pady=5)
    table_toylet_title.grid(row=row, column=6, padx=5, pady=5)
    table_frize_title.grid(row=row, column=7, padx=5, pady=5)
    row += 1

    pr101 = preData(101)
    room_101 = room(
        "101 নিচ তলার সাব ১ (টিনশেড) নং",
        room_name=pr101[4],
        room_fare=pr101[6],
        room_dust=pr101[-5],
        room_kichen=pr101[-4],
        room_toylet=pr101[-3],
        room_frize=pr101[-2],
    )
    pr102 = preData(102)
    room_102 = room(
        "102 নিচ তলার সাব ২ নং",
        room_name=pr102[4],
        room_fare=pr102[7],
        room_dust=pr102[-5],
        room_kichen=pr102[-4],
        room_toylet=pr102[-3],
        room_frize=pr102[-2],
    )
    pr103 = preData(103)
    room_103 = room(
        "103 নিচ তলার মেইন",
        room_name=pr103[4],
        room_fare=pr103[7],
        room_dust=pr103[-5],
        room_kichen=pr103[-4],
        room_toylet=pr103[-3],
        room_frize=pr103[-2],
    )
    pr201 = preData(201)
    room_201 = room(
        "201 ২ তলার সাব ১ নং",
        room_name=pr201[4],
        room_fare=pr201[7],
        room_dust=pr201[-5],
        room_kichen=pr201[-4],
        room_toylet=pr201[-3],
        room_frize=pr201[-2],
    )
    pr202 = preData(202)
    room_202 = room(
        "202 ২ তলার সাব ২ নং",
        room_name=pr202[4],
        room_fare=pr202[7],
        room_dust=pr202[-5],
        room_kichen=pr202[-4],
        room_toylet=pr202[-3],
        room_frize=pr202[-2],
    )
    pr203 = preData(203)
    room_203 = room(
        "203 ২ তলার মেইন",
        room_name=pr203[4],
        room_fare=pr203[7],
        room_dust=pr203[-5],
        room_kichen=pr203[-4],
        room_toylet=pr203[-3],
        room_frize=pr203[-2],
    )
    pr401 = preData(401)
    room_401 = room(
        "401 ৪ তলার সাব ১ নং",
        room_name=pr401[4],
        room_fare=pr401[7],
        room_dust=pr401[-5],
        room_kichen=pr401[-4],
        room_toylet=pr401[-3],
        room_frize=pr401[-2],
    )
    pr402 = preData(402)
    room_402 = room(
        "402 ৪ তলার সাব ২ নং",
        room_name=pr402[4],
        room_fare=pr402[7],
        room_dust=pr402[-5],
        room_kichen=pr402[-4],
        room_toylet=pr402[-3],
        room_frize=pr402[-2],
    )
    pr403 = preData(403)
    room_403 = room(
        "403 ৪ তলার সাব ৩ নং",
        room_name=pr403[4],
        room_fare=pr403[7],
        room_dust=pr403[-5],
        room_kichen=pr403[-4],
        room_toylet=pr403[-3],
        room_frize=pr403[-2],
    )
    pr404 = preData(404)
    room_404 = room(
        "404 ৪ তলার সাব ৪ নং",
        room_name=pr404[4],
        room_fare=pr404[7],
        room_dust=pr404[-5],
        room_kichen=pr404[-4],
        room_toylet=pr404[-3],
        room_frize=pr404[-2],
    )

    tableFrame2 = Frame(root, padx=10, pady=10, bg="purple", relief=GROOVE)
    tableFrame2.pack()
    month_label = Label(tableFrame2, text="মাসঃ ", font=FONT)
    month_label.grid(row=0, column=0, padx=5, pady=5)
    month = ttk.Combobox(tableFrame2, font=FONT, values=months)
    month.current(datetime.now().month - 2)
    month.grid(row=0, column=1, padx=5, pady=5)

    year_label = Label(tableFrame2, text="বছরঃ ", font=FONT)
    year_label.grid(row=0, column=2, padx=5, pady=5)
    year = Entry(tableFrame2, font=FONT)
    year.insert(0, datetime.now().year)
    year.grid(row=0, column=3, padx=5, pady=5)

    rate_label = Label(tableFrame2, text="রেটঃ ", font=FONT)
    rate_label.grid(row=0, column=4, padx=5, pady=5)
    rate = Entry(tableFrame2, font=FONT)
    rate.insert(0, pr101[5])
    rate.grid(row=0, column=5, padx=5, pady=5)

    buttonFrame = Frame(root, padx=10, pady=10, bg="purple")
    buttonFrame.pack()
    button = Button(buttonFrame, text="সাবমিট", font=FONT, command=callBack, width=10, height=2, bg="green", fg="white", relief=GROOVE, bd=2, activebackground="green", activeforeground="white", cursor="hand2", overrelief=SUNKEN)
    button.pack()

    root.mainloop()

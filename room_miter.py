from db import *
import mysql
from page import *

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


def dbRoom(
    room_net_units,
    month,
    year,
    rate,
    pdata,
    pmon,
    room_101,
    room_102,
    room_201,
    room_202,
    room_203,
    room_401,
    room_402,
    room_403,
    room_404,
):
    global months

    net_info_list = []
    room_list = [
        room_101,
        room_102,
        room_201,
        room_202,
        room_203,
        room_401,
        room_402,
        room_403,
        room_404,
    ]

    conn = mysql.connector.connect(
        host=Host, user=User, password=Password, database=Database
    )
    room_insert = conn.cursor()

    for rnu, rl, pd in zip(room_net_units, room_list, pdata):

        inpt = (
            int(rl.room_no[:3]),
            int(year.get()),
            month.get(),
            rl.room_name,
            float(rate.get()),
            int(rl.room_fare.get()),
            rnu,
            int(rl.room_advance.get()),
            int(rl.room_dust.get()),
            int(rl.room_kichen.get()),
            int(rl.room_toylet.get()),
            int(rl.room_frize.get()),
        )
        # int(rl.room_unit.get()),
        # int(pd),
        net_dict = {
            "নাম": rl.room_name,  # name
            "রুম নং": int(rl.room_no[:3]),  # room_no
            "বছর": int(year.get()),  # year
            "ভাড়া": f"{rl.room_fare.get()} টাকা",  # fare
            f"{month.get()}": f"{rl.room_unit.get()} ইউ.",  # month
            f"{pmon}": f"{pd} ইউ.",  # previous month
            "ইউনিট": f"{rnu} ইউ.",  # unit
            "রেট": f"{rate.get()} টাকা",  # rate
            "বিদ্যুৎ বিল": f"{int(float(rate.get()) * rnu)} টাকা",  # bill
            "ময়লা": f"{rl.room_dust.get()} টাকা",  # dust
            "রান্নাঘর": f"{rl.room_kichen.get()} টাকা",  # kichen
            "টয়লেট": f"{rl.room_toylet.get()} টাকা",  # toylet
            "ফ্রিজ": f"{rl.room_frize.get()} টাকা",  # frize
            "অগ্রিম": f"{rl.room_advance.get()} টাকা",  # advance
            "মোট": f"""{int(rl.room_fare.get())
            + int(float(rate.get()) * rnu)
            + int(rl.room_dust.get())
            + int(rl.room_kichen.get())
            + int(rl.room_toylet.get())
            + int(rl.room_frize.get())
            - int(rl.room_advance.get())} টাকা""",  # total
        }
        net_info_list.append(net_dict)
        room_insert.execute(
            "INSERT INTO `test_elec_bill`.`room` ( `room_no`, `year`, `month`, `name`, `rate`, `room_fare`, `room_unit`, `room_advance`,`room_dust`,`room_kichen`,`room_toylet`,`room_frize`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s);",
            inpt,
        )

    # # print("Data Inserted")
    conn.commit()
    conn.close()
    # showPdf(net_info_list)
    output(net_info_list)
    # # print(net_info_list)


def dbMiter(
    month,
    year,
    rate,
    room_101,
    room_102,
    room_201,
    room_202,
    room_203,
    room_401,
    room_402,
    room_403,
    room_404,
):
    global pmon, months, net_info
    pmon = months[months.index(month.get()) - 1]

    room_list = [
        room_101,
        room_102,
        room_201,
        room_202,
        room_203,
        room_401,
        room_402,
        room_403,
        room_404,
    ]
    room_units = [room.room_unit.get() for room in room_list]
    room_units.extend([month.get(), year.get()])
    # print(room_units)

    conn = mysql.connector.connect(
        host=Host, user=User, password=Password, database=Database
    )
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO `test_elec_bill`.`miter` ( `1st_sub1`,`1st_main`, `2nd_sub1`, `2nd_sub2`,`2nd_main`, `4th_sub1`, `4th_sub2`, `4th_sub3`, `4th_sub4`,  `month`, `year`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
        tuple(room_units),
    )

    try:
        pdata = collect.fetchall()[-1][1:11]
    except IndexError:
        pdata = pmon
    # # print(pdata)

    room_net_units = []
    for rl, rp in zip(room_list, pdata):
        room_net_units.append(int(rl.room_unit.get()) - rp)
    # room_net_units[2] = room_net_units[2] - room_net_units[1]
    # room_net_units[5] = room_net_units[5] - room_net_units[4] - room_net_units[3]
    # print(room_net_units)
    conn.commit()
    conn.close()
    dbRoom(
        room_net_units,
        month,
        year,
        rate,
        pdata,
        pmon,
        room_101,
        room_102,
        room_201,
        room_202,
        room_203,
        room_401,
        room_402,
        room_403,
        room_404,
    )

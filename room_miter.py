from db import *
import mysql
from pdf import *

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def dbRoom(
    room_net_units,
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
):
    global pmon, months

    net_info_list = []
    room_list = [
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
    ]

    conn = mysql.connector.connect(
        host=Host, user=User, password=Password, database=Database
    )
    room_insert = conn.cursor()

    for rnu, rl in zip(room_net_units, room_list):

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
        net_dict = {
            "iæg bs": inpt[0],  # room_no
            "eQi": inpt[1],  # year
            "gvm": inpt[2],  # month
            "bvg": inpt[3],  # name
            "‡iU": inpt[4],  # rate
            "fvov": inpt[5],  # fare
            "BDwbU": inpt[6],  # unit
            "AwMªg": inpt[7],  # advance
            "gqjv": inpt[8],  # dust
            "ivbœvNi": inpt[9],  # kichen
            "Uq‡jU": inpt[10],  # toylet
            "wd&ªR": inpt[11],  # frize
            "wej": int(inpt[4] * inpt[6]),  # bill
        }
        net_info_list.append(net_dict)
        room_insert.execute(
            "INSERT INTO `test_elec_bill`.`room` ( `room_no`, `year`, `month`, `name`, `rate`, `room_fare`, `room_unit`, `room_advance`,`room_dust`,`room_kichen`,`room_toylet`,`room_frize`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s);",
            inpt,
        )

    print("Data Inserted")
    conn.commit()
    conn.close()
    showPdf(net_info_list)


def dbMiter(
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
):
    global pmon, months, net_info
    pmon = months[months.index(month.get()) - 1]

    room_list = [
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
    ]
    room_units = [room.room_unit.get() for room in room_list]
    room_units.extend([month.get(), year.get()])
    print(room_units)

    conn = mysql.connector.connect(
        host=Host, user=User, password=Password, database=Database
    )
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO `test_elec_bill`.`miter` (`1st_main`, `1st_sub1`, `1st_sub2`, `2nd_main`, `2nd_sub1`, `2nd_sub2`, `4th_sub1`, `4th_sub2`, `4th_sub3`, `4th_sub4`,  `month`, `year`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
        tuple(room_units),
    )

    collect = conn.cursor()
    collect.execute(
        "SELECT * FROM `test_elec_bill`.`miter` WHERE `month`=%s AND `year`=%s;",
        (pmon, year.get()),
    )
    try:
        pdata = collect.fetchall()[0][1:11]
    except IndexError:
        pdata = pmon
    print(pdata)

    room_net_units = []
    for rl, rp in zip(room_list, pdata):
        room_net_units.append(int(rl.room_unit.get()) - rp)
    room_net_units[2] = room_net_units[2] - room_net_units[1]
    room_net_units[5] = room_net_units[5] - room_net_units[4] - room_net_units[3]
    print(room_net_units)
    conn.commit()
    conn.close()
    dbRoom(
        room_net_units,
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

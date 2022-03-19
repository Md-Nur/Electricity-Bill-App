from create_table_fpdf2 import PDF


data_as_dict = {
    "First name": ["Jules", "Mary", "Carlson", "Lucas"],
    "Last name": ["Smith", "Ramos", "Banks", "Cimon"],
    "Age": [34, "45", "19", "31"],
}

demo = [
    {
        "iæg bs": 101,
        "eQi": 2022,
        "gvm": "March",
        "bvg": "শরীফ",
        "‡iU": 5.72,
        "fvov": 7500,
        "BDwbU": 3,
        "AwMªg": 0,
        "gqjv": 0,
        "ivbœvNi": 0,
        "Uq‡jU": 0,
        "wd&ªR": 0,
        "wej": 17,
    },
    {
        "iæg bs": 102,
        "eQi": 2022,
        "gvm": "March",
        "bvg": "Arif",
        "‡iU": 5.72,
        "fvov": 4500,
        "BDwbU": 0,
        "AwMªg": 0,
        "gqjv": 25,
        "ivbœvNi": 25,
        "Uq‡jU": 0,
        "wd&ªR": 0,
        "wej": 0,
    },
    {
        "iæg bs": 103,
        "eQi": 2022,
        "gvm": "March",
        "bvg": "Birikhor",
        "‡iU": 5.72,
        "fvov": 4500,
        "BDwbU": 2,
        "AwMªg": 0,
        "gqjv": 0,
        "ivbœvNi": 0,
        "Uq‡jU": 25,
        "wd&ªR": 25,
        "wej": 11,
    },
    {
        "iæg bs": 201,
        "eQi": 2022,
        "gvm": "March",
        "bvg": "Kashem",
        "‡iU": 5.72,
        "fvov": 4000,
        "BDwbU": 46,
        "AwMªg": 0,
        "gqjv": 0,
        "ivbœvNi": 0,
        "Uq‡jU": 0,
        "wd&ªR": 0,
        "wej": 263,
    },
    {
        "iæg bs": 202,
        "eQi": 2022,
        "gvm": "March",
        "bvg": "Bike",
        "‡iU": 5.72,
        "fvov": 7500,
        "BDwbU": -310,
        "AwMªg": 0,
        "gqjv": 25,
        "ivbœvNi": 25,
        "Uq‡jU": 25,
        "wd&ªR": 25,
        "wej": -1773,
    },
    {
        "iæg bs": 203,
        "eQi": 2022,
        "gvm": "March",
        "bvg": "khela hoeb",
        "‡iU": 5.72,
        "fvov": 4999,
        "BDwbU": -2737,
        "AwMªg": 0,
        "gqjv": 0,
        "ivbœvNi": 25,
        "Uq‡jU": 25,
        "wd&ªR": 0,
        "wej": -15655,
    },
    {
        "iæg bs": 401,
        "eQi": 2022,
        "gvm": "March",
        "bvg": "Teacher",
        "‡iU": 5.72,
        "fvov": 39548,
        "BDwbU": -1406,
        "AwMªg": 0,
        "gqjv": 25,
        "ivbœvNi": 0,
        "Uq‡jU": 0,
        "wd&ªR": 25,
        "wej": -8042,
    },
    {
        "iæg bs": 402,
        "eQi": 2022,
        "gvm": "March",
        "bvg": "Cat",
        "‡iU": 5.72,
        "fvov": 6000,
        "BDwbU": -122,
        "AwMªg": 0,
        "gqjv": 0,
        "ivbœvNi": 0,
        "Uq‡jU": 25,
        "wd&ªR": 25,
        "wej": -697,
    },
    {
        "iæg bs": 403,
        "eQi": 2022,
        "gvm": "March",
        "bvg": "Moriyom",
        "‡iU": 5.72,
        "fvov": 4500,
        "BDwbU": -99,
        "AwMªg": 0,
        "gqjv": 25,
        "ivbœvNi": 0,
        "Uq‡jU": 0,
        "wd&ªR": 25,
        "wej": -566,
    },
    {
        "iæg bs": 404,
        "eQi": 2022,
        "gvm": "March",
        "bvg": "Shohag",
        "‡iU": 5.72,
        "fvov": 34300,
        "BDwbU": 413,
        "AwMªg": 0,
        "gqjv": 25,
        "ivbœvNi": 25,
        "Uq‡jU": 0,
        "wd&ªR": 0,
        "wej": 2362,
    },
]
data = [
    [
        "First name",
        "Last name",
        "Age",
        "City",
    ],  # 'testing','size'],
    [
        "Jules",
        "Smith",
        "34",
        "San Juan",
    ],  # 'testing','size'],
    [
        "Mary",
        "Ramos",
        "45",
        "Orlando",
    ],  # 'testing','size'],
    [
        "Carlson",
        "Banks",
        "19",
        "Los Angeles",
    ],  # 'testing','size'],
    [
        "Lucas",
        "Cimon",
        "31",
        "Saint-Mahturin-sur-Loire",
    ],  # 'testing','size'],
]

pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=10)

pdf.create_table(table_data=data, title="I'm the first title", cell_width="even")
pdf.ln()

pdf.create_table(
    table_data=data, title="I start at 25", cell_width="uneven", x_start=25
)
pdf.ln()

pdf.create_table(table_data=data, title="I'm in the middle", cell_width=22, x_start="C")
pdf.ln()

pdf.create_table(
    table_data=data_as_dict,
    title="Is my text red",
    align_header="R",
    align_data="R",
    cell_width=[
        15,
        15,
        10,
        45,
    ],
    x_start="C",
    emphasize_data=["45", "Jules"],
    emphasize_style="BIU",
    emphasize_color=(255, 0, 0),
)
pdf.ln()


pdf.output("table_class.pdf")

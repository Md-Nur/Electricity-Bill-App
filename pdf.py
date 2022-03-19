from http.client import SWITCHING_PROTOCOLS
from unittest import case
from fpdf import FPDF


def bijoyMash(mash):
    if mash == "January":
        return "Rvbyqvwi"
    elif mash == "February":
        return "‡deªæqvwi"
    elif mash == "March":
        return "gvP©"
    elif mash == "April":
        return "GwcÖj"
    elif mash == "May":
        return "‡g"
    elif mash == "June":
        return "Ryb"
    elif mash == "July":
        return "RyjvB"
    elif mash == "August":
        return "AvM÷"
    elif mash == "September":
        return "‡m‡Þ¤^i"
    elif mash == "October":
        return "অক্টোবর"
    elif mash == "November":
        return "b‡f¤^i"
    elif mash == "December":
        return "wW‡m¤^i"
    else:
        return ""


def bijoyName(name):
    if name == "Shorif":
        return "kixd"
    elif name == "Arif":
        return "Avwid"
    elif name == "Birikhor":
        return "MvÄv‡Lvi"
    elif name == "Kashem":
        return "‡wknve"
    elif name == "Nurul":
        return "Kv‡kg"
    elif name == "Shihab":
        return "‡byiæj"
    elif name == "Teacher":
        return "kvšÍv"
    elif name == "Cat":
        return "gv÷vi"
    elif name == "Moriyom":
        return "‡mvnvM"
    elif name == "Shohag":
        return "gwiqg"


def showPdf(details):
    print(details)
    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()
    pdf.add_font("SutonnyMJ", "", "SutonnyMJ Regular.ttf", uni=True)
    pdf.set_font("SutonnyMJ", size=15)
    for dt in details:
        for infoDict in dt:
            if infoDict == "gvm":
                dt[infoDict] = bijoyMash(dt[infoDict])
            if infoDict == "bvg":
                dt[infoDict] = bijoyName(dt[infoDict])

            strings = f"{infoDict} : {dt[infoDict]}"
            pdf.cell(txt=strings, ln=1)
        pdf.ln(10)
    pdf.output("test.pdf")


if __name__ == "__main__":
    print(__name__, "is running")

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

    showPdf(demo)

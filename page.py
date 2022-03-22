from room_miter import *
from os import system

def output(info):
    s1 = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">

    <style>
         body {
            margin: 0;
            padding: 0;
            background-color: #FAFAFA;
            font: 12pt "Tahoma";
        }
        .page {
            width: 29.6cm;
            height: 20.9cm;
            display: flex;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.9);
        }

        .canv {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-evenly;
        }

        .items {
            border: 1px solid black;
            padding: 5px;
            width: 200px;
            display: grid;
            grid-template-columns: 1fr 1fr;

        }
    </style>
</head>
<body>
    <div class="book">
        <div class="page">
            <div class="subpage canv">
            
    """
   
    s2 = """
    </div>
        </div>
        </div>
</body>
</html>
    """
    s3 = '''
    '''
    for dicts in info:
        s4 = '''
        '''
        for lbl in dicts:
            if str(dicts[lbl])[0] !='0':
                s4 += f'''<div>{lbl}</div>
                <div>: {dicts[lbl]}</div>
                '''
        s3 += f"""
        <div class="items">
        {s4}
        </div>
        """

    with open('output.html', 'w',encoding='utf-8') as f:
        f.write(s1 + s3 + s2)
    # print('Done')
    system('output.html')
if __name__ == "__main__":
    demo = [
        {
            "রুম নং": 101,
            "বছর": 2022,
            "মাস": "March",
            "নাম": "Shorif",
            "রেট": 5.72,
            "ভাড়া": 7500,
            "ইউনিট": 3,
            "অগ্রিম": 0,
            "ময়লা": 0,
            "রান্নাঘর": 0,
            "টয়লেট": 0,
            "ফ্রিজ": 0,
            "বিল": 17,
            "মোট": 7517,
        },
        {
            "রুম নং": 102,
            "বছর": 2022,
            "মাস": "March",
            "নাম": "Arif",
            "রেট": 5.72,
            "ভাড়া": 4500,
            "ইউনিট": 42,
            "অগ্রিম": 0,
            "ময়লা": 25,
            "রান্নাঘর": 25,
            "টয়লেট": 0,
            "ফ্রিজ": 0,
            "বিল": 240,
            "মোট": 4790,
        },
        {
            "রুম নং": 103,
            "বছর": 2022,
            "মাস": "March",
            "নাম": "Birikhor",
            "রেট": 5.72,
            "ভাড়া": 4500,
            "ইউনিট": -518,
            "অগ্রিম": 0,
            "ময়লা": 0,
            "রান্নাঘর": 0,
            "টয়লেট": 25,
            "ফ্রিজ": 25,
            "বিল": -2962,
            "মোট": 1588,
        },
        {
            "রুম নং": 201,
            "বছর": 2022,
            "মাস": "March",
            "নাম": "Kashem",
            "রেট": 5.72,
            "ভাড়া": 4000,
            "ইউনিট": 22,
            "অগ্রিম": 0,
            "ময়লা": 0,
            "রান্নাঘর": 0,
            "টয়লেট": 0,
            "ফ্রিজ": 0,
            "বিল": 125,
            "মোট": 4125,
        },
        {
            "রুম নং": 202,
            "বছর": 2022,
            "মাস": "March",
            "নাম": "Nurul",
            "রেট": 5.72,
            "ভাড়া": 7500,
            "ইউনিট": -286,
            "অগ্রিম": 0,
            "ময়লা": 25,
            "রান্নাঘর": 25,
            "টয়লেট": 25,
            "ফ্রিজ": 25,
            "বিল": -1635,
            "মোট": 5965,
        },
        {
            "রুম নং": 203,
            "বছর": 2022,
            "মাস": "March",
            "নাম": "Shihab",
            "রেট": 5.72,
            "ভাড়া": 4999,
            "ইউনিট": -3904,
            "অগ্রিম": 0,
            "ময়লা": 0,
            "রান্নাঘর": 25,
            "টয়লেট": 25,
            "ফ্রিজ": 0,
            "বিল": -22330,
            "মোট": -17281,
        },
        {
            "রুম নং": 401,
            "বছর": 2022,
            "মাস": "March",
            "নাম": "Teacher",
            "রেট": 5.72,
            "ভাড়া": 39548,
            "ইউনিট": -1373,
            "অগ্রিম": 0,
            "ময়লা": 25,
            "রান্নাঘর": 0,
            "টয়লেট": 0,
            "ফ্রিজ": 25,
            "বিল": -7853,
            "মোট": 31745,
        },
        {
            "রুম নং": 402,
            "বছর": 2022,
            "মাস": "March",
            "নাম": "Cat",
            "রেট": 5.72,
            "ভাড়া": 6000,
            "ইউনিট": -65,
            "অগ্রিম": 0,
            "ময়লা": 0,
            "রান্নাঘর": 0,
            "টয়লেট": 25,
            "ফ্রিজ": 25,
            "বিল": -371,
            "মোট": 5679,
        },
        {
            "রুম নং": 403,
            "বছর": 2022,
            "মাস": "March",
            "নাম": "Moriyom",
            "রেট": 5.72,
            "ভাড়া": 4500,
            "ইউনিট": -55,
            "অগ্রিম": 0,
            "ময়লা": 25,
            "রান্নাঘর": 0,
            "টয়লেট": 0,
            "ফ্রিজ": 25,
            "বিল": -314,
            "মোট": 4236,
        },
        {
            "রুম নং": 404,
            "বছর": 2022,
            "মাস": "March",
            "নাম": "Shohag",
            "রেট": 5.72,
            "ভাড়া": 34300,
            "ইউনিট": -111,
            "অগ্রিম": 0,
            "ময়লা": 25,
            "রান্নাঘর": 25,
            "টয়লেট": 0,
            "ফ্রিজ": 0,
            "বিল": -634,
            "মোট": 33716,
        },
    ]
    output(demo)
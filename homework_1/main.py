from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/clothes/")
def clothes():
    clothes_list = [
        {
            "photo": "https://img4.traektoria.ru/upload/resized/2/11129069/11129069-200x200.jpg",
            "name": "одежда_1",
            "cost": 15000,
        },
        {
            "photo": "https://img3.traektoria.ru/upload/resized/2/11081190/11081190-200x200.jpg",
            "name": "одежда_2",
            "cost": 20000,
        },
    ]
    return render_template("clothes.html", clothes_list=clothes_list)


@app.route("/jackets/")
def jackets():
    jacket_list = [
        {
            "photo": "https://stok-m.ru/image//fromnew/Z0720232820234320230201/image63da0ee47a1df.jpg",
            "name": "кутка_1",
            "cost": 5000,
        },
        {
            "photo": "https://stok-m.ru/image//fromnew/Z1220223120222420220509/image62790fd9c4021.jpg",
            "name": "кутка_2",
            "cost": 10000,
        },
    ]
    return render_template("jackets.html", jacket_list=jacket_list)


@app.route("/shoes/")
def shoes():
    shoes_list = [
        {
            "photo": "https://www.shoes.ru/images/all/ware_new/133301.jpg",
            "name": "обувь_1",
            "cost": 3500,
        },
        {
            "photo": "https://www.shoes.ru/images/all/ware_new/133265.jpg",
            "name": "обувь_2",
            "cost": 8000,
        },
    ]
    return render_template("shoes.html", shoes_list=shoes_list)


if __name__ == "__main__":
    app.run(debug=True)

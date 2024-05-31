from flask import render_template, request
from lesson1 import app

@app.route('/')
def input():
    return render_template("input.html") # render_template = Flaskの機能(クライアント側にhtmlを返す)

@app.route('/', methods=["GET", "POST"]) # データ通信の役割
def calc():
    input_num = int(request.form["price"])
    result = input_num * 1.1
    return render_template("output.html", complete=result) # output.htmlにresultの値を出力させる(=は指定であり、新たな変数に代入する)
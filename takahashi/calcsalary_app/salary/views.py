from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from flask import request, make_response, jsonify
# from flask_cors import CORS
import sys
from decimal import Decimal, ROUND_HALF_UP


@app.route('/')
def input():
    return render_template("input.html")

@app.route('/',methods=['GET','POST'])
def calc():
    if request.form['salary'] == "":
        flash("給与が未入力です。入力してください。")
        return render_template("input.html")
    
    elif int(request.form['salary']) < 0:
        flash("給与にはマイナスの値は入力できません")
        return None

    elif len(str(request.form['salary'])) > 10:
        flash("給与には最大9,999,999,999まで入力可能です。")
        return None
    
    salary = request.form['salary']
    salary = int(salary)
    #税額計算のため、給与1,000,000での判定
    if (salary > 1000000):
        tax = (salary - 1000000) * 0.2 + 100000
    else:
        tax = salary * 0.1

    tax = round(tax)
    tax = int(tax)
    #支給額 = 給与 - 税額
    pay = salary - tax
    salary = f'{salary:,}'
    tax = f'{tax:,}'
    pay = f'{pay:,}'
    list = [salary,tax,pay]
    return render_template("output.html", salary=list)


        
        
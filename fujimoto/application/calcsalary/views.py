from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

import sys
args = sys.argv

def calcsalary(salary):
    #100万円を超えるか
    if (salary<=1000000):
        tax = salary * 0.1
        allowance = salary - tax
    else:
        tax = 1000000*0.1 + (salary- 1000000) * 0.2
        allowance = salary - tax

    allowance = int(round(allowance,1))
    tax = int(round(tax,1))

    return allowance, tax

@app.route('/')
def input():
    return render_template("input.html")

@app.route('/', methods=['GET','POST'])
def calc():
    if salary not in request.form:
        flash('給与が未入力です。入力してください')
        return render_template("input.html")
        elif request.form['password']!=app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in']=True
            flash('ログインしました')
            return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect('/')
# 入力画面の呼び出し
from flask import request, redirect, url_for, render_template, flash, session
from holiday import app, db
from functools import wraps
from holiday.models.mst_holiday import Holiday

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/input.html', methods=['POST'])
def add_holiday():
    holiday=Holiday(
        holi_date=request.form['holi_date'],
        holi_text=request.form['holi_text']
    )
    db.session.add(holiday)
    db.session.commit()
    return redirect(url_for('show_holidays'))

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['username']!=app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password']!=app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in']=True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))
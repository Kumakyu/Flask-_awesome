from flask import render_template, request, redirect, flash
from holiday import app, db
from holiday.models.mst_holiday import Holiday

@app.route('/')
def input():
    return render_template("input.html")

@app.route('/happy', methods=["GET","POST"])
def insert():
    # entry = Holiday(
    #     date=request.form['title'],
    #     text=request.form['text']
    # )
    # db.session.add(entry)
    # db.session.commit()
    flash('新しく記事が作成されました')
    print('新しく記事が作成されました')
    return redirect ("/")

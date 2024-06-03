# 登録、更新、削除のDB処理、その後の結果画面の呼び出し
from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday
# from flask_blog.views.views import login_required

@app.route('/list.html')
def show_holidays():
    holidays=Holiday.query.order_by(Holiday.holi_date.desc()).all()
    return render_template('templates/input.html', holidays=holidays)



# @app.route('/entries/new', methods=['GET'])
# def new_entry():
#     return render_template('entries/new.html')

@app.route('/entries/<int:id>', methods=['GET'])
def show_entry(id):
    holiday=Holiday.query.get(id)
    return render_template('entries/show.html', holiday=holiday)

@app.route('/entries/<int:id>/edit', methods=['GET'])
def edit_entry(id):
    holiday=Holiday.query.get(id)
    return render_template('entries/edit.html', holiday=holiday)

@app.route('/entries/<int:id>/update', methods=['POST'])
def update_entry(id):
    holiday=Holiday.query.get(id)
    holiday.title=request.form['title']
    holiday.text=request.form['text']
    db.session.merge(holiday)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>/delete', methods=['POST'])
def delete_entry(id):
    holiday=Holiday.query.get(id)
    db.session.delete(holiday)
    db.session.commit()
    flash('記事が削除されました')
    return redirect(url_for('show_entries'))
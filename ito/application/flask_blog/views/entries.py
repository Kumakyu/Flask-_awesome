from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask import request, make_response, jsonify
from flask_cors import CORS
from flask_blog import db
from flask_blog.models.entries import Entry
from flask_blog.views.views import login_required


@app.route('/')
@login_required
def show_entries():
    # if not session.get("logged_in"):
    #     return redirect(url_for("login"))
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template("entries/index.html",entries=entries)

@app.route('/entries/new',methods=['GET'])
@login_required
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')

@app.route('/entries', methods=['POST'])
@login_required
def add_entry():
    entry = Entry(
        title=request.form['title'],
        text=request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect (url_for('show_entries'))


from flask import (
    request, 
    redirect, 
    url_for, 
    render_template, 
    flash, 
    session)
from holiday import app
from holiday.models.mst_holiday import Holiday
from holiday import db
from datetime import date


@app.route('/maintenance_date', methods=['GET', 'POST'])
def update():
    holiday_date = request.form['holiday'] # 入力されたデータを取得
    holiday_text = request.form['holiday_text'] # 入力されたデータを取得

    if holiday_date == "" and holiday_text == "":
        flash("テキストに入力してください")
        redirect('/')
    elif holiday_date == "":
        flash("日付を入力してください")
        redirect('/')
    elif holiday_text == "":
        flash("祝日名を入力してください")
        redirect('/')
    elif len(holiday_text) > 20:
        flash("20文字以内で入力してください")
    else:
        holidate = date(int(holiday_date[0:4]), int(holiday_date[4:6]), int(holiday_date[6:8]))
        get_date = session.query(Holiday.holi_date).filter_by(holiday_date = holidate).first() # 日付をint型に

        holi_table = Holiday(  # 表の作成-->格納用
             hol_date = holiday_date,
             hol_text = holiday_text
        )

        # 神のアイディア
        mgId = ""

        if get_date is None:
            if request.form["button"] == "insert_update":
                new_holiday = holi_table
                db.session.add(new_holiday)
                db.session.commit()
                mgId = "I01"
            elif request.form["button"] == "delete":
                flash(str(get_date) + "は、祝日マスタに登録されていません")
                return redirect('/')
        elif get_date == holiday_date:
            if request.form["button"] == "insert_update":
                new_holiday = holi_table
                db.session.merge(new_holiday)
                db.session.commit()
                mgId = "I02"
            elif request.form["button"] == "delete":
                new_holiday = holi_table
                db.session.delete(new_holiday)
                db.session.commit() 
                mgId = "I03"
        else:
            mgId = "I04"

    return render_template(
        'result.html',
        holiday_date = holiday_date,
        holiday_text = holiday_text,
        mgId = mgId
        )
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

@app.route('/')
def input():
    render_template('input.html')
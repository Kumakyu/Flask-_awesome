from holiday import db
from datetime import datetime, timezone

class Holiday(db.Model):
    __tablename__='holiday'
    holi_date=db.Column(db.Date,primary_key=True)
    holi_text=db.Column(db.String(20))
    

    def __init__(self,date=None,text=None):
        self.holi_date = date
        self.holi_text = text

    def __rper__(self):
        return '<Holiday date:{} text:{}>'.format(self.holi_date,self.holi_text)

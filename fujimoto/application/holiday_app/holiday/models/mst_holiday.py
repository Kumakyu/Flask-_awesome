from flask_blog import db
from datetime import datetime, timezone

class Holiday(db.Model):
    __tablename__='holiday'
    holi_date=db.Column(db.Date,primary_key=True)
    holi_text=db.Column(db.String(20),unique=True)
    created_at=db.Column(db.DateTime)

    def __init__(self,holi_date=None,holi_text=None):
        self.holi_date=holi_date
        self.holi_text=holi_text
        self.created_at=datetime.now(timezone.utc)

    def __rper__(self):
        return '<Holiday holi_date:{} holi_text:{}>'.format(self.holi_date,self.holi_text)
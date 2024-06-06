from holiday import db # データベースのモジュール
from datetime import datetime, timezone # 日付関連のモジュール

class Holiday(db.Model):
    __tablename__ = 'holiday' # テーブルの名前の宣言（今回はholiday）
    holi_date = db.Column(db.Date, primary_key = True) # 日付
    holi_text = db.Column(db.String(20), unique = True) # 祝日名

    def __init__(self, holi_date=None, holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text

    def __repr__(self):
        return '<Holiday holi_date:{} holi_text:{}>'.format(self.holi_date, self.holi_text)
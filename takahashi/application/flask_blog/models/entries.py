from flask_blog import db # データベースのモジュール
from datetime import datetime, timezone # 日付関連のモジュール

class Entry(db.Model):
    __tablename__ = 'entries' # テーブルの名前の宣言（今回はentries）
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), unique = True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        self.created_at = datetime.now(timezone.utc)

    def __repr__(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)
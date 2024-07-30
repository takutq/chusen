from chusentest import db
import datetime 


class Guest(db.Model):
    __tablename__ = 'guest'
    id = db.Column(db.Integer, primary_key=True)     #自動番号割り当て
    ic_card = db.Column(db.Integer())
    name = db.Column(db.String(255))    #名前255文字制限
    age = db.Column(db.Integer())  #年齢２桁制限
    created_at = db.Column(db.Time, nullable=False, default=datetime.datetime.now())  #作成日時　　#timezoneをjst→python3.9以降
    updated_at = db.Column(db.Time, nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now())    #更新日時

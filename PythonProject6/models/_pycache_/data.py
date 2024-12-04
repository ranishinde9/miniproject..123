from utils.db import db


# parent table

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    UserBehaviorClass = db.Column(db.String(100), nullable=False)

    data = db.relationship('Mobile', backref=User, lazy=True)

class Mobile(db.Model):
    mobile id= db.Column(db.Integer, primary_key=True)
    DeviceModel = db.Column(db.String(100), nullable=False)
    OperatingSystem= db.Column(db.String(100), nullable=False)
    AppUsageTime= db.Column(db.Integer, nullable=False)
    BatteryDrain= db.Column(db.Integer, nullable=False)
    ScreenOnTime(hours / day)= db.Column(db.Integer, nullable=False)
    NumberofAppsInstalled= db.Column(db.Integer, nullable=False)
    DataUsage(MB / day)= db.Column(db.Integer, nullable=False)

    User_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

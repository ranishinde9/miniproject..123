from flask import Flask, render_template, request, redirect
from utils.db import db
from models.data import *
from flask_sqlalchemy import SQLAlchemy


flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'




@flask_app.route('/')
def index():
    data =Mobile.query.all()
    return render_template('index.html', content=data)


@flask_app.route('/help')
def help():
    return render_template('help.html')




@flask_app.route('/add_data')
def add_data():
    return render_template('add_data.html')

db.init_app(flask_app)


with flask_app.app_context():
    db.create_all()



@flask_app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

     id= form_data.get('id')
    age = form_data.get('age')
    gender = form_data.get('gender')
    UserBehaviorClass= form_data.get('UserBehaviorClass')

mobile id= form_data.get('mobile id')
     DeviceModel= form_data.get('DeviceModel')
     OperatingSystem= form_data.get('OperatingSystem')
     AppUsageTime = form_data.get('AppUsageTime')
     BatteryDrain=form_data.get('BatteryDrain')
     ScreenOnTime(hours / day)= form_data.get('ScreenOnTime(hours / day')
     NumberofAppsInstalled= form_data.get('NumberofAppsInstalled')
     DataUsage(MB / day)= form_data.get('DataUsage(MB / day)')

    user=User.query.filter_by( id= id).first()
    if not  user:
        user =User( id= id, age=age, gender=gender, UserBehaviorClass=UserBehaviorClass)
        db.session.add(user)
        db.session.commit()

    data = Mobile(DeviceModel=DeviceModel, mobile id=mobile id,OperatingSystem= OperatingSystem, BatteryDrain=BatteryDrain, AppUsageTime= AppUsageTime, ScreenOnTime(hours / day)=ScreenOnTime(hours / day),NumberofAppsInstalled=NumberofAppsInstalled, DataUsage(MB / day)=DataUsage(MB / day))
    db.session.add(data)
    db.session.commit()
    print("sumitted successfully")
    return redirect('/')


if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=8005,
        debug=True
    )
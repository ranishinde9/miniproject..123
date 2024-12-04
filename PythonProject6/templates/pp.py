from flask import Flask, render_template, request, redirect
from utils.db import db
from models.data import *
from flask_sqlalchemy import SQLAlchemy


flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'




@flask_app.route('/')
def index():
    data = Mobile.query.all()
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


    

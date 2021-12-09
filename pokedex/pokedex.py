import sqlite3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import query

app = Flask(__name__)
conn = sqlite3.connect('database.sqlite',check_same_thread=False)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"

db = SQLAlchemy(app)

@app.route('/', methods = ['GET'])
def home():
   return render_template('homePokedex.html')

if __name__ == '__main__':
   app.run(debug = True)
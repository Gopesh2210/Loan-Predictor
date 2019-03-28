from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_bcrypt import Bcrypt



app = Flask(__name__)

app.config['SECRET_KEY'] = 'ee556c4ef73062527783828c5651fff6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from LoanPrediction import routes
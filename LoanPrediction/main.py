from flask import Flask, render_template, url_for,request, flash,redirect,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_bcrypt import Bcrypt
from forms import RegistrationForm, LoginForm
import view as var
import _pickle as pickle
import json
pred_model = pickle.load(open('trainedModel.sav','rb'))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ee556c4ef73062527783828c5651fff6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)




class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False)
	bank_name = db.Column(db.String(20), nullable=False)
	email_addr = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(20), nullable=False)


	def __repr__(self):
		return f"User('{self.username}', '{self.bank_name}', '{self.email_addr}')"



@app.route("/")
@app.route("/home")
def home():
    return render_template('MainLayout.html', title='Home')

@app.route("/login", methods=['GET','POST'])
def login():

		if request.method == "POST":
				username = request.form['username']
				bank_name = request.form['bank_name']
				email = request.form['email_addr']
				password= request.form['password']
				register = User(username = username, bank_name=bank_name, email_addr = email, password = password)
				db.session.add(register)
				db.session.commit()
				return redirect(url_for("login"))
				flash('You were successfully signed up')

		if request.method == 'GET':
			return render_template('login1.html', title='Login/Register')


@app.route("/view", methods=['GET','POST'])
def view():
	if request.method == 'GET':
		return render_template('view.html', title='View')
	elif request.method == 'POST':
		info = var.search_cid(request.form['cid'])
		return render_template('view.html', data=info)


@app.route("/analyze")
def analyze():
	data = pred_model.feature_importances_
	data = [round(x*100,2) for x in data]
	labels = var.labels()
	return render_template('analyze.html',data = data,labels = json.dumps(labels))

@app.route("/generate")
def generate():
	return render_template('generate.html', title='Generate')


if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)    

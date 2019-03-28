from LoanPrediction.model import User
from flask import render_template, url_for,request, flash,redirect,session,logging,request
from LoanPrediction.forms import RegistrationForm, LoginForm
from sqlalchemy import Column, Integer, String

from LoanPrediction import app, db, bcrypt
import LoanPrediction.view as var
import _pickle as pickle
import json
pred_model = pickle.load(open('./trainedModel.sav','rb'))



@app.route("/")
@app.route("/home")
def home():
    return render_template('MainLayout.html', title='Home')

@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, bank_name=form.bank_name.data , email_addr=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register',form=form)
     


@app.route("/login", methods=['GET','POST'])
def login():
		form = LoginForm()
		if form.validate_on_submit():
			if form.email.data == 'admin@blog.com' and form.password.data == 'password':
				flash('You have been logged in!', 'success')
				return redirect(url_for('home'))
			else:
				flash('Login Unsuccessful. Please check username and password', 'danger')

		return render_template('login.html', title='Login', form=form)


'''@app.route("/login", methods=['GET','POST'])
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
'''


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

@app.route("/generate",methods=['GET', 'POST'])
def generate():
	if request.method == 'GET':
		return render_template('generate.html', title='Generate')
	if request.method == 'POST':
		form = request.form
		attribut = []
		attribut.append(float(form['amount']))
		attribut.append(float(form['cscore']))
		attribut.append(float(form['annualincome']))
		attribut.append(float(form['monthlydebt']))
		attribut.append(float(form['yearsofhistory']))
		attribut.append(float(form['openacc']))
		attribut.append(float(form['creditbalance']))
		attribut.append(float(form['maxopencredit']))
		val = pred_model.predict_proba([attribut])[0]
		data = []
		data.append(val[1])
		data.append(val[0])
		labels =[]
		labels.append(str(data[0]))
		labels.append("")
		print(data)
		# return render_template('score.html',data=data)
		return render_template('score.html',data = data,labels = json.dumps(labels))

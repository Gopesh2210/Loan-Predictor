from flask import Flask, render_template, url_for,request
from forms import RegistrationForm, LoginForm
import view as var
import pygal
import _pickle as pickle
import json
pred_model = pickle.load(open('trainedModel.sav','rb'))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ee556c4ef73062527783828c5651fff6'



@app.route("/")
@app.route("/home")
def home():
    return render_template('MainLayout.html', title='Home')

@app.route("/login", methods=['GET','POST'])
def login():
		#form = RegistrationForm()
		return render_template('Login.html', title='Login/Register')

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
	app.run(debug=True)    

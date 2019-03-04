from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{	
		'name': 'Gopesh',
		'Current_Loan_Amount': '400000',
		'Credit_Score': '709'		
	},
	{
		'name': 'Anisha',					
		'Current_Loan_Amount': '120500',
		'Credit_Score': '710'	
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('MainLayout.html', title='Home')

@app.route("/login")
def login():
	return render_template('login.html', title='Login')

@app.route("/view")
def view():
	return render_template('view.html', title='View')

@app.route("/analyze")
def analyze():
	return render_template('analyze.html', title='Analyze')

@app.route("/generate")
def generate():
	return render_template('generate.html', title='Generate')


if __name__ == '__main__':
	app.run(debug=True)    
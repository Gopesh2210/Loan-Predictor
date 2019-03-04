from flask import Flask, render_template, url_for
app = Flask(__name__)



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

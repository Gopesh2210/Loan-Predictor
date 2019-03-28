from LoanPrediction import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False)
	bank_name = db.Column(db.String(20), nullable=False)
	email_addr = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(20), nullable=False)


	def __repr__(self):
		return f"User('{self.username}', '{self.bank_name}', '{self.email_addr}')"

From LoanPrediction import db
df = pd.read_csv('./credit_train_edited_version.csv')
from sqlalchemy import create_engine
engine = create_engine('sqlite:///LoanPrediction/site.db', echo=False)
df.to_sql('Loanee', con=engine)
# print(engine.execute("SELECT * FROM loanee").fetchall())
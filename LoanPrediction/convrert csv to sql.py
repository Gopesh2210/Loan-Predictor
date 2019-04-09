import pandas as pd 
df = pd.read_csv('./credit_train_edited_version.csv')
from sqlalchemy import create_engine
engine = create_engine('sqlite:///gg.db', echo=False)
df.to_sql('Loane', con=engine)
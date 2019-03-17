import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import pickle

df = pd.read_csv('./credit_train_edited_version.csv')

df_b=df.drop(['Tax Liens','Bankruptcies','Number of Credit Problems','Loan ID','Customer ID','Loan Status','Term','Home Ownership','Purpose','Years in current job'],axis=1)

X = df_b.drop(['Fully Paid'],axis=1)
Y = df_b['Fully Paid']

X_trn,X_tst,Y_trn,Y_tst = train_test_split(X,Y,test_size=0.2,random_state=42)
rc = RandomForestClassifier(n_estimators=1000)
rc.fit(X_trn,Y_trn)
pc = rc.predict(X_tst)
print(classification_report(Y_tst,pc))
print(confusion_matrix(Y_tst,pc))
model = "./LoanPrediction/trainedModel.sav"
pickle.dump(rc, open(model, 'wb'))
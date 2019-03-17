import pickle
import pandas as pd
import matplotlib.pyplot as plt
pred_model = pickle.load(open('./LoanPrediction/trainedModel.sav','rb'))
imp = pred_model.feature_importances_
df = pd.read_csv('./credit_train_edited_version.csv',nrows=0)
df = df.drop(['Tax Liens','Bankruptcies','Number of Credit Problems','Loan ID','Customer ID','Loan Status','Term','Home Ownership','Purpose','Years in current job','Fully Paid'],axis=1)
plt.barh(df.columns,imp)
plt.show()
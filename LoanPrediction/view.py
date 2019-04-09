from sqlalchemy import create_engine
import pandas as pd
df = pd.read_csv('./credit_train_edited_version.csv',nrows=1)
def search_cid(id):
        engine = create_engine('sqlite:///LoanPrediction/site.db', echo=False)
        val = sanitize(id)
        if val == False:
                return "Customer ID should only contain alphabet,numbers and - "
        res = engine.execute('SELECT * FROM Loanee where "Customer ID" == "'+id.strip()+'"')
        res = [r for r in res]
        if len(res) == 0 :
                return "Invalid Customer ID"
        res = [r for r in res[0]]
        return res
def debug(val):
    if val:
        print(search_cid(id))
def print_loc(val):
    return df.loc[val].values[1]
def labels():
        var = df.drop(['Tax Liens','Bankruptcies','Number of Credit Problems','Loan ID','Customer ID','Loan Status','Term','Home Ownership','Purpose','Years in current job','Fully Paid'],axis=1).columns
        var = var.to_list()
        print(var)
        print(type(var))
        return var
def attr():
        return df.columns.to_list()

def sanitize(id):
        for letter in id:
                if not((letter >= 'a'  and  letter <='z') or (letter>='0' and letter<='9') or letter == '-'):
                        return False
                return True  
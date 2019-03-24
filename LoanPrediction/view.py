import pandas as pd
df = pd.read_csv('../credit_train_edited_version.csv')
id = df.loc[0].values[1]
def search_cid(id):
    for i in range(len(df)):
        tmp = df.loc[i].to_dict()
        if tmp['Customer ID'] == id:
            return tmp
def debug(val):
    if val:
        print(search_cid(id))
def print_loc(val):
    return df.loc[val].values[1]
def labels():
        var = df.drop(['Tax Liens','Bankruptcies','Number of Credit Problems','Loan ID','Customer ID','Loan Status','Term','Home Ownership','Purpose','Years in current job','Fully Paid'],axis=1).columns
        print(var)
        print(type(var))
        var = var.to_list()
        return var
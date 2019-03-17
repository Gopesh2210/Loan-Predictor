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
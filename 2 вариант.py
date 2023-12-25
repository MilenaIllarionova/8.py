import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

def one_hot_encode(df, column):
    categories = df[column].unique()
    for category in categories:
        df[category] = (df[column] == category).astype(int)
    df.drop(column, axis=1, inplace=True)
    return df

data_encoded = one_hot_encode(data.copy(), 'whoAmI')
data_encoded.head()
print(data_encoded)
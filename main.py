import pandas as pd

data = pd.DataFrame({
    'whoAmI': ['cat', 'dog', 'dog', 'cat', 'rabbit']
})
one_hot = pd.get_dummies(data['whoAmI'])
data = data.drop('whoAmI', axis=1)
data = data.join(one_hot)
print(data)

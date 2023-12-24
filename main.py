import random
import pandas as pd

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем пустой DataFrame с колонками для каждого уникального значения из столбца 'whoAmI'
one_hot = pd.get_dummies(data['whoAmI'])

# Объединяем исходный DataFrame с полученным one-hot DataFrame
data_one_hot = pd.concat([data, one_hot], axis=1)

data_one_hot.head()


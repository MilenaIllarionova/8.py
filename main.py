from sklearn.preprocessing import LabelBinarizer
lb = LabelBinarizer()
one_hot_encoded = lb.fit_transform(data['whoAmI'])
one_hot_df = pd.DataFrame(one_hot_encoded, columns=lb.classes_)
data = data.join(one_hot_df)
data.head()

# This program is a part of assignment of CE807 Text Analytics
# Atiwat Onsuwan 1802514
# Referrence https://towardsdatascience.com/named-entity-recognition-and-classification-with-scikit-learn-f05372f07ba2

import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB

# read test set
data_set = pd.read_csv("wikigold.conll.txt", sep="\n", delimiter=" ", header=None)
# define words & IOBs column names
data_set.columns = ['word', "iob_tag"]
test_set = data_set.iloc[:, [0, 1]]
test_set.word.nunique(), test_set.iob_tag.nunique()
test_set.groupby('iob_tag').size().reset_index(name='counts')
# drop iob tag from list 'word_test_list'
word_test_list = test_set.drop('iob_tag', axis=1)
# get values of iob_tag and store into another list
iob_test_list = test_set.iob_tag.values

# read data set
train_data = pd.read_csv("wikiner.txt", sep="\n", delimiter=" ", header=None)
# define words & IOBs column names
train_data.columns = ['word', "iob_tag"]
train_set = train_data.iloc[:, [0, 1]]
# cope training data to 18000 rows to avoid memory error
train_set = train_set[:18000]

train_set.word.nunique(), train_set.iob_tag.nunique()
train_set.groupby('iob_tag').size().reset_index(name='counts')
# drop iob tag from list 'word_train_list'
word_train_list = train_set.drop('iob_tag', axis=1)

# create object DictVectorizer
v = DictVectorizer(sparse=False)
# turn word of training set into vector for training
word_train_list = v.fit_transform(word_train_list.to_dict('records'))
# use the same object to transform words in test set to vector
word_test_list = v.transform(word_test_list.to_dict('records'))
# get values of IOB tags from iob_tag column
iob_train_list = train_set.iob_tag.values

# initialize Naive Bayes classifier for Multinomial models object
nb = MultinomialNB(alpha=0.01, class_prior=None, fit_prior= True)

# Train the model
model = nb.fit(word_train_list, iob_train_list)

# Evaluate the model over wiki gold standard
print(classification_report(y_pred=model.predict(word_test_list), y_true=iob_test_list))
# display accuracy
print("Accuracy: ", accuracy_score(iob_test_list, model.predict(word_test_list)))


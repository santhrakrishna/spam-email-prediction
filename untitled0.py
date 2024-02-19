# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1utv7pseaPNpYBshlZWJh3cJBKgLaomiN
"""

#import libraries
import numpy as np
import pandas as pd

"""## **Read data**"""

data=pd.read_csv('../content/spam email prediction.csv')
data.head()

print('There are {} rows and {} columns in train'.format(data.shape[0],data.shape[1]))

data.columns

data.dtypes

data.corr()

"""## **DATA SPILITING**"""

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

data['Prediction'].value_counts()

data.describe(include='all').T

data.nunique()

data.isnull().sum()

"""# **EDA (Exploratory Data Analysis)**"""

data.Prediction.hist()

data.boxplot()

"""## **visualization**"""

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(20,5))
plt.xticks(rotation=90)
ax=sns.countplot(x="spam", data=data)
plt.show()

targetCounts = data['spam'].value_counts()
targetLabels = data['spam'].unique()
plt.figure(figsize=(20,5))
plt.pie(targetCounts, labels=targetLabels, autopct='%1.1f%%', shadow=True)
plt.title("type of emails")
plt.show()

sns.heatmap(data.corr())

""" **Building model**"""

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=40)

"""**Applying LogisticRegression Model**


"""

from sklearn.linear_model import LogisticRegression
X_train = pd.DataFrame(X_train)
y_train = pd.DataFrame(y_train)

# Print the first few rows of X_train
print(X_train.head())

# Print the number of missing values in X_train
print(X_train.isnull().sum())
print(y_train.isnull().sum())

# Drop rows with missing values
X_train = X_train.dropna()
y_train = y_train.dropna()

# Impute missing values with the mean
X_train = X_train.fillna(X_train.mean())
y_train = y_train.fillna(y_train.mean())

LogisticRegression_model = LogisticRegression(tol=0.1, C=0.6, max_iter=1500, random_state=40)
LogisticRegression_model.fit(X_train, y_train)

#Calculating Score for train and test
print('the score is {}'.format(LogisticRegression_model.score(X_test, y_test)))
print('LogisticRegressionModel Classes are : ' , LogisticRegression_model.classes_)
print('LogisticRegressionModel No. of iteratios is : ' , LogisticRegression_model.n_iter_)

y_pred = LogisticRegression_model.predict(X_test)
#calculating Confusion Matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
CM = confusion_matrix(y_test, y_pred)
print('Confusion Matrix is : \n', CM)
# drawing confusion matrix
sns.heatmap(CM, center = True,annot=True)
plt.show()

"""**Calculating classification report**"""

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
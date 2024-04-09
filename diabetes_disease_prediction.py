# -*- coding: utf-8 -*-
"""Diabetes Disease prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nUY1aMPs9_HmbwQrKiXt8TjaPibhk3Aq

## **DIABETES DISEASE PREDICTION**

##**IMPORT**
"""

import pandas as pd
import numpy as np

BC=pd.read_csv('https://raw.githubusercontent.com/BarathPrince/Data-Set/main/diabetes_w.csv')

"""##**Data Analysis**"""

BC.head(10)

BC.describe()

BC.info()

BC.columns

BC.replace({'Outcome':{'YES':1,'NO':0}},inplace=True)
BC.head()

"""##**Dependent Variable**"""

y=BC['Outcome']
y.shape

"""##**Independent Variable**"""

X=BC[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age']]
X.shape

"""##**Train Test Split**"""

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size = 0.1,random_state = 0)
X_train.shape,X_test.shape,y_train.shape,y_test.shape

"""##**Logistic Regression**"""

from sklearn.linear_model import  LogisticRegression
l=LogisticRegression()
l.fit(X_train,y_train)

y_pred=l.predict(X_test)
y_pred.shape

"""##**Model Evaluating**"""

from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test,y_pred))

print(accuracy_score(y_test,y_pred))

"""##**Future Prediction**"""

BC1=BC.sample()
BC1

X1 =BC1[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']]

y_pred_new=l.predict(X1)
y_pred_new
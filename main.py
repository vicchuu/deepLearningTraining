#cleared
import numpy as np
import pandas as ps

dataset = ps.read_csv("Churn_Modelling.csv")

(dataset.drop_duplicates())

print(a)
X=dataset.iloc[:,3:-1].values
Y=dataset.iloc[:,-1].values
#print(X)

#data preprocessing
"""Converting geography and sex into label encoder"""

from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
X[:,2]=label.fit_transform(X[:,2])


"""Converting georaphy into label encoder with One hot Encoder"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct=ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[1])],remainder="passthrough")
X=np.array(ct.fit_transform(X))

"""Scaling occurs for converting all values to -4.0 to +3.0"""

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X=sc.fit_transform(X)

"""Spiltting data set and training set"""
from sklearn.model_selection import train_test_split
xtrain , xtest, ytrain,ytest= train_test_split(X,Y,test_size=0.2,random_state=21)

print(xtrain)

"""Building ANN Artificial Neural Network"""

import tensor as tf

t=tf.keras 




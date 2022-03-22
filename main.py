#cleared
import numpy as np
import pandas as ps

dataset = ps.read_csv("Churn_Modelling.csv")

(dataset.drop_duplicates())


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
print(X)
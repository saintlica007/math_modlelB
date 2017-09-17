from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
import numpy as np
# download the file
raw_data = "dg.csv"
raw_data1 = "test1.csv"
# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")
dataset1 = np.loadtxt(raw_data1, delimiter=",")
# separate the data from the target attributes
X = dataset[:,0:3]
y = dataset[:,4]
z = dataset1[:,0:3]
ob=dataset1[:,4]
# normalize the data attributes
normalized_X = preprocessing.normalize(X)
normalized_z = preprocessing.normalize(z)
# standardize the data attributes
standardized_X = preprocessing.scale(X)
standardized_z = preprocessing.scale(z)
model = DecisionTreeClassifier()
model.fit(X, y)
print(model)
# make predictions
expected = y
predicted = model.predict(X)
predicted2 = model.predict(z)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
print(metrics.classification_report(ob, predicted2))
print(metrics.confusion_matrix(ob, predicted2))
c=0
for k in predicted2:
    if k==1:
        c+=1
print(c)


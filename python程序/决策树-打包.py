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
z = list(dataset1[:,0:3])
ob=dataset1[:,4]
numb=[]
for i in range(0,21):
    l=list(open(".\分类2\分类%d.txt"%(i)))
    if len(l)>=2 and len(l)<15:
        po=[]
        for j in range(0,len(l)):
            k=l[j].split()
            po.append(int(k[2]))
        for cLo in range(1,len(po)):
            z[po[0]][2]+=z[cLo][2]
            z[po[0]][1]+=z[cLo][1]
        del po[0]
        numb.append(po[0])
    else: continue
cC=0
for j in range(0,len(numb)):
    del z[j]
    cC+=1
    if j<len(numb)-1:
        numb[j+1]-=cC
z=np.array(z)
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
#print(metrics.classification_report(ob, predicted2))
#print(metrics.confusion_matrix(ob, predicted2))
c=0
for k in predicted2:
    if k==1:
        c+=1
print(c/len(predicted2))


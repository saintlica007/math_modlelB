import numpy as np
from sklearn import linear_model, datasets
import matplotlib.pyplot as plt
from scipy.stats import norm
l=list(open('dis4.txt'))
x=[]
y=[]
for i in l:
    k=i.split()
    k[0],k[1]=float(k[0]),float((k[1]))
    y.append(int((k[0])*1000))
    x.append(int(k[1]*10))
X=np.array(x)
y=np.array(y)
#---logistic regression--------
from sklearn.linear_model import LogisticRegression
logclf = LogisticRegression()
logclf.fit(X.reshape(len(x),1), y)
def lr_model(clf, X):
    k=clf.intercept_
    n=clf.coef_ * X
    for i in range(0,len(k)):
        for j in range(0,len(n)):
            n[j]=n[j]+k[i]
    for j in range(1,len(n)):
        n[0]=n[0]+n[j]
    return 1.0 / (1.0 + np.exp(-(n[0])))
#----plot---------------------------    
plt.figure(figsize=(10, 5))
plt.scatter(X, y,2,color="b")
plt.plot(X, lr_model(logclf, X).ravel(),"+",color="r")
plt.xlabel("feature value")
plt.ylabel("class")
plt.title("logistic fit")
plt.grid(True, linestyle='-', color='0.75')
plt.tight_layout(pad=0.4, w_pad=0, h_pad=1.0)     
plt.show()

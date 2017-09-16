import numpy as np
from sklearn import linear_model, datasets
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from scipy.stats import norm
l=list(open('dis3.txt'))
x=[]
y=[]
z=[]
for i in l:
    k=i.split()
    k[0],k[1]=float(k[0]),float((k[1]))
    y.append(int((k[0])*1000))
    x.append(int(k[1]*10))
    z.append(int(k[2]))
x=np.array(x)
y=np.array(y)
cd=x.reshape(836,1)
logclf = LogisticRegression()
logclf.fit(cd, y)
def lr_model(clf, x):
    return 1.0 / (1.0 + np.exp(-(clf.intercept_ + clf.coef_ * x)))
plt.figure(figsize=(10, 5))
plt.scatter(x, y, c=y)
plt.plot(x, lr_model(logclf, cd).ravel(),"o",color="c")
plt.xlabel("feature value")
plt.ylabel("class")
plt.title("logistic fit")
plt.grid(True, linestyle='-', color='0.75')
plt.tight_layout(pad=0.4, w_pad=0, h_pad=1.0)
plt.show()

    

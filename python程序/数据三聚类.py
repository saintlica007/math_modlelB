import numpy as np
from math import cos,pi
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
l=list(open('fj3da.txt'))
s=[]
x=[]
for i in l:
    k=i.split()
    k[0],k[1]=float(k[1]),float(k[0])
    k[0]=k[0]/cos(pi*(k[1]/180))
    x.append(k)

#生产数据
X=np.array(x)
#对数据进行标准化
#X = StandardScaler().fit_transform(x)

#计算
db = DBSCAN(eps=0.005,min_samples=5).fit(X)
core_samples_mask = np.zeros_like(db.labels_,dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

n_clusters_ = len(set(labels))-(1 if -1 in labels else 0)

unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0,1,len(unique_labels)))
for k,col in zip(unique_labels,colors):
    if k == -1:
        col = 'k'
    class_member_mask = (labels == k)
    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=7)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=2)
    s.append(list(xy))

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()

    

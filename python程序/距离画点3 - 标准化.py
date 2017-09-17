from math import radians, cos, sin, asin, sqrt
from scipy import stats
import numpy as np
from sklearn import preprocessing
def haversine(lat1,lon1,lat2,lon2):
    lon1,lat1,lon2,lat2=map(radians, [lon1,lat1,lon2,lat2])
    dlon=lon2-lon1
    dlat=lat2-lat1
    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c=2*asin(sqrt(a))
    r=6371
    return c *r*1000
l=list(open('fj2.txt'))
cen=list(open('centerpoints.txt'))
loc=[]
de=[]
pr=[]
ce=[]
ye=[]
for i in cen:
    te=i.split()
    te[0],te[1]=float(te[0]),float(te[1])
    ce.append(te)
for i in l:
    k=i.split()
    k[0],k[1]=float(k[0]),float(k[1])
    pr.append(float(k[2]))
    des=[]
    for te in ce:
        des.append(haversine(k[0],k[1],te[0],te[1]))
    des.sort()
    de.append(des[0])
    ye.append(k[2])
de1=np.array(de)
de1=preprocessing.scale(de1)
pr1=np.array(pr)
pr1=preprocessing.scale(pr1)
print(stats.spearmanr(de1, pr1, axis=None))
for j in range(0,len(de1)):
    loc.append(str(de1[j])+"\t"+str(pr1[j])+"\t"+k[2])
f=open("dis4.txt","w")
f.write("\n".join(loc))
f.close()

    

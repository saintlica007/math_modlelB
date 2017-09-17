from math import radians, cos, sin, asin, sqrt
from scipy import stats
import numpy as np  
import matplotlib.pyplot as plt
def haversine(lat1,lon1,lat2,lon2):
    lon1,lat1,lon2,lat2=map(radians, [lon1,lat1,lon2,lat2])
    dlon=lon2-lon1
    dlat=lat2-lat1
    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c=2*asin(sqrt(a))
    r=6371
    return c *r*1000
l=list(open('fj1.txt'))
cen=list(open('centerpoints.txt'))
loc=[]
pr=[]
ce=[]
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
    loc.append(des[0])
fig = plt.figure()  
ax1 = fig.add_subplot(111)    
ax1.set_title('price-distance')  
plt.xlabel('distance')   
plt.ylabel('price')   
ax1.scatter(loc,pr,s=3,c = 'r',marker = '.')
plt.legend('x1')    
plt.show()  
c=[loc,pr]
d=np.corrcoef(c)
print(d)
print(stats.spearmanr(loc, pr, axis=None))
f=open("dis.txt","w")
for i in range(0,len(loc)):
    loc[i]=str(loc[i])
f.write("\n".join(loc))
f.close() 
from math import radians, cos, sin, asin, sqrt
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
loc=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
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
    kk=list()
    kk=kk+des
    des.sort()
    inde=kk.index(des[0])
    if des[0]<3000 and float(k[2])<66:
        loc[inde].append(str(des[0])+","+str(k[2]))
f=open("dis1.txt","w")
f.write("\n".join(("\t".join(l)for l in loc)))
f.close()

    

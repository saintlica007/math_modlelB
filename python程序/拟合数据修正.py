from math import radians, cos, sin, asin, sqrt
def haversine(lat1,lon1,lat2,lon2):
    lon1,lat1,lon2,lat2=map(radians, [lon1,lat1,lon2,lat2])
    dlon=lon2-lon1
    dlat=lat2-lat1
    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c=2*asin(sqrt(a))
    r=6371
    return c *r*1000
l=list(open('ex3datapr.txt'))
cen=list(open('prec1.txt'))
ciy=list(open('cities.txt'))
loc=[]
ci=[]
pr=[]
ce=[]
for i in cen:
    te=i.split()
    te[0]=float(te[0])
    pr.extend(te)
for i in ciy:
    te=i.split()
    te[0],te[1],te[2]=float(te[0]),float(te[1]),float(te[2])
    ci.append(te)
for i in range(0,len(l)):
    k=l[i].split()
    cit=[]
    for te in ci:
        cit.append(haversine(float(k[0]),float(k[1]),te[0],te[1]))
    tem=[]
    tem.extend(cit)
    cit.sort()
    ind=tem.index(cit[0])
    pr[i]=pr[i]*(ci[ind][2]/ci[1][2]) #价格缩放
    k.append(str(pr[i]))
    loc.append("\t".join(k))
f=open("resulc.txt","w")
f.write("\n".join(loc))
f.close()   
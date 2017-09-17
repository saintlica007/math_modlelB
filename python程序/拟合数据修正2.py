from math import radians, cos, sin, asin, sqrt
def haversine(lat1,lon1,lat2,lon2):
    lon1,lat1,lon2,lat2=map(radians, [lon1,lat1,lon2,lat2])
    dlon=lon2-lon1
    dlat=lat2-lat1
    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c=2*asin(sqrt(a))
    r=6371
    return c *r*1000
l=list(open('ex3data2.txt'))
cen=list(open('ex2data2.txt'))
loc=[]
ci=[]
ce=[]
for i in cen:
    te=i.split()
    te[0],te[1],te[2]=float(te[0]),float(te[1]),float(te[2])
    ce.append(te)
for i in l:
    k=i.split()
    des=0.0
    for te in ce:
        if(haversine(float(k[0]),float(k[1]),te[0],te[1]))<=3000:
            des=des+te[2]
    if des>0:
        loc.append("\t".join(k))
f=open("ex3datapr.txt","w")
f.write("\n".join(loc))
f.close()   

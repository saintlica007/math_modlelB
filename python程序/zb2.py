l=list(open('zb2.txt'))
s=[]
for i in l:
    k=i.split()
    k[0],k[1]=k[1],k[0]
    b=",".join(k)
    s.append(b)
f=open("zb2cl.txt","w")
f.write("\n".join(s))
f.close()

    

l=list(open('da3.txt'))
s=[]
for i in l:
    k=i.split()
    b="\t".join(k)
    s.append(b)
for k in range(0,7):
    o=open("聚类%d.txt"%(k))
    jlj=o.read()
    jl=jlj.split()
    o.close()
    for j in jl:
        s[int(j)]=s[int(j)]+"\t"+"%d"%(k)
f=open("dsf.txt","w")
f.write("\n".join(s))
f.close()

    

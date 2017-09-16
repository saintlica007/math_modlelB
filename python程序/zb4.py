l=list(open('da3.txt'))
s=[]
for i in l:
    k=i.split()
    b="\t".join(k[0:2])
    s.append(b)
f=open("zb2cl3.txt","w")
f.write("\n".join(s))
f.close()

    

l=list(open('zb2.txt'))
s=[]
for i in l:
    k=i.split()
    k[0],k[1]=k[1],k[0]
    #if(float(k[0])>110.5) and (float(k[0])<114.5) and (float(k[1])>22.3) and (float(k[1])<25):
    b="\t".join(k)
    s.append(b)
f=open("zb2cl2.txt","w")
f.write("\n".join(s))
f.close()

    

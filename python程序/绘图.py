import numpy as np  
import matplotlib.pyplot as plt
l=list(open('zb2.txt'))
x=[]
y=[]
for i in l:
    k=i.split()
    y.append(float(k[0]))
    x.append(float(k[1]))
#产生测试数据   
fig = plt.figure()  
ax1 = fig.add_subplot(111)  
#设置标题  
ax1.set_title('Scatter Plot')  
#设置X轴标签  
plt.xlabel('X')  
#设置Y轴标签  
plt.ylabel('Y')  
#画散点图  
ax1.scatter(x,y,s=3,c = 'r',marker = '.')
#设置图标  
plt.legend('x1')  
#显示所画的图  
plt.show()  
    

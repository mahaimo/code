# -*- coding: utf-8 -*-

import xlrd 
import numpy  
import math 
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean,stdev,variance 
import pylab 

Data = xlrd.open_workbook('xydata.xls')
sheet = excel.sheets()[0]
table = Data.sheets()[0]

x1=table.col_values(0)
y1=table.col_values(1)
x2=table.col_values(2)
y2=table.col_values(3)
x3=table.col_values(4)
y3=table.col_values(5)
x4=table.col_values(6)
y4=table.col_values(7)

#求四组x,y值的平均值ֵ
y1=mean(sheet.col_values(1))
x2=mean(sheet.col_values(2))
y2=mean(sheet.col_values(3))
x3=mean(sheet.col_values(4))
y3=mean(sheet.col_values(5))
x4=mean(sheet.col_values(6))
y4=mean(sheet.col_values(7))
print('average value��','x1=',x1,'y1=',y1,'x2=',x2,'y2=',y2,'x3=',x3,'y3=',y3,'x4=',x4,'y4=',y4)

#求四组x,y值的标准差
sx1=stdev(sheet.col_values(0))
sy1=stdev(sheet.col_values(1))
sx2=stdev(sheet.col_values(2))
sy2=stdev(sheet.col_values(3))
sx3=stdev(sheet.col_values(4))
sy3=stdev(sheet.col_values(5))
sx4=stdev(sheet.col_values(6))
sy4=stdev(sheet.col_values(7))
print('standard deviation��','sx1=',sx1,'sy1=',sy1,'sx2=',sx2,'sy2=',sy2,'sx3=',sx3,'sy3=',sy3,'sx4=',sx4,'sy4=',sy4)

#求四组x,y值的方差
vx1=variance(sheet.col_values(0))
vy1=variance(sheet.col_values(1))
vx2=variance(sheet.col_values(2))
vy2=variance(sheet.col_values(3))
vx3=variance(sheet.col_values(4))
vy3=variance(sheet.col_values(5))
vx4=variance(sheet.col_values(6))
vy4=variance(sheet.col_values(7))
print('variance��','vx1=',vx1,'vy1=',vy1,'vx2=',vx2,'vy2=',vy2,'vx3=',vx3,'vy3=',vy3,'vx4=',vx4,'vy4=',vy4)

def pearson(x,y): #计算皮尔逊相关系数
    n=len(x)
    # Simple sums
    sumx=sum([float(x[i]) for i in range(n)])
    sumy=sum([float(y[i]) for i in range(n)])
    # Sum up the squares
    sumxSq=sum([x[i]**2 for i in range(n)])
    sumySq=sum([y[i]**2 for i in range(n)])
    # Sum up the products
    pSum=sum([x[i]*y[i] for i in range(n)])
    # Calculate Pearson score
    num=pSum-(sumx*sumy/n)
    den=((sumxSq-pow(sumx,2)/n)*(sumySq-pow(sumy,2)/n))**0.5
    if den==0: return 0
    r=num/den
    return r

print('第1组皮尔逊相关系数' , pearson(x1,y1))
print('第2组皮尔逊相关系数' , pearson(x2,y2))
print('第3组皮尔逊相关系数' , pearson(x3,y3))
print('第4组皮尔逊相关系数' , pearson(x4,y4),'\n')

#第一组数据
x1 = pylab.array(x1)
y1 = pylab.array(y1)
pylab.figure(1)
pylab.title('practice6_Group1')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.plot(x1, y1,'go')
#find linear fit
a,b = pylab.polyfit(x1, y1, 1)
predictedy = a*pylab.array(x1) + b
pylab.plot(x1, predictedy) 

#第二组数据回归
x2 = pylab.array(x2)
y2 = pylab.array(y2)
pylab.figure(2)
pylab.title('practice6_Group2')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.plot(x2, y2,'go')
#find linear fit
a,b = pylab.polyfit(x2, y2, 1)
predictedy = a*pylab.array(x2) + b
pylab.plot(x2, predictedy) 

#第三组数据回归
x3 = pylab.array(x3)
y3 = pylab.array(y3)
pylab.figure(3)
pylab.title('practice6_Group3')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.plot(x3, y3,'go')
#find linear fit
a,b = pylab.polyfit(x3, y3, 1)
predictedy = a*pylab.array(x3) + b
pylab.plot(x3, predictedy) 

#第四组数据回归
x4 = pylab.array(x4)
y4 = pylab.array(y4)
pylab.figure(4)
pylab.title('practice6_Group4')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.plot(x4, y4,'go')
#find linear fit
a,b = pylab.polyfit(x4, y4, 1)
predictedy = a*pylab.array(x4) + b
pylab.plot(x4, predictedy)

pylab.show()

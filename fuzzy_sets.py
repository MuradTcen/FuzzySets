#!bin/python3
import xlrd
import xlwt
import pylab
import math
from matplotlib import mlab
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal 
from decimal import getcontext
getcontext().prec=2
'''
print
Универсум, Носитель, Точки перехода, унимодальность функции принадлежности,
нормально или субнормальное нечеткого множества, высота, ядро, границы
нечеткого множества
links:
http://www.bogotobogo.com/python/python_numpy_array_tutorial_basic_A.php
http://www.programcreek.com/python/example/504/numpy.array
http://cs231n.github.io/python-numpy-tutorial/#matplotlib
koldunov.net
'''
'''
Создать пользоват ф, резалтом кот явл массив значений, заносящийся в ячейки рабочего листа. Выполнить графическое отображение результата работы функции.
    x, x<=0
y = cos(x), 0<x<5
    sqrt(x**3), x>=5
    x принадлежит [-5;10]
   
'''


def printSet(l2,l1,xlabel,ylabel,title):
    x=l1
    y=l2
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.plot(x,y)
    pylab.show()
    
    
def print_3_sets(x0,y0,x1,y1,x2,y2,xlabel,ylabel,title0,title1,title2):
    pylab.subplot(3,1,1)
    pylab.title(title0)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.grid()
    pylab.plot(y0,x0)
    
    pylab.subplot(3,1,2)
    pylab.title(title1)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.grid()
    pylab.plot(y1,x1)
    
    pylab.subplot(3,1,3)
    pylab.title(title2)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.plot(y2,x2)
    pylab.grid()
    
    pylab.show()
'''       
def print_excel(title,xlabel,ylabel,l1,l2,ll1,ll2,ll3):
    writer = ExcelWriter('output.xlsx')
    df1.to_excel(writer,'Sheet1')
    df2.to_excel(writer,'Sheet2')
    writer.save()
    tmp=list('  '.join(map(str, l1)))
    df=pd.DataFrame()
    
'''
def decomp_by_level(l1,l2):
    while l1:
        min_group=min(l1)
        i=0
        while i<len(l1) and min_group==min(l1):    
            if l1[i]==min_group:

                print (min_group,l2[i])
                del l1[i]
                del l2[i]
            else: i+=1       
#----------------------4\/
    
    
def disjunction_sets(x,y):
    res=[]
    for i in range(len(x)):
        res.append(max(x[i],y[i]))      
    return res
    
   
def conjunction_sets(x,y):
    res=[]
    for i in range(len(x)):
        res.append(min(x[i],y[i]))      
    return res
        
        
def inv_set(x):
    res=[]
    for i in range(len(x)):
        res.append(1-x[i])        
    return res


def drastic_intersection(x,y):
    res=[]
    for i in range(len(x)):
        if x[i]==1: res.append(y[i])
        elif y[i]==1: res.append(x[i])
        else: res.append(0)
    return res
    
def drastic_join(x,y):
    res=[]
    for i in range(len(x)):
        if x[i]==0: res.append(y[i])
        elif y[i]==0: res.append(x[i])
        else: res.append(1)
    return res
    
    
def mul_sets(x,y):
    res=[]
    for i in range(len(x)):
        res.append(x[i]*y[i])
    return res
    

def total_sets(x,y):
    res=[]
    for i in range(len(x)):
        res.append(x[i]+y[i]-x[i]*y[i])
    return res
        

def disjuctive_total(x,y):
    return disjunction_sets((conjunction_sets(x,(inv_set(y)))),(conjunction_sets(inv_set(x),y))) 


def inv_conjunction_sets(x,y):
    return inv_set(conjunction_sets(x,y))
    
    
def con_dis_inv_drastic(x,y):
    return conjunction_sets(disjunction_sets(x,inv_set(y)),drastic_join(x,y))


def mul_dstotal_total(x,y):
    return mul_sets(disjuctive_total(x,y),total_sets(x,y)) 
#----------------------4 /\   

#----------------------5 \/
def con_set(x):
    res=[]
    for i in range(len(x)):
        res.append(x[i]**2)
    return res
    
    
def dil_set(x):
    res=[]
    for i in range(len(x)):
        res.append(x[i]**0.5)
    return res
    

def diff_sets(x,y):
    res=[]
    for i in range(len(x)):
        res.append(max(x[i]-y[i],0))
    return res    
#----------------------5 /\

#----------------------8 \/
def linear_hem_ind(x):
    tmp=[]
    dist=0
    quad_dist=0
    for i in range(len(x)):
        if x[i]>=0.5: tmp.append(1)
        else: tmp.append(0)
        dist+=abs(x[i]-tmp[i])
        quad_dist+=(x[i]-tmp[i])**2
    rel_dist_hem=dist/len(x)
    quad_dist=quad_dist**0.5
    rel_quad_dist=quad_dist/(len(x)**0.5)
    return 2*rel_dist_hem   
#----------------------8 /\


#----------------------9 \/
def euclid_ind(x):
    tmp=[]
    dist=0
    quad_dist=0
    for i in range(len(x)):
        if x[i]>=0.5: tmp.append(1)
        else: tmp.append(0)
        dist+=abs(x[i]-tmp[i])
        quad_dist+=(x[i]-tmp[i])**2
    rel_dist_hem=dist/len(x)
    quad_dist=quad_dist**0.5
    rel_quad_dist=quad_dist/(len(x)**0.5)
    return 2*rel_quad_dist
#----------------------9 /\

  
#----------------------10 \/  
def comp_ind(a,b):
    if a>b: print('%f more than %f' % (a,b))
    elif a==b: print('%f equel %f' % (a,b))
    else: print('%f less than %f' % (a,b))    
    
    
#----------------------10 /\ 
def calcToExcel(title,xlabel,ylabel,l1,l2,l3,l4,ll1,ll2,ll3):
    '''
    some shitty function
    '''
    xc=0
    wb=xlwt.Workbook()
    ws=wb.add_sheet('Task')
    ws.write(0,0,'Решение задачи 4')
    x0=np.linspace(-5,0,50)
    x1=np.linspace(0.01,4.99,50)
    x2=np.linspace(5,10,50)
    y1=np.cos(x1)
    y2=(x2**3)**0.5
    ws.write(0,1,'X')
    ws.write(1,1,'Y')
    for i in range(2,len(x0)+len(x1)+len(x2)):
        if i<len(x0): 
            ws.write(0,i,x0[i-2])
            ws.write(1,i,x0[i-2])
        elif i<len(x0)+len(x1):
            ws.write(0,i,x1[i-2-len(x0)])
            ws.write(1,i,y1[i-2-len(x0)])
        elif i<len(x0)+len(x1)+len(x2):
            ws.write(0,i,x2[i-2-len(x0)-len(x1)])
            ws.write(1,i,y2[i-2-len(x0)-len(x1)])   
    
            
    ws.write(xc+2,0,'Универсум:')
    ws.write(xc+3,0,'  '.join(map(str, l1)))
    ws.write(xc+4,0,'  '.join(map(str, l2)))
    ws.write(xc+5,0,'Носитель:')
    k=0
    for i in range(len(l1)):
        if l2[i]>0:
            ws.write(xc+6,k,l2[i])
            k+=1
    ws.write(xc+7,0,'Точки перехода:')
    tmp=0
    for i in range(len(l1)):
        if l1[i]==0.5:
            ws.write(xc+8,tmp,l2[i])
            tmp+=1
    if tmp==0: ws.write(xc+8,0,'Нет')
    ws.write(xc+10,0,'Унимодально: ')
    tmp=0
    for i in range(len(l1)):
        if l1[i]==1:
            tmp+=1
    if tmp==1: ws.write(xc+11,1,'Да')
    else: ws.write(xc+11,1,'Нет')
    tmps='Высота: '+str(max(l1))
    ws.write(xc+12,0,tmps)
    if max(l1)==1.0: ws.write(xc+13,0,'Нечеткое множество - нормально')
    else: ws.write(xc+13,0,'Нечеткое множество - субнормально')

    ws.write(xc+14,0,'Ядро: ')
    tmp=0
    k=0
    for i in range(len(l1)): 
        if l1[i]==1:
            ws.write(xc+15,k,l2[i])
            k+=1     
            tmp+=1
    if tmp==0: ws.write(xc+16,0,'Нет')
    k=0
    ws.write(xc+17,0,'Граница: ') 
    for i in range(len(l1)):
        if l1[i]>0 and l1[i]<1:
            ws.write(xc+18,k,l2[i])  
            k+=1
            
    ws.write(xc+19,0,'Нормализация: ')  
    for i in range(len(l1)):
        l1[i]/=max(l1)
        l1[i]=round(l1[i],1)
    ws.write(xc+20,0,'  '.join(map(str, l1)))
    ws.write(xc+21,0,'  '.join(map(str, l2))) 
    ws.write(xc+22,0,'Разложение нечеткого множества по множествам уровня: ')
    tmpl=l1
    tmpl1=l2
    tmpc=0
    while tmpl:
        ws.write(xc+tmpc+23,0,min(tmpl))
        k=0
        group=min(tmpl)
        i=0
        while i<len(tmpl) and group==min(tmpl):    
            if tmpl[i]==group:
                ws.write(xc+tmpc+23,k+1,tmpl1[i])
                print (group,tmpl1[i])
                del tmpl[i]
                del tmpl1[i]
                k+=1
            i+=1
        tmpc+=1
    #________________________________________
    
    xc=30
    ws.write(xc+1,0,'Характеристика нечеткого множества Y')
    ws.write(xc+2,0,'Универсум:')
    ws.write(xc+3,0,'  '.join(map(str, l3)))
    ws.write(xc+4,0,'  '.join(map(str, l4)))
    ws.write(xc+5,0,'Носитель:')
    k=0
    for i in range(len(l4)):
        if l4[i]>0:
            ws.write(xc+6,k,l4[i])
            k+=1
    ws.write(xc+7,0,'Точки перехода:')
    tmp=0
    for i in range(len(l3)):
        if l3[i]==0.5:
            ws.write(xc+8,tmp,l4[i])
            tmp+=1
    if tmp==0: ws.write(xc+8,0,'Нет')
    ws.write(xc+10,0,'Унимодально: ')
    tmp=0
    for i in range(len(l3)):
        if l3[i]==1:
            tmp+=1
    if tmp==1: ws.write(xc+11,1,'Да')
    else: ws.write(xc+11,1,'Нет')
    tmps='Высота: '+str(max(l3))
    ws.write(xc+12,0,tmps)
    if max(l3)==1.0: ws.write(xc+13,0,'Нечеткое множество - нормально')
    else: ws.write(xc+13,0,'Нечеткое множество - субнормально')

    ws.write(xc+14,0,'Ядро: ')
    tmp=0
    k=0
    for i in range(len(l3)): 
        if l3[i]==1:
            ws.write(xc+15,k,l4[i])
            k+=1     
            tmp+=1
    if tmp==0: ws.write(xc+16,0,'Нет')
    k=0
    ws.write(xc+17,0,'Граница: ') 
    for i in range(len(l3)):
        if l3[i]>0 and l3[i]<1:
            ws.write(xc+18,k,l4[i])  
            k+=1
            
    ws.write(xc+19,0,'Нормализация: ')  
    for i in range(len(l3)):
        l3[i]/=max(l3)
        l3[i]=round(l3[i],1)
    ws.write(xc+20,0,'  '.join(map(str, l3)))
    ws.write(xc+21,0,'  '.join(map(str, l4)))     
        
    pylab.title(title)
    
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)    
    line_1=pylab.plot(x0,x0,'bD:')
    line_2=pylab.plot(x1,y1)
    line_3=pylab.plot(x2,y2)
    legend=pylab.legend((ll1,ll2,ll3),loc='upper center')
    #frame = legend.get_frame()
    #frame.set_facecolor('0.90')
    #pylab.grid()
    pylab.show()    
    wb.save('solution.xlsx')
    
  
def ploting(l0,title,xlabel,ylabel):
    #formatedYVector=['%.2f' % elem for elem in ylist ]
    x=np.arange(l0[0],l0[1],l0[2])
    y=l0[3]*x*x-l0[4]*x+l0[5]
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.plot(x,y)
    pylab.show()


def subnormalToNormal(l1,l2):
    print ('')
    for i in range(len(l1)):
        l1[i]/=max(l1)
        l1[i]=round(l1[i],1)
    print ('  '.join(map(str, l1))+'\n'+'  '.join(map(str, l2)),'\n')
    
    
def printPropertyFuzzySet(l1,l2):
    print ('\nУниверсум:')
    #print (str(l1)[1:-1]) or print (str(l1).strip('[]'))
    print ('  '.join(map(str, l1))+'\n'+'  '.join(map(str, l2)),'\n')
    print ('Носитель:')
    for i in range(len(l1)):
        if l2[i]>0:
            print (l2[i],' ',end='')
    print ('\nТочки перехода:')
    tmp=0
    for i in range(len(l1)):
        if l1[i]==0.5:
            print (l2[i],' ',end='')
            tmp+=1
    if tmp==0: print ('Нет')
    print ('\nУнимодально: ',end='')
    tmp=0
    for i in range(len(l1)):
        if l1[i]==1:
            tmp+=1
    if tmp==1: print ('Да')
    else: print ('Нет')
    print ('Высота: ',max(l1),end='')
    print('')
    if max(l1)==1.0: print ('Нечеткое множество - нормально')
    else: print ('Нечеткое множество - субнормально')
 
    print ('Ядро: ',end='')
    tmp=0
    for i in range(len(l1)): 
        if l1[i]==1: print (l2[i],' ',end='')     
    if tmp==0: print ('Нет')

    print ('\nГраница: ',end='') 
    for i in range(len(l1)):
        if l1[i]>0 and l1[i]<1: print (l2[i],' ',end='')  

'''
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def parsing(listParse):
    i=0
    while i<len(listParse):
        if listParse[i]=='':
            listParse.pop(i)
            i-=1
        if not is_number(listParse[i]):
            listParse.pop(i)
            i-=1           
        i+=1
    return listParse
'''







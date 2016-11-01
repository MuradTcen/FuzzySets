#!bin/python3
import xlrd
import xlwt
import pandas as pd
import pylab
import math
from matplotlib import mlab
import matplotlib.pyplot as plt
import numpy as np


'''
links:
http://www.bogotobogo.com/python/python_numpy_array_tutorial_basic_A.php
http://www.programcreek.com/python/example/504/numpy.array
http://cs231n.github.io/python-numpy-tutorial/#matplotlib
koldunov.net
'''


def list_to_exc(lst0):
    t='title'
    exc_f='pandas.xlsx'
    #df=pd.DataFrame({'data':[1,3,4,5]})
    df=pd.DataFrame({'data':[x for x in lst0]})
    writer=pd.ExcelWriter(exc_f)
    df.to_excel(writer,sheet_name='Sheet1')
    writer.save()


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

         
def decomp_by_level(l1,l2):
    res=[]
    tmp=[]
    tmp1=[]
    while len(l1)>1:
        min_group=min(l1)
        i=0
        while i<len(l1) and min_group==min(l1):    
            if l1[i]==min_group:
                tmp.append(min_group)
                tmp1.append(l2[i])
                del l1[i]
                del l2[i]
            else: i+=1 
    res.append(tmp) 
    res.append(tmp1) 
    return res   
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

#----------------------PROPERTIES \/
NO='Нет'
YES='Да'

def half_dots(x,y):
    res=''
    tmp=0
    for i in range(len(x)):
        if x[i]==0.5:
            res+=str(y[i])+' '
            tmp+=1
    if tmp==0: return NO
    return res
    

def is_unimodal(x):
    tmp=0
    for i in range(len(x)):
        if x[i]==1:
            tmp+=1
    if tmp==1: return YES
    else: return NO
    

hight_set=(lambda x: max(x)) 


def str_uni(y):
    res=''
    for i in range(len(y)):
        res=res+str(y[i])+' '
    return res
    

def is_normal(x):
    if max(x)==1.0: return 'нормально'
    else: return 'субнормально'
    
def core_of_set(x,y): 
    res=''   
    is_absent=True
    for i in range(len(x)): 
        if x[i]==1:
            res+=str(y[i])
            res+=' '     
            is_absent=True
    if is_absent: return NO
    return res
    

def edge_of_set(x,y): 
    res=''
    is_abcent=True
    for i in range(len(x)):
        if x[i]>0 and x[i]<1:
            res+=str(x[i])  
            res+=' '
            is_abcent=False
    if is_abcent: return NO
    return res
    
    
def set_to_str(x,y):
    res=''
    for i in range(len(x)):
        res=res+str(x[i])+'/'+str(y[i])+' '
    return res
    
    
def normal_set(x,y):
    res=''  
    for i in range(len(x)):
        res=res+str(round(x[i]/max(x),2))+'/'+str(y[i])+' '
    return res 
#ленина 74f 218 

 
#----------------------PROPERTIES /\ 

'''        
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
'''    
  
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







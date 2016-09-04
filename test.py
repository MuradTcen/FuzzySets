#!bin/python3
import xlrd
import pylab
from matplotlib import mlab
import numpy as np


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
   
def ploting(l0):
    #formatedYVector=['%.2f' % elem for elem in ylist ]
    x=np.arange(l0[0],l0[1],l0[2])
    y=l0[3]*x*x-l0[4]*x+l0[5]
    pylab.plot(x,y)
    pylab.show()

def subnormalToNormal(l1,l2,l3,l4):
    print ('')
    for i in range(len(l1)):
        l1[i]/=max(l1)
    for i in range(len(l3)):
        l3[i]/=max(l3)
    print ('  '.join(map(str, l1))+'\n'+'  '.join(map(str, l2)),'\n')
    print ('  '.join(map(str, l3))+'\n'+'  '.join(map(str, l4)),'\n')
    
def printPropertyFuzzySet(l1,l2,l3,l4):
    print ('Универсумы:')
    #print (str(l1)[1:-1]) or print (str(l1).strip('[]'))
    print ('  '.join(map(str, l1))+'\n'+'  '.join(map(str, l2)),'\n')
    print ('  '.join(map(str, l3))+'\n'+'  '.join(map(str, l4)),'\n')
    #---------------------------
    print ('Носитель:')
    for i in range(len(l1)):
        if l1[i]>0:
            print (l2[i],' ',end='')
    print ('')
    for i in range(len(l3)):
        if l3[i]>0:
            print (l4[i],' ',end='')
    #---------------------------
    print ('\nТочки перехода:')
    for i in range(len(l1)):
        if l1[i]==0.5:
            print (l2[i],' ',end='')
    print ('')
    for i in range(len(l3)):
        if l3[i]==0.5:
            print (l4[i],' ',end='')
    #---------------------------
    print ('\nX унимодально: ',end='')
    tmp=0
    for i in range(len(l1)):
        if l1[i]==1:
            tmp+=1
    if tmp==1: print ('Да')
    else: print ('Нет')
    #---------------------------
    print ('Y унимодально: ',end='')
    tmp=0
    for i in range(len(l1)):
        if l1[i]==1:
            tmp+=1
    if tmp==1: print ('Да')
    else: print ('Нет')
    #---------------------------
    print ('Высота X: ',max(l1),'\nВысота Y: ',max(l3),'\n',end='')
    #---------------------------
    if max(l1)==1.0: print ('Нечеткое множество X - нормально')
    else: print ('Нечеткое множество X - субнормально')
    if max(l3)==1.0: print ('Нечеткое множество Y - нормально')
    else: print ('Нечеткое множество Y - субнормально')   
    #---------------------------
    print ('Ядро X: ',end='')
    for i in range(len(l1)): 
        if l1[i]==1: print (l2[i],' ',end='')     
    print ('\nЯдро Y: ',end='')
    for i in range(len(l3)): 
        if l3[i]==1: print (l4[i],' ',end='')   
    #---------------------------
    print ('\nГраница X: ',end='') 
    for i in range(len(l1)):
        if l1[i]>0 and l1[i]<1: print (l2[i],' ',end='')  
    print ('\nГраница Y: ',end='') 
    for i in range(len(l3)):
        if l3[i]>0 and l3[i]<1: print (l4[i],' ',end='') 

'''

'''
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
'''

'''
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

'''----------------------------------------------'''

rb=xlrd.open_workbook('Нечеткие множества.xlsx')
sheet = rb.sheet_by_index(1)
listData0=listData1=listData2=listData3=listData4=[]      
#filling lists
listData0=parsing(sheet.row_values(2))
listData1=parsing(sheet.row_values(3))
listData2=parsing(sheet.row_values(4))
listData3=parsing(sheet.row_values(6))
listData4=parsing(sheet.row_values(7))

'''TODO:
    1. parsing function-done'''

''''''

print (listData0)
print (listData1)
print (listData2)
print (listData3)
print (listData4)
printPropertyFuzzySet(listData1,listData2,listData3,listData4)
subnormalToNormal(listData1,listData2,listData3,listData4)
ploting(listData0)




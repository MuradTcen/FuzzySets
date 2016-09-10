#!bin/python3
import xlrd
import xlwt
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
'''
Создать пользоват ф, резалтом кот явл массив значений, заносящийся в ячейки рабочего листа. Выполнить графическое отображение результата работы функции.
    x, x<=0
y = cos(x), 0<x<5
    sqrt(x**3), x>=5
    x принадлежит [-5;10]
   
'''

def calcToExcel():
    #df=read_excel('Нечеткие множества.xlsx')
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
    pylab.plot(x0,x0)
    pylab.plot(x1,y1)
    pylab.plot(x2,y2)
    pylab.show()    
    wb.save('solution.xlsx')
  
  
def ploting(l0):
    #formatedYVector=['%.2f' % elem for elem in ylist ]
    x=np.arange(l0[0],l0[1],l0[2])
    y=l0[3]*x*x-l0[4]*x+l0[5]
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






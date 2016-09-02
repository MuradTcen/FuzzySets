#python3
import xlrd


'''
print
Универсум, Носитель, Точки перехода, унимодальность функции принадлежности,
нормально или субнормальное нечеткого множества, высота, ядро, границы
нечеткого множества

'''
def plot():
    print (' ')

def subnormalToNormal():
    print (' ')
def printPropertyFuzzySet(l0,l1,l2,l3,l4):
    print ('Универсум:')
    for i in range(len(l1)):
        print (l1[i],' ',end='')
    print ('')
    for i in range(len(l1)):
        print ('--- ',end=' ')
    print ('')
    for i in range(len(l1)):
        print (l2[i],' ',end='')
    print ('')
    for i in range(len(l3)):
        print (l3[i],' ',end='')
    print ('')
    for i in range(len(l4)):
        print ('--- ',end=' ')
    print ('')
    for i in range(len(l4)):
        print (l4[i],' ',end='')
    #---------------------------
    print ('\nНоситель:')
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
    if tmp==0: print ('Да')
    else: print ('Нет')
    #---------------------------
    print ('Y унимодально: ',end='')
    tmp=0
    for i in range(len(l1)):
        if l1[i]==1:
            tmp+=1
    if tmp==0: print ('Да')
    else: print ('Нет')
    #---------------------------
    print ('Высота: ',end='')
    
  

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
printPropertyFuzzySet(listData0,listData1,listData2,listData3,listData4)




#!bin/python3
import xlrd
import xlwt
import pylab
from matplotlib import mlab
import numpy as np
import fuzzy_sets


rb=xlrd.open_workbook('FuzzySets.xlsx')
sheet = rb.sheet_by_index(0)
listData0=listData1=listData2=listData3=listData4=[]      
#filling lists
listData0=fuzzy_sets.parsing(sheet.row_values(2))
listData1=fuzzy_sets.parsing(sheet.row_values(3))
listData2=fuzzy_sets.parsing(sheet.row_values(4))
listData3=fuzzy_sets.parsing(sheet.row_values(6))
listData4=fuzzy_sets.parsing(sheet.row_values(7))

'''TODO:
    1. parsing function-done'''
   

''''''
title1='Graph y=ax**2 bx + c'
title2='Graph of function'
legend1="function y=x, x<0"
legend2='function y=cos(x), x c[0;5)'
legend3='function y=sqrt(x**3), x c[5;10]'
xlabel1='X'
ylabel1='uA(x)'
xlabel2='X'
ylabel2='Y'
print (listData1)
print (listData2)
print (listData3)
print (listData4)
fuzzy_sets.printPropertyFuzzySet(listData1,listData2)
fuzzy_sets.printPropertyFuzzySet(listData3,listData4)
print('\nНормализация')
fuzzy_sets.subnormalToNormal(listData1,listData2)
fuzzy_sets.subnormalToNormal(listData3,listData4)
fuzzy_sets.ploting(listData0,title1,xlabel1,ylabel1)
fuzzy_sets.calcToExcel(title2,xlabel2,ylabel2,listData1,listData2,listData3,listData4,
legend1,legend2,legend3)

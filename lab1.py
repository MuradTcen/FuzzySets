#!bin/python3
import xlrd
import xlwt
import pylab
from matplotlib import mlab
import numpy as np
import fuzzy_sets


rb=xlrd.open_workbook('Нечеткие множества.xlsx')
sheet = rb.sheet_by_index(2)
listData0=listData1=listData2=listData3=[]      
#filling lists
listData0=fuzzy_sets.parsing(sheet.row_values(2))
listData1=fuzzy_sets.parsing(sheet.row_values(3))
listData2=fuzzy_sets.parsing(sheet.row_values(5))
listData3=fuzzy_sets.parsing(sheet.row_values(6))


'''TODO:
   

'''
print (listData0)
print (listData1)
print (listData2)
print (listData3)
'''
fuzzy_sets.printPropertyFuzzySet(listData1,listData2)
fuzzy_sets.printPropertyFuzzySet(listData3,listData4)
print('\nНормализация')
fuzzy_sets.subnormalToNormal(listData1,listData2)
fuzzy_sets.subnormalToNormal(listData3,listData4)
fuzzy_sets.ploting(listData0)
fuzzy_sets.calcToExcel()
'''

#!bin/python3
import pylab
from matplotlib import mlab
import numpy as np
import fuzzy_sets
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
'''
1 2 3 4 5 6 7 8 9 10
- - - - - - - - - ++
'''
testx=[0.1,0.6,0.9,1,0.5,0.8,0.4,0.5]
testy=[0.7,0.5,1,0.6,0.4,0.3,0,0.2]
tstx=[0.3,0.5,0.7,0.9,1.0]
tsty=[0.3,0.5,0.8,0.8]
titleFS='$Graph of Fuzzy Set$'
titlex0='$X$'
titlex1='$CON(X)$'
titlex2='$DIL(X)$'
titley0='$Y$'
titley1='$CON(Y)$'
titley2='$DIL(Y)$'
x_label_F_S='$X$'
y_label_F_S='$\mu(X)$'
y_x_label_F_S='$Y$'
y_y_label_F_S='$\mu(Y)$'
df=pd.read_excel('FuzzySets.xlsx',sheetname='Sheet3')  

l0=df['µa(x1n)']
l1=df['x1']
l2=df['µa(x2n)']
l3=df['x2']
l0=l0[np.logical_not(np.isnan(l0))]
l1=l1[~np.isnan(l1)]
l2=l2[~np.isnan(l2)]
l3=l3[~np.isnan(l3)]

ll0=l0.tolist()
ll1=l1.tolist()
ll2=l2.tolist()
ll3=l3.tolist()

#---------------------3
#fuzzy_sets.decomp_by_level(ll0,ll1)
#fuzzy_sets.printSet(l1,l0,x_label_F_S,y_label_F_S,titleFS)
#fuzzy_sets.printSet(l3,l2,x_label_F_S,y_label_F_S,titleFS)
#---------------------3


#---------------------4
#disjunction of x and y
disjunctionXY=fuzzy_sets.disjunction_sets(l0,l2)
#conjunction of x and y
conjunctionXY=fuzzy_sets.conjunction_sets(l0,l2)
#inversion of conjuction's X an Y
inv_con_XY=fuzzy_sets.inv_conjunction_sets(l0,l2)
#con's dis's invX and Y..
cons_dis_invYX_drasticXY=fuzzy_sets.con_dis_inv_drastic(l0,l2)
#dis's total..
mul_distotal_total=fuzzy_sets.mul_dstotal_total(l0,l2)
#---------------------4

#---------------------5
con_x=fuzzy_sets.con_set(l0)
con_y=fuzzy_sets.con_set(l2)
dil_x=fuzzy_sets.dil_set(l0)
dil_y=fuzzy_sets.dil_set(l2)
alg_adj_x=fuzzy_sets.inv_set(l0)
alg_adj_y=fuzzy_sets.inv_set(l2)
dis_total=fuzzy_sets.disjuctive_total(l0,l2)
#---------------------5
'''
#---------------------6
fuzzy_sets.print_3_sets(l0,l1,con_x,l1,dil_x,l1,x_label_F_S,y_label_F_S,titlex0,titlex1,titlex2)
fuzzy_sets.print_3_sets(l2,l3,con_y,l3,dil_y,l3,y_x_label_F_S,y_y_label_F_S,titley0,titley1,titley2)
#---------------------6
'''
#---------------------8
hem_x=fuzzy_sets.linear_hem_ind(l0)
hem_con_x=fuzzy_sets.linear_hem_ind(con_x)
hem_dil_x=fuzzy_sets.linear_hem_ind(dil_x)
hem_y=fuzzy_sets.linear_hem_ind(l2)
hem_con_y=fuzzy_sets.linear_hem_ind(con_y)
hem_dil_y=fuzzy_sets.linear_hem_ind(dil_y)
#---------------------8
#---------------------9
euc_x=fuzzy_sets.euclid_ind(l0)
euc_con_x=fuzzy_sets.euclid_ind(con_x)
euc_dil_x=fuzzy_sets.euclid_ind(dil_x)
euc_y=fuzzy_sets.euclid_ind(l2)
euc_con_y=fuzzy_sets.euclid_ind(con_y)
euc_dil_y=fuzzy_sets.euclid_ind(dil_y)
#---------------------9

'''
#---------------------10
fuzzy_sets.comp_ind(hem_x,hem_dil_x)
fuzzy_sets.comp_ind(hem_x,hem_con_x)
fuzzy_sets.comp_ind(hem_con_x,hem_dil_x)

fuzzy_sets.comp_ind(euc_x,euc_dil_x)
fuzzy_sets.comp_ind(euc_x,euc_con_x)
fuzzy_sets.comp_ind(euc_con_x,euc_dil_x)

fuzzy_sets.comp_ind(hem_y,hem_dil_y)
fuzzy_sets.comp_ind(hem_y,hem_con_y)
fuzzy_sets.comp_ind(hem_con_y,hem_dil_y)

fuzzy_sets.comp_ind(euc_y,euc_dil_y)
fuzzy_sets.comp_ind(euc_y,euc_con_y)
fuzzy_sets.comp_ind(euc_con_y,euc_dil_y)
#---------------------10
'''
#fuzzy_sets.calcToExcel#(titleFS,x_label_F_S,x_label_F_S,l0,l1,l2,l3,'','','')

#fuzzy_sets.calcToExcel(titleFS,x_label_F_S,x_label_F_S,listData0,listData1,listData2,
#                        listData3,'','','')

'''
fuzzy_sets.printPropertyFuzzySet(listData1,listData2)
fuzzy_sets.printPropertyFuzzySet(listData3,listData4)
print('\nНормализация')
fuzzy_sets.subnormalToNormal(listData1,listData2)
fuzzy_sets.subnormalToNormal(listData3,listData4)
fuzzy_sets.ploting(listData0)
fuzzy_sets.calcToExcel()
'''

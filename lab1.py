#!bin/python3
import pylab
from matplotlib import mlab
import numpy as np
import fuzzy_sets as fs
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
'''
1 2 3 4 5 6 7 8 9 10
- - - - - - - - - ++
'''

def nor(a,b):
    for i in range(len(b)-len(a)):
        a.append(np.nan)
        
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
'''
l0=l0[np.logical_not(np.isnan(l0))]
l1=l1[~np.isnan(l1)]
l2=l2[~np.isnan(l2)]
l3=l3[~np.isnan(l3)]
'''
ll0=l0.tolist()
ll1=l1.tolist()
ll2=l2.tolist()
ll3=l3.tolist()
#---------------------3
decomp=fs.decomp_by_level(ll0,ll1)
dec_x_0=decomp[0]
dec_x_1=decomp[1]
nor(dec_x_1,ll2)
nor(dec_x_0,ll2)

decomp1=fs.decomp_by_level(ll2,ll3)
dec_y_0=decomp1[0]
dec_y_1=decomp1[1]
#fs.printSet(l1,l0,x_label_F_S,y_label_F_S,titleFS)
#fs.printSet(l3,l2,x_label_F_S,y_label_F_S,titleFS)
#---------------------3


#---------------------4
disjunctionXY=fs.disjunction_sets(l0,l2)
conjunctionXY=fs.conjunction_sets(l0,l2)
inv_con_XY=fs.inv_conjunction_sets(l0,l2)
cons_dis_invYX_drasticXY=fs.con_dis_inv_drastic(l0,l2)
mul_distotal_total=fs.mul_dstotal_total(l0,l2)
#---------------------4

#---------------------5
con_x=fs.con_set(l0)
con_y=fs.con_set(l2)
dil_x=fs.dil_set(l0)
dil_y=fs.dil_set(l2)
alg_adj_x=fs.inv_set(l0)
alg_adj_y=fs.inv_set(l2)
dis_total=fs.disjuctive_total(l0,l2)
#---------------------5
'''
#---------------------6
fs.print_3_sets(l0,l1,con_x,l1,dil_x,l1,x_label_F_S,y_label_F_S,titlex0,titlex1,titlex2)
fs.print_3_sets(l2,l3,con_y,l3,dil_y,l3,y_x_label_F_S,y_y_label_F_S,titley0,titley1,titley2)
#---------------------6
'''
#---------------------8
hem_x=fs.linear_hem_ind(l0)
hem_con_x=fs.linear_hem_ind(con_x)
hem_dil_x=fs.linear_hem_ind(dil_x)
hem_y=fs.linear_hem_ind(l2)
hem_con_y=fs.linear_hem_ind(con_y)
hem_dil_y=fs.linear_hem_ind(dil_y)
#---------------------8
#---------------------9
euc_x=fs.euclid_ind(l0)
euc_con_x=fs.euclid_ind(con_x)
euc_dil_x=fs.euclid_ind(dil_x)
euc_y=fs.euclid_ind(l2)
euc_con_y=fs.euclid_ind(con_y)
euc_dil_y=fs.euclid_ind(dil_y)
#---------------------9
half_dots_x=fs.half_dots(l0,l1)
half_dots_y=fs.half_dots(l2,l3)
unim_x=fs.is_unimodal(l0)
unim_y=fs.is_unimodal(l2)
hi_x=fs.hight_set(l0)
hi_y=fs.hight_set(l0)
norm_x=fs.is_normal(l0)
norm_y=fs.is_normal(l2)
core_y=fs.core_of_set(l2,l3)
core_x=fs.core_of_set(l0,l1)
edge_x=fs.edge_of_set(l0,l1)
edge_y=fs.edge_of_set(l0,l1)
str_x=fs.set_to_str(l0,l1)
str_y=fs.set_to_str(l2,l3)
norm_x=fs.normal_set(l0,l1)
norm_y=fs.normal_set(l2,l3)
uni_x=fs.str_uni(l1)
uni_y=fs.str_uni(l3)
#---------------------TO_EXCEL \/
df=pd.DataFrame({'mu(x)':[x for x in l1],'x':[x for x in l0],
                'mu(y)':[x for x in l3],'y':[x for x in l2],
                'Уровни':[x for x in dec_x_0],
                'Уровни mu(x)':[x for x in dec_x_1],
                'stage_y':[x for x in dec_y_0],
                'dmu(y)':[x for x in dec_y_1],
                'DisjuctionXY':[x for x in disjunctionXY],
                'ConjuctionXY':[x for x in conjunctionXY],
                'inv_con_XY':[x for x in inv_con_XY],
                'cons_dis_invYX_drasticXY':[x for x in cons_dis_invYX_drasticXY],
                'mul_distotal_total':[x for x in mul_distotal_total],
                'inv_con_XY':[x for x in inv_con_XY],
                'con_x':[x for x in con_x],
                'dil_x':[x for x in dil_x],
                'con_y':[x for x in con_y],
                'dil_y':[x for x in dil_y],
                'alg_adj_x':[x for x in alg_adj_x],
                'alg_adj_y':[x for x in alg_adj_y],
                'dis_total':[x for x in dis_total]
                })
                
df1=pd.DataFrame({'hem_x':[hem_x],
                'hem_con_x':hem_con_x,
                'hem_dil_x':hem_dil_x,
                'hem_y':hem_y,
                'hem_con_y':hem_con_y,
                'hem_dil_y':[hem_dil_y],
                
                'euc_x':euc_x,
                'euc_con_x':euc_con_x,
                'euc_dil_x':euc_dil_x,
                'euc_y':euc_y,
                'euc_con_y':euc_con_y,
                'euc_dil_y':euc_dil_y
                })
df2=pd.DataFrame({'Точки перехода X':[half_dots_x],
                'Унимодально ':[unim_x],
                'Высота':[hi_x],
                'Ядро': core_x,
                'Граница':edge_x,
                'Нечеткое мн-во':str_x,
                'Нормал.':norm_x,
                'Универсум':uni_x
                })
writer=pd.ExcelWriter('pandas.xlsx')
df.to_excel(writer,sheet_name='sets')
df1.to_excel(writer,sheet_name='indices')
df2.to_excel(writer,sheet_name='property_x')
writer.save()
#---------------------TO_EXCEL /\
'''
#---------------------10
fs.comp_ind(hem_x,hem_dil_x)
fs.comp_ind(hem_x,hem_con_x)
fs.comp_ind(hem_con_x,hem_dil_x)

fs.comp_ind(euc_x,euc_dil_x)
fs.comp_ind(euc_x,euc_con_x)
fs.comp_ind(euc_con_x,euc_dil_x)

fs.comp_ind(hem_y,hem_dil_y)
fs.comp_ind(hem_y,hem_con_y)
fs.comp_ind(hem_con_y,hem_dil_y)

fs.comp_ind(euc_y,euc_dil_y)
fs.comp_ind(euc_y,euc_con_y)
fs.comp_ind(euc_con_y,euc_dil_y)
#---------------------10
'''
#fs.calcToExcel#(titleFS,x_label_F_S,x_label_F_S,l0,l1,l2,l3,'','','')

#fs.calcToExcel(titleFS,x_label_F_S,x_label_F_S,listData0,listData1,listData2,
#                        listData3,'','','')

'''
fs.printPropertyFuzzySet(listData1,listData2)
fs.printPropertyFuzzySet(listData3,listData4)
print('\nНормализация')
fs.subnormalToNormal(listData1,listData2)
fs.subnormalToNormal(listData3,listData4)
fs.ploting(listData0)
fs.calcToExcel()
'''

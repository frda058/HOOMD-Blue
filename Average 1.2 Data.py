#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:52:46 2021

@author: francescaabulencia
"""


import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

#%%

phi = [0.55, 0.57, 0.58]

relaxtime_0_2_radii = [1.0, 1.2, 0.2]

relaxtime_0_2_rA = 1.0
relaxtime_0_2_rB = 1.2
relaxtime_0_2_rC = 0.2

relaxtime_0_2_particleA = np.array([])
relaxtime_0_2_particleA[:] = [x/(relaxtime_0_2_rA**2) for x in relaxtime_0_2_particleA]

relaxtime_0_2_particleB = np.array([])
relaxtime_0_2_particleB[:] = [x/(relaxtime_0_2_rB**2) for x in relaxtime_0_2_particleB]

relaxtime_0_2_particleC = np.array([])
relaxtime_0_2_particleC[:] = [x/(relaxtime_0_2_rC**2) for x in relaxtime_0_2_particleC]

relaxtime_0_2_particleA_rep1 = np.array([])
relaxtime_0_2_particleA_rep1[:] = np.array([x/(relaxtime_0_2_rA**2) for x in relaxtime_0_2_particleA_rep1])

relaxtime_0_2_particleB_rep1 = np.array([])
relaxtime_0_2_particleB_rep1[:] = [x/(relaxtime_0_2_rB**2) for x in relaxtime_0_2_particleB_rep1]

relaxtime_0_2_particleC_rep1 = np.array([])
relaxtime_0_2_particleC_rep1[:] = [x/(relaxtime_0_2_rC**2) for x in relaxtime_0_2_particleC_rep1]

relaxtime_0_2_particleA_rep2 = np.array([])
relaxtime_0_2_particleA_rep2[:] = [x/(relaxtime_0_2_rA**2) for x in relaxtime_0_2_particleA_rep2]

relaxtime_0_2_particleB_rep2 = np.array([])
relaxtime_0_2_particleB_rep2[:] = [x/(relaxtime_0_2_rB**2) for x in relaxtime_0_2_particleB_rep2]

relaxtime_0_2_particleC_rep2 = np.array([])
relaxtime_0_2_particleC_rep2[:] = [x/(relaxtime_0_2_rC**2) for x in relaxtime_0_2_particleC_rep2]

a = [relaxtime_0_2_particleA, relaxtime_0_2_particleA_rep1, relaxtime_0_2_particleA_rep2]
b = [relaxtime_0_2_particleB, relaxtime_0_2_particleB_rep1, relaxtime_0_2_particleB_rep2]
c = [relaxtime_0_2_particleC, relaxtime_0_2_particleC_rep1, relaxtime_0_2_particleC_rep2]

relaxtime_0_2_particleA_avg = np.mean(a, axis=0)
relaxtime_0_2_particleB_avg = np.mean(b, axis=0)
relaxtime_0_2_particleC_avg = np.mean(c, axis=0)



#%%

phi = [0.55, 0.57, 0.58]

relaxtime_0_3_radii = [1.0, 1.2, 0.3]

relaxtime_0_3_rA = 1.0
relaxtime_0_3_rB = 1.2
relaxtime_0_3_rC = 0.3

relaxtime_0_3_particleA = np.array([])
relaxtime_0_3_particleA[:] = [x/(relaxtime_0_3_rA**2) for x in relaxtime_0_3_particleA]

relaxtime_0_3_particleB = np.array([])
relaxtime_0_3_particleB[:] = [x/(relaxtime_0_3_rB**2) for x in relaxtime_0_3_particleB]

relaxtime_0_3_particleC = np.array([])
relaxtime_0_3_particleC[:] = [x/(relaxtime_0_3_rC**2) for x in relaxtime_0_3_particleC]

relaxtime_0_3_particleA_rep1 = np.array([])
relaxtime_0_3_particleA_rep1[:] = np.array([x/(relaxtime_0_3_rA**2) for x in relaxtime_0_3_particleA_rep1])

relaxtime_0_3_particleB_rep1 = np.array([])
relaxtime_0_3_particleB_rep1[:] = [x/(relaxtime_0_3_rB**2) for x in relaxtime_0_3_particleB_rep1]

relaxtime_0_3_particleC_rep1 = np.array([])
relaxtime_0_3_particleC_rep1[:] = [x/(relaxtime_0_3_rC**2) for x in relaxtime_0_3_particleC_rep1]

relaxtime_0_3_particleA_rep2 = np.array([])
relaxtime_0_3_particleA_rep2[:] = [x/(relaxtime_0_3_rA**2) for x in relaxtime_0_3_particleA_rep2]

relaxtime_0_3_particleB_rep2 = np.array([])
relaxtime_0_3_particleB_rep2[:] = [x/(relaxtime_0_3_rB**2) for x in relaxtime_0_3_particleB_rep2]

relaxtime_0_3_particleC_rep2 = np.array([])
relaxtime_0_3_particleC_rep2[:] = [x/(relaxtime_0_3_rC**2) for x in relaxtime_0_3_particleC_rep2]

a = [relaxtime_0_3_particleA, relaxtime_0_3_particleA_rep1, relaxtime_0_3_particleA_rep2]
b = [relaxtime_0_3_particleB, relaxtime_0_3_particleB_rep1, relaxtime_0_3_particleB_rep2]
c = [relaxtime_0_3_particleC, relaxtime_0_3_particleC_rep1, relaxtime_0_3_particleC_rep2]

relaxtime_0_3_particleA_avg = np.mean(a, axis=0)
relaxtime_0_3_particleB_avg = np.mean(b, axis=0)
relaxtime_0_3_particleC_avg = np.mean(c, axis=0)



#%%

phi = [0.55, 0.57, 0.58]

relaxtime_0_4_radii = [1.0, 1.2, 0.4]

relaxtime_0_4_rA = 1.0
relaxtime_0_4_rB = 1.2
relaxtime_0_4_rC = 0.4

relaxtime_0_4_particleA = np.array([])
relaxtime_0_4_particleA[:] = [x/(relaxtime_0_4_rA**2) for x in relaxtime_0_4_particleA]

relaxtime_0_4_particleB = np.array([])
relaxtime_0_4_particleB[:] = [x/(relaxtime_0_4_rB**2) for x in relaxtime_0_4_particleB]

relaxtime_0_4_particleC = np.array([])
relaxtime_0_4_particleC[:] = [x/(relaxtime_0_4_rC**2) for x in relaxtime_0_4_particleC]

relaxtime_0_4_particleA_rep1 = np.array([])
relaxtime_0_4_particleA_rep1[:] = np.array([x/(relaxtime_0_4_rA**2) for x in relaxtime_0_4_particleA_rep1])

relaxtime_0_4_particleB_rep1 = np.array([])
relaxtime_0_4_particleB_rep1[:] = [x/(relaxtime_0_4_rB**2) for x in relaxtime_0_4_particleB_rep1]

relaxtime_0_4_particleC_rep1 = np.array([])
relaxtime_0_4_particleC_rep1[:] = [x/(relaxtime_0_4_rC**2) for x in relaxtime_0_4_particleC_rep1]

relaxtime_0_4_particleA_rep2 = np.array([])
relaxtime_0_4_particleA_rep2[:] = [x/(relaxtime_0_4_rA**2) for x in relaxtime_0_4_particleA_rep2]

relaxtime_0_4_particleB_rep2 = np.array([])
relaxtime_0_4_particleB_rep2[:] = [x/(relaxtime_0_4_rB**2) for x in relaxtime_0_4_particleB_rep2]

relaxtime_0_4_particleC_rep2 = np.array([])
relaxtime_0_4_particleC_rep2[:] = [x/(relaxtime_0_4_rC**2) for x in relaxtime_0_4_particleC_rep2]

a = [relaxtime_0_4_particleA, relaxtime_0_4_particleA_rep1, relaxtime_0_4_particleA_rep2]
b = [relaxtime_0_4_particleB, relaxtime_0_4_particleB_rep1, relaxtime_0_4_particleB_rep2]
c = [relaxtime_0_4_particleC, relaxtime_0_4_particleC_rep1, relaxtime_0_4_particleC_rep2]

relaxtime_0_4_particleA_avg = np.mean(a, axis=0)
relaxtime_0_4_particleB_avg = np.mean(b, axis=0)
relaxtime_0_4_particleC_avg = np.mean(c, axis=0)



#%%
phi = [0.55, 0.57, 0.58]

relaxtime_0_45_rA = 1.0
relaxtime_0_45_rB = 1.2
relaxtime_0_45_rC = 0.45


relaxtime_0_45_particleA = np.array([])
relaxtime_0_45_particleA[:] = [x/(relaxtime_0_45_rA**2) for x in relaxtime_0_45_particleA]

relaxtime_0_45_particleB= np.array([])
relaxtime_0_45_particleB[:] = [x/(relaxtime_0_45_rB**2) for x in relaxtime_0_45_particleB]

relaxtime_0_45_particleC = np.array([])
relaxtime_0_45_particleC[:] = [x/(relaxtime_0_45_rC**2) for x in relaxtime_0_45_particleC]


relaxtime_0_45_particleA_rep1 = np.array([])
relaxtime_0_45_particleA_rep1[:] = [x/(relaxtime_0_45_rA**2) for x in relaxtime_0_45_particleA_rep1]

relaxtime_0_45_particleB_rep1 = np.array([])
relaxtime_0_45_particleB_rep1[:] = [x/(relaxtime_0_45_rB**2) for x in relaxtime_0_45_particleB_rep1]

relaxtime_0_45_particleC_rep1 = np.array([])
relaxtime_0_45_particleC_rep1[:] = [x/(relaxtime_0_45_rC**2) for x in relaxtime_0_45_particleC_rep1]


relaxtime_0_45_particleA_rep2 = np.array([])
relaxtime_0_45_particleA_rep2[:] = [x/(relaxtime_0_45_rA**2) for x in relaxtime_0_45_particleA_rep2]

relaxtime_0_45_particleB_rep2 = np.array([])
relaxtime_0_45_particleB_rep2[:] = [x/(relaxtime_0_45_rB**2) for x in relaxtime_0_45_particleB_rep2]

relaxtime_0_45_particleC_rep2 = np.array([])
relaxtime_0_45_particleC_rep2[:] = [x/(relaxtime_0_45_rC**2) for x in relaxtime_0_45_particleC_rep2]


a = [relaxtime_0_45_particleA, relaxtime_0_45_particleA_rep1, relaxtime_0_45_particleA_rep2]
b = [relaxtime_0_45_particleB, relaxtime_0_45_particleB_rep1, relaxtime_0_45_particleB_rep2]
c = [relaxtime_0_45_particleC, relaxtime_0_45_particleC_rep1, relaxtime_0_45_particleC_rep2]

relaxtime_0_45_particleA_avg = np.mean(a, axis=0)
relaxtime_0_45_particleB_avg = np.mean(b, axis=0)
relaxtime_0_45_particleC_avg = np.mean(c, axis=0)




#%%

phi = [0.55, 0.57, 0.58]

relaxtime_0_5_radii = [1.0, 1.2, 0.5]

relaxtime_0_5_rA = 1.0
relaxtime_0_5_rB = 1.2
relaxtime_0_5_rC = 0.5

relaxtime_0_5_particleA = np.array([238.76463296689803, 691.12929245321789, 1293.4718003790279])
relaxtime_0_5_particleA[:] = [x/(relaxtime_0_5_rA**2) for x in relaxtime_0_5_particleA]

relaxtime_0_5_particleB = np.array([592.52426046921664, 1830.6962529753712, 4283.9602437262920])
relaxtime_0_5_particleB[:] = [x/(relaxtime_0_5_rB**2) for x in relaxtime_0_5_particleB]

relaxtime_0_5_particleC = np.array([3.3711211991998020, 4.3942933967283073, 5.2363746814701013])
relaxtime_0_5_particleC[:] = [x/(relaxtime_0_5_rC**2) for x in relaxtime_0_5_particleC]

relaxtime_0_5_particleA_rep1 = np.array([235.37624803986986, 629.70745444011163, 1287.9159207958446])
relaxtime_0_5_particleA_rep1[:] = np.array([x/(relaxtime_0_5_rA**2) for x in relaxtime_0_5_particleA_rep1])

relaxtime_0_5_particleB_rep1 = np.array([582.12560409767320, 1621.7978563598758, 4154.7276358890686])
relaxtime_0_5_particleB_rep1[:] = [x/(relaxtime_0_5_rB**2) for x in relaxtime_0_5_particleB_rep1]

relaxtime_0_5_particleC_rep1 = np.array([3.3830993593989236, 4.4268972218725597, 5.1850128762139862])
relaxtime_0_5_particleC_rep1[:] = [x/(relaxtime_0_5_rC**2) for x in relaxtime_0_5_particleC_rep1]

relaxtime_0_5_particleA_rep2 = np.array([233.39210038546528, 683.92343461268320, 1265.0953571526538])
relaxtime_0_5_particleA_rep2[:] = [x/(relaxtime_0_5_rA**2) for x in relaxtime_0_5_particleA_rep2]

relaxtime_0_5_particleB_rep2 = np.array([584.71504270962328, 1812.4288976752546, 3718.8097297105892])
relaxtime_0_5_particleB_rep2[:] = [x/(relaxtime_0_5_rB**2) for x in relaxtime_0_5_particleB_rep2]

relaxtime_0_5_particleC_rep2 = np.array([3.3786908522624590, 4.3969599696202932, 5.2882838936698011])
relaxtime_0_5_particleC_rep2[:] = [x/(relaxtime_0_5_rC**2) for x in relaxtime_0_5_particleC_rep2]

a = [relaxtime_0_5_particleA, relaxtime_0_5_particleA_rep1, relaxtime_0_5_particleA_rep2]
b = [relaxtime_0_5_particleB, relaxtime_0_5_particleB_rep1, relaxtime_0_5_particleB_rep2]
c = [relaxtime_0_5_particleC, relaxtime_0_5_particleC_rep1, relaxtime_0_5_particleC_rep2]

relaxtime_0_5_particleA_avg = np.mean(a, axis=0)
relaxtime_0_5_particleB_avg = np.mean(b, axis=0)
relaxtime_0_5_particleC_avg = np.mean(c, axis=0)


#%%
phi = [0.55, 0.57, 0.58]

relaxtime_0_55_rA = 1.0
relaxtime_0_55_rB = 1.2
relaxtime_0_55_rC = 0.55


relaxtime_0_55_particleA = np.array([235.26854870738876, 629.48082283235999, 1461.5920533636865])
relaxtime_0_55_particleA[:] = [x/(relaxtime_0_55_rA**2) for x in relaxtime_0_55_particleA]

relaxtime_0_55_particleB= np.array([583.24330612764857, 1596.4688628215058, 4050.6752244923291])
relaxtime_0_55_particleB[:] = [x/(relaxtime_0_55_rB**2) for x in relaxtime_0_55_particleB]

relaxtime_0_55_particleC = np.array([5.5200282211650489, 8.1484551783745456, 10.472545859285249])
relaxtime_0_55_particleC[:] = [x/(relaxtime_0_55_rC**2) for x in relaxtime_0_55_particleC]


relaxtime_0_55_particleA_rep1 = np.array([248.57618434382405, 666.06765726628350, 1496.4561664419816])
relaxtime_0_55_particleA_rep1[:] = [x/(relaxtime_0_55_rA**2) for x in relaxtime_0_55_particleA_rep1]

relaxtime_0_55_particleB_rep1 = np.array([584.72627223829636, 1701.7686108044486, 4545.7348615474002])
relaxtime_0_55_particleB_rep1[:] = [x/(relaxtime_0_55_rB**2) for x in relaxtime_0_55_particleB_rep1]

relaxtime_0_55_particleC_rep1 = np.array([5.4972640731690330, 8.0759817339685949, 10.514543871136404])
relaxtime_0_55_particleC_rep1[:] = [x/(relaxtime_0_55_rC**2) for x in relaxtime_0_55_particleC_rep1]


relaxtime_0_55_particleA_rep2 = np.array([236.76697082459600, 672.49972161219773, 1338.9023001455912])
relaxtime_0_55_particleA_rep2[:] = [x/(relaxtime_0_55_rA**2) for x in relaxtime_0_55_particleA_rep2]

relaxtime_0_55_particleB_rep2 = np.array([573.15959599182486, 1873.0978225484021, 4169.0977417929071])
relaxtime_0_55_particleB_rep2[:] = [x/(relaxtime_0_55_rB**2) for x in relaxtime_0_55_particleB_rep2]

relaxtime_0_55_particleC_rep2 = np.array([5.5007867370198511, 8.1396626205797222, 10.800643979112479])
relaxtime_0_55_particleC_rep2[:] = [x/(relaxtime_0_55_rC**2) for x in relaxtime_0_55_particleC_rep2]


a = [relaxtime_0_55_particleA, relaxtime_0_55_particleA_rep1, relaxtime_0_55_particleA_rep2]
b = [relaxtime_0_55_particleB, relaxtime_0_55_particleB_rep1, relaxtime_0_55_particleB_rep2]
c = [relaxtime_0_55_particleC, relaxtime_0_55_particleC_rep1, relaxtime_0_55_particleC_rep2]

relaxtime_0_55_particleA_avg = np.mean(a, axis=0)
relaxtime_0_55_particleB_avg = np.mean(b, axis=0)
relaxtime_0_55_particleC_avg = np.mean(c, axis=0)




#%%

phi = [0.55, 0.57, 0.58]

relaxtime_0_6_radii = [1.0, 1.2, 0.6]

relaxtime_0_6_rA = 1.0
relaxtime_0_6_rB = 1.2
relaxtime_0_6_rC = 0.6

relaxtime_0_6_particleA = np.array([244.79950147656024, 751.02861518614691, 1726.9493597975147])
relaxtime_0_6_particleA[:] = [x/(relaxtime_0_6_rA**2) for x in relaxtime_0_6_particleA]

relaxtime_0_6_particleB = np.array([607.44293057059633, 2048.7972518748984, 4747.7803980002500])
relaxtime_0_6_particleB[:] = [x/(relaxtime_0_6_rB**2) for x in relaxtime_0_6_particleB]

relaxtime_0_6_particleC = np.array([9.3288611643683641, 15.705260550638556, 22.772778998232980])
relaxtime_0_6_particleC[:] = [x/(relaxtime_0_6_rC**2) for x in relaxtime_0_6_particleC]

relaxtime_0_6_particleA_rep1 = np.array([242.84020232179299, 713.19535564892965, 1523.6179400762603])
relaxtime_0_6_particleA_rep1[:] = [x/(relaxtime_0_6_rA**2) for x in relaxtime_0_6_particleA_rep1]

relaxtime_0_6_particleB_rep1 = np.array([610.50910775234490, 1959.9546884861045, 4330.5078082947994])
relaxtime_0_6_particleB_rep1[:] = [x/(relaxtime_0_6_rB**2) for x in relaxtime_0_6_particleB_rep1]

relaxtime_0_6_particleC_rep1 = np.array([9.2803475386250636, 16.187395497145204, 23.550362019598349])
relaxtime_0_6_particleC_rep1[:] = [x/(relaxtime_0_6_rC**2) for x in relaxtime_0_6_particleC_rep1]

relaxtime_0_6_particleA_rep2 = np.array([248.63984936718123, 740.83142760150076, 1537.7253701350241])
relaxtime_0_6_particleA_rep2[:] = [x/(relaxtime_0_6_rA**2) for x in relaxtime_0_6_particleA_rep2]

relaxtime_0_6_particleB_rep2 = np.array([613.08873176355598, 1938.2171132603846, 4185.9788537572931])
relaxtime_0_6_particleB_rep2[:] = [x/(relaxtime_0_6_rB**2) for x in relaxtime_0_6_particleB_rep2]

relaxtime_0_6_particleC_rep2 = np.array([9.3506423202350302, 15.606963629683602, 22.907307198556492])
relaxtime_0_6_particleC_rep2[:] = [x/(relaxtime_0_6_rC**2) for x in relaxtime_0_6_particleC_rep2]

a = [relaxtime_0_6_particleA, relaxtime_0_6_particleA_rep1, relaxtime_0_6_particleA_rep2]
b = [relaxtime_0_6_particleB, relaxtime_0_6_particleB_rep1, relaxtime_0_6_particleB_rep2]
c = [relaxtime_0_6_particleC, relaxtime_0_6_particleC_rep1, relaxtime_0_6_particleC_rep2]

relaxtime_0_6_particleA_avg = np.mean(a, axis=0)
relaxtime_0_6_particleB_avg = np.mean(b, axis=0)
relaxtime_0_6_particleC_avg = np.mean(c, axis=0)



#%%
phi = [0.55, 0.57, 0.58]

relaxtime_0_65_rA = 1.0
relaxtime_0_65_rB = 1.2
relaxtime_0_65_rC = 0.65


relaxtime_0_65_particleA = np.array([256.43070990993732, 813.26171693402534, 1730.4254577917563])
relaxtime_0_65_particleA[:] = [x/(relaxtime_0_65_rA**2) for x in relaxtime_0_65_particleA]

relaxtime_0_65_particleB= np.array([657.60402273924069, 2707.6854338017465, 5922.3393914199169])
relaxtime_0_65_particleB[:] = [x/(relaxtime_0_65_rB**2) for x in relaxtime_0_65_particleB]

relaxtime_0_65_particleC = np.array([16.153194634635167, 32.350586411829099, 53.561199651640642])
relaxtime_0_65_particleC[:] = [x/(relaxtime_0_65_rC**2) for x in relaxtime_0_65_particleC]


relaxtime_0_65_particleA_rep1 = np.array([255.73277947332690, 834.09927209665739, 1872.3516270533780])
relaxtime_0_65_particleA_rep1[:] = [x/(relaxtime_0_65_rA**2) for x in relaxtime_0_65_particleA_rep1]

relaxtime_0_65_particleB_rep1 = np.array([642.90538621013991, 2366.0981085605877, 4857.9645150433007])
relaxtime_0_65_particleB_rep1[:] = [x/(relaxtime_0_65_rB**2) for x in relaxtime_0_65_particleB_rep1]

relaxtime_0_65_particleC_rep1 = np.array([16.034285951749617, 33.041861170980766, 56.689674470372211])
relaxtime_0_65_particleC_rep1[:] = [x/(relaxtime_0_65_rC**2) for x in relaxtime_0_65_particleC_rep1]


relaxtime_0_65_particleA_rep2 = np.array([260.55012382899611, 815.07516387593898, 1971.1275010624624])
relaxtime_0_65_particleA_rep2[:] = [x/(relaxtime_0_65_rA**2) for x in relaxtime_0_65_particleA_rep2]

relaxtime_0_65_particleB_rep2 = np.array([631.69617830957486, 2262.0869003362768, 7273.2053882144428])
relaxtime_0_65_particleB_rep2[:] = [x/(relaxtime_0_65_rB**2) for x in relaxtime_0_65_particleB_rep2]

relaxtime_0_65_particleC_rep2 = np.array([15.972668784985771, 31.441777318638064, 53.318147199518805])
relaxtime_0_65_particleC_rep2[:] = [x/(relaxtime_0_65_rC**2) for x in relaxtime_0_65_particleC_rep2]


a = [relaxtime_0_65_particleA, relaxtime_0_65_particleA_rep1, relaxtime_0_65_particleA_rep2]
b = [relaxtime_0_65_particleB, relaxtime_0_65_particleB_rep1, relaxtime_0_65_particleB_rep2]
c = [relaxtime_0_65_particleC, relaxtime_0_65_particleC_rep1, relaxtime_0_65_particleC_rep2]

relaxtime_0_65_particleA_avg = np.mean(a, axis=0)
relaxtime_0_65_particleB_avg = np.mean(b, axis=0)
relaxtime_0_65_particleC_avg = np.mean(c, axis=0)




#%%
phi = [0.55, 0.57, 0.58]


relaxtime_0_7_rA = 1.0
relaxtime_0_7_rB = 1.2
relaxtime_0_7_rC = 0.7


relaxtime_0_7_particleA = np.array([260.93057451084138, 845.81602649265471, 1979.6361568717939])
relaxtime_0_7_particleA[:] = [x/(relaxtime_0_7_rA**2) for x in relaxtime_0_7_particleA]

relaxtime_0_7_particleB = np.array([641.90012733105425, 2460.3099966471332, 6943.0262417277545])
relaxtime_0_7_particleB[:] = [x/(relaxtime_0_7_rB**2) for x in relaxtime_0_7_particleB]

relaxtime_0_7_particleC = np.array([27.343924236091489, 65.273394877437823, 120.91524427681711])
relaxtime_0_7_particleC[:] = [x/(relaxtime_0_7_rC**2) for x in relaxtime_0_7_particleC]

relaxtime_0_7_particleA_rep1 = np.array([254.12869397414923, 901.53245083861520, 2208.8801279085005])
relaxtime_0_7_particleA_rep1[:] = [x/(relaxtime_0_7_rA**2) for x in relaxtime_0_7_particleA_rep1]

relaxtime_0_7_particleB_rep1 = np.array([676.13103316695378, 2715.9587664847936, 9744.9318005496534])
relaxtime_0_7_particleB_rep1[:] = [x/(relaxtime_0_7_rB**2) for x in relaxtime_0_7_particleB_rep1]

relaxtime_0_7_particleC_rep1 = np.array([27.519737298023738, 61.064991621900241, 118.90901231461734])
relaxtime_0_7_particleC_rep1[:] = [x/(relaxtime_0_7_rC**2) for x in relaxtime_0_7_particleC_rep1]

relaxtime_0_7_particleA_rep2 = np.array([274.31926895259051, 915.89084903985167, 2041.1366110414153])
relaxtime_0_7_particleA_rep2[:] = [x/(relaxtime_0_7_rA**2) for x in relaxtime_0_7_particleA_rep2]

relaxtime_0_7_particleB_rep2 = np.array([708.54603582051175, 2667.4780701698674, 6741.2944025683937])
relaxtime_0_7_particleB_rep2[:] = [x/(relaxtime_0_7_rB**2) for x in relaxtime_0_7_particleB_rep2]

relaxtime_0_7_particleC_rep2 = np.array([27.631894859628424, 64.393081660952021, 125.54310047405404])
relaxtime_0_7_particleC_rep2[:] = [x/(relaxtime_0_7_rC**2) for x in relaxtime_0_7_particleC_rep2]


a = [relaxtime_0_7_particleA, relaxtime_0_7_particleA_rep1, relaxtime_0_7_particleA_rep2]
b = [relaxtime_0_7_particleB, relaxtime_0_7_particleB_rep1, relaxtime_0_7_particleB_rep2]
c = [relaxtime_0_7_particleC, relaxtime_0_7_particleC_rep1, relaxtime_0_7_particleC_rep2]

relaxtime_0_7_particleA_avg = np.mean(a, axis=0)
relaxtime_0_7_particleB_avg = np.mean(b, axis=0)
relaxtime_0_7_particleC_avg = np.mean(c, axis=0)


#%%
phi = [0.55, 0.57, 0.58]

relaxtime_0_75_rA = 1.0
relaxtime_0_75_rB = 1.2
relaxtime_0_75_rC = 0.75


relaxtime_0_75_particleA = np.array([295.29559982395051, 1023.5586837900289, 2335.6451717614627])
relaxtime_0_75_particleA[:] = [x/(relaxtime_0_75_rA**2) for x in relaxtime_0_75_particleA]

relaxtime_0_75_particleB= np.array([757.30316048162342, 3301.8598877607465, 8941.8110556945230])
relaxtime_0_75_particleB[:] = [x/(relaxtime_0_75_rB**2) for x in relaxtime_0_75_particleB]

relaxtime_0_75_particleC = np.array([46.432358210347857, 124.03506930128506, 260.27294179870302])
relaxtime_0_75_particleC[:] = [x/(relaxtime_0_75_rC**2) for x in relaxtime_0_75_particleC]


relaxtime_0_75_particleA_rep1 = np.array([274.10808236863426, 1099.7782758085698, 2222.6690773119553])
relaxtime_0_75_particleA_rep1[:] = [x/(relaxtime_0_75_rA**2) for x in relaxtime_0_75_particleA_rep1]

relaxtime_0_75_particleB_rep1 = np.array([688.19643501838800, 2804.4438766253720, 6992.6349254396137])
relaxtime_0_75_particleB_rep1[:] = [x/(relaxtime_0_75_rB**2) for x in relaxtime_0_75_particleB_rep1]

relaxtime_0_75_particleC_rep1 = np.array([46.474944900512476, 129.28167782218136, 251.90857545669874])
relaxtime_0_75_particleC_rep1[:] = [x/(relaxtime_0_75_rC**2) for x in relaxtime_0_75_particleC_rep1]


relaxtime_0_75_particleA_rep2 = np.array([284.47794484102491, 1092.4407981445825, 2407.1723049964185])
relaxtime_0_75_particleA_rep2[:] = [x/(relaxtime_0_75_rA**2) for x in relaxtime_0_75_particleA_rep2]

relaxtime_0_75_particleB_rep2 = np.array([738.43683842947269, 2974.5061789494621, 9057.0149867758901])
relaxtime_0_75_particleB_rep2[:] = [x/(relaxtime_0_75_rB**2) for x in relaxtime_0_75_particleB_rep2]

relaxtime_0_75_particleC_rep2 = np.array([46.137898635711736, 123.81763588192294, 257.28626315225256])
relaxtime_0_75_particleC_rep2[:] = [x/(relaxtime_0_75_rC**2) for x in relaxtime_0_75_particleC_rep2]


a = [relaxtime_0_75_particleA, relaxtime_0_75_particleA_rep1, relaxtime_0_75_particleA_rep2]
b = [relaxtime_0_75_particleB, relaxtime_0_75_particleB_rep1, relaxtime_0_75_particleB_rep2]
c = [relaxtime_0_75_particleC, relaxtime_0_75_particleC_rep1, relaxtime_0_75_particleC_rep2]

relaxtime_0_75_particleA_avg = np.mean(a, axis=0)
relaxtime_0_75_particleB_avg = np.mean(b, axis=0)
relaxtime_0_75_particleC_avg = np.mean(c, axis=0)



#%%
phi = [0.55, 0.57, 0.58]

relaxtime_0_8_radii = [1.0, 1.2, 0.8]

relaxtime_0_8_rA = 1.0
relaxtime_0_8_rB = 1.2
relaxtime_0_8_rC = 0.8

relaxtime_0_8_particleA = np.array([299.57951486659925, 1167.7885078538568, 2840.0024221202157])
relaxtime_0_8_particleA[:] = [x/(relaxtime_0_8_rA**2) for x in relaxtime_0_8_particleA]

relaxtime_0_8_particleB = np.array([760.38707506028288, 3280.1971167017914, 9434.9904086448732])
relaxtime_0_8_particleB[:] = [x/(relaxtime_0_8_rB**2) for x in relaxtime_0_8_particleB]

relaxtime_0_8_particleC = np.array([73.995466631100456, 233.99642060887865, 485.99688486127371])
relaxtime_0_8_particleC[:] = [x/(relaxtime_0_8_rC**2) for x in relaxtime_0_8_particleC]

relaxtime_0_8_particleA_rep1 = np.array([302.11161063871458, 1355.6642940277056, 2404.6199720006539])
relaxtime_0_8_particleA_rep1[:] = [x/(relaxtime_0_8_rA**2) for x in relaxtime_0_8_particleA_rep1]

relaxtime_0_8_particleB_rep1 = np.array([750.79799049368671, 3784.4366229019406, 6836.8081438524659])
relaxtime_0_8_particleB_rep1[:] = [x/(relaxtime_0_8_rB**2) for x in relaxtime_0_8_particleB_rep1]

relaxtime_0_8_particleC_rep1 = np.array([73.903200829446334, 244.62209843796543, 481.60623380011026])
relaxtime_0_8_particleC_rep1[:] = [x/(relaxtime_0_8_rC**2) for x in relaxtime_0_8_particleC_rep1]

relaxtime_0_8_particleA_rep2 = np.array([309.72465976514962, 1154.3914293864702, 2644.3261168265431])
relaxtime_0_8_particleA_rep2[:] = [x/(relaxtime_0_8_rA**2) for x in relaxtime_0_8_particleA_rep2]

relaxtime_0_8_particleB_rep2 = np.array([811.42825085200525, 3808.7758800610641, 7696.4012736915156])
relaxtime_0_8_particleB_rep2[:] = [x/(relaxtime_0_8_rB**2) for x in relaxtime_0_8_particleB_rep2]

relaxtime_0_8_particleC_rep2 = np.array([74.703952887318039, 238.91293122110790, 545.05189869867161])
relaxtime_0_8_particleC_rep2[:] = [x/(relaxtime_0_8_rC**2) for x in relaxtime_0_8_particleC_rep2]


a = [relaxtime_0_8_particleA, relaxtime_0_8_particleA_rep1, relaxtime_0_8_particleA_rep2]
b = [relaxtime_0_8_particleB, relaxtime_0_8_particleB_rep1, relaxtime_0_8_particleB_rep2]
c = [relaxtime_0_8_particleC, relaxtime_0_8_particleC_rep1, relaxtime_0_8_particleC_rep2]

relaxtime_0_8_particleA_avg = np.mean(a, axis=0)
relaxtime_0_8_particleB_avg = np.mean(b, axis=0)
relaxtime_0_8_particleC_avg = np.mean(c, axis=0)


#%%
phi = [0.55, 0.57, 0.58]

relaxtime_0_85_rA = 1.0
relaxtime_0_85_rB = 1.2
relaxtime_0_85_rC = 0.85


relaxtime_0_85_particleA = np.array([320.37716224923565, 1218.6394420368406, 2630.1860277700530])
relaxtime_0_85_particleA[:] = [x/(relaxtime_0_85_rA**2) for x in relaxtime_0_85_particleA]

relaxtime_0_85_particleB= np.array([856.08890902170015, 3538.1702377831866, 8803.5200375186414])
relaxtime_0_85_particleB[:] = [x/(relaxtime_0_85_rB**2) for x in relaxtime_0_85_particleB]

relaxtime_0_85_particleC = np.array([117.76410874047215, 405.52617037386830, 882.16826454255954])
relaxtime_0_85_particleC[:] = [x/(relaxtime_0_85_rC**2) for x in relaxtime_0_85_particleC]


relaxtime_0_85_particleA_rep1 = np.array([319.60182993937786, 1181.4771459255792, 2791.9110068432515])
relaxtime_0_85_particleA_rep1[:] = [x/(relaxtime_0_85_rA**2) for x in relaxtime_0_85_particleA_rep1]

relaxtime_0_85_particleB_rep1 = np.array([820.00511545077836, 3609.6024366009588, 10479.104096893847])
relaxtime_0_85_particleB_rep1[:] = [x/(relaxtime_0_85_rB**2) for x in relaxtime_0_85_particleB_rep1]

relaxtime_0_85_particleC_rep1 = np.array([116.37485014942744, 393.48030918327345, 1003.2424772434962])
relaxtime_0_85_particleC_rep1[:] = [x/(relaxtime_0_85_rC**2) for x in relaxtime_0_85_particleC_rep1]


relaxtime_0_85_particleA_rep2 = np.array([319.19465857079513, 1219.6703206642196, 3657.6309852586305])
relaxtime_0_85_particleA_rep2[:] = [x/(relaxtime_0_85_rA**2) for x in relaxtime_0_85_particleA_rep2]

relaxtime_0_85_particleB_rep2 = np.array([857.80383844650009, 3568.1286993186600, 9730.7585513394806])
relaxtime_0_85_particleB_rep2[:] = [x/(relaxtime_0_85_rB**2) for x in relaxtime_0_85_particleB_rep2]

relaxtime_0_85_particleC_rep2 = np.array([119.82663359851792, 403.78960023726779, 1037.4394766134772])
relaxtime_0_85_particleC_rep2[:] = [x/(relaxtime_0_85_rC**2) for x in relaxtime_0_85_particleC_rep2]


a = [relaxtime_0_85_particleA, relaxtime_0_85_particleA_rep1, relaxtime_0_85_particleA_rep2]
b = [relaxtime_0_85_particleB, relaxtime_0_85_particleB_rep1, relaxtime_0_85_particleB_rep2]
c = [relaxtime_0_85_particleC, relaxtime_0_85_particleC_rep1, relaxtime_0_85_particleC_rep2]

relaxtime_0_85_particleA_avg = np.mean(a, axis=0)
relaxtime_0_85_particleB_avg = np.mean(b, axis=0)
relaxtime_0_85_particleC_avg = np.mean(c, axis=0)




#%%
phi = [0.55, 0.57, 0.58]

relaxtime_0_9_rA = 1.0
relaxtime_0_9_rB = 1.2
relaxtime_0_9_rC = 0.9


relaxtime_0_9_particleA = np.array([331.09121550451300, 1492.4136539813330, 3151.2624733966077])
relaxtime_0_9_particleA[:] = [x/(relaxtime_0_9_rA**2) for x in relaxtime_0_9_particleA]

relaxtime_0_9_particleB = np.array([844.60743596757482, 4636.4769383067760, 10014.626632506768])
relaxtime_0_9_particleB[:] = [x/(relaxtime_0_9_rB**2) for x in relaxtime_0_9_particleB]

relaxtime_0_9_particleC = np.array([181.79968842497323, 738.03079859467516, 1698.5888312774889])
relaxtime_0_9_particleC[:] = [x/(relaxtime_0_9_rC**2) for x in relaxtime_0_9_particleC]


relaxtime_0_9_particleA_rep1 = np.array([341.56308064145935, 1351.5062264586018, 3043.5357141948143])
relaxtime_0_9_particleA_rep1[:] = [x/(relaxtime_0_9_rA**2) for x in relaxtime_0_9_particleA_rep1]

relaxtime_0_9_particleB_rep1 = np.array([915.33586333966832, 3998.4330584512991, 8605.3231472136576])
relaxtime_0_9_particleB_rep1[:] = [x/(relaxtime_0_9_rB**2) for x in relaxtime_0_9_particleB_rep1]

relaxtime_0_9_particleC_rep1 = np.array([178.93538790736500, 654.79551540430975, 1404.5566567984617])
relaxtime_0_9_particleC_rep1[:] = [x/(relaxtime_0_9_rC**2) for x in relaxtime_0_9_particleC_rep1]


relaxtime_0_9_particleA_rep2 = np.array([329.54346762106343, 1661.8781056753703, 3133.8637916594457])
relaxtime_0_9_particleA_rep2[:] = [x/(relaxtime_0_9_rA**2) for x in relaxtime_0_9_particleA_rep2]

relaxtime_0_9_particleB_rep2 = np.array([852.10653789192395, 6563.5962052906170, 9631.7877994379087])
relaxtime_0_9_particleB_rep2[:] = [x/(relaxtime_0_9_rB**2) for x in relaxtime_0_9_particleB_rep2]

relaxtime_0_9_particleC_rep2 = np.array([176.30581540855965, 804.84047533926787, 1657.0522796559544])
relaxtime_0_9_particleC_rep2[:] = [x/(relaxtime_0_9_rC**2) for x in relaxtime_0_9_particleC_rep2]


a = [relaxtime_0_9_particleA, relaxtime_0_9_particleA_rep1, relaxtime_0_9_particleA_rep2]
b = [relaxtime_0_9_particleB, relaxtime_0_9_particleB_rep1, relaxtime_0_9_particleB_rep2]
c = [relaxtime_0_9_particleC, relaxtime_0_9_particleC_rep1, relaxtime_0_9_particleC_rep2]

relaxtime_0_9_particleA_avg = np.mean(a, axis=0)
relaxtime_0_9_particleB_avg = np.mean(b, axis=0)
relaxtime_0_9_particleC_avg = np.mean(c, axis=0)




#%%
phi = [0.55, 0.57, 0.58]

relaxtime_0_95_rA = 1.0
relaxtime_0_95_rB = 1.2
relaxtime_0_95_rC = 0.95


relaxtime_0_95_particleA = np.array([335.88378882545004, 2123.2644438457382, 3917.1716966179156])
relaxtime_0_95_particleA[:] = [x/(relaxtime_0_95_rA**2) for x in relaxtime_0_95_particleA]

relaxtime_0_95_particleB= np.array([832.57162751393594, 7690.6114947856813 ,36576.288718686221])
relaxtime_0_95_particleB[:] = [x/(relaxtime_0_95_rB**2) for x in relaxtime_0_95_particleB]

relaxtime_0_95_particleC = np.array([247.44897492198982, 1540.8160260507977 ,2357.6998404230458])
relaxtime_0_95_particleC[:] = [x/(relaxtime_0_95_rC**2) for x in relaxtime_0_95_particleC]


relaxtime_0_95_particleA_rep1 = np.array([331.87645428830405, 1808.2828254553747, 7016.4569191261253])
relaxtime_0_95_particleA_rep1[:] = [x/(relaxtime_0_95_rA**2) for x in relaxtime_0_95_particleA_rep1]

relaxtime_0_95_particleB_rep1 = np.array([896.71370618741992, 6520.3527119886148, 92186.890298939950])
relaxtime_0_95_particleB_rep1[:] = [x/(relaxtime_0_95_rB**2) for x in relaxtime_0_95_particleB_rep1]

relaxtime_0_95_particleC_rep1 = np.array([232.59204358780846, 1298.9995785989718, 3740.5594962582195])
relaxtime_0_95_particleC_rep1[:] = [x/(relaxtime_0_95_rC**2) for x in relaxtime_0_95_particleC_rep1]


relaxtime_0_95_particleA_rep2 = np.array([357.54438040777939, 1720.2063369847335, 4564.0488571788546])
relaxtime_0_95_particleA_rep2[:] = [x/(relaxtime_0_95_rA**2) for x in relaxtime_0_95_particleA_rep2]

relaxtime_0_95_particleB_rep2 = np.array([931.14927967910899, 4850.5274577227046, 12265.369526221544])
relaxtime_0_95_particleB_rep2[:] = [x/(relaxtime_0_95_rB**2) for x in relaxtime_0_95_particleB_rep2]

relaxtime_0_95_particleC_rep2 = np.array([265.04767222712206, 1217.0729106857891, 2995.5508877991242])
relaxtime_0_95_particleC_rep2[:] = [x/(relaxtime_0_95_rC**2) for x in relaxtime_0_95_particleC_rep2]


a = [relaxtime_0_95_particleA, relaxtime_0_95_particleA_rep1, relaxtime_0_95_particleA_rep2]
b = [relaxtime_0_95_particleB, relaxtime_0_95_particleB_rep1, relaxtime_0_95_particleB_rep2]
c = [relaxtime_0_95_particleC, relaxtime_0_95_particleC_rep1, relaxtime_0_95_particleC_rep2]

relaxtime_0_95_particleA_avg = np.mean(a, axis=0)
relaxtime_0_95_particleB_avg = np.mean(b, axis=0)
relaxtime_0_95_particleC_avg = np.mean(c, axis=0)



#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_0_radii = [1.0, 1.2, 1.0]

relaxtime_1_0_rA = 1.0
relaxtime_1_0_rB = 1.2
relaxtime_1_0_rC = 1.0


relaxtime_1_0_particleA = np.array([340.27248300828040, 1577.4784958517271, 3196.2935330680311])
relaxtime_1_0_particleA[:] = [x/(relaxtime_1_0_rA**2) for x in relaxtime_1_0_particleA]

relaxtime_1_0_particleB = np.array([753.73375805095509, 4436.9406736524215, 10166.091022796318])
relaxtime_1_0_particleB[:] = [x/(relaxtime_1_0_rB**2) for x in relaxtime_1_0_particleB]


relaxtime_1_0_particleA_rep1 = np.array([341.40033990733832, 1700.2529207656385, 5277.5601158730578])
relaxtime_1_0_particleA_rep1[:] = [x/(relaxtime_1_0_rA**2) for x in relaxtime_1_0_particleA_rep1]

relaxtime_1_0_particleB_rep1 = np.array([905.61832370411742, 5537.9763091850891, 14229.319196827788])
relaxtime_1_0_particleB_rep1[:] = [x/(relaxtime_1_0_rB**2) for x in relaxtime_1_0_particleB_rep1]


relaxtime_1_0_particleA_rep2 = np.array([331.35701803763487, 2148.7569810909436, 3242.6595774616912])
relaxtime_1_0_particleA_rep2[:] = [x/(relaxtime_1_0_rA**2) for x in relaxtime_1_0_particleA_rep2]

relaxtime_1_0_particleB_rep2 = np.array([826.27645434154408, 7853.8669519950654, 9824.4260662835841])
relaxtime_1_0_particleB_rep2[:] = [x/(relaxtime_1_0_rB**2) for x in relaxtime_1_0_particleB_rep2]

a = [relaxtime_1_0_particleA, relaxtime_1_0_particleA_rep1, relaxtime_1_0_particleA_rep2]
b = [relaxtime_1_0_particleB, relaxtime_1_0_particleB_rep1, relaxtime_1_0_particleB_rep2]

relaxtime_1_0_particleA_avg = np.mean(a, axis=0)
relaxtime_1_0_particleB_avg = np.mean(b, axis=0)


#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_05_radii = [1.0, 1.2, 1.0]

relaxtime_1_05_rA = 1.0
relaxtime_1_05_rB = 1.2
relaxtime_1_05_rC = 1.05


relaxtime_1_05_particleA = np.array([331.22418161922184, 1700.0147448786884, 4563.5076868388951])
relaxtime_1_05_particleA[:] = [x/(relaxtime_1_05_rA**2) for x in relaxtime_1_05_particleA]

relaxtime_1_05_particleB = np.array([595.51650043598761, 3420.0454983146865, 8171.8530647417847])
relaxtime_1_05_particleB[:] = [x/(relaxtime_1_05_rB**2) for x in relaxtime_1_05_particleB]

relaxtime_1_05_particleC = np.array([629.35340802161988, 3224.3091617414552, 8316.4786344521672])
relaxtime_1_05_particleC[:] = [x/(relaxtime_1_05_rC**2) for x in relaxtime_1_05_particleC]

relaxtime_1_05_particleA_rep1 = np.array([322.30093889812559, 1198.3890141568793, 4537.8552027546102])
relaxtime_1_05_particleA_rep1[:] = [x/(relaxtime_1_05_rA**2) for x in relaxtime_1_05_particleA_rep1]

relaxtime_1_05_particleB_rep1 = np.array([610.54772128147317, 2525.5078590134194, 9971.9848148731544])
relaxtime_1_05_particleB_rep1[:] = [x/(relaxtime_1_05_rB**2) for x in relaxtime_1_05_particleB_rep1]

relaxtime_1_05_particleC_rep1 = np.array([624.40282691832226, 2813.7530894260071, 12629.645466241509])
relaxtime_1_05_particleC_rep1[:] = [x/(relaxtime_1_05_rC**2) for x in relaxtime_1_05_particleC_rep1]

relaxtime_1_05_particleA_rep2 = np.array([341.29842223342985, 1888.2049192297000, 2558.7474029998771])
relaxtime_1_05_particleA_rep2[:] = [x/(relaxtime_1_05_rA**2) for x in relaxtime_1_05_particleA_rep2]

relaxtime_1_05_particleB_rep2 = np.array([634.36340313234484, 3911.3212830124867, 5018.9864247066034])
relaxtime_1_05_particleB_rep2[:] = [x/(relaxtime_1_05_rB**2) for x in relaxtime_1_05_particleB_rep2]

relaxtime_1_05_particleC_rep2 = np.array([645.87965858364305, 3985.1849813094382, 5821.1790648147353])
relaxtime_1_05_particleC_rep2[:] = [x/(relaxtime_1_05_rC**2) for x in relaxtime_1_05_particleC_rep2]

a = [relaxtime_1_05_particleA, relaxtime_1_05_particleA_rep1, relaxtime_1_05_particleA_rep2]
b = [relaxtime_1_05_particleB, relaxtime_1_05_particleB_rep1, relaxtime_1_05_particleB_rep2]
c = [relaxtime_1_05_particleC, relaxtime_1_05_particleC_rep1, relaxtime_1_05_particleC_rep2]

relaxtime_1_05_particleA_avg = np.mean(a, axis=0)
relaxtime_1_05_particleB_avg = np.mean(b, axis=0)
relaxtime_1_05_particleC_avg = np.mean(c, axis=0)



#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_1_radii = [1.0, 1.2, 1.1]

relaxtime_1_1_rA = 1.0
relaxtime_1_1_rB = 1.2
relaxtime_1_1_rC = 1.1


relaxtime_1_1_particleA = np.array([309.92182528254119, 1663.2807714560640, 2987.4998245916599])
relaxtime_1_1_particleA[:] = [x/(relaxtime_1_1_rA**2) for x in relaxtime_1_1_particleA]

relaxtime_1_1_particleB = np.array([644.39486072973853, 4449.2898482632954, 7891.1646838743563])
relaxtime_1_1_particleB[:] = [x/(relaxtime_1_1_rB**2) for x in relaxtime_1_1_particleB]

relaxtime_1_1_particleC = np.array([658.56691176101208, 4232.2181121898993, 9118.5725996176116])
relaxtime_1_1_particleC[:] = [x/(relaxtime_1_1_rC**2) for x in relaxtime_1_1_particleC]

relaxtime_1_1_particleA_rep1 = np.array([299.55639624407684, 1542.8179140660147, 3614.2499169323901])
relaxtime_1_1_particleA_rep1[:] = [x/(relaxtime_1_1_rA**2) for x in relaxtime_1_1_particleA_rep1]

relaxtime_1_1_particleB_rep1 = np.array([624.55018940389061, 3258.4965095950242, 7374.1075466247348])
relaxtime_1_1_particleB_rep1[:] = [x/(relaxtime_1_1_rB**2) for x in relaxtime_1_1_particleB_rep1]

relaxtime_1_1_particleC_rep1 = np.array([625.15488358843459, 3972.8546636026035, 7867.2793422272889])
relaxtime_1_1_particleC_rep1[:] = [x/(relaxtime_1_1_rC**2) for x in relaxtime_1_1_particleC_rep1]

relaxtime_1_1_particleA_rep2 = np.array([308.49641451924958, 1215.9925619737589, 3363.6190458375709])
relaxtime_1_1_particleA_rep2[:] = [x/(relaxtime_1_1_rA**2) for x in relaxtime_1_1_particleA_rep2]

relaxtime_1_1_particleB_rep2 = np.array([641.35494145142377, 2744.1050050861008, 6581.4599722924086])
relaxtime_1_1_particleB_rep2[:] = [x/(relaxtime_1_1_rB**2) for x in relaxtime_1_1_particleB_rep2]

relaxtime_1_1_particleC_rep2 = np.array([649.91780922293026, 3082.4843079749421, 8162.6851438958947])
relaxtime_1_1_particleC_rep2[:] = [x/(relaxtime_1_1_rC**2) for x in relaxtime_1_1_particleC_rep2]

a = [relaxtime_1_1_particleA, relaxtime_1_1_particleA_rep1, relaxtime_1_1_particleA_rep2]
b = [relaxtime_1_1_particleB, relaxtime_1_1_particleB_rep1, relaxtime_1_1_particleB_rep2]
c = [relaxtime_1_1_particleC, relaxtime_1_1_particleC_rep1, relaxtime_1_1_particleC_rep2]

relaxtime_1_1_particleA_avg = np.mean(a, axis=0)
relaxtime_1_1_particleB_avg = np.mean(b, axis=0)
relaxtime_1_1_particleC_avg = np.mean(c, axis=0)




#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_125_radii = [1.0, 1.2, 1.125]

relaxtime_1_125_rA = 1.0
relaxtime_1_125_rB = 1.2
relaxtime_1_125_rC = 1.125

relaxtime_1_125_particleA = np.array([299.51864846399241, 1290.0409701488550, 3282.1337886910346])
relaxtime_1_125_particleA[:] = [x/(relaxtime_1_125_rA**2) for x in relaxtime_1_125_particleA]

relaxtime_1_125_particleB = np.array([668.19571471622817, 3583.2405382017755, 6826.8815565933928])
relaxtime_1_125_particleB[:] = [x/(relaxtime_1_125_rB**2) for x in relaxtime_1_125_particleB]

relaxtime_1_125_particleC = np.array([776.95966756703945, 3827.3593852160861, 8111.0182064084966])
relaxtime_1_125_particleC[:] = [x/(relaxtime_1_125_rC**2) for x in relaxtime_1_125_particleC]

relaxtime_1_125_particleA_rep1 = np.array([283.98617873581378, 1419.8129870259770, 2646.7883219734617])
relaxtime_1_125_particleA_rep1[:] = [x/(relaxtime_1_125_rA**2) for x in relaxtime_1_125_particleA_rep1]

relaxtime_1_125_particleB_rep1 = np.array([634.29637275994980, 3889.3408938168245, 6579.8781247449251])
relaxtime_1_125_particleB_rep1[:] = [x/(relaxtime_1_125_rB**2) for x in relaxtime_1_125_particleB_rep1]

relaxtime_1_125_particleC_rep1 = np.array([741.42294882671661, 4802.8576925426887, 6540.3974211704863])
relaxtime_1_125_particleC_rep1[:] = [x/(relaxtime_1_125_rC**2) for x in relaxtime_1_125_particleC_rep1]

relaxtime_1_125_particleA_rep2 = np.array([303.50950772415075, 1618.0050319494844, 3258.7936344544364])
relaxtime_1_125_particleA_rep2[:] = [x/(relaxtime_1_125_rA**2) for x in relaxtime_1_125_particleA_rep2]

relaxtime_1_125_particleB_rep2 = np.array([669.41526887983105, 5141.7148157161428, 9378.4971711767739])
relaxtime_1_125_particleB_rep2[:] = [x/(relaxtime_1_125_rB**2) for x in relaxtime_1_125_particleB_rep2]

relaxtime_1_125_particleC_rep2 = np.array([758.97551176945001, 5920.7197175766205, 9316.3478005788238])
relaxtime_1_125_particleC_rep2[:] = [x/(relaxtime_1_125_rC**2) for x in relaxtime_1_125_particleC_rep2]

a = [relaxtime_1_125_particleA, relaxtime_1_125_particleA_rep1, relaxtime_1_125_particleA_rep2]
b = [relaxtime_1_125_particleB, relaxtime_1_125_particleB_rep1, relaxtime_1_125_particleB_rep2]
c = [relaxtime_1_125_particleC, relaxtime_1_125_particleC_rep1, relaxtime_1_125_particleC_rep2]
relaxtime_1_125_particleA_avg = np.mean(a, axis=0)
relaxtime_1_125_particleB_avg = np.mean(b, axis=0)
relaxtime_1_125_particleC_avg = np.mean(c, axis=0)


#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_15_radii = [1.0, 1.2, 1.15]

relaxtime_1_15_rA = 1.0
relaxtime_1_15_rB = 1.2
relaxtime_1_15_rC = 1.15

relaxtime_1_15_particleA = np.array([275.98575990817858, 1369.5634601341649, 4611.5899314371800])
relaxtime_1_15_particleA[:] = [x/(relaxtime_1_15_rA**2) for x in relaxtime_1_15_particleA]

relaxtime_1_15_particleB = np.array([650.19125201124052, 4434.2065704629949, 14986.304661649619])
relaxtime_1_15_particleB[:] = [x/(relaxtime_1_15_rB**2) for x in relaxtime_1_15_particleB]

relaxtime_1_15_particleC = np.array([670.38396224211328, 4334.2105966549880, 12235.723178413724])
relaxtime_1_15_particleC[:] = [x/(relaxtime_1_15_rC**2) for x in relaxtime_1_15_particleC]

relaxtime_1_15_particleA_rep1 = np.array([264.42717193853321, 1254.1062819756644, 4070.1828564625257])
relaxtime_1_15_particleA_rep1[:] = [x/(relaxtime_1_15_rA**2) for x in relaxtime_1_15_particleA_rep1]

relaxtime_1_15_particleB_rep1 = np.array([626.14158198880068, 3467.1371686291604, 10591.678524829693])
relaxtime_1_15_particleB_rep1[:] = [x/(relaxtime_1_15_rB**2) for x in relaxtime_1_15_particleB_rep1]

relaxtime_1_15_particleC_rep1 = np.array([623.82585191155579, 3818.7351148952334, 10249.525086924041])
relaxtime_1_15_particleC_rep1[:] = [x/(relaxtime_1_15_rC**2) for x in relaxtime_1_15_particleC_rep1]

relaxtime_1_15_particleA_rep2 = np.array([276.16641518721843, 1048.7899990214216, 3092.4736676550187])
relaxtime_1_15_particleA_rep2[:] = [x/(relaxtime_1_15_rA**2) for x in relaxtime_1_15_particleA_rep2]

relaxtime_1_15_particleB_rep2 = np.array([649.30332790796331, 2914.6509194357145, 9127.7738476391169])
relaxtime_1_15_particleB_rep2[:] = [x/(relaxtime_1_15_rB**2) for x in relaxtime_1_15_particleB_rep2]

relaxtime_1_15_particleC_rep2 = np.array([661.40055830860581, 2738.1482685085784, 12703.849768815528])
relaxtime_1_15_particleC_rep2[:] = [x/(relaxtime_1_15_rC**2) for x in relaxtime_1_15_particleC_rep2]

a = [relaxtime_1_15_particleA, relaxtime_1_15_particleA_rep1, relaxtime_1_15_particleA_rep2]
b = [relaxtime_1_15_particleB, relaxtime_1_15_particleB_rep1, relaxtime_1_15_particleB_rep2]
c = [relaxtime_1_15_particleC, relaxtime_1_15_particleC_rep1, relaxtime_1_15_particleC_rep2]

relaxtime_1_15_particleA_avg = np.mean(a, axis=0)
relaxtime_1_15_particleB_avg = np.mean(b, axis=0)
relaxtime_1_15_particleC_avg = np.mean(c, axis=0)






#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_175_radii = [1.0, 1.2, 1.175]

relaxtime_1_175_rA = 1.0
relaxtime_1_175_rB = 1.2
relaxtime_1_175_rC = 1.175

relaxtime_1_175_particleA = np.array([255.15930890726347, 1282.308314858435, 2757.1309297010985])
relaxtime_1_175_particleA[:] = [x/(relaxtime_1_175_rA**2) for x in relaxtime_1_175_particleA]

relaxtime_1_175_particleB = np.array([662.37709931758400, 3450.5087213620318, 10978.254819367972])
relaxtime_1_175_particleB[:] = [x/(relaxtime_1_175_rB**2) for x in relaxtime_1_175_particleB]

relaxtime_1_175_particleC = np.array([648.03394757987576, 3559.1441914635966, 10233.735460086426])
relaxtime_1_175_particleC[:] = [x/(relaxtime_1_175_rC**2) for x in relaxtime_1_175_particleC]

relaxtime_1_175_particleA_rep1 = np.array([268.15491000261346, 1438.9400885328791, 4576.8422442711908])
relaxtime_1_175_particleA_rep1[:] = [x/(relaxtime_1_175_rA**2) for x in relaxtime_1_175_particleA_rep1]

relaxtime_1_175_particleB_rep1 = np.array([673.49126588815602, 4504.8403574661033, 13825.782883405478])
relaxtime_1_175_particleB_rep1[:] = [x/(relaxtime_1_175_rB**2) for x in relaxtime_1_175_particleB_rep1]

relaxtime_1_175_particleC_rep1 = np.array([690.27433037444882, 4277.9315889772897, 12768.199594318265])
relaxtime_1_175_particleC_rep1[:] = [x/(relaxtime_1_175_rC**2) for x in relaxtime_1_175_particleC_rep1]

relaxtime_1_175_particleA_rep2 = np.array([261.14227804212425, 1694.0606768261277, 2505.9943301949615])
relaxtime_1_175_particleA_rep2[:] = [x/(relaxtime_1_175_rA**2) for x in relaxtime_1_175_particleA_rep2]

relaxtime_1_175_particleB_rep2 = np.array([649.42526746940041, 4716.0562853341698, 6700.2714348053569])
relaxtime_1_175_particleB_rep2[:] = [x/(relaxtime_1_175_rB**2) for x in relaxtime_1_175_particleB_rep2]

relaxtime_1_175_particleC_rep2 = np.array([666.60282722889497, 4783.7447896692129, 7828.1340595419770])
relaxtime_1_175_particleC_rep2[:] = [x/(relaxtime_1_175_rC**2) for x in relaxtime_1_175_particleC_rep2]

a = [relaxtime_1_175_particleA, relaxtime_1_175_particleA_rep1, relaxtime_1_175_particleA_rep2]
b = [relaxtime_1_175_particleB, relaxtime_1_175_particleB_rep1, relaxtime_1_175_particleB_rep2]
c = [relaxtime_1_175_particleC, relaxtime_1_175_particleC_rep1, relaxtime_1_175_particleC_rep2]
relaxtime_1_175_particleA_avg = np.mean(a, axis=0)
relaxtime_1_175_particleB_avg = np.mean(b, axis=0)
relaxtime_1_175_particleC_avg = np.mean(c, axis=0)

#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_2_radii = [1.0, 1.2, 1.2]

relaxtime_1_2_rA = 1.0
relaxtime_1_2_rB = 1.2
relaxtime_1_2_rC = 1.2


relaxtime_1_2_particleA = np.array([234.49889721476265, 1073.8664205599043, 2604.5655428048804])
relaxtime_1_2_particleA[:] = [x/(relaxtime_1_2_rA**2) for x in relaxtime_1_2_particleA]

relaxtime_1_2_particleB = np.array([653.78701008691087, 2793.3986614867940, 11573.862999556341])
relaxtime_1_2_particleB[:] = [x/(relaxtime_1_2_rB**2) for x in relaxtime_1_2_particleB]

relaxtime_1_2_particleA_rep1 = np.array([256.01996931787568, 1088.1555279774707, 2866.9045846323020])
relaxtime_1_2_particleA_rep1[:] = [x/(relaxtime_1_2_rA**2) for x in relaxtime_1_2_particleA_rep1]

relaxtime_1_2_particleB_rep1 = np.array([686.97583137369372, 3852.0861341674367, 7328.9468549104167])
relaxtime_1_2_particleB_rep1[:] = [x/(relaxtime_1_2_rB**2) for x in relaxtime_1_2_particleB_rep1]

relaxtime_1_2_particleA_rep2 = np.array([242.12210779688598, 1206.1789256065647, 2521.0282993656256])
relaxtime_1_2_particleA_rep2[:] = [x/(relaxtime_1_2_rA**2) for x in relaxtime_1_2_particleA_rep2]

relaxtime_1_2_particleB_rep2 = np.array([646.54805508948903, 3837.1699846972228, 7103.7774832304813])
relaxtime_1_2_particleB_rep2[:] = [x/(relaxtime_1_2_rB**2) for x in relaxtime_1_2_particleB_rep2]


a = [relaxtime_1_2_particleA, relaxtime_1_2_particleA_rep1, relaxtime_1_2_particleA_rep2]
b = [relaxtime_1_2_particleB, relaxtime_1_2_particleB_rep1, relaxtime_1_2_particleB_rep2]

relaxtime_1_2_particleA_avg = np.mean(a, axis=0)
relaxtime_1_2_particleB_avg = np.mean(b, axis=0)


#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_25_radii = [1.0, 1.2, 1.25]

relaxtime_1_25_rA = 1.0
relaxtime_1_25_rB = 1.2
relaxtime_1_25_rC = 1.25

relaxtime_1_25_particleA = np.array([218.65686845239216, 903.27477175692911, 2558.0613480839129])
relaxtime_1_25_particleA[:] = [x/(relaxtime_1_25_rA**2) for x in relaxtime_1_25_particleA]

relaxtime_1_25_particleB = np.array([601.29022798153187, 3060.8468385146757, 8120.7636469254594])
relaxtime_1_25_particleB[:] = [x/(relaxtime_1_25_rB**2) for x in relaxtime_1_25_particleB]

relaxtime_1_25_particleC = np.array([725.17656618699345, 3804.2840700771594, 10135.165691419706])
relaxtime_1_25_particleC[:] = [x/(relaxtime_1_25_rC**2) for x in relaxtime_1_25_particleC]

relaxtime_1_25_particleA_rep1 = np.array([220.15653586919635, 1084.2787462571937, 2022.9425853354794])
relaxtime_1_25_particleA_rep1[:] = [x/(relaxtime_1_25_rA**2) for x in relaxtime_1_25_particleA_rep1]

relaxtime_1_25_particleB_rep1 = np.array([586.98059245594607, 3909.1290127255083, 7971.1931624689314])
relaxtime_1_25_particleB_rep1[:] = [x/(relaxtime_1_25_rB**2) for x in relaxtime_1_25_particleB_rep1]

relaxtime_1_25_particleC_rep1 = np.array([718.32376469158180, 4607.9149806691048, 9985.5864058100833])
relaxtime_1_25_particleC_rep1[:] = [x/(relaxtime_1_25_rC**2) for x in relaxtime_1_25_particleC_rep1]

relaxtime_1_25_particleA_rep2 = np.array([209.23325962625987, 818.89076065976769, 1770.2812319717289])
relaxtime_1_25_particleA_rep2[:] = [x/(relaxtime_1_25_rA**2) for x in relaxtime_1_25_particleA_rep2]

relaxtime_1_25_particleB_rep2 = np.array([576.77920727777007, 2602.3546678060957, 5279.3770588933858])
relaxtime_1_25_particleB_rep2[:] = [x/(relaxtime_1_25_rB**2) for x in relaxtime_1_25_particleB_rep2]

relaxtime_1_25_particleC_rep2 = np.array([693.29361365012494, 3219.2504982762939, 6582.4577226943038])
relaxtime_1_25_particleC_rep2[:] = [x/(relaxtime_1_25_rC**2) for x in relaxtime_1_25_particleC_rep2]

a = [relaxtime_1_25_particleA, relaxtime_1_25_particleA_rep1, relaxtime_1_25_particleA_rep2]
b = [relaxtime_1_25_particleB, relaxtime_1_25_particleB_rep1, relaxtime_1_25_particleB_rep2]
c = [relaxtime_1_25_particleC, relaxtime_1_25_particleC_rep1, relaxtime_1_25_particleC_rep2]

relaxtime_1_25_particleA_avg = np.mean(a, axis=0)
relaxtime_1_25_particleB_avg = np.mean(b, axis=0)
relaxtime_1_25_particleC_avg = np.mean(c, axis=0)

data_relaxtime_1 = {'phi':phi, 
              'Particle A': relaxtime_1_25_particleA, 
              'Particle B': relaxtime_1_25_particleB, 
              'Particle C': relaxtime_1_25_particleC}

df_relaxtime_1 = pd.DataFrame (data_relaxtime_1)

fig1 = df_relaxtime_1.plot(x ='phi', y='Particle A', kind = 'scatter',  logy=True, color='Green', label = 'R = 1.0')
df_relaxtime_1.plot(x ='phi', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig1)
df_relaxtime_1.plot(x ='phi', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = 1.', ax= fig1)

fig1.set_ylabel("time/R^2")
fig1.set_title('Relaxation Time | rrr = r**2')

plt.ylim([1, 10000])
plt.show()
plt.close



#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_3_radii = [1.0, 1.2, 1.3]

relaxtime_1_3_rA = 1.0
relaxtime_1_3_rB = 1.2
relaxtime_1_3_rC = 1.3


relaxtime_1_3_particleA = np.array([191.15251467307289, 925.87335103110036, 1596.6384772691752])
relaxtime_1_3_particleA[:] = [x/(relaxtime_1_3_rA**2) for x in relaxtime_1_3_particleA]

relaxtime_1_3_particleB = np.array([530.56465811515375, 3445.3771820532133, 5282.3932503901642])
relaxtime_1_3_particleB[:] = [x/(relaxtime_1_3_rB**2) for x in relaxtime_1_3_particleB]

relaxtime_1_3_particleC = np.array([757.86321230514943, 7477.5361907577844, 8187.3175535259024])
relaxtime_1_3_particleC[:] = [x/(relaxtime_1_3_rC**2) for x in relaxtime_1_3_particleC]


relaxtime_1_3_particleA_rep1 = np.array([193.30600337297699, 894.66494124314158, 1865.3792286250502])
relaxtime_1_3_particleA_rep1[:] = [x/(relaxtime_1_3_rA**2) for x in relaxtime_1_3_particleA_rep1]

relaxtime_1_3_particleB_rep1 = np.array([549.09209250896765, 3406.8211244689169, 7540.7308674250698])
relaxtime_1_3_particleB_rep1[:] = [x/(relaxtime_1_3_rB**2) for x in relaxtime_1_3_particleB_rep1]

relaxtime_1_3_particleC_rep1 = np.array([793.23000752555083, 4820.1127045601934, 9841.5100047847918])
relaxtime_1_3_particleC_rep1[:] = [x/(relaxtime_1_3_rC**2) for x in relaxtime_1_3_particleC_rep1]

relaxtime_1_3_particleA_rep2 = np.array([198.06379327286993, 1017.8482656336651, 1737.3092533375036])
relaxtime_1_3_particleA_rep2[:] = [x/(relaxtime_1_3_rA**2) for x in relaxtime_1_3_particleA_rep2]

relaxtime_1_3_particleB_rep2 = np.array([550.22637555467463, 4150.3528186891717, 7451.5322233748466])
relaxtime_1_3_particleB_rep2[:] = [x/(relaxtime_1_3_rB**2) for x in relaxtime_1_3_particleB_rep2]

relaxtime_1_3_particleC_rep2 = np.array([842.40747358215481, 7131.6509136090699, 11343.197390527283])
relaxtime_1_3_particleC_rep2[:] = [x/(relaxtime_1_3_rC**2) for x in relaxtime_1_3_particleC_rep2]

a = [relaxtime_1_3_particleA, relaxtime_1_3_particleA_rep1, relaxtime_1_3_particleA_rep2]
b = [relaxtime_1_3_particleB, relaxtime_1_3_particleB_rep1, relaxtime_1_3_particleB_rep2]
c = [relaxtime_1_3_particleC, relaxtime_1_3_particleC_rep1, relaxtime_1_3_particleC_rep2]

relaxtime_1_3_particleA_avg = np.mean(a, axis=0)
relaxtime_1_3_particleB_avg = np.mean(b, axis=0)
relaxtime_1_3_particleC_avg = np.mean(c, axis=0)


data_relaxtime_1 = {'phi':phi, 
              'Particle A': relaxtime_1_3_particleA, 
              'Particle B': relaxtime_1_3_particleB, 
              'Particle C': relaxtime_1_3_particleC}

df_relaxtime_1 = pd.DataFrame (data_relaxtime_1)

fig1 = df_relaxtime_1.plot(x ='phi', y='Particle A', kind = 'scatter',  logy=True, color='Green', label = 'R = 1.0')
df_relaxtime_1.plot(x ='phi', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig1)
df_relaxtime_1.plot(x ='phi', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = 1.3', ax= fig1)

fig1.set_ylabel("time/R^2")
fig1.set_title('Relaxation Time | rrr = r**2')

plt.ylim([1, 10000])
plt.show()
plt.close


#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_35_radii = [1.0, 1.2, 1.35]

relaxtime_1_35_rA = 1.0
relaxtime_1_35_rB = 1.2
relaxtime_1_35_rC = 1.35

relaxtime_1_35_particleA = np.array([164.40206982037066, 584.80929028108926, 1604.7373058631624])
relaxtime_1_35_particleA[:] = [x/(relaxtime_1_35_rA**2) for x in relaxtime_1_35_particleA]

relaxtime_1_35_particleB = np.array([470.85314568664910, 1920.5518428416574, 6372.9248106085142])
relaxtime_1_35_particleB[:] = [x/(relaxtime_1_35_rB**2) for x in relaxtime_1_35_particleB]

relaxtime_1_35_particleC = np.array([837.35513326143860, 3867.1824783084621, 12974.884086559478])
relaxtime_1_35_particleC[:] = [x/(relaxtime_1_35_rC**2) for x in relaxtime_1_35_particleC]

relaxtime_1_35_particleA_rep1 = np.array([161.63743209269603, 591.84458020034594, 1705.1723419817017])
relaxtime_1_35_particleA_rep1[:] = [x/(relaxtime_1_35_rA**2) for x in relaxtime_1_35_particleA_rep1]

relaxtime_1_35_particleB_rep1 = np.array([475.89403891797764, 2017.6126019544483, 8660.1925198309691])
relaxtime_1_35_particleB_rep1[:] = [x/(relaxtime_1_35_rB**2) for x in relaxtime_1_35_particleB_rep1]

relaxtime_1_35_particleC_rep1 = np.array([877.30758722892858, 4094.5101116457422, 16276.821792181934])
relaxtime_1_35_particleC_rep1[:] = [x/(relaxtime_1_35_rC**2) for x in relaxtime_1_35_particleC_rep1]

relaxtime_1_35_particleA_rep2 = np.array([157.90470487859295, 719.25721807674756, 1472.0425575685751])
relaxtime_1_35_particleA_rep2[:] = [x/(relaxtime_1_35_rA**2) for x in relaxtime_1_35_particleA_rep2]

relaxtime_1_35_particleB_rep2 = np.array([455.07942184050955, 2459.3089722017912, 6411.3105001743252])
relaxtime_1_35_particleB_rep2[:] = [x/(relaxtime_1_35_rB**2) for x in relaxtime_1_35_particleB_rep2]

relaxtime_1_35_particleC_rep2 = np.array([846.43224074526972, 5997.8463904433202, 11166.390482505827])
relaxtime_1_35_particleC_rep2[:] = [x/(relaxtime_1_35_rC**2) for x in relaxtime_1_35_particleC_rep2]

a = [relaxtime_1_35_particleA, relaxtime_1_35_particleA_rep1, relaxtime_1_35_particleA_rep2]
b = [relaxtime_1_35_particleB, relaxtime_1_35_particleB_rep1, relaxtime_1_35_particleB_rep2]
c = [relaxtime_1_35_particleC, relaxtime_1_35_particleC_rep1, relaxtime_1_35_particleC_rep2]

relaxtime_1_35_particleA_avg = np.mean(a, axis=0)
relaxtime_1_35_particleB_avg = np.mean(b, axis=0)
relaxtime_1_35_particleC_avg = np.mean(c, axis=0)





#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_4_radii = [1.0, 1.2, 1.4]

relaxtime_1_4_rA = 1.0
relaxtime_1_4_rB = 1.2
relaxtime_1_4_rC = 1.4

relaxtime_1_4_particleA = np.array([145.22339807204614, 502.66475432178424,1326.1608382239031])
relaxtime_1_4_particleA[:] = [x/(relaxtime_1_4_rA**2) for x in relaxtime_1_4_particleA]

relaxtime_1_4_particleB = np.array([407.75463748137037, 1742.8909717107447, 5854.6322125374581])
relaxtime_1_4_particleB[:] = [x/(relaxtime_1_4_rB**2) for x in relaxtime_1_4_particleB]

relaxtime_1_4_particleC = np.array([914.48907067899256, 5257.4793824186199, 47277.668557739133])
relaxtime_1_4_particleC[:] = [x/(relaxtime_1_4_rC**2) for x in relaxtime_1_4_particleC]

relaxtime_1_4_particleA_rep1 = np.array([138.62794607019435, 463.23587940656341, 1054.7501620756434])
relaxtime_1_4_particleA_rep1[:] = [x/(relaxtime_1_4_rA**2) for x in relaxtime_1_4_particleA_rep1]

relaxtime_1_4_particleB_rep1 = np.array([432.98289178689356, 1549.3403560205411, 4837.5904634636736])
relaxtime_1_4_particleB_rep1[:] = [x/(relaxtime_1_4_rB**2) for x in relaxtime_1_4_particleB_rep1]

relaxtime_1_4_particleC_rep1 = np.array([918.12102524627653, 3861.4011647230732, 18444.780275916470])
relaxtime_1_4_particleC_rep1[:] = [x/(relaxtime_1_4_rC**2) for x in relaxtime_1_4_particleC_rep1]

relaxtime_1_4_particleA_rep2 = np.array([136.59979624684451, 526.88428466836979, 1152.8836619744761])
relaxtime_1_4_particleA_rep2[:] = [x/(relaxtime_1_4_rA**2) for x in relaxtime_1_4_particleA_rep2]

relaxtime_1_4_particleB_rep2 = np.array([395.33715933129452, 1893.7369375535170, 4564.6735666068571])
relaxtime_1_4_particleB_rep2[:] = [x/(relaxtime_1_4_rB**2) for x in relaxtime_1_4_particleB_rep2]

relaxtime_1_4_particleC_rep2 = np.array([893.13954630277101, 5295.5544876483200, 11948.728886145933])
relaxtime_1_4_particleC_rep2[:] = [x/(relaxtime_1_4_rC**2) for x in relaxtime_1_4_particleC_rep2]

a = [relaxtime_1_4_particleA, relaxtime_1_4_particleA_rep1, relaxtime_1_4_particleA_rep2]
b = [relaxtime_1_4_particleB, relaxtime_1_4_particleB_rep1, relaxtime_1_4_particleB_rep2]
c = [relaxtime_1_4_particleC, relaxtime_1_4_particleC_rep1, relaxtime_1_4_particleC_rep2]

relaxtime_1_4_particleA_avg = np.mean(a, axis=0)
relaxtime_1_4_particleB_avg = np.mean(b, axis=0)
relaxtime_1_4_particleC_avg = np.mean(c, axis=0)



#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_45_radii = [1.0, 1.2, 1.45]

relaxtime_1_45_rA = 1.0
relaxtime_1_45_rB = 1.2
relaxtime_1_45_rC = 1.45

relaxtime_1_45_particleA = np.array([120.23436496353321, 408.70161388343121, 827.68716850337387])
relaxtime_1_45_particleA[:] = [x/(relaxtime_1_45_rA**2) for x in relaxtime_1_45_particleA]

relaxtime_1_45_particleB = np.array([372.82489075995557, 1291.2006688108463, 2942.9559359831933])
relaxtime_1_45_particleB[:] = [x/(relaxtime_1_45_rB**2) for x in relaxtime_1_45_particleB]

relaxtime_1_45_particleC = np.array([985.04910383537697, 3809.8023579979217, 9155.9900423055151])
relaxtime_1_45_particleC[:] = [x/(relaxtime_1_45_rC**2) for x in relaxtime_1_45_particleC]

relaxtime_1_45_particleA_rep1 = np.array([120.27154661136230, 371.42018191318363, 948.09569000353713])
relaxtime_1_45_particleA_rep1[:] = [x/(relaxtime_1_45_rA**2) for x in relaxtime_1_45_particleA_rep1]

relaxtime_1_45_particleB_rep1 = np.array([363.27314769752024, 1276.6499870764073, 3540.9310223481575])
relaxtime_1_45_particleB_rep1[:] = [x/(relaxtime_1_45_rB**2) for x in relaxtime_1_45_particleB_rep1]

relaxtime_1_45_particleC_rep1 = np.array([955.85132239092354, 4082.3380264025732, 10326.588120173099])
relaxtime_1_45_particleC_rep1[:] = [x/(relaxtime_1_45_rC**2) for x in relaxtime_1_45_particleC_rep1]

relaxtime_1_45_particleA_rep2 = np.array([117.53014074116531, 374.09242192179960, 841.27661635303150])
relaxtime_1_45_particleA_rep2[:] = [x/(relaxtime_1_45_rA**2) for x in relaxtime_1_45_particleA_rep2]

relaxtime_1_45_particleB_rep2 = np.array([349.53631720251354, 1477.7320857037944, 2950.1728384162002])
relaxtime_1_45_particleB_rep2[:] = [x/(relaxtime_1_45_rB**2) for x in relaxtime_1_45_particleB_rep2]

relaxtime_1_45_particleC_rep2 = np.array([874.19588887793850, 4647.3206485785749, 8912.1940720868170])
relaxtime_1_45_particleC_rep2[:] = [x/(relaxtime_1_45_rC**2) for x in relaxtime_1_45_particleC_rep2]

a = [relaxtime_1_45_particleA, relaxtime_1_45_particleA_rep1, relaxtime_1_45_particleA_rep2]
b = [relaxtime_1_45_particleB, relaxtime_1_45_particleB_rep1, relaxtime_1_45_particleB_rep2]
c = [relaxtime_1_45_particleC, relaxtime_1_45_particleC_rep1, relaxtime_1_45_particleC_rep2]

relaxtime_1_45_particleA_avg = np.mean(a, axis=0)
relaxtime_1_45_particleB_avg = np.mean(b, axis=0)
relaxtime_1_45_particleC_avg = np.mean(c, axis=0)





#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_5_radii = [1.0, 1.2, 1.5]

relaxtime_1_5_rA = 1.0
relaxtime_1_5_rB = 1.2
relaxtime_1_5_rC = 1.5


relaxtime_1_5_particleA = np.array([101.79001217226723, 329.67079165826078, 608.66651819386720])
relaxtime_1_5_particleA[:] = [x/(relaxtime_1_5_rA**2) for x in relaxtime_1_5_particleA]

relaxtime_1_5_particleB = np.array([311.91944955182839, 1138.2579905917523, 2167.6365131438292])
relaxtime_1_5_particleB[:] = [x/(relaxtime_1_5_rB**2) for x in relaxtime_1_5_particleB]

relaxtime_1_5_particleC = np.array([984.43361048233646, 4551.8124646326469, 8025.7457590923750])
relaxtime_1_5_particleC[:] = [x/(relaxtime_1_5_rC**2) for x in relaxtime_1_5_particleC]

relaxtime_1_5_particleA_rep1 = np.array([102.90701774288576, 290.58882185255663, 599.82112551094906])
relaxtime_1_5_particleA_rep1[:] = [x/(relaxtime_1_5_rA**2) for x in relaxtime_1_5_particleA_rep1]

relaxtime_1_5_particleB_rep1 = np.array([314.88297165392828, 1214.1751610333752, 2076.0188209775029])
relaxtime_1_5_particleB_rep1[:] = [x/(relaxtime_1_5_rB**2) for x in relaxtime_1_5_particleB_rep1]

relaxtime_1_5_particleC_rep1 = np.array([1016.3376490121042, 4899.9191502687227, 8824.2591817709435])
relaxtime_1_5_particleC_rep1[:] = [x/(relaxtime_1_5_rC**2) for x in relaxtime_1_5_particleC_rep1]

relaxtime_1_5_particleA_rep2 = np.array([103.77415105159257, 296.44895995968102, 725.68660507898858])
relaxtime_1_5_particleA_rep2[:] = [x/(relaxtime_1_5_rA**2) for x in relaxtime_1_5_particleA_rep2]

relaxtime_1_5_particleB_rep2 = np.array([324.52379257510734, 1081.7101138168318, 2864.7847377295711])
relaxtime_1_5_particleB_rep2[:] = [x/(relaxtime_1_5_rB**2) for x in relaxtime_1_5_particleB_rep2]

relaxtime_1_5_particleC_rep2 = np.array([989.42704115816673, 4031.7618015706530, 13781.943793683449])
relaxtime_1_5_particleC_rep2[:] = [x/(relaxtime_1_5_rC**2) for x in relaxtime_1_5_particleC_rep2]


a = [relaxtime_1_5_particleA, relaxtime_1_5_particleA_rep1, relaxtime_1_5_particleA_rep2]
b = [relaxtime_1_5_particleB, relaxtime_1_5_particleB_rep1, relaxtime_1_5_particleB_rep2]
c = [relaxtime_1_5_particleC, relaxtime_1_5_particleC_rep1, relaxtime_1_5_particleC_rep2]

relaxtime_1_5_particleA_avg = np.mean(a, axis=0)
relaxtime_1_5_particleB_avg = np.mean(b, axis=0)
relaxtime_1_5_particleC_avg = np.mean(c, axis=0)


#%%
phi = [0.55, 0.57, 0.58]

relaxtime_1_8_radii = [1.0, 1.2, 1.8]

relaxtime_1_8_rA = 1.0
relaxtime_1_8_rB = 1.2
relaxtime_1_8_rC = 1.8


relaxtime_1_8_particleA = np.array([39.625279798335526, 75.157351136433604, 121.09115227943980])
relaxtime_1_8_particleA[:] = [x/(relaxtime_1_8_rA**2) for x in relaxtime_1_8_particleA]

relaxtime_1_8_particleB = np.array([119.10960232839751, 284.62318349120829, 520.20386270904396])
relaxtime_1_8_particleB[:] = [x/(relaxtime_1_8_rB**2) for x in relaxtime_1_8_particleB]

relaxtime_1_8_particleC = np.array([954.67802452448154, 3005.0910406033609, 8092.4684579969489])
relaxtime_1_8_particleC[:] = [x/(relaxtime_1_8_rC**2) for x in relaxtime_1_8_particleC]

relaxtime_1_8_particleA_rep1 = np.array([39.203891892616454, 75.718724325618410, 113.87413688715124])
relaxtime_1_8_particleA_rep1[:] = [x/(relaxtime_1_8_rA**2) for x in relaxtime_1_8_particleA_rep1]

relaxtime_1_8_particleB_rep1 = np.array([120.55185849669510, 278.20458952374383, 464.50547540352369])
relaxtime_1_8_particleB_rep1[:] = [x/(relaxtime_1_8_rB**2) for x in relaxtime_1_8_particleB_rep1]

relaxtime_1_8_particleC_rep1 = np.array([1034.6583868754428, 2761.2883998663988, 6896.4115449263045])
relaxtime_1_8_particleC_rep1[:] = [x/(relaxtime_1_8_rC**2) for x in relaxtime_1_8_particleC_rep1]

relaxtime_1_8_particleA_rep2 = np.array([39.501207242509125, 77.614242897459562, 124.45727298516286])
relaxtime_1_8_particleA_rep2[:] = [x/(relaxtime_1_8_rA**2) for x in relaxtime_1_8_particleA_rep2]

relaxtime_1_8_particleB_rep2 = np.array([119.33230187001310, 261.10348431693234, 462.45268795735564])
relaxtime_1_8_particleB_rep2[:] = [x/(relaxtime_1_8_rB**2) for x in relaxtime_1_8_particleB_rep2]

relaxtime_1_8_particleC_rep2 = np.array([996.73810221837527, 3311.8342895370533, 4641.0384585341371])
relaxtime_1_8_particleC_rep2[:] = [x/(relaxtime_1_8_rC**2) for x in relaxtime_1_8_particleC_rep2]


a = [relaxtime_1_8_particleA, relaxtime_1_8_particleA_rep1, relaxtime_1_8_particleA_rep2]
b = [relaxtime_1_8_particleB, relaxtime_1_8_particleB_rep1, relaxtime_1_8_particleB_rep2]
c = [relaxtime_1_8_particleC, relaxtime_1_8_particleC_rep1, relaxtime_1_8_particleC_rep2]

relaxtime_1_8_particleA_avg = np.mean(a, axis=0)
relaxtime_1_8_particleB_avg = np.mean(b, axis=0)
relaxtime_1_8_particleC_avg = np.mean(c, axis=0)


#%%
phi = [0.55, 0.57, 0.58]

relaxtime_1_rA = 1.0
relaxtime_1_rB = 1.2
relaxtime_1_rC = 2.0


relaxtime_1_rrr = [1.0, 1.44, 4.0]

relaxtime_1_particleA = np.array([24.531615029615146, 39.662810826894393, 55.957679287911326])
relaxtime_1_particleA[:] = [x/(relaxtime_1_rA**2) for x in relaxtime_1_particleA]


relaxtime_1_particleB = np.array([72.745388376030533, 137.44848625390290, 209.54894943244537])
relaxtime_1_particleB[:] = [x/(relaxtime_1_rB**2) for x in relaxtime_1_particleB]


relaxtime_1_particleC = np.array([949.67238509123717, 2371.6512539335558, 4854.7093488083729])
relaxtime_1_particleC[:] = [x/(relaxtime_1_rC**2) for x in relaxtime_1_particleC]


relaxtime_1_particleA_rep1 = np.array([24.192882376870894, 39.586912618687748, 55.165800406259663])
relaxtime_1_particleA_rep1[:] = [x/(relaxtime_1_rA**2) for x in relaxtime_1_particleA_rep1]


relaxtime_1_particleB_rep1 = np.array([71.533273489197228, 136.09546554510646, 209.11574627454490])
relaxtime_1_particleB_rep1[:] = [x/(relaxtime_1_rB**2) for x in relaxtime_1_particleB_rep1]


relaxtime_1_particleC_rep1 = np.array([953.57802158981792, 2271.9178701102446, 4723.2293210521402])
relaxtime_1_particleC_rep1[:] = [x/(relaxtime_1_rC**2) for x in relaxtime_1_particleC_rep1]


relaxtime_1_particleA_rep2 = np.array([24.159382356458124, 39.158352909858287, 52.242330122582004])
relaxtime_1_particleA_rep2[:] = [x/(relaxtime_1_rA**2) for x in relaxtime_1_particleA_rep2]


relaxtime_1_particleB_rep2 = np.array([71.022342515355476, 129.44835628774294, 200.59664338804046])
relaxtime_1_particleB_rep2[:] = [x/(relaxtime_1_rB**2) for x in relaxtime_1_particleB_rep2]


relaxtime_1_particleC_rep2 = np.array([1030.1898226752057, 2352.8429453670028, 4349.2952709919809])
relaxtime_1_particleC_rep2[:] = [x/(relaxtime_1_rC**2) for x in relaxtime_1_particleC_rep2]


a = [relaxtime_1_particleA, relaxtime_1_particleA_rep1, relaxtime_1_particleA_rep2]
b = [relaxtime_1_particleB, relaxtime_1_particleB_rep1, relaxtime_1_particleB_rep2]
c = [relaxtime_1_particleC, relaxtime_1_particleC_rep1, relaxtime_1_particleC_rep2]


relaxtime_1_particleA_avg = np.mean(a, axis=0)
relaxtime_1_particleB_avg = np.mean(b, axis=0)
relaxtime_1_particleC_avg = np.mean(c, axis=0)


#%%
phi = [0.55, 0.57, 0.58]

relaxtime_2_rA = 1.0
relaxtime_2_rB = 1.2
relaxtime_2_rC = 2.5

relaxtime_2_rrr = [1.0, 1.44, 6.25]

relaxtime_2_particleA = [11.282911905943156, 14.008482200650466, 16.129293060062384]
relaxtime_2_particleA[:] = [x/(relaxtime_2_rA**2) for x in relaxtime_2_particleA]

relaxtime_2_particleB = [26.574425242172236, 38.028334009462931, 46.605981658614724]
relaxtime_2_particleB[:] = [x/(relaxtime_2_rB**2) for x in relaxtime_2_particleB]

relaxtime_2_particleC = [1209.2867638981484, 2329.6507688105244, 3291.0706920488683]
relaxtime_2_particleC[:] = [x/(relaxtime_2_rC**2) for x in relaxtime_2_particleC]

relaxtime_2_particleA_rep1 = np.array([11.201870863346393, 13.947005106848023, 15.991657404131384])
relaxtime_2_particleA_rep1[:] = [x/(relaxtime_2_rA**2) for x in relaxtime_2_particleA_rep1]


relaxtime_2_particleB_rep1 = np.array([26.755644399391805, 37.853356053582438, 47.465990091970511])
relaxtime_2_particleB_rep1[:] = [x/(relaxtime_2_rB**2) for x in relaxtime_2_particleB_rep1]


relaxtime_2_particleC_rep1 = np.array([1170.1995595853771, 2273.5051247770380, 3668.4313725852726])
relaxtime_2_particleC_rep1[:] = [x/(relaxtime_2_rC**2) for x in relaxtime_2_particleC_rep1]


relaxtime_2_particleA_rep2 = np.array([11.250881737991127, 13.900789977943798, 15.801708498201959])
relaxtime_2_particleA_rep2[:] = [x/(relaxtime_2_rA**2) for x in relaxtime_2_particleA_rep2]


relaxtime_2_particleB_rep2 = np.array([26.679239374557316, 37.476459063425352, 46.139301680294892])
relaxtime_2_particleB_rep2[:] = [x/(relaxtime_2_rB**2) for x in relaxtime_2_particleB_rep2]


relaxtime_2_particleC_rep2 = np.array([1190.6131226364698, 2204.2613992860729, 4430.9131627189054])
relaxtime_2_particleC_rep2[:] = [x/(relaxtime_2_rC**2) for x in relaxtime_2_particleC_rep2]

a = [relaxtime_2_particleA, relaxtime_2_particleA_rep1, relaxtime_2_particleA_rep2]
b = [relaxtime_2_particleB, relaxtime_2_particleB_rep1, relaxtime_2_particleB_rep2]
c = [relaxtime_2_particleC, relaxtime_2_particleC_rep1, relaxtime_2_particleC_rep2]


relaxtime_2_particleA_avg = np.mean(a, axis=0)
relaxtime_2_particleB_avg = np.mean(b, axis=0)
relaxtime_2_particleC_avg = np.mean(c, axis=0)


data_relaxtime_1 = {'phi':phi, 
              'Particle A': relaxtime_2_particleA, 
              'Particle B': relaxtime_2_particleB, 
              'Particle C': relaxtime_2_particleC}

df_relaxtime_1 = pd.DataFrame (data_relaxtime_1)

fig1 = df_relaxtime_1.plot(x ='phi', y='Particle A', kind = 'scatter',  logy=True, color='Green', label = 'R = 1.0')
df_relaxtime_1.plot(x ='phi', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig1)
df_relaxtime_1.plot(x ='phi', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = 2.0', ax= fig1)

fig1.set_ylabel("time/R^2")
fig1.set_title('Relaxation Time | rrr = r**2')

#plt.ylim([1, 10000])
plt.show()
plt.close

#%%

phi = [0.55, 0.57, 0.58]

relaxtime_3_rA = 1.0
relaxtime_3_rB = 1.2
relaxtime_3_rC = 3.0

relaxtime_3_rrr = [1.0, 1.44, 9.0]

relaxtime_3_particleA = np.array([7.7395673129222473, 8.6760221343645885, 9.2980973596166994])
relaxtime_3_particleA[:] = [x/(relaxtime_3_rA**2) for x in relaxtime_3_particleA]

relaxtime_3_particleB = np.array([15.114006743795187, 18.377671142023772, 20.754348161389196])
relaxtime_3_particleB[:] = [x/(relaxtime_3_rB**2) for x in relaxtime_3_particleB]

relaxtime_3_particleC = np.array([1672.6843126996964, 2839.6236101702311, 5384.0841812237240])
relaxtime_3_particleC[:] = [x/(relaxtime_3_rC**2) for x in relaxtime_3_particleC]

relaxtime_3_particleA_rep1 = np.array([7.7258433474816934, 8.6623677222937570, 9.3351212011396179])
relaxtime_3_particleA_rep1[:] = [x/(relaxtime_3_rA**2) for x in relaxtime_3_particleA_rep1]

relaxtime_3_particleB_rep1 = np.array([15.048931706658843, 18.091436844030810, 20.561000307681173])
relaxtime_3_particleB_rep1[:] = [x/(relaxtime_3_rB**2) for x in relaxtime_3_particleB_rep1]

relaxtime_3_particleC_rep1 = np.array([1611.8911343340460, 3005.4623243376109, 6035.8201483573548])
relaxtime_3_particleC_rep1[:] = [x/(relaxtime_3_rC**2) for x in relaxtime_3_particleC_rep1]


relaxtime_3_particleA_rep2 = np.array([7.7282168244980669, 8.7048359715266592, 9.2956372290648801])
relaxtime_3_particleA_rep2[:] = [x/(relaxtime_3_rA**2) for x in relaxtime_3_particleA_rep2]


relaxtime_3_particleB_rep2 = np.array([15.108861761485516, 18.099414010699078, 20.581030084439380])
relaxtime_3_particleB_rep2[:] = [x/(relaxtime_3_rB**2) for x in relaxtime_3_particleB_rep2]


relaxtime_3_particleC_rep2 = np.array([1700.1799238098990, 3410.1590319387051, 4937.9286095954703])
relaxtime_3_particleC_rep2[:] = [x/(relaxtime_3_rC**2) for x in relaxtime_3_particleC_rep2]


a = [relaxtime_3_particleA, relaxtime_3_particleA_rep1, relaxtime_3_particleA_rep2]
b = [relaxtime_3_particleB, relaxtime_3_particleB_rep1, relaxtime_3_particleB_rep2]
c = [relaxtime_3_particleC, relaxtime_3_particleC_rep1, relaxtime_3_particleC_rep2]

relaxtime_3_particleA_avg = np.mean(a, axis=0)
relaxtime_3_particleB_avg = np.mean(b, axis=0)
relaxtime_3_particleC_avg = np.mean(c, axis=0)


#%%
phi = [0.01, 0.40, 0.50, 0.53, 0.55, 0.57, 0.58]

relaxtime_4_radii = [1.0, 1.2, 4.0]

relaxtime_4_rA = 1.0
relaxtime_4_rB = 1.2
relaxtime_4_rC = 4.0

relaxtime_4_particleA = np.array([5.7102582920478344, 5.9708954426786995, 6.1665451372325855])
relaxtime_4_particleA[:] = [x/(relaxtime_4_rA**2) for x in relaxtime_4_particleA]

relaxtime_4_particleB = np.array([9.3228530957299878, 10.045826238474810, 10.512740186956318])
relaxtime_4_particleB[:] = [x/(relaxtime_4_rB**2) for x in relaxtime_4_particleB]

relaxtime_4_particleC = np.array([3271.9152607744936, 6381.9763788176842, 14591.649644042756])
relaxtime_4_particleC[:] = [x/(relaxtime_4_rC**2) for x in relaxtime_4_particleC]


relaxtime_4_particleA_rep1 = np.array([5.6888102789199584, 5.9807083559643415, 6.1324000461621848])
relaxtime_4_particleA_rep1[:] = [x/(relaxtime_4_rA**2) for x in relaxtime_4_particleA_rep1]


relaxtime_4_particleB_rep1 = np.array([9.3544367613966202, 10.042063660580938, 10.518562166248293])
relaxtime_4_particleB_rep1[:] = [x/(relaxtime_4_rB**2) for x in relaxtime_4_particleB_rep1]


relaxtime_4_particleC_rep1 = np.array([3175.5551078537537, 9396.0324904180125, 12320.471528932232])
relaxtime_4_particleC_rep1[:] = [x/(relaxtime_4_rC**2) for x in relaxtime_4_particleC_rep1]


relaxtime_4_particleA_rep2 = np.array([5.7021531123647193, 5.9858587113635444, 6.1417200524783047])
relaxtime_4_particleA_rep2[:] = [x/(relaxtime_4_rA**2) for x in relaxtime_4_particleA_rep2]


relaxtime_4_particleB_rep2 = np.array([9.3563464062170301, 10.087968104994918, 10.589506244279100])
relaxtime_4_particleB_rep2[:] = [x/(relaxtime_4_rB**2) for x in relaxtime_4_particleB_rep2]


relaxtime_4_particleC_rep2 = np.array([3351.0151553568080, 5211.4360085320550, 7477.3783459877659])
relaxtime_4_particleC_rep2[:] = [x/(relaxtime_4_rC**2) for x in relaxtime_4_particleC_rep2]

a = [relaxtime_4_particleA, relaxtime_4_particleA_rep1, relaxtime_4_particleA_rep2]
b = [relaxtime_4_particleB, relaxtime_4_particleB_rep1, relaxtime_4_particleB_rep2]
c = [relaxtime_4_particleC, relaxtime_4_particleC_rep1, relaxtime_4_particleC_rep2]

relaxtime_4_particleA_avg = np.mean(a, axis=0)
relaxtime_4_particleB_avg = np.mean(b, axis=0)
relaxtime_4_particleC_avg = np.mean(c, axis=0)

#%%
phi = [0.55, 0.57, 0.58]

relaxtime_5_radii = [1.0, 1.2, 5.0]

relaxtime_5_rA = 1.0
relaxtime_5_rB = 1.2
relaxtime_5_rC = 5.0

relaxtime_5_particleA = np.array([5.0489153824164115, 5.2071305648331778, 5.2896243845059656])
relaxtime_5_particleA[:] = [x/(relaxtime_5_rA**2) for x in relaxtime_5_particleA]

relaxtime_5_particleB = np.array([7.8295801159488461, 8.1410029854184334, 8.3276046599842228])
relaxtime_5_particleB[:] = [x/(relaxtime_5_rB**2) for x in relaxtime_5_particleB]

relaxtime_5_particleC = np.array([6590.8894455770051, 12227.254724520095, 22284.114948003476])
relaxtime_5_particleC[:] = [x/(relaxtime_5_rC**2) for x in relaxtime_5_particleC]


relaxtime_5_particleA_rep1 = np.array([5.0559647835272177, 5.2075667483408790, 5.2741344555174550])
relaxtime_5_particleA_rep1[:] = [x/(relaxtime_5_rA**2) for x in relaxtime_5_particleA_rep1]


relaxtime_5_particleB_rep1 = np.array([7.8272286186132431, 8.1313819141986503, 8.3271047431140044])
relaxtime_5_particleB_rep1[:] = [x/(relaxtime_5_rB**2) for x in relaxtime_5_particleB_rep1]


relaxtime_5_particleC_rep1 = np.array([5773.3514804513097, 14008.127451316219, 18817.873589904084])
relaxtime_5_particleC_rep1[:] = [x/(relaxtime_5_rC**2) for x in relaxtime_5_particleC_rep1]


relaxtime_5_particleA_rep2 = np.array([5.0561024921027746, 5.2039018725677240, 5.2671722942557047])
relaxtime_5_particleA_rep2[:] = [x/(relaxtime_5_rA**2) for x in relaxtime_5_particleA_rep2]


relaxtime_5_particleB_rep2 = np.array([7.8018473907558477, 8.1202667496781036, 8.3008350364669798])
relaxtime_5_particleB_rep2[:] = [x/(relaxtime_5_rB**2) for x in relaxtime_5_particleB_rep2]


relaxtime_5_particleC_rep2 = np.array([7524.7718470505242, 13347.305884653346, 18563.564512282581])
relaxtime_5_particleC_rep2[:] = [x/(relaxtime_5_rC**2) for x in relaxtime_5_particleC_rep2]

a = [relaxtime_5_particleA, relaxtime_5_particleA_rep1, relaxtime_5_particleA_rep2]
b = [relaxtime_5_particleB, relaxtime_5_particleB_rep1, relaxtime_5_particleB_rep2]
c = [relaxtime_5_particleC, relaxtime_5_particleC_rep1, relaxtime_5_particleC_rep2]

relaxtime_5_particleA_avg = np.mean(a, axis=0)
relaxtime_5_particleB_avg = np.mean(b, axis=0)
relaxtime_5_particleC_avg = np.mean(c, axis=0)

ratio5 = [i / j for i, j in zip(relaxtime_5_particleC_avg,relaxtime_5_particleB_avg)] 
print(ratio5)



data_relaxtime_1 = {'phi':phi, 
              'Particle A': relaxtime_5_particleA, 
              'Particle B': relaxtime_5_particleB, 
              'Particle C': relaxtime_5_particleC}

df_relaxtime_1 = pd.DataFrame (data_relaxtime_1)

fig1 = df_relaxtime_1.plot(x ='phi', y='Particle A', kind = 'scatter',  logy=True, color='Green', label = 'R = 1.0')
df_relaxtime_1.plot(x ='phi', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig1)
df_relaxtime_1.plot(x ='phi', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = 5', ax= fig1)

fig1.set_ylabel("time/R^2")
fig1.set_title('Relaxation Time | rrr = r**2')

#plt.ylim([1, 10000])
plt.show()
plt.close

#%%
phi = [0.55, 0.57, 0.58]

relaxtime_6_radii = [1.0, 1.2, 6.0]

relaxtime_6_rA = 1.0
relaxtime_6_rB = 1.2
relaxtime_6_rC = 6.0

relaxtime_6_particleA = np.array([4.7662971559712535, 4.8569139810370832, 4.9099332986533151])
relaxtime_6_particleA[:] = [x/(relaxtime_6_rA**2) for x in relaxtime_6_particleA]

relaxtime_6_particleB = np.array([7.2002346930428978, 7.3829101280628606, 7.4759175256935801])
relaxtime_6_particleB[:] = [x/(relaxtime_6_rB**2) for x in relaxtime_6_particleB]

relaxtime_6_particleC = np.array([8448.7127170368367, 12181.985044384744, 16105.131231953745])
relaxtime_6_particleC[:] = [x/(relaxtime_6_rC**2) for x in relaxtime_6_particleC]


relaxtime_6_particleA_rep1 = np.array([4.7728720071322366, 4.8576454146692081, 4.8980505091323510])
relaxtime_6_particleA_rep1[:] = [x/(relaxtime_6_rA**2) for x in relaxtime_6_particleA_rep1]


relaxtime_6_particleB_rep1 = np.array([7.1948851591231247, 7.3994678084588523, 7.4905594973253704])
relaxtime_6_particleB_rep1[:] = [x/(relaxtime_6_rB**2) for x in relaxtime_6_particleB_rep1]


relaxtime_6_particleC_rep1 = np.array([6887.6242956398728, 11194.042072699955, 27042.726509554559])
relaxtime_6_particleC_rep1[:] = [x/(relaxtime_6_rC**2) for x in relaxtime_6_particleC_rep1]


relaxtime_6_particleA_rep2 = np.array([4.7836925747468122, 4.8547638570019878, 4.9013637633762670])
relaxtime_6_particleA_rep2[:] = [x/(relaxtime_6_rA**2) for x in relaxtime_6_particleA_rep2]


relaxtime_6_particleB_rep2 = np.array([7.1756709890893378, 7.3809136200044012, 7.4755002779839854])
relaxtime_6_particleB_rep2[:] = [x/(relaxtime_6_rB**2) for x in relaxtime_6_particleB_rep2]


relaxtime_6_particleC_rep2 = np.array([7368.2598777564981, 14550.732453633053, 18024.683860387719])
relaxtime_6_particleC_rep2[:] = [x/(relaxtime_6_rC**2) for x in relaxtime_6_particleC_rep2]

a = [relaxtime_6_particleA, relaxtime_6_particleA_rep1, relaxtime_6_particleA_rep2]
b = [relaxtime_6_particleB, relaxtime_6_particleB_rep1, relaxtime_6_particleB_rep2]
c = [relaxtime_6_particleC, relaxtime_6_particleC_rep1, relaxtime_6_particleC_rep2]

relaxtime_6_particleA_avg = np.mean(a, axis=0)
relaxtime_6_particleB_avg = np.mean(b, axis=0)
relaxtime_6_particleC_avg = np.mean(c, axis=0)

data_relaxtime_6 = {'phi':phi, 
              'Particle A': relaxtime_6_particleA_avg, 
              'Particle B': relaxtime_6_particleB_avg, 
              'Particle C': relaxtime_6_particleC_avg}


ratio6 = [i / j for i, j in zip(relaxtime_6_particleC_avg,relaxtime_6_particleB_avg)] 
print(ratio6)

#%%
# phi = 0.58


radius = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05,
          1.1, 1.125, 1.15, 1.175, 1.2, 1.25, 1.3, 1.35, 1.45, 1.5, 1.8, 
          2.0, 2.5, 3.0, 4.0, 5.0, 6.0]

vf58_A = [relaxtime_0_5_particleA_avg[-1], relaxtime_0_55_particleA_avg[-1],
          relaxtime_0_6_particleA_avg[-1], relaxtime_0_65_particleA_avg[-1],
          relaxtime_0_7_particleA_avg[-1], relaxtime_0_75_particleA_avg[-1],
          relaxtime_0_8_particleA_avg[-1], relaxtime_0_85_particleA_avg[-1],
          relaxtime_0_9_particleA_avg[-1], relaxtime_0_95_particleA_avg[-1],
          relaxtime_1_0_particleA_avg[-1], relaxtime_1_05_particleA_avg[-1],
          relaxtime_1_1_particleA_avg[-1], relaxtime_1_125_particleA_avg[-1],
          relaxtime_1_15_particleA_avg[-1], relaxtime_1_175_particleA_avg[-1],
          relaxtime_1_2_particleA_avg[-1], relaxtime_1_25_particleA_avg[-1],
          relaxtime_1_3_particleA_avg[-1], relaxtime_1_35_particleA_avg[-1],
          relaxtime_1_45_particleA_avg[-1],
          relaxtime_1_5_particleA_avg[-1], relaxtime_1_8_particleA_avg[-1],
          relaxtime_1_particleA_avg[-1], relaxtime_2_particleA_avg[-1],
          relaxtime_3_particleA_avg[-1], relaxtime_4_particleA_avg[-1],
          relaxtime_5_particleA_avg[-1], relaxtime_6_particleA_avg[-1]]

vf58_B = [relaxtime_0_5_particleB_avg[-1], relaxtime_0_55_particleB_avg[-1],
          relaxtime_0_6_particleB_avg[-1], relaxtime_0_65_particleB_avg[-1],
          relaxtime_0_7_particleB_avg[-1], relaxtime_0_75_particleB_avg[-1],
          relaxtime_0_8_particleB_avg[-1], relaxtime_0_85_particleB_avg[-1],
          relaxtime_0_9_particleB_avg[-1], relaxtime_0_95_particleB_avg[-1],
          relaxtime_1_0_particleB_avg[-1], relaxtime_1_05_particleB_avg[-1],
          relaxtime_1_1_particleB_avg[-1], relaxtime_1_125_particleB_avg[-1],
          relaxtime_1_15_particleB_avg[-1], relaxtime_1_175_particleB_avg[-1],
          relaxtime_1_2_particleB_avg[-1], relaxtime_1_25_particleB_avg[-1],
          relaxtime_1_3_particleB_avg[-1], relaxtime_1_35_particleB_avg[-1],
          relaxtime_1_45_particleB_avg[-1],
          relaxtime_1_5_particleB_avg[-1], relaxtime_1_8_particleB_avg[-1],
          relaxtime_1_particleB_avg[-1], relaxtime_2_particleB_avg[-1],
          relaxtime_3_particleB_avg[-1], relaxtime_4_particleB_avg[-1],
          relaxtime_5_particleB_avg[-1], relaxtime_6_particleB_avg[-1]]

vf58_C = [relaxtime_0_5_particleC_avg[-1], relaxtime_0_55_particleC_avg[-1],
          relaxtime_0_6_particleC_avg[-1], relaxtime_0_65_particleC_avg[-1],
          relaxtime_0_7_particleC_avg[-1], relaxtime_0_75_particleC_avg[-1],
          relaxtime_0_8_particleC_avg[-1], relaxtime_0_85_particleC_avg[-1],
          relaxtime_0_9_particleC_avg[-1], relaxtime_0_95_particleC_avg[-1],
          relaxtime_1_0_particleA_avg[-1],  relaxtime_1_05_particleA_avg[-1],
          relaxtime_1_1_particleC_avg[-1], relaxtime_1_125_particleC_avg[-1],
          relaxtime_1_15_particleC_avg[-1], relaxtime_1_175_particleC_avg[-1],
          relaxtime_1_2_particleB_avg[-1],  relaxtime_1_25_particleC_avg[-1],
          relaxtime_1_3_particleC_avg[-1], relaxtime_1_35_particleC_avg[-1],
          relaxtime_1_45_particleC_avg[-1],
          relaxtime_1_5_particleC_avg[-1],  relaxtime_1_8_particleC_avg[-1],
          relaxtime_1_particleC_avg[-1], relaxtime_2_particleC_avg[-1],
          relaxtime_3_particleC_avg[-1], relaxtime_4_particleC_avg[-1],
          relaxtime_5_particleC_avg[-1], relaxtime_6_particleC_avg[-1]]


data_vf58 = {'radius': radius, 
              'Particle A': vf58_A , 
              'Particle B': vf58_B , 
              'Particle C': vf58_C}

df_vf58  = pd.DataFrame (data_vf58)

fig_all = df_vf58.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, color='Green', label = 'R = 1.0')
df_vf58.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf58.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)

fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.58')
plt.show()
plt.close

fig_all = df_vf58.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, logx=True, color='Green', label = 'R = 1.0')
df_vf58.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf58.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)
plt.xlim(0.1, 10)
fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.58')
#plt.xlim([0.1, 10])

plt.show()
plt.close



#%%
# phi = 0.58


radius = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05,
          1.1, 1.125, 1.15, 1.175, 1.2, 1.25, 1.3, 1.35, 1.45, 1.5]

vf58_A = [relaxtime_0_5_particleA_avg[-1], relaxtime_0_55_particleA_avg[-1],
          relaxtime_0_6_particleA_avg[-1], relaxtime_0_65_particleA_avg[-1],
          relaxtime_0_7_particleA_avg[-1], relaxtime_0_75_particleA_avg[-1],
          relaxtime_0_8_particleA_avg[-1], relaxtime_0_85_particleA_avg[-1],
          relaxtime_0_9_particleA_avg[-1], relaxtime_0_95_particleA_avg[-1],
          relaxtime_1_0_particleA_avg[-1], relaxtime_1_05_particleA_avg[-1],
          relaxtime_1_1_particleA_avg[-1], relaxtime_1_125_particleA_avg[-1],
          relaxtime_1_15_particleA_avg[-1], relaxtime_1_175_particleA_avg[-1],
          relaxtime_1_2_particleA_avg[-1], relaxtime_1_25_particleA_avg[-1],
          relaxtime_1_3_particleA_avg[-1], relaxtime_1_35_particleA_avg[-1],
          relaxtime_1_45_particleA_avg[-1],
          relaxtime_1_5_particleA_avg[-1]]

vf58_B = [relaxtime_0_5_particleB_avg[-1], relaxtime_0_55_particleB_avg[-1],
          relaxtime_0_6_particleB_avg[-1], relaxtime_0_65_particleB_avg[-1],
          relaxtime_0_7_particleB_avg[-1], relaxtime_0_75_particleB_avg[-1],
          relaxtime_0_8_particleB_avg[-1], relaxtime_0_85_particleB_avg[-1],
          relaxtime_0_9_particleB_avg[-1], relaxtime_0_95_particleB_avg[-1],
          relaxtime_1_0_particleB_avg[-1], relaxtime_1_05_particleB_avg[-1],
          relaxtime_1_1_particleB_avg[-1], relaxtime_1_125_particleB_avg[-1],
          relaxtime_1_15_particleB_avg[-1], relaxtime_1_175_particleB_avg[-1],
          relaxtime_1_2_particleB_avg[-1], relaxtime_1_25_particleB_avg[-1],
          relaxtime_1_3_particleB_avg[-1], relaxtime_1_35_particleB_avg[-1],
          relaxtime_1_45_particleB_avg[-1],
          relaxtime_1_5_particleB_avg[-1]]

vf58_C = [relaxtime_0_5_particleC_avg[-1], relaxtime_0_55_particleC_avg[-1],
          relaxtime_0_6_particleC_avg[-1], relaxtime_0_65_particleC_avg[-1],
          relaxtime_0_7_particleC_avg[-1], relaxtime_0_75_particleC_avg[-1],
          relaxtime_0_8_particleC_avg[-1], relaxtime_0_85_particleC_avg[-1],
          relaxtime_0_9_particleC_avg[-1], relaxtime_0_95_particleC_avg[-1],
          relaxtime_1_0_particleA_avg[-1],  relaxtime_1_05_particleC_avg[-1],
          relaxtime_1_1_particleC_avg[-1], relaxtime_1_125_particleC_avg[-1],
          relaxtime_1_15_particleC_avg[-1], relaxtime_1_175_particleC_avg[-1],
          relaxtime_1_2_particleB_avg[-1],  relaxtime_1_25_particleC_avg[-1],
          relaxtime_1_3_particleC_avg[-1], relaxtime_1_35_particleC_avg[-1],
          relaxtime_1_45_particleC_avg[-1],
          relaxtime_1_5_particleC_avg[-1]]


data_vf58 = {'radius': radius, 
              'Particle A': vf58_A , 
              'Particle B': vf58_B , 
              'Particle C': vf58_C}

df_vf58  = pd.DataFrame (data_vf58)

fig_all = df_vf58.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, color='Green', label = 'R = 1.0')
df_vf58.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf58.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)

fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.58')
plt.show()
plt.close

fig_all = df_vf58.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, logx=True, color='Green', label = 'R = 1.0')
df_vf58.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf58.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)
#plt.xlim(0.2, 10)
fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.58')
plt.xlim([0.45, 2])

plt.show()
plt.close


#%%
# phi = 0.57


radius = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05,
          1.1, 1.125, 1.15, 1.175, 1.2, 1.25, 1.3, 1.35, 1.45, 1.5, 1.8, 
          2.0, 2.5, 3.0, 4.0, 5.0, 6.0]

vf57_A = [relaxtime_0_5_particleA_avg[-2], relaxtime_0_55_particleA_avg[-2],
          relaxtime_0_6_particleA_avg[-2], relaxtime_0_65_particleA_avg[-2],
          relaxtime_0_7_particleA_avg[-2], relaxtime_0_75_particleA_avg[-2],
          relaxtime_0_8_particleA_avg[-2], relaxtime_0_85_particleA_avg[-2],
          relaxtime_0_9_particleA_avg[-2], relaxtime_0_95_particleA_avg[-2],
          relaxtime_1_0_particleA_avg[-2], relaxtime_1_05_particleA_avg[-2], 
          relaxtime_1_1_particleA_avg[-2], relaxtime_1_125_particleA_avg[-2],
          relaxtime_1_15_particleA_avg[-2], relaxtime_1_175_particleA_avg[-2],
          relaxtime_1_2_particleA_avg[-2], relaxtime_1_25_particleA_avg[-2],
          relaxtime_1_3_particleA_avg[-2], relaxtime_1_35_particleA_avg[-2],
          relaxtime_1_45_particleA_avg[-2],
          relaxtime_1_5_particleA_avg[-2], relaxtime_1_8_particleA_avg[-2],
          relaxtime_1_particleA_avg[-2], relaxtime_2_particleA_avg[-2],
          relaxtime_3_particleA_avg[-2], relaxtime_4_particleA_avg[-2],
          relaxtime_5_particleA_avg[-2], relaxtime_6_particleA_avg[-2]]

vf57_B = [relaxtime_0_5_particleB_avg[-2], relaxtime_0_55_particleB_avg[-2],
          relaxtime_0_5_particleB_avg[-2], relaxtime_0_65_particleB_avg[-2],
          relaxtime_0_7_particleB_avg[-2], relaxtime_0_75_particleB_avg[-2],
          relaxtime_0_8_particleB_avg[-2], relaxtime_0_85_particleB_avg[-2],
          relaxtime_0_9_particleB_avg[-2], relaxtime_0_95_particleB_avg[-2],
          relaxtime_1_0_particleB_avg[-2], relaxtime_1_05_particleB_avg[-2],
          relaxtime_1_1_particleB_avg[-2], relaxtime_1_125_particleB_avg[-2], 
          relaxtime_1_15_particleB_avg[-2], relaxtime_1_175_particleB_avg[-2], 
          relaxtime_1_2_particleB_avg[-2], relaxtime_1_25_particleB_avg[-2], 
          relaxtime_1_3_particleB_avg[-2], relaxtime_1_35_particleB_avg[-2],
          relaxtime_1_45_particleB_avg[-2],
          relaxtime_1_5_particleB_avg[-2], relaxtime_1_8_particleB_avg[-2],
          relaxtime_1_particleB_avg[-2], relaxtime_2_particleB_avg[-2],
          relaxtime_3_particleB_avg[-2], relaxtime_4_particleB_avg[-2],
          relaxtime_5_particleB_avg[-2], relaxtime_6_particleB_avg[-2]]

vf57_C = [relaxtime_0_5_particleC_avg[-2], relaxtime_0_55_particleC_avg[-2],
          relaxtime_0_6_particleC_avg[-2], relaxtime_0_65_particleC_avg[-2],
          relaxtime_0_7_particleC_avg[-2], relaxtime_0_75_particleC_avg[-2],
          relaxtime_0_8_particleC_avg[-2], relaxtime_0_85_particleC_avg[-2],
          relaxtime_0_9_particleC_avg[-2], relaxtime_0_95_particleC_avg[-2],
          relaxtime_1_0_particleA_avg[-2],  relaxtime_1_05_particleC_avg[-2],
          relaxtime_1_1_particleC_avg[-2], relaxtime_1_125_particleC_avg[-2],
          relaxtime_1_15_particleC_avg[-2], relaxtime_1_175_particleC_avg[-2],
          relaxtime_1_2_particleB_avg[-2], relaxtime_1_25_particleC_avg[-2],
          relaxtime_1_3_particleC_avg[-2], relaxtime_1_35_particleC_avg[-2],
          relaxtime_1_45_particleC_avg[-2],
          relaxtime_1_5_particleC_avg[-2],  relaxtime_1_8_particleC_avg[-2],
          relaxtime_1_particleC_avg[-2], relaxtime_2_particleC_avg[-2],
          relaxtime_3_particleC_avg[-2], relaxtime_4_particleC_avg[-2],
          relaxtime_5_particleC_avg[-2], relaxtime_6_particleC_avg[-2]]


data_vf57 = {'radius': radius, 
              'Particle A': vf57_A , 
              'Particle B': vf57_B , 
              'Particle C': vf57_C}

df_vf57  = pd.DataFrame (data_vf57)

fig_all = df_vf57.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, color='Green', label = 'R = 1.0')
df_vf57.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf57.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)

fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.57')
plt.show()
plt.close

fig_all = df_vf58.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, logx=True, color='Green', label = 'R = 1.0')
df_vf58.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf58.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)
plt.xlim(0.2, 10)
fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.57')
#plt.xlim([0.1, 10])

plt.show()
plt.close


#%%
# phi = 0.57


radius = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05,
          1.1, 1.125, 1.15, 1.175, 1.2, 1.25, 1.3, 1.35, 1.45, 1.5]

vf57_A = [relaxtime_0_5_particleA_avg[-2], relaxtime_0_55_particleA_avg[-2],
          relaxtime_0_6_particleA_avg[-2], relaxtime_0_65_particleA_avg[-2],
          relaxtime_0_7_particleA_avg[-2], relaxtime_0_75_particleA_avg[-2],
          relaxtime_0_8_particleA_avg[-2], relaxtime_0_85_particleA_avg[-2],
          relaxtime_0_9_particleA_avg[-2], relaxtime_0_95_particleA_avg[-2],
          relaxtime_1_0_particleA_avg[-2], relaxtime_1_05_particleA_avg[-2], 
          relaxtime_1_1_particleA_avg[-2], relaxtime_1_125_particleA_avg[-2],
          relaxtime_1_15_particleA_avg[-2], relaxtime_1_175_particleA_avg[-2],
          relaxtime_1_2_particleA_avg[-2], relaxtime_1_25_particleA_avg[-2],
          relaxtime_1_3_particleA_avg[-2], relaxtime_1_35_particleA_avg[-2],
          relaxtime_1_45_particleA_avg[-2],
          relaxtime_1_5_particleA_avg[-2]]

vf57_B = [relaxtime_0_5_particleB_avg[-2], relaxtime_0_55_particleB_avg[-2],
          relaxtime_0_5_particleB_avg[-2], relaxtime_0_65_particleB_avg[-2],
          relaxtime_0_7_particleB_avg[-2], relaxtime_0_75_particleB_avg[-2],
          relaxtime_0_8_particleB_avg[-2], relaxtime_0_85_particleB_avg[-2],
          relaxtime_0_9_particleB_avg[-2], relaxtime_0_95_particleB_avg[-2],
          relaxtime_1_0_particleB_avg[-2], relaxtime_1_05_particleB_avg[-2],
          relaxtime_1_1_particleB_avg[-2], relaxtime_1_125_particleB_avg[-2], 
          relaxtime_1_15_particleB_avg[-2], relaxtime_1_175_particleB_avg[-2], 
          relaxtime_1_2_particleB_avg[-2], relaxtime_1_25_particleB_avg[-2], 
          relaxtime_1_3_particleB_avg[-2], relaxtime_1_35_particleB_avg[-2],
          relaxtime_1_45_particleB_avg[-2],
          relaxtime_1_5_particleB_avg[-2]]

vf57_C = [relaxtime_0_5_particleC_avg[-2], relaxtime_0_55_particleC_avg[-2],
          relaxtime_0_6_particleC_avg[-2], relaxtime_0_65_particleC_avg[-2],
          relaxtime_0_7_particleC_avg[-2], relaxtime_0_75_particleC_avg[-2],
          relaxtime_0_8_particleC_avg[-2], relaxtime_0_85_particleC_avg[-2],
          relaxtime_0_9_particleC_avg[-2], relaxtime_0_95_particleC_avg[-2],
          relaxtime_1_0_particleA_avg[-2],  relaxtime_1_05_particleC_avg[-2],
          relaxtime_1_1_particleC_avg[-2], relaxtime_1_125_particleC_avg[-2],
          relaxtime_1_15_particleC_avg[-2], relaxtime_1_175_particleC_avg[-2],
          relaxtime_1_2_particleB_avg[-2], relaxtime_1_25_particleC_avg[-2],
          relaxtime_1_3_particleC_avg[-2], relaxtime_1_35_particleC_avg[-2],
          relaxtime_1_45_particleC_avg[-2],
          relaxtime_1_5_particleC_avg[-2]]


data_vf57 = {'radius': radius, 
              'Particle A': vf57_A , 
              'Particle B': vf57_B , 
              'Particle C': vf57_C}

df_vf57  = pd.DataFrame (data_vf57)

fig_all = df_vf57.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, color='Green', label = 'R = 1.0')
df_vf57.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf57.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)

fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.57')
plt.show()
plt.close

fig_all = df_vf58.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, logx=True, color='Green', label = 'R = 1.0')
df_vf58.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf58.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)
plt.xlim(0.2, 10)
fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.57')
#plt.xlim([0.1, 10])

plt.show()
plt.close


#%%
# phi = 0.55


radius = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05,
          1.1, 1.125, 1.15, 1.175, 1.2, 1.25, 1.3, 1.35, 1.45, 1.5, 1.8, 
          2.0, 2.5, 3.0, 4.0, 5.0, 6.0]

vf55_A = [relaxtime_0_5_particleA_avg[-3], relaxtime_0_55_particleA_avg[-3],
          relaxtime_0_6_particleA_avg[-3], relaxtime_0_65_particleA_avg[-3],
          relaxtime_0_7_particleA_avg[-3], relaxtime_0_75_particleA_avg[-3],
          relaxtime_0_8_particleA_avg[-3], relaxtime_0_85_particleA_avg[-3],
          relaxtime_0_9_particleA_avg[-3], relaxtime_0_95_particleA_avg[-3],
          relaxtime_1_0_particleA_avg[-3], relaxtime_1_05_particleA_avg[-3], 
          relaxtime_1_1_particleA_avg[-3], relaxtime_1_125_particleA_avg[-3], 
          relaxtime_1_15_particleA_avg[-3], relaxtime_1_175_particleA_avg[-3], 
          relaxtime_1_2_particleA_avg[-3], relaxtime_1_25_particleA_avg[-3],
          relaxtime_1_3_particleA_avg[-3], relaxtime_1_35_particleA_avg[-3],
          relaxtime_1_45_particleA_avg[-3],
          relaxtime_1_5_particleA_avg[-3], relaxtime_1_8_particleA_avg[-3],
          relaxtime_1_particleA_avg[-3], relaxtime_2_particleA_avg[-3],
          relaxtime_3_particleA_avg[-3], relaxtime_4_particleA_avg[-3],
          relaxtime_5_particleA_avg[-3], relaxtime_6_particleA_avg[-3]]

vf55_B = [relaxtime_0_5_particleB_avg[-3], relaxtime_0_55_particleB_avg[-3],
          relaxtime_0_6_particleB_avg[-3], relaxtime_0_65_particleB_avg[-3],
          relaxtime_0_7_particleB_avg[-3], relaxtime_0_75_particleB_avg[-3],
          relaxtime_0_8_particleB_avg[-3], relaxtime_0_85_particleB_avg[-3],
          relaxtime_0_9_particleB_avg[-3], relaxtime_0_95_particleB_avg[-3],
          relaxtime_1_0_particleB_avg[-3], relaxtime_1_05_particleB_avg[-3],
          relaxtime_1_1_particleB_avg[-3], relaxtime_1_125_particleB_avg[-3],
          relaxtime_1_15_particleB_avg[-3], relaxtime_1_175_particleB_avg[-3],
          relaxtime_1_2_particleB_avg[-3], relaxtime_1_25_particleB_avg[-3],
          relaxtime_1_3_particleB_avg[-3], relaxtime_1_35_particleB_avg[-3],
          relaxtime_1_45_particleB_avg[-3],
          relaxtime_1_5_particleB_avg[-3], relaxtime_1_8_particleB_avg[-3],
          relaxtime_1_particleB_avg[-3], relaxtime_2_particleB_avg[-3],
          relaxtime_3_particleB_avg[-3], relaxtime_4_particleB_avg[-3],
          relaxtime_5_particleB_avg[-3], relaxtime_6_particleB_avg[-3]]

vf55_C = [relaxtime_0_5_particleC_avg[-3], relaxtime_0_55_particleC_avg[-3],
          relaxtime_0_6_particleC_avg[-3], relaxtime_0_65_particleC_avg[-3],
          relaxtime_0_7_particleC_avg[-3], relaxtime_0_75_particleC_avg[-3],
          relaxtime_0_8_particleC_avg[-3], relaxtime_0_85_particleC_avg[-3],
          relaxtime_0_9_particleC_avg[-3], relaxtime_0_95_particleC_avg[-3],
          relaxtime_1_0_particleA_avg[-3], relaxtime_1_05_particleC_avg[-3],
          relaxtime_1_1_particleC_avg[-3], relaxtime_1_125_particleC_avg[-3],
          relaxtime_1_15_particleC_avg[-3], relaxtime_1_175_particleC_avg[-3],
          relaxtime_1_2_particleB_avg[-3],  relaxtime_1_25_particleC_avg[-3],
          relaxtime_1_3_particleC_avg[-3], relaxtime_1_35_particleC_avg[-3],
          relaxtime_1_45_particleC_avg[-3],
          relaxtime_1_5_particleC_avg[-3],  relaxtime_1_8_particleC_avg[-3],
          relaxtime_1_particleC_avg[-3], relaxtime_2_particleC_avg[-3],
          relaxtime_3_particleC_avg[-3], relaxtime_4_particleC_avg[-3],
          relaxtime_5_particleC_avg[-3], relaxtime_6_particleC_avg[-3]]


data_vf55 = {'radius': radius, 
              'Particle A': vf55_A , 
              'Particle B': vf55_B , 
              'Particle C': vf55_C}

df_vf55  = pd.DataFrame (data_vf55)

fig_all = df_vf55.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, color='Green', label = 'R = 1.0')
df_vf55.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf55.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)

fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.55')
plt.show()
plt.close

fig_all = df_vf58.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, logx=True, color='Green', label = 'R = 1.0')
df_vf58.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf58.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)
plt.xlim(0.2, 10)
fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.55')
#plt.xlim([0.1, 10])

plt.show()
plt.close

#%%
# phi = 0.55


radius = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05,
          1.1, 1.125, 1.15, 1.175, 1.2, 1.25, 1.3, 1.35, 1.45, 1.5]

vf55_A = [relaxtime_0_5_particleA_avg[-3], relaxtime_0_55_particleA_avg[-3],
          relaxtime_0_6_particleA_avg[-3], relaxtime_0_65_particleA_avg[-3],
          relaxtime_0_7_particleA_avg[-3], relaxtime_0_75_particleA_avg[-3],
          relaxtime_0_8_particleA_avg[-3], relaxtime_0_85_particleA_avg[-3],
          relaxtime_0_9_particleA_avg[-3], relaxtime_0_95_particleA_avg[-3],
          relaxtime_1_0_particleA_avg[-3], relaxtime_1_05_particleA_avg[-3], 
          relaxtime_1_1_particleA_avg[-3], relaxtime_1_125_particleA_avg[-3], 
          relaxtime_1_15_particleA_avg[-3], relaxtime_1_175_particleA_avg[-3], 
          relaxtime_1_2_particleA_avg[-3], relaxtime_1_25_particleA_avg[-3],
          relaxtime_1_3_particleA_avg[-3], relaxtime_1_35_particleA_avg[-3],
          relaxtime_1_45_particleA_avg[-3],
          relaxtime_1_5_particleA_avg[-3]]

vf55_B = [relaxtime_0_5_particleB_avg[-3], relaxtime_0_55_particleB_avg[-3],
          relaxtime_0_6_particleB_avg[-3], relaxtime_0_65_particleB_avg[-3],
          relaxtime_0_7_particleB_avg[-3], relaxtime_0_75_particleB_avg[-3],
          relaxtime_0_8_particleB_avg[-3], relaxtime_0_85_particleB_avg[-3],
          relaxtime_0_9_particleB_avg[-3], relaxtime_0_95_particleB_avg[-3],
          relaxtime_1_0_particleB_avg[-3], relaxtime_1_05_particleB_avg[-3],
          relaxtime_1_1_particleB_avg[-3], relaxtime_1_125_particleB_avg[-3],
          relaxtime_1_15_particleB_avg[-3], relaxtime_1_175_particleB_avg[-3],
          relaxtime_1_2_particleB_avg[-3], relaxtime_1_25_particleB_avg[-3],
          relaxtime_1_3_particleB_avg[-3], relaxtime_1_35_particleB_avg[-3],
          relaxtime_1_45_particleB_avg[-3],
          relaxtime_1_5_particleB_avg[-3]]

vf55_C = [relaxtime_0_5_particleC_avg[-3], relaxtime_0_55_particleC_avg[-3],
          relaxtime_0_6_particleC_avg[-3], relaxtime_0_65_particleC_avg[-3],
          relaxtime_0_7_particleC_avg[-3], relaxtime_0_75_particleC_avg[-3],
          relaxtime_0_8_particleC_avg[-3], relaxtime_0_85_particleC_avg[-3],
          relaxtime_0_9_particleC_avg[-3], relaxtime_0_95_particleC_avg[-3],
          relaxtime_1_0_particleA_avg[-3], relaxtime_1_05_particleC_avg[-3],
          relaxtime_1_1_particleC_avg[-3], relaxtime_1_125_particleC_avg[-3],
          relaxtime_1_15_particleC_avg[-3], relaxtime_1_175_particleC_avg[-3],
          relaxtime_1_2_particleB_avg[-3],  relaxtime_1_25_particleC_avg[-3],
          relaxtime_1_3_particleC_avg[-3], relaxtime_1_35_particleC_avg[-3],
          relaxtime_1_45_particleC_avg[-3],
          relaxtime_1_5_particleC_avg[-3]]


data_vf55 = {'radius': radius, 
              'Particle A': vf55_A , 
              'Particle B': vf55_B , 
              'Particle C': vf55_C}

df_vf55  = pd.DataFrame (data_vf55)

fig_all = df_vf55.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, color='Green', label = 'R = 1.0')
df_vf55.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf55.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)

fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.55')
plt.show()
plt.close

fig_all = df_vf58.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, logx=True, color='Green', label = 'R = 1.0')
df_vf58.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf58.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)
plt.xlim(0.2, 10)
fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.55')
#plt.xlim([0.1, 10])

plt.show()
plt.close
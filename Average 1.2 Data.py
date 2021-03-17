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

relaxtime_0_5_radii = [1.0, 1.2, 0.5]

relaxtime_0_5_rA = 1.0
relaxtime_0_5_rB = 1.2
relaxtime_0_5_rC = 0.5

relaxtime_0_5_particleA = np.array([26.474018301531352, 41.155055388008279, 56.630317268511099])
relaxtime_0_5_particleA[:] = [x/(relaxtime_0_5_rA**2) for x in relaxtime_0_5_particleA]

relaxtime_0_5_particleB = np.array([374.72793485352400, 1104.4258091511556, 2087.9735971614996])
relaxtime_0_5_particleB[:] = [x/(relaxtime_0_5_rB**2) for x in relaxtime_0_5_particleB]

relaxtime_0_5_particleC = np.array([52.657563473842416, 144.68060091362793, 281.52385017515525])
relaxtime_0_5_particleC[:] = [x/(relaxtime_0_5_rC**2) for x in relaxtime_0_5_particleC]

relaxtime_0_5_particleA_rep1 = np.array([26.315917743192479, 42.114376688347832, 54.635177181537884])
relaxtime_0_5_particleA_rep1[:] = np.array([x/(relaxtime_0_5_rA**2) for x in relaxtime_0_5_particleA_rep1])

relaxtime_0_5_particleB_rep1 = np.array([367.99495826079539, 979.67642015245815, 2103.6897021200266])
relaxtime_0_5_particleB_rep1[:] = [x/(relaxtime_0_5_rB**2) for x in relaxtime_0_5_particleB_rep1]

relaxtime_0_5_particleC_rep1 = np.array([52.554205399373039, 136.18309155199148, 287.22278196462321])
relaxtime_0_5_particleC_rep1[:] = [x/(relaxtime_0_5_rC**2) for x in relaxtime_0_5_particleC_rep1]

relaxtime_0_5_particleA_rep2 = np.array([26.428918516133560, 40.760766359465862, 56.172977157228800])
relaxtime_0_5_particleA_rep2[:] = [x/(relaxtime_0_5_rA**2) for x in relaxtime_0_5_particleA_rep2]

relaxtime_0_5_particleB_rep2 = np.array([367.27814924992077, 1084.3035622823429, 2058.8471548216648])
relaxtime_0_5_particleB_rep2[:] = [x/(relaxtime_0_5_rB**2) for x in relaxtime_0_5_particleB_rep2]

relaxtime_0_5_particleC_rep2 = np.array([52.694360943046846, 147.69008616713990, 260.45213385796308])
relaxtime_0_5_particleC_rep2[:] = [x/(relaxtime_0_5_rC**2) for x in relaxtime_0_5_particleC_rep2]

a = [relaxtime_0_5_particleA, relaxtime_0_5_particleA_rep1, relaxtime_0_5_particleA_rep2]
b = [relaxtime_0_5_particleB, relaxtime_0_5_particleB_rep1, relaxtime_0_5_particleB_rep2]
c = [relaxtime_0_5_particleC, relaxtime_0_5_particleC_rep1, relaxtime_0_5_particleC_rep2]

relaxtime_0_5_particleA_avg = np.mean(a, axis=0)
relaxtime_0_5_particleB_avg = np.mean(b, axis=0)
relaxtime_0_5_particleC_avg = np.mean(c, axis=0)


#%%

phi = [0.55, 0.57, 0.58]

relaxtime_0_6_radii = [1.0, 1.2, 0.6]

relaxtime_0_6_rA = 1.0
relaxtime_0_6_rB = 1.2
relaxtime_0_6_rC = 0.6

relaxtime_0_6_particleA = np.array([47.573502739187319, 93.525177308599069, 150.72081826664061])
relaxtime_0_6_particleA[:] = [x/(relaxtime_0_6_rA**2) for x in relaxtime_0_6_particleA]

relaxtime_0_6_particleB = np.array([382.26731233037924, 1186.8490639707654, 2855.4610190113126])
relaxtime_0_6_particleB[:] = [x/(relaxtime_0_6_rB**2) for x in relaxtime_0_6_particleB]

relaxtime_0_6_particleC = np.array([103.12220347160449, 316.57134747522366, 699.20102582327343])
relaxtime_0_6_particleC[:] = [x/(relaxtime_0_6_rC**2) for x in relaxtime_0_6_particleC]

relaxtime_0_6_particleA_rep1 = np.array([47.438182789021134, 96.679430533558346,158.32926478287627 ])
relaxtime_0_6_particleA_rep1[:] = [x/(relaxtime_0_6_rA**2) for x in relaxtime_0_6_particleA_rep1]

relaxtime_0_6_particleB_rep1 = np.array([376.65710434717147, 1114.5799461730010, 2393.3084472927462])
relaxtime_0_6_particleB_rep1[:] = [x/(relaxtime_0_6_rB**2) for x in relaxtime_0_6_particleB_rep1]

relaxtime_0_6_particleC_rep1 = np.array([103.73698161379077, 311.15955445491102, 651.11616086407787])
relaxtime_0_6_particleC_rep1[:] = [x/(relaxtime_0_6_rC**2) for x in relaxtime_0_6_particleC_rep1]

relaxtime_0_6_particleA_rep2 = np.array([47.685698532435403, 92.817689010928007, 146.24995645947922])
relaxtime_0_6_particleA_rep2[:] = [x/(relaxtime_0_6_rA**2) for x in relaxtime_0_6_particleA_rep2]

relaxtime_0_6_particleB_rep2 = np.array([386.48223698769664, 1163.6423209127122, 2483.9173059181853])
relaxtime_0_6_particleB_rep2[:] = [x/(relaxtime_0_6_rB**2) for x in relaxtime_0_6_particleB_rep2]

relaxtime_0_6_particleC_rep2 = np.array([101.43279188782741, 315.34795285130764, 656.99411462452258])
relaxtime_0_6_particleC_rep2[:] = [x/(relaxtime_0_6_rC**2) for x in relaxtime_0_6_particleC_rep2]

a = [relaxtime_0_6_particleA, relaxtime_0_6_particleA_rep1, relaxtime_0_6_particleA_rep2]
b = [relaxtime_0_6_particleB, relaxtime_0_6_particleB_rep1, relaxtime_0_6_particleB_rep2]
c = [relaxtime_0_6_particleC, relaxtime_0_6_particleC_rep1, relaxtime_0_6_particleC_rep2]

relaxtime_0_6_particleA_avg = np.mean(a, axis=0)
relaxtime_0_6_particleB_avg = np.mean(b, axis=0)
relaxtime_0_6_particleC_avg = np.mean(c, axis=0)



#%%
phi = [0.55, 0.57, 0.58]


relaxtime_0_7_rA = 1.0
relaxtime_0_7_rB = 1.2
relaxtime_0_7_rC = 0.7


relaxtime_0_7_particleA = np.array([83.147556262440204, 215.56743087557388, 409.29313565937872])
relaxtime_0_7_particleA[:] = [x/(relaxtime_0_7_rA**2) for x in relaxtime_0_7_particleA]

relaxtime_0_7_particleB = np.array([404.32228753383072, 1318.9123653728834, 3147.4093992167509])
relaxtime_0_7_particleB[:] = [x/(relaxtime_0_7_rB**2) for x in relaxtime_0_7_particleB]

relaxtime_0_7_particleC = np.array([170.88342007336084, 591.98998807896533, 1582.6700111267328])
relaxtime_0_7_particleC[:] = [x/(relaxtime_0_7_rC**2) for x in relaxtime_0_7_particleC]

relaxtime_0_7_particleA_rep1 = np.array([83.332175581332791, 201.92272656938150, 414.33633719283625])
relaxtime_0_7_particleA_rep1[:] = [x/(relaxtime_0_7_rA**2) for x in relaxtime_0_7_particleA_rep1]

relaxtime_0_7_particleB_rep1 = np.array([394.50893306466924, 1415.7666691479935, 3685.4809362150249])
relaxtime_0_7_particleB_rep1[:] = [x/(relaxtime_0_7_rB**2) for x in relaxtime_0_7_particleB_rep1]

relaxtime_0_7_particleC_rep1 = np.array([171.98113345176040, 640.43900521030116, 1563.4244924163297])
relaxtime_0_7_particleC_rep1[:] = [x/(relaxtime_0_7_rC**2) for x in relaxtime_0_7_particleC_rep1]

relaxtime_0_7_particleA_rep2 = np.array([84.841255934065515, 208.60239809899005, 421.40141389854637])
relaxtime_0_7_particleA_rep2[:] = [x/(relaxtime_0_7_rA**2) for x in relaxtime_0_7_particleA_rep2]

relaxtime_0_7_particleB_rep2 = np.array([425.89225117459057, 1444.9047660371900, 3263.2364134645486])
relaxtime_0_7_particleB_rep2[:] = [x/(relaxtime_0_7_rB**2) for x in relaxtime_0_7_particleB_rep2]

relaxtime_0_7_particleC_rep2 = np.array([182.69625235370205, 635.80328868815764, 1438.5494995002646])
relaxtime_0_7_particleC_rep2[:] = [x/(relaxtime_0_7_rC**2) for x in relaxtime_0_7_particleC_rep2]


a = [relaxtime_0_7_particleA, relaxtime_0_7_particleA_rep1, relaxtime_0_7_particleA_rep2]
b = [relaxtime_0_7_particleB, relaxtime_0_7_particleB_rep1, relaxtime_0_7_particleB_rep2]
c = [relaxtime_0_7_particleC, relaxtime_0_7_particleC_rep1, relaxtime_0_7_particleC_rep2]

relaxtime_0_7_particleA_avg = np.mean(a, axis=0)
relaxtime_0_7_particleB_avg = np.mean(b, axis=0)
relaxtime_0_7_particleC_avg = np.mean(c, axis=0)


#%%
phi = [0.55, 0.57, 0.58]

relaxtime_0_8_radii = [1.0, 1.2, 0.8]

relaxtime_0_8_rA = 1.0
relaxtime_0_8_rB = 1.2
relaxtime_0_8_rC = 0.8

relaxtime_0_8_particleA = np.array([142.89208528309322, 460.48195425514513, 963.71346059001519])
relaxtime_0_8_particleA[:] = [x/(relaxtime_0_8_rA**2) for x in relaxtime_0_8_particleA]

relaxtime_0_8_particleB = np.array([463.58986809729822, 1817.2172693906641, 4676.5006380255118])
relaxtime_0_8_particleB[:] = [x/(relaxtime_0_8_rB**2) for x in relaxtime_0_8_particleB]

relaxtime_0_8_particleC = np.array([284.50064051210376, 1115.2690416718597, 3187.3028066557172])
relaxtime_0_8_particleC[:] = [x/(relaxtime_0_8_rC**2) for x in relaxtime_0_8_particleC]

relaxtime_0_8_particleA_rep1 = np.array([141.56125916204979, 488.06252171963706, 936.87526621878214])
relaxtime_0_8_particleA_rep1[:] = [x/(relaxtime_0_8_rA**2) for x in relaxtime_0_8_particleA_rep1]

relaxtime_0_8_particleB_rep1 = np.array([472.07633393470167, 2241.5595677217011, 3900.6994458512759])
relaxtime_0_8_particleB_rep1[:] = [x/(relaxtime_0_8_rB**2) for x in relaxtime_0_8_particleB_rep1]

relaxtime_0_8_particleC_rep1 = np.array([281.98236940986595, 1257.3729061882250, 2321.5382123352697])
relaxtime_0_8_particleC_rep1[:] = [x/(relaxtime_0_8_rC**2) for x in relaxtime_0_8_particleC_rep1]

relaxtime_0_8_particleA_rep2 = np.array([144.03434161664259, 483.09119191812960, 1072.5719516388247])
relaxtime_0_8_particleA_rep2[:] = [x/(relaxtime_0_8_rA**2) for x in relaxtime_0_8_particleA_rep2]

relaxtime_0_8_particleB_rep2 = np.array([484.61765270971330, 1849.0668069491996, 4303.3559835390042])
relaxtime_0_8_particleB_rep2[:] = [x/(relaxtime_0_8_rB**2) for x in relaxtime_0_8_particleB_rep2]

relaxtime_0_8_particleC_rep2 = np.array([290.24452043671278, 1233.9514062259534, 2446.3846755060945])
relaxtime_0_8_particleC_rep2[:] = [x/(relaxtime_0_8_rC**2) for x in relaxtime_0_8_particleC_rep2]


a = [relaxtime_0_8_particleA, relaxtime_0_8_particleA_rep1, relaxtime_0_8_particleA_rep2]
b = [relaxtime_0_8_particleB, relaxtime_0_8_particleB_rep1, relaxtime_0_8_particleB_rep2]
c = [relaxtime_0_8_particleC, relaxtime_0_8_particleC_rep1, relaxtime_0_8_particleC_rep2]

relaxtime_0_8_particleA_avg = np.mean(a, axis=0)
relaxtime_0_8_particleB_avg = np.mean(b, axis=0)
relaxtime_0_8_particleC_avg = np.mean(c, axis=0)

#%%
phi = [0.55, 0.57, 0.58]

relaxtime_0_9_rA = 1.0
relaxtime_0_9_rB = 1.2
relaxtime_0_9_rC = 0.9


relaxtime_0_9_particleA = np.array([243.99812425497629, 1002.3332662541537, 2317.5806596408170])
relaxtime_0_9_particleA[:] = [x/(relaxtime_0_9_rA**2) for x in relaxtime_0_9_particleA]

relaxtime_0_9_particleB= np.array([518.97113862246556, 2496.8724456313225, 5211.1081572863804])
relaxtime_0_9_particleB[:] = [x/(relaxtime_0_9_rB**2) for x in relaxtime_0_9_particleB]

relaxtime_0_9_particleC = np.array([423.71737566335196, 2097.2353730403352, 4854.7344872869544])
relaxtime_0_9_particleC[:] = [x/(relaxtime_0_9_rC**2) for x in relaxtime_0_9_particleC]


relaxtime_0_9_particleA_rep1 = np.array([241.45005929330065, 879.30620078504796, 1924.6719812854235])
relaxtime_0_9_particleA_rep1[:] = [x/(relaxtime_0_9_rA**2) for x in relaxtime_0_9_particleA_rep1]

relaxtime_0_9_particleB_rep1 = np.array([540.14492604524787, 2123.4328828682542, 4965.0681327751145])
relaxtime_0_9_particleB_rep1[:] = [x/(relaxtime_0_9_rB**2) for x in relaxtime_0_9_particleB_rep1]

relaxtime_0_9_particleC_rep1 = np.array([448.30047082083786, 1829.4025549224173, 4011.5321642946496])
relaxtime_0_9_particleC_rep1[:] = [x/(relaxtime_0_9_rC**2) for x in relaxtime_0_9_particleC_rep1]


relaxtime_0_9_particleA_rep2 = np.array([236.46591401655030, 1099.2182670918717, 2200.4567322499875])
relaxtime_0_9_particleA_rep2[:] = [x/(relaxtime_0_9_rA**2) for x in relaxtime_0_9_particleA_rep2]

relaxtime_0_9_particleB_rep2 = np.array([522.08169332443083, 2812.3854898259365, 5518.6207079391543])
relaxtime_0_9_particleB_rep2[:] = [x/(relaxtime_0_9_rB**2) for x in relaxtime_0_9_particleB_rep2]

relaxtime_0_9_particleC_rep2 = np.array([421.17798795977876, 2709.5605508238573, 4381.2400908074305])
relaxtime_0_9_particleC_rep2[:] = [x/(relaxtime_0_9_rC**2) for x in relaxtime_0_9_particleC_rep2]


a = [relaxtime_0_9_particleA, relaxtime_0_9_particleA_rep1, relaxtime_0_9_particleA_rep2]
b = [relaxtime_0_9_particleB, relaxtime_0_9_particleB_rep1, relaxtime_0_9_particleB_rep2]
c = [relaxtime_0_9_particleC, relaxtime_0_9_particleC_rep1, relaxtime_0_9_particleC_rep2]

relaxtime_0_9_particleA_avg = np.mean(a, axis=0)
relaxtime_0_9_particleB_avg = np.mean(b, axis=0)
relaxtime_0_9_particleC_avg = np.mean(c, axis=0)


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

ratio4 = [i / j for i, j in zip(relaxtime_4_particleC_avg,relaxtime_4_particleB_avg)] 
print(ratio4)

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


radius = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.5, 1.8, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0]

vf58_A = [relaxtime_0_5_particleA_avg[-1],  relaxtime_0_6_particleA_avg[-1], relaxtime_0_7_particleA_avg[-1],
          relaxtime_0_8_particleA_avg[-1],  relaxtime_0_9_particleA_avg[-1],
          relaxtime_1_0_particleA_avg[-1], relaxtime_1_1_particleA_avg[-1], 
          relaxtime_1_2_particleA_avg[-1], relaxtime_1_3_particleA_avg[-1],
          relaxtime_1_5_particleA_avg[-1], relaxtime_1_8_particleA_avg[-1],
          relaxtime_1_particleA_avg[-1], relaxtime_2_particleA_avg[-1],
          relaxtime_3_particleA_avg[-1], relaxtime_4_particleA_avg[-1],
          relaxtime_5_particleA_avg[-1], relaxtime_6_particleA_avg[-1]]

vf58_B = [relaxtime_0_5_particleB_avg[-1], relaxtime_0_6_particleB_avg[-1], relaxtime_0_7_particleB_avg[-1],
          relaxtime_0_8_particleB_avg[-1],  relaxtime_0_9_particleB_avg[-1],
          relaxtime_1_0_particleB_avg[-1], relaxtime_1_1_particleB_avg[-1], 
          relaxtime_1_2_particleB_avg[-1], relaxtime_1_3_particleB_avg[-1],
          relaxtime_1_5_particleB_avg[-1], relaxtime_1_8_particleB_avg[-1],
          relaxtime_1_particleB_avg[-1], relaxtime_2_particleB_avg[-1],
          relaxtime_3_particleB_avg[-1], relaxtime_4_particleB_avg[-1],
          relaxtime_5_particleB_avg[-1], relaxtime_6_particleB_avg[-1]]

vf58_C = [relaxtime_0_5_particleC_avg[-1], relaxtime_0_6_particleC_avg[-1], relaxtime_0_7_particleC_avg[-1],
          relaxtime_0_8_particleC_avg[-1],  relaxtime_0_9_particleC_avg[-1],
          relaxtime_1_0_particleA_avg[-1],  relaxtime_1_1_particleC_avg[-1], 
          relaxtime_1_2_particleB_avg[-1],  relaxtime_1_3_particleC_avg[-1],
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
plt.xlim(0.2, 10)
fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius| rrr = r**2 | n=3 | phi=0.58')
#plt.xlim([0.1, 10])

plt.show()
plt.close


#%%
# phi = 0.57


radius = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.5, 1.8, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0]

vf57_A = [relaxtime_0_5_particleA_avg[-2], relaxtime_0_6_particleA_avg[-2], relaxtime_0_7_particleA_avg[-2],
          relaxtime_0_8_particleA_avg[-2],  relaxtime_0_9_particleA_avg[-2],
          relaxtime_1_0_particleA_avg[-2], relaxtime_1_1_particleA_avg[-2], 
          relaxtime_1_2_particleA_avg[-2], relaxtime_1_3_particleA_avg[-2],
          relaxtime_1_5_particleA_avg[-2], relaxtime_1_8_particleA_avg[-2],
          relaxtime_1_particleA_avg[-2], relaxtime_2_particleA_avg[-2],
          relaxtime_3_particleA_avg[-2], relaxtime_4_particleA_avg[-2],
          relaxtime_5_particleA_avg[-2], relaxtime_6_particleA_avg[-2]]

vf57_B = [relaxtime_0_5_particleB_avg[-2], relaxtime_0_6_particleB_avg[-2], relaxtime_0_7_particleB_avg[-2],
          relaxtime_0_8_particleB_avg[-2],  relaxtime_0_9_particleB_avg[-2],
          relaxtime_1_0_particleB_avg[-2], relaxtime_1_1_particleB_avg[-2], 
          relaxtime_1_2_particleB_avg[-2], relaxtime_1_3_particleB_avg[-2],
          relaxtime_1_5_particleB_avg[-2], relaxtime_1_8_particleB_avg[-2],
          relaxtime_1_particleB_avg[-2], relaxtime_2_particleB_avg[-2],
          relaxtime_3_particleB_avg[-2], relaxtime_4_particleB_avg[-2],
          relaxtime_5_particleB_avg[-2], relaxtime_6_particleB_avg[-2]]

vf57_C = [relaxtime_0_5_particleC_avg[-2], relaxtime_0_6_particleC_avg[-2], relaxtime_0_7_particleC_avg[-2],
          relaxtime_0_8_particleC_avg[-2],  relaxtime_0_9_particleC_avg[-2],
          relaxtime_1_0_particleA_avg[-2],  relaxtime_1_1_particleC_avg[-2], 
          relaxtime_1_2_particleB_avg[-2],  relaxtime_1_3_particleC_avg[-2],
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
# phi = 0.55


radius = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.5, 1.8, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0]

vf55_A = [relaxtime_0_5_particleA_avg[-3],  relaxtime_0_6_particleA_avg[-3], relaxtime_0_7_particleA_avg[-3],
          relaxtime_0_8_particleA_avg[-3],  relaxtime_0_9_particleA_avg[-3],
          relaxtime_1_0_particleA_avg[-3], relaxtime_1_1_particleA_avg[-3], 
          relaxtime_1_2_particleA_avg[-3], relaxtime_1_3_particleA_avg[-3],
          relaxtime_1_5_particleA_avg[-3], relaxtime_1_8_particleA_avg[-3],
          relaxtime_1_particleA_avg[-3], relaxtime_2_particleA_avg[-3],
          relaxtime_3_particleA_avg[-3], relaxtime_4_particleA_avg[-3],
          relaxtime_5_particleA_avg[-3], relaxtime_6_particleA_avg[-3]]

vf55_B = [relaxtime_0_5_particleB_avg[-3],  relaxtime_0_6_particleB_avg[-3],relaxtime_0_7_particleB_avg[-3],
          relaxtime_0_8_particleB_avg[-3],  relaxtime_0_9_particleB_avg[-3],
          relaxtime_1_0_particleB_avg[-3], relaxtime_1_1_particleB_avg[-3], 
          relaxtime_1_2_particleB_avg[-3], relaxtime_1_3_particleB_avg[-3],
          relaxtime_1_5_particleB_avg[-3], relaxtime_1_8_particleB_avg[-3],
          relaxtime_1_particleB_avg[-3], relaxtime_2_particleB_avg[-3],
          relaxtime_3_particleB_avg[-3], relaxtime_4_particleB_avg[-3],
          relaxtime_5_particleB_avg[-3], relaxtime_6_particleB_avg[-3]]

vf55_C = [relaxtime_0_5_particleC_avg[-3],  relaxtime_0_6_particleC_avg[-3],relaxtime_0_7_particleC_avg[-3],
          relaxtime_0_8_particleC_avg[-3],  relaxtime_0_9_particleC_avg[-3],
          relaxtime_1_0_particleA_avg[-3],  relaxtime_1_1_particleC_avg[-3], 
          relaxtime_1_2_particleB_avg[-3],  relaxtime_1_3_particleC_avg[-3],
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
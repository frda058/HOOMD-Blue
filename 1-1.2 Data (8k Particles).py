#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 22:26:12 2021

@author: francescaabulencia
"""

import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

#%%
phi = [0.55, 0.57, 0.58]

relaxtime_0_9_rA = 1.0
relaxtime_0_9_rB = 1.2
relaxtime_0_9_rC = 0.9


relaxtime_0_9_particleA = np.array([3903.3459665685268])
relaxtime_0_9_particleA[:] = [x/(relaxtime_0_9_rA**2) for x in relaxtime_0_9_particleA]

relaxtime_0_9_particleB= np.array([10057.850596909015])
relaxtime_0_9_particleB[:] = [x/(relaxtime_0_9_rB**2) for x in relaxtime_0_9_particleB]

relaxtime_0_9_particleC = np.array([1810.6944238727287])
relaxtime_0_9_particleC[:] = [x/(relaxtime_0_9_rC**2) for x in relaxtime_0_9_particleC]

#%%
phi = [0.55, 0.57, 0.58]

relaxtime_0_95_rA = 1.0
relaxtime_0_95_rB = 1.2
relaxtime_0_95_rC = 0.95


relaxtime_0_95_particleA = np.array([3956.8315881569497])
relaxtime_0_95_particleA[:] = [x/(relaxtime_0_95_rA**2) for x in relaxtime_0_95_particleA]

relaxtime_0_95_particleB= np.array([9141.9785695541996])
relaxtime_0_95_particleB[:] = [x/(relaxtime_0_95_rB**2) for x in relaxtime_0_95_particleB]

relaxtime_0_95_particleC = np.array([2797.5718628349905])
relaxtime_0_95_particleC[:] = [x/(relaxtime_0_95_rC**2) for x in relaxtime_0_95_particleC]


#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_0_radii = [1.0, 1.2, 1.0]

relaxtime_1_0_rA = 1.0
relaxtime_1_0_rB = 1.2
relaxtime_1_0_rC = 1.0


relaxtime_1_0_particleA = np.array([4267.6918537266019])
relaxtime_1_0_particleA[:] = [x/(relaxtime_1_0_rA**2) for x in relaxtime_1_0_particleA]

relaxtime_1_0_particleB = np.array([9923.0992434003620])
relaxtime_1_0_particleB[:] = [x/(relaxtime_1_0_rB**2) for x in relaxtime_1_0_particleB]


#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_05_radii = [1.0, 1.2, 1.0]

relaxtime_1_05_rA = 1.0
relaxtime_1_05_rB = 1.2
relaxtime_1_05_rC = 1.05


relaxtime_1_05_particleA = np.array([4127.4395333368811])
relaxtime_1_05_particleA[:] = [x/(relaxtime_1_05_rA**2) for x in relaxtime_1_05_particleA]

relaxtime_1_05_particleB = np.array([9023.8555961649545])
relaxtime_1_05_particleB[:] = [x/(relaxtime_1_05_rB**2) for x in relaxtime_1_05_particleB]

relaxtime_1_05_particleC = np.array([5421.2511055232681])
relaxtime_1_05_particleC[:] = [x/(relaxtime_1_05_rC**2) for x in relaxtime_1_05_particleC]

#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_1_radii = [1.0, 1.2, 1.1]

relaxtime_1_1_rA = 1.0
relaxtime_1_1_rB = 1.2
relaxtime_1_1_rC = 1.1


relaxtime_1_1_particleA = np.array([3420.2237694655114])
relaxtime_1_1_particleA[:] = [x/(relaxtime_1_1_rA**2) for x in relaxtime_1_1_particleA]

relaxtime_1_1_particleB = np.array([8844.8302851569151])
relaxtime_1_1_particleB[:] = [x/(relaxtime_1_1_rB**2) for x in relaxtime_1_1_particleB]

relaxtime_1_1_particleC = np.array([5894.2093967046285])
relaxtime_1_1_particleC[:] = [x/(relaxtime_1_1_rC**2) for x in relaxtime_1_1_particleC]

#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_125_radii = [1.0, 1.2, 1.125]

relaxtime_1_125_rA = 1.0
relaxtime_1_125_rB = 1.2
relaxtime_1_125_rC = 1.125

relaxtime_1_125_particleA = np.array([3369.4082931666449])
relaxtime_1_125_particleA[:] = [x/(relaxtime_1_125_rA**2) for x in relaxtime_1_125_particleA]

relaxtime_1_125_particleB = np.array([8073.8574035879928])
relaxtime_1_125_particleB[:] = [x/(relaxtime_1_125_rB**2) for x in relaxtime_1_125_particleB]

relaxtime_1_125_particleC = np.array([6123.2942143277405])
relaxtime_1_125_particleC[:] = [x/(relaxtime_1_125_rC**2) for x in relaxtime_1_125_particleC]


#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_15_radii = [1.0, 1.2, 1.15]

relaxtime_1_15_rA = 1.0
relaxtime_1_15_rB = 1.2
relaxtime_1_15_rC = 1.15

relaxtime_1_15_particleA = np.array([3175.5862017818090])
relaxtime_1_15_particleA[:] = [x/(relaxtime_1_15_rA**2) for x in relaxtime_1_15_particleA]

relaxtime_1_15_particleB = np.array([8516.1311030632478])
relaxtime_1_15_particleB[:] = [x/(relaxtime_1_15_rB**2) for x in relaxtime_1_15_particleB]

relaxtime_1_15_particleC = np.array([7223.0248081438440])
relaxtime_1_15_particleC[:] = [x/(relaxtime_1_15_rC**2) for x in relaxtime_1_15_particleC]


#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_175_radii = [1.0, 1.2, 1.175]

relaxtime_1_175_rA = 1.0
relaxtime_1_175_rB = 1.2
relaxtime_1_175_rC = 1.175

relaxtime_1_175_particleA = np.array([2973.2152393554602])
relaxtime_1_175_particleA[:] = [x/(relaxtime_1_175_rA**2) for x in relaxtime_1_175_particleA]

relaxtime_1_175_particleB = np.array([8443.9397140187339])
relaxtime_1_175_particleB[:] = [x/(relaxtime_1_175_rB**2) for x in relaxtime_1_175_particleB]

relaxtime_1_175_particleC = np.array([7472.4106512761418])
relaxtime_1_175_particleC[:] = [x/(relaxtime_1_175_rC**2) for x in relaxtime_1_175_particleC]


#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_2_radii = [1.0, 1.2, 1.2]

relaxtime_1_2_rA = 1.0
relaxtime_1_2_rB = 1.2
relaxtime_1_2_rC = 1.2


relaxtime_1_2_particleA = np.array([2995.7549103587435])
relaxtime_1_2_particleA[:] = [x/(relaxtime_1_2_rA**2) for x in relaxtime_1_2_particleA]

relaxtime_1_2_particleB = np.array([7423.5342718243883])
relaxtime_1_2_particleB[:] = [x/(relaxtime_1_2_rB**2) for x in relaxtime_1_2_particleB]



#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_25_radii = [1.0, 1.2, 1.25]

relaxtime_1_25_rA = 1.0
relaxtime_1_25_rB = 1.2
relaxtime_1_25_rC = 1.25

relaxtime_1_25_particleA = np.array([2444.1666328632214])
relaxtime_1_25_particleA[:] = [x/(relaxtime_1_25_rA**2) for x in relaxtime_1_25_particleA]

relaxtime_1_25_particleB = np.array([7000.7827487283121])
relaxtime_1_25_particleB[:] = [x/(relaxtime_1_25_rB**2) for x in relaxtime_1_25_particleB]

relaxtime_1_25_particleC = np.array([8389.0893318885574])
relaxtime_1_25_particleC[:] = [x/(relaxtime_1_25_rC**2) for x in relaxtime_1_25_particleC]


#%%

phi = [0.55, 0.57, 0.58]

relaxtime_1_3_radii = [1.0, 1.2, 1.3]

relaxtime_1_3_rA = 1.0
relaxtime_1_3_rB = 1.2
relaxtime_1_3_rC = 1.3


relaxtime_1_3_particleA = np.array([2124.7439106856891])
relaxtime_1_3_particleA[:] = [x/(relaxtime_1_3_rA**2) for x in relaxtime_1_3_particleA]

relaxtime_1_3_particleB = np.array([6529.2855251713336])
relaxtime_1_3_particleB[:] = [x/(relaxtime_1_3_rB**2) for x in relaxtime_1_3_particleB]

relaxtime_1_3_particleC = np.array([9620.5538600726686])
relaxtime_1_3_particleC[:] = [x/(relaxtime_1_3_rC**2) for x in relaxtime_1_3_particleC]


#%%
# phi = 0.58


radius = [0.9, 0.95, 1.0, 1.05,
          1.1, 1.125, 1.15, 1.175, 1.2, 1.25, 1.3]

vf58_A = [
          relaxtime_0_9_particleA[-1], relaxtime_0_95_particleA[-1],
          relaxtime_1_0_particleA[-1], relaxtime_1_05_particleA[-1],
          relaxtime_1_1_particleA[-1], relaxtime_1_125_particleA[-1],
          relaxtime_1_15_particleA[-1], relaxtime_1_175_particleA[-1],
          relaxtime_1_2_particleA[-1], relaxtime_1_25_particleA[-1],
          relaxtime_1_3_particleA[-1]]

vf58_B = [
          relaxtime_0_9_particleB[-1], relaxtime_0_95_particleB[-1],
          relaxtime_1_0_particleB[-1], relaxtime_1_05_particleB[-1],
          relaxtime_1_1_particleB[-1], relaxtime_1_125_particleB[-1],
          relaxtime_1_15_particleB[-1], relaxtime_1_175_particleB[-1],
          relaxtime_1_2_particleB[-1], relaxtime_1_25_particleB[-1],
          relaxtime_1_3_particleB[-1]]

vf58_C = [
          relaxtime_0_9_particleC[-1], relaxtime_0_95_particleC[-1],
          relaxtime_1_0_particleA[-1],  relaxtime_1_05_particleC[-1],
          relaxtime_1_1_particleC[-1], relaxtime_1_125_particleC[-1],
          relaxtime_1_15_particleC[-1], relaxtime_1_175_particleC[-1],
          relaxtime_1_2_particleB[-1],  relaxtime_1_25_particleC[-1],
          relaxtime_1_3_particleC[-1]]


data_vf58 = {'radius': radius, 
              'Particle A': vf58_A , 
              'Particle B': vf58_B , 
              'Particle C': vf58_C}

df_vf58  = pd.DataFrame (data_vf58)

fig_all = df_vf58.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, color='Green', label = 'R = 1.0')
df_vf58.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf58.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)

fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius | 8400 particles | phi=0.58')
plt.ylim([100, 100000])
plt.show()
plt.close

fig_all = df_vf58.plot(x ='radius', y='Particle A', kind = 'scatter', logy=True, logx=True, color='Green', label = 'R = 1.0')
df_vf58.plot(x ='radius', y='Particle B', kind = 'scatter',  color='Black' , label = 'R = 1.2', ax= fig_all)
df_vf58.plot(x ='radius', y='Particle C', kind = 'scatter',  color='Red' , label = 'R = R', ax= fig_all)
#plt.xlim(0.2, 10)
fig_all.set_ylabel("time/R^2")
fig_all.set_title('Relaxation Time as a Function of Radius | 8400 particles | phi=0.58')
plt.xlim([0.8, 2])


plt.show()
plt.close

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 19:34:05 2021

@author: francescaabulencia
"""

import math
import numpy
import pandas
import hoomd
import hoomd.md
import hoomd.hpmc
import gsd, gsd.hoomd
import hoomd.deprecated


# Set up Initial Conditions from IDL Code

df = pandas.read_table('rcp3.txt', delim_whitespace=True, names=("x", "y", "z", "radius", "boxLen"))

# Extract box length produced by IDL; info found on 2nd row, 5th column of text file
boxLen = df.iloc[1,4] 

print('boxLen: ', boxLen)

radparticles = df.radius.unique()
radius = pandas.DataFrame(data=radparticles)
radius = radius.sort_values(radius.columns[0])

rad_particleA = radius.iloc[0,0]
rad_particleB = radius.iloc[1,0]
rad_particleC = radius.iloc[2,0]

count_particleA = (df.radius == rad_particleA).sum()
count_particleB = (df.radius == rad_particleB).sum()
count_particleC = (df.radius == rad_particleC).sum()
print('# of A:', count_particleA, '# of B:', count_particleB, '# of C:', count_particleC)

count_totalParticles = count_particleA + count_particleB + count_particleC 
print("num of total particles is ", count_totalParticles)
print("num of 2 largest particles is ", count_particleB + count_particleC)

vol_particleA = (4/3)*(math.pi)*(rad_particleA)**3
vol_particleB = (4/3)*(math.pi)*(rad_particleB)**3
vol_particleC = (4/3)*(math.pi)*(rad_particleC)**3

volTotal_particleA = vol_particleA * count_particleA
volTotal_particleB = vol_particleB * count_particleB
volTotal_particleC = vol_particleC * count_particleC

volTotal_ABC = volTotal_particleA + volTotal_particleB + volTotal_particleC

#new_volTotal_BC = volTotal_particleB + volTotal_particleC

phi_initial = volTotal_ABC / (boxLen)**3


print("phi initial: ", phi_initial)

phi_goal = 0.55

print("phi goal is ", phi_goal)

adjFactor = (phi_initial/phi_goal)**(1/3)

boxLen_goal = boxLen * adjFactor
print ('boxLen_goal: ', boxLen_goal)

df = df.sort_values('radius')
print(df)

x_pos = df[['x']].to_numpy()
y_pos = df[['y']].to_numpy()
z_pos = df[['z']].to_numpy()

x_pos = (x_pos - (boxLen/2) )* adjFactor
y_pos = (y_pos - (boxLen/2) )* adjFactor
z_pos = (z_pos - (boxLen/2) )* adjFactor

# Combine initial positions into (x,y,z) format
xyz_coords =  numpy.column_stack((x_pos, y_pos, z_pos))

# Hard Particle Monte Carlo Simulation for PhiRCP = 0.64
hoomd.context.initialize("--mode=cpu")

box = hoomd.data.boxdim(L=boxLen_goal)

config = hoomd.data.make_snapshot(N = count_totalParticles, box = box, particle_types=['A', 'B','C'])

#my_position = [(numpy.random.uniform(-boxLen_goal/2, boxLen_goal/2),numpy.random.uniform(-boxLen_goal/2, boxLen_goal/2), numpy.random.uniform(-boxLen_goal/2, boxLen_goal/2)) for i in range (count_totalParticles) ]

config.particles.position[:] = xyz_coords[:]


config.particles.typeid[:] = count_particleA * [0] + count_particleB * [1] + count_particleC * [2]

hoomd.init.read_snapshot(config)

mc = hoomd.hpmc.integrate.sphere(d=0.25, seed=1)
mc.shape_param['A'].set(diameter= 2*rad_particleA)
mc.shape_param['B'].set(diameter= 2*rad_particleB)
mc.shape_param['C'].set(diameter= 2*rad_particleC)


# Create .gsd file with snapshots at every one time step 

all = hoomd.group.all() 
hoomd.dump.gsd('./snapshot_phi66_case3_phi55_100K_TS_10S.gsd', period=1, group=all, overwrite=True)

# Run the simulation for N time-steps
S = 100000
hoomd.run(S)

# Store the snapshots.gsd file in a variable
snapshots = gsd.hoomd.open(name='./snapshot_phi66_case3_phi55_100K_TS_10S.gsd', mode="rb")

# Create a text file for snapshot data
f = open('snapshot_phi66_case3_phi55_100K_TS_10S.txt',"w+")

#Access snapshot data for N time-steps
sample=10
for i in range(S):
    if i % sample == 0:
        snap = snapshots[i]
        position = snap.particles.position
        numpy.savetxt(f, (position))
f.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:00:35 2020

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

rad_particleA = 1.1
rad_particleB = 1.3
rad_particleC = 1.5

df = pandas.read_table('rcp5.txt', delim_whitespace=True, names=("x", "y", "z", "radius", "boxLen"))

# Extract box length produced by IDL; info found on 2nd row, 5th column of text file
boxLen = df.iloc[1,4] 
print(boxLen)

df = df.sort_values('radius')
print(df)

count_particleA = (df.radius == rad_particleA).sum()
count_particleB = (df.radius == rad_particleB).sum()
count_particleC = (df.radius == rad_particleC).sum()
print(count_particleA, count_particleB, count_particleC)

count_totalParticles = count_particleA + count_particleB + count_particleC 
print("num of total particles is ", count_totalParticles)


vol_particleA = (4/3)*(math.pi)*(rad_particleA)**3
vol_particleB = (4/3)*(math.pi)*(rad_particleB)**3
vol_particleC = (4/3)*(math.pi)*(rad_particleC)**3

volTotal_particleA = vol_particleA * count_particleA
volTotal_particleB = vol_particleB * count_particleB
volTotal_particleC = vol_particleC * count_particleC

volTotal_ABC = volTotal_particleA + volTotal_particleB + volTotal_particleC

phi_initial = volTotal_ABC / (boxLen)**3
print("phi initial is ", phi_initial)

phi_goal = 0.40

adjFactor = (phi_initial/phi_goal)**(1/3)

boxLen_goal = boxLen * adjFactor

print("boxLen_goal is ", boxLen_goal)


# Extract initial positions from data frame into array
x_pos = df[['x']].to_numpy()
y_pos = df[['y']].to_numpy()
z_pos = df[['z']].to_numpy()

# Adjust initial positions to (-L/2 to L/2) times the adjusting factor
x_pos = (x_pos - (boxLen/2) )* adjFactor
y_pos = (y_pos - (boxLen/2) )* adjFactor
z_pos = (z_pos - (boxLen/2) )* adjFactor

# Combine initial positions into (x,y,z) format
xyz_coords =  numpy.column_stack((x_pos, y_pos, z_pos))

# Hard Particle Monte Carlo Simulation for PhiRCP = 0.64
hoomd.context.initialize("--mode=cpu")

# Simulation 1
# 26 Particles: r=1.1 (6 particles); r= 1.3 (17 particles); r= 1.5 (3 particles)
# PhiRCP = 0.64

box = hoomd.data.boxdim(L=boxLen_goal)

config = hoomd.data.make_snapshot(N = count_totalParticles, box = box, particle_types=['A', 'B','C'])

#my_position = [(numpy.random.uniform(-boxLen_goal/2, boxLen_goal/2),numpy.random.uniform(-boxLen_goal/2, boxLen_goal/2), numpy.random.uniform(-boxLen_goal/2, boxLen_goal/2)) for i in range (count_totalParticles) ]

config.particles.position[:] = xyz_coords[:]


config.particles.typeid[:] = count_particleA * [0] + count_particleB * [1] + count_particleC * [2]

hoomd.init.read_snapshot(config)

mc = hoomd.hpmc.integrate.sphere(d=0.5, seed=1)
mc.shape_param['A'].set(diameter= 2*rad_particleA)
mc.shape_param['B'].set(diameter= 2*rad_particleB)
mc.shape_param['C'].set(diameter= 2*rad_particleC)


# Create .gsd file with snapshots at every one time step 

all = hoomd.group.all() 
hoomd.dump.gsd('./snapshots5.gsd', period=1, group=all, overwrite=True)

# Run the simulation for N time-steps
S = 500
hoomd.run(S)

# Store the snapshots.gsd file in a variable
snapshots = gsd.hoomd.open(name='./snapshots5.gsd', mode="rb")

# Create a text file for snapshot data
f = open("snapshot5.txt","w+")

#Access snapshot data for N time-steps
for i in range(S):
    snap = snapshots[i]
    position = snap.particles.position
    numpy.savetxt(f, (position))
f.close()
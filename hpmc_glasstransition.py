#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:00:35 2020

@author: francescaabulencia
"""
import random
import numpy

import hoomd
import hoomd.md
import hoomd.hpmc
import gsd, gsd.hoomd
import hoomd.deprecated

hoomd.context.initialize("--mode=cpu")


# Hard Particle Monte Carlo Simulation for PhiRCP = 0.66

# Simulation 1
# 26 Particles: d=2.0 (11 particles); d= 5.0 (8 particles); d= 6.0 (7 particles)
# Skew = -0.171026314
# Polydispersity = 0.43852901
# PhiRCP = 0.660036564

L = 50
box = hoomd.data.boxdim(Lx=L, Ly=L, Lz=L)

config = hoomd.data.make_snapshot(N=26, box=box, particle_types=['A', 'B','C'])
my_velocity = (15,15,15)
my_position = [(numpy.random.uniform(0,25), numpy.random.uniform(0,25), numpy.random.uniform(0,25)) for i in range(26)]
config.particles.velocity[:] = my_velocity[:]
config.particles.position[:] = my_position[:]
config.particles.typeid[:] = 11 * [0] + 8 * [1] + 7 * [2]

hoomd.init.read_snapshot(config)

#print(config.particles.position)

mc = hoomd.hpmc.integrate.sphere(d=4, seed=1)
mc.shape_param['A'].set(diameter=2.0)
mc.shape_param['B'].set(diameter=5.0)
mc.shape_param['C'].set(diameter=6.0)

# dA = mc.shape_param['A'].diameter
# dB = mc.shape_param['B'].diameter
# dC = mc.shape_param['C'].diameter


# Create .gsd file with snapshots at every one time step 
all = hoomd.group.all() 
hoomd.dump.gsd('./snapshots.gsd', period=1, group=all, overwrite=True)

# Run the simulation for N time-steps
S = 1000
hoomd.run(S)

# Store the snapshots.gsd file in a variable
snapshots = gsd.hoomd.open(name='./snapshots.gsd', mode="rb")


# Create a text file for snapshot data
f = open("particle_position.txt","w+")

#Access snapshot data for N time-steps
for i in range(S):
    snap = snapshots[i]
    position = snap.particles.position
    numpy.savetxt(f, position)
f.close()


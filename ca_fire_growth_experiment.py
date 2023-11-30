#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:20:00 2023

@author: Fabio Vanegas
"""
from ca_fire import evolve_forest, write_netcdf


# defaults
GRID_N_X = 300  # sub-divisions along X axis
PROB_GROWTH = 1.0e-5  # probability of new growth per cell per unit time
PROB_NEW_FIRE = 1.0e-7  # probability of new fire per cell per unit time
N_TIME_STEP = 100000  # number of time-steps
VERBOSE = True # set to False to suppress printing
#added on the main
# run the model
result = evolve_forest(
    (GRID_N_X, GRID_N_X), N_TIME_STEP, PROB_GROWTH, PROB_NEW_FIRE, verbose=VERBOSE)

#output
file_name = f'forest_grid_{N_TIME_STEP:06d}.nc'

if VERBOSE:
    print(f'writing final output to {file_name}')

write_netcdf(file_name , *result)

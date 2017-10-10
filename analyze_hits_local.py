import json
import os
import numpy as np
from data_analysis_local import compile_dataset, add_plates, load_dataset, load_OD_data, print_data, filter_hits, compile_dataset_by_name
import matplotlib.pyplot as plt


direc = direc = '/Users/nicolasquach/Documents/stanford/covert_lab/thesis/'
plate_numbers = ['1_1','1_2', 3, 5, 7, '9_1','9_2', 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 39, 41, 43, 45, 47, 49, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 89, 95]
#dataset = load_dataset(direc)
#OD_data = load_OD_data(direc)

#get_OD_data(plate_numbers = plate_numbers)

#add_plates(direc, plate_numbers)

#compile_dataset(direc, plate_numbers)

#compile_dataset_by_name(direc, plate_numbers)#

#print_data(direc, plate=None)
name = None
mode_lb = 0.9
mode_ub = 1
n_infected_lb = 0
n_infected_ub = 10000
n_cell_lb = 30
n_cell_ub = 10000
frac_infected_lb = 0
frac_infected_ub = 1
var_lb = 0
var_ub = 10000
n_lytic_lb = 0
n_lytic_ub = 10000
n_lyso_lb = 0
n_lyso_ub = 10000
OD_lb = 0.04
OD_ub = 1
in_maynard = False
is_TF = False
save_hits = False
save_name = 'lyso_hits.txt'

filter_hits(name = name, mode_lb = mode_lb, mode_ub = mode_ub, n_infected_lb = n_infected_lb, n_infected_ub = n_infected_ub, n_cell_lb = n_cell_lb, n_cell_ub = n_cell_ub, frac_infected_lb = frac_infected_lb, frac_infected_ub = frac_infected_ub, var_lb = var_lb, var_ub = var_ub, n_lytic_lb = n_lytic_lb, n_lytic_ub = n_lytic_ub, n_lyso_lb = n_lyso_lb, n_lyso_ub = n_lyso_ub, OD_lb = OD_lb, OD_ub = OD_ub, in_maynard = in_maynard, is_TF = is_TF, save_hits = save_hits, save_name = save_name)



##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
#
# Goal: 
#  This program is intended to correlate all possible pairs of 
# comparable columns, label the results and append to a list if
# above threshold, sort the list, write list to file. 
##

import os
import sys
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

labels = ['scale', 'id', 'desc_scale', 'desc_id', 'num_prog',\
 'pid', 'upid', 'desc_pid', 'phantom', 'sam_mvir', 'mvir',\
 'rvir', 'rs', 'vrms', 'is_mmp', 'scale_of_last_MM', 'vmax',\
 'x', 'y', 'z', 'vx', 'vy', 'vz', 'Jx', 'Jy', 'Jz', 'Spin', \
 'Breadth_first_ID', 'Depth_first_ID', 'Tree_root_ID',\
 'Orig_halo_ID', 'Snap_num',\
 'Next_coprogenitor_depthfirst_ID', \
 'Last_progenitor_depthfirst_ID', \
 'Last_mainleaf_depthfirst_ID', 'Tidal_Force', 'Tidal_ID',\
 'Rs_Klypin', 'Mvir_all', 'M200b', 'M200c', 'M500c', 'M2500c',\
 'Xoff', 'Voff', 'Spin_Bullock', 'b_to_a', 'c_to_a', 'A_x',\
 'A_y', 'A_z', 'b_to_a_500c', 'c_to_a_500c', 'A_x_500c',\
 'A_y_500c', 'A_z_500c', 'T_per_magnitude_U', 'M_pe_Behroozi',\
 'M_pe_Diemer', 'Macc', 'Mpeak', 'Vacc', 'Vpeak', \
 'Halfmass_Scale', 'Acc_Rate_Inst', 'Acc_Rate_100Myr', \
 'Acc_Rate_x_Tdyn', 'Acc_Rate_x_2Tdyn', 'Acc_Rate_Mpeak', \
 'Mpeak_Scale', 'Acc_Scale', 'First_Acc_Scale', \
 'First_Acc_Mvir', 'First_Acc_Vmax', 'Vmax_at_Mpeak', \
 'Tidal_Force_Tdyn', 'wall1', 'wall2', 'wall3', 'fila1', \
 'fila2', 'fila3', 'dist2', 'dist2', 'dist3']

"""
interesting_things = ['num_prog',\
 'sam_mvir', 'mvir',\
 'rvir', 'rs', 'vrms', 'scale_of_last_MM', 'vmax',\
 'Spin', \
 'Tidal_Force',\
 'Rs_Klypin', 'Mvir_all', 'M200b', 'M200c', 'M500c', 'M2500c',\
 'Xoff', 'Voff', 'Spin_Bullock', 'b_to_a', 'c_to_a', 'b_to_a_500c', \
 'c_to_a_500c', 'A_x_500c',\
 'A_y_500c', 'A_z_500c', 'T_per_magnitude_U', 'M_pe_Behroozi',\
 'M_pe_Diemer', 'Macc', 'Mpeak', 'Vacc', 'Vpeak', \
 'Halfmass_Scale', 'Acc_Rate_Inst', 'Acc_Rate_100Myr', \
 'Acc_Rate_x_Tdyn', 'Acc_Rate_x_2Tdyn', 'Acc_Rate_Mpeak', \
 'Mpeak_Scale', 'Acc_Scale', 'First_Acc_Scale', \
 'First_Acc_Mvir', 'First_Acc_Vmax', 'Vmax_at_Mpeak', \
 'Tidal_Force_Tdyn', 'dist1', 'dist2', 'dist3']
"""
interesting_things = ["c_to_a"]

if len(sys.argv) != 2:
  print "Usage: $ python program_name.py in.csv"
  exit()

inputfilename = sys.argv[1]

if not os.path.isfile(inputfilename):
  print "Error: " + inputfilename + " is not a file!"
  exit()

catalog = []
with open(inputfilename) as file:
  for line in file:
      catalog.append(line.rstrip().split(','))

#now that it's built, convert type and store in numpy array
halos = np.array([[float(y) for y in x] for x in catalog])

for i in xrange(1, halos.shape[1]):
  if labels[i] in interesting_things:
    plt.hist(halos[:,i], bins = 1000)
    plt.xlabel(labels[i])
    plt.ylabel("Count")
    plt.savefig(labels[i] + "_histogram.png")
    plt.clf()

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
 'fila2', 'fila3', 'dist1', 'dist2', 'dist3']

if len(sys.argv) != 3:
  print "Usage: $ python program_name.py in.csv, out.txt"
  exit()

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

if not os.path.isfile(inputfilename):
  print "Error: " + inputfilename + " is not a file!"
  exit()

if os.path.isfile(outputfilename):
  print "Error: " + outputfilename + " exists!"
  exit()

catalog = []
with open(inputfilename) as file:
  for line in file:
    catalog.append(line.rstrip().split(','))

#now that it's built, convert type and store in numpy array
halos = np.array([[float(y) for y in x] for x in catalog])

results = []
for i in xrange(0, halos.shape[1]):
  results.append(stats.normaltest(halos[:,i]))

with open(outputfilename, 'w') as out:
  for i in xrange(0, len(results)):
    if results[i][1] > 0.05: 
      out.write(labels[i] + ': \n' + str(results[i]) + '\n')

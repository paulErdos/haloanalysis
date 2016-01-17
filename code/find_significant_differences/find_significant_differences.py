##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
#
##

import os
import sys
from scipy import stats
import numpy as np

labels = ['scale', 'id', 'desc_scale', 'desc_id', 'num_prog', 'pid', 'upid', 'desc_pid', 'phantom', 'sam_mvir', 'mvir', 'rvir', 'rs', 'vrms', 'is_mmp', 'scale_of_last_MM', 'vmax', 'x', 'y', 'z', 'vx', 'vy', 'vz', 'Jx', 'Jy', 'Jz', 'Spin', 'Breadth_first_ID', 'Depth_first_ID', 'Tree_root_ID', 'Orig_halo_ID', 'Snap_num', 'Next_coprogenitor_depthfirst_ID', 'Last_progenitor_depthfirst_ID', 'Last_mainleaf_depthfirst_ID', 'Tidal_Force', 'Tidal_ID', 'Rs_Klypin', 'Mvir_all', 'M200b', 'M200c', 'M500c', 'M2500c', 'Xoff', 'Voff', 'Spin_Bullock', 'b_to_a', 'c_to_a', 'A_x', 'A_y', 'A_z', 'b_to_a_500c', 'c_to_a_500c', 'A_x_500c', 'A_y_500c', 'A_z_500c', 'T_per_magnitude_U', 'M_pe_Behroozi', 'M_pe_Diemer', 'Macc', 'Mpeak', 'Vacc', 'Vpeak', 'Halfmass_Scale', 'Acc_Rate_Inst', 'Acc_Rate_100Myr', 'Acc_Rate_x_Tdyn', 'Acc_Rate_x_2Tdyn', 'Acc_Rate_Mpeak', 'Mpeak_Scale', 'Acc_Scale', 'First_Acc_Scale', 'First_Acc_Mvir', 'First_Acc_Vmax', 'Vmax_at_Mpeak', 'Tidal_Force_Tdyn', 'wall1', 'wall2', 'wall3', 'fila1', 'fila2', 'fila3', 'dist1', 'dist2', 'dist3']

if len(sys.argv) != 3:
  print "Usage: $ python program_name.py in.csv, out.what"
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

#now that it's built, convert type
halos = [[float(y) for y in x] for x in catalog]

#column 76 is <id halo is inside wall @ 1 Mpc smoothing>
halos_in_wall = [halo for halo in halos if halo[76] == 1]
halos_not_in_wall = [halo for halo in halos if halo[76] != 1]

in_wall = np.array(halos_in_wall)
not_in_wall = np.array(halos_not_in_wall)

results = []
for i in xrange(0, 75):
  results.append(\
    stats.ttest_ind(in_wall[:,i], not_in_wall[:,i]))

with open(outputfilename, 'w') as out:
  for i in xrange(0, len(results)):
    line = results[i]
    if line[1] > 0.95:
      print i
      out.write(labels[i] + ': ' + str(line) + '\n')

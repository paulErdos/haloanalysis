##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
#
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

#now that it's built, convert type
halos = [[float(y) for y in x] for x in catalog]

#column 76 is <id halo is inside wall @ 1 Mpc smoothing>
in_wall_in_fila = \
  np.array([h for h in halos \
    if h[76] == 1 and h[79] == 1])
in_wall_no_fila = \
  np.array([h for h in halos \
    if h[76] == 1 and h[79] == 0])
no_wall_in_fila = \
  np.array([h for h in halos \
    if h[76] == 0 and h[79] == 1])
no_wall_no_fila = \
  np.array([h for h in halos \
    if h[76] == 0 and h[79] == 0])

groupings = [in_wall_in_fila, in_wall_no_fila,\
             no_wall_in_fila, no_wall_no_fila]
 
results_1110 = []
for i in xrange(0, 75):
  results_1110.append(\
    stats.ttest_ind(in_wall_in_fila[:,i], \
                    in_wall_no_fila[:,i]))


results_1101 = []
for i in xrange(0, 75):
  results_1101.append(\
    stats.ttest_ind(in_wall_in_fila[:,i], \
                    no_wall_in_fila[:,i]))


results_1100 = []
for i in xrange(0, 75):
  results_1100.append(\
    stats.ttest_ind(in_wall_in_fila[:,i], \
                    no_wall_no_fila[:,i]))

results_1001 = []
for i in xrange(0, 75):
  results_1001.append(\
    stats.ttest_ind(in_wall_no_fila[:,i], \
                    no_wall_in_fila[:,i]))

results_1000 = []
for i in xrange(0, 75):
  results_1000.append(\
    stats.ttest_ind(in_wall_no_fila[:,i], \
                    no_wall_no_fila[:,i]))

results_0100 = []
for i in xrange(0, 75):
  results_0100.append(\
    stats.ttest_ind(no_wall_in_fila[:,i], \
                    no_wall_no_fila[:,i]))

with open(outputfilename, 'w') as out:
  
  out.write("Halos in walls and in filaments: " + \
    str(len(in_wall_in_fila)) + '\n')
  out.write("Halos in walls and not in filaments: " + \
    str(len(in_wall_no_fila)) + '\n')
  out.write("Halos not in walls and in filaments: " + \
    str(len(no_wall_in_fila)) + '\n')
  out.write("Halos not in walls and not in filaments: " + \
    str(len(no_wall_no_fila)) + '\n')

  out.write('\n\n1110:\n')
  for i in xrange(0, len(results_1110)):
    line = results_1110[i]
    if line[1] > 0.95:
      out.write(labels[i] + ': ' + str(line) + '\n')

  out.write('\n\n1101:\n')
  for i in xrange(0, len(results_1110)):
    line = results_1101[i]
    if line[1] > 0.95:
      out.write(labels[i] + ': ' + str(line) + '\n')

  out.write('\n\n1100:\n')
  for i in xrange(0, len(results_1110)):
    line = results_1100[i]
    if line[1] > 0.95:
      out.write(labels[i] + ': ' + str(line) + '\n')

  out.write('\n\n1001:\n')
  for i in xrange(0, len(results_1110)):
    line = results_1001[i]
    if line[1] > 0.95:
      out.write(labels[i] + ': ' + str(line) + '\n')

  out.write('\n\n1000:\n')
  for i in xrange(0, len(results_1110)):
    line = results_1000[i]
    if line[1] > 0.95:
      out.write(labels[i] + ': ' + str(line) + '\n')

  out.write('\n\n0100:\n')
  for i in xrange(0, len(results_1110)):
    line = results_0100[i]
    if line[1] > 0.95:
      out.write(labels[i] + ': ' + str(line) + '\n')

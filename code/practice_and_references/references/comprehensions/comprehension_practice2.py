from scipy import stats
from subprocess import call
call(["clear"])

mass = 0
in_filament = 1
in_wall = 2

halo1 = [4, 1, 0]
halo2 = [8, 0, 1]
halo3 = [2, 1, 0]
halo4 = [6, 0, 1]
halo5 = [7, 1, 0]
halo6 = [2, 0, 1]
halo7 = [1, 1, 0]

catalog = [halo1, halo2, halo3, halo4, halo5, halo6, halo7]

filament_masses = [x[mass] for x in catalog \
                  if x[in_filament] == 1]
wall_masses = [x[mass] for x in catalog if x[in_wall] == 1]

print stats.ttest_ind(filament_masses, wall_masses)

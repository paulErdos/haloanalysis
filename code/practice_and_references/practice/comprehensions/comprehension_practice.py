from subprocess import call
call(["clear"])

mass = 0
radius = 1

halo1 = [1, 2]
halo2 = [3, 4]

catalog = [halo1, halo2]

print [x[mass] for x in catalog]

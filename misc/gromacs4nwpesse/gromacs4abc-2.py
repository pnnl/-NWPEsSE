#!/usr/bin/env python

# For using NWPEsSe with GROMACS

import sys
import os

nm2AA = 10.

gro_fn = sys.argv[1]    # min.gro
log_fn = sys.argv[2]    # min.log
output_fn = sys.argv[3] # $out$

coords = []
with open(gro_fn, 'r') as fd:
    lines = fd.readlines()
    for line in lines[2:-1]:
        line = line.split()
        coords.append([line[1], float(line[3])*nm2AA, float(line[4])*nm2AA, float(line[5])*nm2AA])

energy = 0.
with open(log_fn, 'r') as fd:
    lines = fd.readlines()
    for line in lines:
        line = line.split()
        if len(line) == 4:
            if line[0] == 'Potential' and line[1] == 'Energy':
                energy = float(line[3])

with open(output_fn, 'w') as fd:    
    fd.write('%d\n' % (len(coords)))
    fd.write('%15.8f\n' % (energy))
    for coord in coords:
        fd.write('%5s %15.8f %15.8f %15.8f\n' % (coord[0], coord[1], coord[2], coord[3]))

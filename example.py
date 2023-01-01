#!/usr/bin/env python

import matplotlib.pyplot as plt
import eulerspirals as ers


spiral = ers.Spiral(1.123)
spiral.calculate(1000000)
spiral.save()

plt.rcParams['agg.path.chunksize'] = 10000
plt.figure(dpi=600)
plt.plot(spiral.x, spiral.y, lw=0.1, alpha=0.7, c="black")
plt.savefig("eulerspiral.jpg")
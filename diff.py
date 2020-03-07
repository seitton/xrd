"""using 2-col file to draw a plot"""
import os
import math
import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import (AutoMinorLocator)
from scipy import optimize, signal
from lmfit import models

font = {'family': 'sans-serif',
        'color':  'k',
        'weight': 'normal',
        'size': 14,
        }
#reading file
fn = input()
col1, col2 = np.genfromtxt(fn, comments='*', skip_footer = 20, usecols=(0, 1), unpack=True, encoding="latin-1")


#plot
fig = plt.figure()
# plot area - fig.add_subplot(rows,columns,position on the list)
ax = fig.add_subplot(111)
# plot itself
ax.plot(col1, col2, '-k', linewidth=1.5, label="pd_sum")
# axis labels, title
ax.set_xlabel('2theta', fontdict=font)
ax.set_ylabel('Интенсивность, a.u.', fontdict=font)
ax.set_title(fn, fontdict=font)
# axis limits
ax.set(xlim=(30, 80))
#ax.set_ylim(ymin=0, ymax=None)
ax.xaxis.set_minor_locator(AutoMinorLocator())
# tick labels format
ax.ticklabel_format(axis='y', scilimits=(0, 0), useMathText=True)
plt.tight_layout()
plt.show()

# two plots
# col1, col2 = np.loadtxt("pd_a00", usecols=(0, 1), unpack=True)
# col3, col4 = np.loadtxt("pd_s00", usecols=(0, 1), unpack=True)
# fig = plt.figure()
# ax = fig.add_subplot(211)
# ax.plot(col1, col2, '-b', linewidth=1, label="det_a00")
# ax.set_ylabel('Intensity, a.u.', fontdict=font)
# ax.set_title('Neutron diffraction pattern for U. pictorum', fontdict=font)
# ax.set(xlim=(0, 3000))
# ax.set_ylim(ymin=0, ymax=None)
#
#
# ax1 = fig.add_subplot(212)
# ax1.plot(col3, col4, '-r', linewidth=1, label="det_s00")
# ax1.set_xlabel('Channel', fontdict=font)
# ax1.set_ylabel('Intensity, a.u.', fontdict=font)
# ax1.set(xlim=(0, 3000))
# ax1.set_ylim(ymin=0, ymax=None)
# ax1.xaxis.set_minor_locator(AutoMinorLocator())
#
# fig.legend([ax, ax1], labels=('det_a00', 'det_s00'),
#                 bbox_to_anchor=(0.95, 0.93))

#plt.tight_layout()

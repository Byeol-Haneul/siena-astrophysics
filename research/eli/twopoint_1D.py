import numpy as np
from operator import add
import matplotlib.pylab as plt
import math
from matplotlib.colors import LogNorm
import matplotlib as mpl
import sys

tag = ""
if len(sys.argv)>1:
    tag = sys.argv[1]

DD=np.loadtxt(tag+'DD.dat',dtype='float',unpack=True,delimiter=',')
DR=np.loadtxt(tag+'DR.dat',dtype='float',unpack=True,delimiter=',')
RR=np.loadtxt(tag+'RR.dat',dtype='float',unpack=True,delimiter=',')

ndata=DD[0][0]
nrand=RR[0][0]

x = DD[1][1:]
DD = DD[3][1:]
DR = DR[3][1:]
RR = RR[3][1:]

DD /= ((ndata**2-ndata)/2.)
DR /= ((nrand*ndata)/1.)
RR /= ((nrand**2-nrand)/2.)
w = (DD - 2*DR + RR)/RR

print w
print ndata
print nrand

plt.figure(figsize=(8,8))
plt.plot(x,w,'ko')
plt.xlabel(r'Some sort of separation (Mpc)',fontsize=18)
plt.ylabel(r'$\xi$',fontsize=24)
plt.title(r'$\xi$')
plt.xlim(50,180)
plt.ylim(-0.01,0.10)

plt.tight_layout()

plt.show()

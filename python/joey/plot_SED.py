#! usr/bin/env python
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import sextutils as se
import math


if __name__ == '__main__':

    #read the catalog
    datafile = '/home/obsastro1/siena-astrophysics/summer2013/clash/arcphot.txt'
    savepath = '/home/obsastro1/siena-astrophysics/python/joey/sed_plot.png'

    cat = se.se_catalog(datafile)
    #convert flux to mag
###########################################

    plt.figure()

    um1 = cat.weff*.0001

    mag1 = (-2.5*log10(cat.flux1))

    mag_err1 = (2.5/log(10))*((1/sqrt(cat.ivar1))/cat.flux1)

    plt.plot(um1,mag1,'g-',label='Total')

    plt.errorbar(um1,mag1,mag_err1, fmt = 'go')

##########################################

    um2 = cat.weff*.0001

    mag2 = (-2.5*log10(cat.flux2))

    mag_err2 = (2.5/log(10))*((1/sqrt(cat.ivar2))/cat.flux2)

    plt.plot(um2,mag2,'r-',label='Red')

    plt.errorbar(um2,mag2,yerr= mag_err2, fmt ='ro')

#########################################

    um3 = cat.weff*.0001

    mag3 = (-2.5*log10(cat.flux3))

    mag_err3 = (2.5/log(10))*((1/sqrt(cat.ivar3))/cat.flux3)

    plt.plot(um3,mag3,'b-',label='Blue')

    plt.errorbar(um3,mag3,yerr=mag_err3, fmt ='bo')

########################################

    bestfit_path = '/home/obsastro1/siena-astrophysics/summer2013/clash/arcphot_bestfit.txt'
    
    ca = se.se_catalog(bestfit_path)
    bestfit_um1 = ca.wave1*.0001
    bestfit_mag1 = ca.flux1
    plt.plot(bestfit_um1, bestfit_mag1, 'g-')

    bestfit_um2 = ca.wave2*.0001
    bestfit_mag2 = ca.flux2
    plt.plot(bestfit_um2, bestfit_mag2, 'r-')

    bestfit_um3 = ca.wave3*.0001
    bestfit_mag3 = ca.flux3
    plt.plot(bestfit_um3, bestfit_mag3, 'b-')
    
   
    ax = plt.gca()
    ax.set_ylim(30,18)
    ax.set_xlim(0,1.6)
    #ax.set_ylim(ax.get_ylim()[::-1])
    #legend(('Total','Red','Blue'),loc='upper left')
    plt.legend()
    plt.title('SED')
    plt.xlabel('observed wavelength (um)')
    plt.ylabel('Magnitude (AB)')
    plt.savefig(savepath)
    plt.show()
   


#mag = math.log10(cat.flux1[i])*(-2.5)

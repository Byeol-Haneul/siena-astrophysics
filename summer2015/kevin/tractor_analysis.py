#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
import os
from astrometry.libkd.spherematch import match_radec

indir = '/global/work/decam/scratch'
tractor_table = fits.getdata(indir+'/tractor/242/tractor-2428p117.fits')
true_table = fits.getdata(os.getenv('FAKE_DECALS_DIR')+'/priors_2428p117.fits')
m1, m2, d12 = match_radec(tractor_table['ra'],tractor_table['dec'],true_table['ra'],true_table['dec'],1.0/3600)
tractor_flux = tractor_table['decam_flux'][m1,2]
true_flux = true_table['r'][m2]
magnitude_difference = -2.5*np.log10(tractor_flux)+22.5-true_flux

def flux_graph():
    plt.plot(true_flux,magnitude_difference,'ko',markersize=3)
    plt.title('True Flux')
    plt.xlabel('Flux')

    
def size_graph():
    size = true_table['DISK_R50'][m2]
    plt.plot(size,magnitude_difference,'bo',markersize=3)
    plt.title('Size')
    plt.xlabel('r50')
    
def ellipticity_graph():
    ellipticity = true_table['DISK_BA'][m2]
    plt.plot(ellipticity,magnitude_difference,'ro',markersize=3)
    plt.title('Ellipticity')
    plt.xlabel('b/a')

def ra_position_graph():
    ra_position = true_table['ra'][m2]
    plt.plot(ra_position,magnitude_difference,'co',markersize=3)
    plt.title('Ra')
    plt.xlabel('ra')

def dec_position_graph():
    dec_position = true_table['dec'][m2]   
    plt.plot(dec_position,magnitude_difference,'yo',markersize=3)
    plt.title('Dec')
    plt.xlabel('dec')



plt.subplot(1,5,1)
flux_graph()

plt.subplot(1,5,2)
size_graph()

plt.subplot(1,5,3)
ellipticity_graph()

plt.subplot(1,5,4)
ra_position_graph()

plt.subplot(1,5,5,sharey=True)
dec_position_graph()

fig,axes = plt.subplots(ncols=5, sharex=False, sharey=True)

plt.savefig('/home/desi3/kevin'+'/2428p117_graphs',clobber=True)
plt.show()

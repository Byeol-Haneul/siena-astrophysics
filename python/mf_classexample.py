#!/usr/bin/env python
from pylab import *
import atpy


class cluster:
    def __init__(self,clustername):
        infile='/home/rfinn/research/LocalClusters/NSAmastertables/'+clustername+'_NSAmastertable.fits'
        self.mdat=atpy.Table(infile)
    def plotradec(self):
        figure()
        plot(self.mdat.RA,self.mdat.DEC,'b.')
    def plotredshift(self):
        figure()
        hist(self.mdat.ZDIST)
        title('RedShift MKW11')
        

class nasasloan:
    def __init__(self):
        infile='/home/share/research/nsa/nsa_v0_1_2topcat.fits'
        #infile='/home/share/research/nsa/NSA_LCSregion.fits'
        self.ndat=atpy.Table(infile)
    def absgbandmag(self):
        figure()
        hist(self.ndat.ABSMAG[:,3],bins=100)
        title('Absolute g-band Magnitude (NSA_LCS Region) ')
        xlim(xmax=-7)
        xlim(xmin=-25) 
        ax=gca()
        ax.set_yscale('log')
        xlabel('Absolute g-band Magnitude')
        ylabel('Number of Galaxies')

nsa=nasasloan()


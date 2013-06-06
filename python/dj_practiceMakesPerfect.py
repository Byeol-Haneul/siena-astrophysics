#! /user/bin/env python
from pylab import *
import atpy


class cluster:
    def __init__(self,clustername):
        infile='/home/share/research/LocalClusters/NSAmastertables/'+clustername+'_NSAmastertable.fits'
        self.mdat=atpy.Table(infile)
    def plotradec(self):
        figure()
        plot(self.mdat.RA,self.mdat.DEC,'b.')
    def plotrs(self):
        figure()
        hist(self.mdat.ZDIST,bins=20,histtype='step')
        
    def plotlf(self):
        #figure()
        hist(self.mdat.ABSMAG[:,3],bins=100)


mkw11=cluster('MKW11')
mkw8=cluster('MKW8')
coma=cluster('Coma')
def plotboth():
    figure()
    subplot(1,3,1)
    mkw11.plotlf()
    title('MKW 11')
    ax=gca()
    ax.set_yscale('log')
    ylabel('Number of Galaxies')
    subplot(1,3,2)
    mkw8.plotlf()
    title('MKW 8')
    xlabel('g band luminosity')
    subplot(1,3,3)
    coma.plotlf()
    title('Coma')
    ax=gca()
    ax.set_yscale('log')


    
    
    
    

#!/usr/bin/env python
from pylab import *
import atpy

class nasasloan:
    def __init__(self):
        infile='/home/share/research/nsa/nsa_v0_1_2topcat.fits'
        #infile='/home/share/research/nsa/NSA_LCSregion.fits'
        self.ndat=atpy.Table(infile)
    def plotLF(self):
        self.amag=self.ndat.ABSMAG[:,3]
        self.luminosity=(self.amag-4.83)/-2.5
        figure()
        t=hist(self.luminosity, bins=50)
        clf()
        print t
        #split t
        #bins =xvalues
        bins = t[1]
        yvalue = t[0]

        bincenters=[]
        for x in range(len(yvalue)):
            bincenters.append((bins[x]+bins[x+1])/2)
            print bincenters
        print len(bincenters)
            
        yerror = sqrt(t[0])
        yplot = log10(yvalue)
        plot(bincenters, yplot,'bo') 
        ylabel('log(N)')
        xlabel('log(L)')
        yerrup=log10(yvalue+yerror)-log10(yvalue)
        yerrdown=log10(yvalue)-log10(yvalue-yerror)
        yerrboth=zip(yerrdown,yerrup)
        yerrboth=transpose(yerrboth)
        errorbar(bincenters, yplot, yerr=yerrboth)
        legend(['All-Sky Survey'], loc='upper right')

        #ax=gca()
        #ax.set_yscale('log')
        #ax=gca()
         #ax.set_xscale('log')
        Lvalues = linspace(-2, 25, 100)
        Llinear = 10**(Lvalues)
        schect = 55*(Llinear**(-0.25))*exp(-Llinear)
        plot(Lvalues, log10(schect))

nsa=nasasloan()

    
"""alphabest=0.
    logphistarbest=0.
    loglstarbest=0.
    chisqmin=1.*10**7

    for i in range(len(yerror)):
        if yerror[i]==0:
            yerror[i]=0.1

        for alpha in arange(-2,2,.1):
            for loglstar in arange(-1,1,.1):
                for logphistar in arange(-3,3,.1):
                    a=log(10)*10.**logphistar
                    b=(10.**array(bincenters))/(10.**loglstar)
                    c=alpha+1
                    d=exp(-(10**array(bincenters))/(10.**loglstar))
                    yfit=a*(b**c)*d
                    chisq = sum(log(array(yfit-yvalue)**2./array(yerror)**2.))
                    if chisq < chisqmin:
                        alphabest = alpha
                        loglstarbest = loglstar
                        logphistarbest = logphistar
                        chisqmin=chisq
                        yfit2=a*(b**c)*d

plot(bincenters, log10(yfit2))
show()

print 'alpha = ' + str(alphabest)
print 'loglstar = ' + str(loglstarbest)
print 'logphistar = ' + str(logphistarbest)
print 'chisqmin = ' + str(chisqmin)"""

        

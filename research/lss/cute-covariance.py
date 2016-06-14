#!/usr/bin/python

from __future__ import division, print_function

import os
import sys
import argparse
import glob

import numpy as np
import matplotlib.pyplot as plt
import pdb

def main():
    
    # argument parsing
    parser = argparse.ArgumentParser()

    parser.add_argument('--dr', type=str, default='dr11', help='Specify the SDSS data release.')
    parser.add_argument('--type', type=str, default='3D_rm', help='Specify the correlation type used.')
    parser.add_argument('--cov', action='store_true', help='Compute the covariace matrix.')

    args = parser.parse_args()

    # convenience variables
    datadir = os.path.join(os.getenv('LSS_BOSS'), args.dr, 'cuteout', args.type)
    corrfiles = glob.glob(os.path.join(datadir, '*_fkp_????.dat'))
    outdir = os.path.join(os.getenv('LSS_BOSS'), args.dr, 'covariance')

    corrfiles = corrfiles[:20] # testing!
    ncorr = len(corrfiles)
    xi = np.zeros((ncorr, 2, 2000))

    for ii, cfile in enumerate(corrfiles):
        print('Reading {}'.format(cfile))
        data = np.loadtxt(cfile)
        xi[:,ii] = data[:,2] # grab xi

    cov = np.zeros((20, 2000))
    xibar = np.mean(xi, axis=0)

    for mm, corrf in enumerate(xi): # (0, thing[0])
        for jj, _ in enumerate(corrf):
            if jj < 1999:
                cov[mm, jj] = (corrf[jj]-xibar[mm])*(corrf[jj+1]-xibar[mm])
    pdb.set_trace()
        
    # sys.exit(1)
    # if args.cov:
                    
if __name__ == "__main__":
    main()
    

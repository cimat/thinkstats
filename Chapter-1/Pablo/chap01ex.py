"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys
import pandas as pd

#import nsfg
#import thinkstats2

def read_gzip_file(filename):
	df = pd.read_csv(filename, compression='gzip', header=0, sep=',', quotechar='"')
	return df

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    df = read_gzip_file('../../data/2002FemResp.dat.gz')

    print(df.columns)




if __name__ == '__main__':
    main(*sys.argv)

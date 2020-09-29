#Author(s): Bikram Keshari Sahu (15051) and Parth Nayak (15118)
#Code under the project of the course PHY312 Numerical Methods and Programming

import time
t1=time.clock()

import pyfits as pf
#import median as mdn
import numpy as np
import statistics as st

print "Collecting all the bias files..."

with open("bias.in") as bias_list:
    BL=[line for line in bias_list]

n=len(BL)
BL=[BL[i].split("\n")[0] for i in range(n)]
DL=[pf.getdata(s) for s in BL]

print "The bias files collected are:"
for i in BL:
    print i
    
print "Combining all bias files as median..."

mbias=st.median_arrays(DL)

print "Saving median bias..."

pf.writeto("mbias.fits", mbias, clobber=True)

print "Median bias is saved as mbias.fits."

t2=time.clock()
T=abs(t2-t1)
print "The taken for execution of the program is", T, "seconds."
    
    

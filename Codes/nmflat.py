#Author(s): Bikram Keshari Sahu (15051) and Parth Nayak (15118)
#Code under the project of the course PHY312 Numerical Methods and Programming

import time
t1=time.clock()

import numpy as np
import pyfits as pf
import statistics as st

print "Collecting all flat files..."

with open("flat.in") as flat_list:
    FL=[line for line in flat_list]

FL=[x.split("\n")[0] for x in FL]

print "Flats collected are:"
for i in FL:
    print i
    
DL=[pf.getdata(s) for s in FL]

print "Getting MBias..."

#mbias=pf.getdata("mbias.fits")

#print "Subtracting MBias from all flats..."

CDL=DL

print "Combining all clean flats as median..."

mflat=st.median_arrays(CDL)

print "Normalising median flat..."

mean=st.avg(mflat)
nmflat=1.0*mflat/mean

print "Saving Normalised median flat..."

pf.writeto("nmflat.fits", nmflat, clobber=True)

print "Normalized median flat is saved as nmflat.fits."

t2=time.clock()
T=abs(t2-t1)
print "Time taken for execution of the program is", T,"seconds."

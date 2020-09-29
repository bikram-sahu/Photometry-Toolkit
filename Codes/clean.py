#Author(s): Bikram Keshari Sahu (15051) and Parth Nayak (15118)
#Code under the project of the course PHY312 Numerical Methods and Programming

import time
t1=time.clock()

import numpy as np
import pyfits as pf

print "Collecting all science frames..."

with open("sci.in") as sci_list:
    SL=[line for line in sci_list]

SL=[x.split("\n")[0] for x in SL]
NL=[x.split(".fits")[0] for x in SL]
DL=[pf.getdata(x) for x in SL]

print "Science frames collected are:"
for i in SL:
    print i

print "Collecting MBias..."
mbias=pf.getdata("mbias.fits")

print "Collecting NMFlat..."
nmflat=pf.getdata("nmflat.fits")

print "Cleaning science frames now..."

CSF=[(k-mbias)/nmflat for k in DL]

print "Saving clean science frames..."

for i in range(len(CSF)):
    pf.writeto('Clean/'+NL[i]+'_clean.fits', CSF[i], clobber=True)
    print NL[i]+'_clean.fits'

print "Clean science frames saved successfully"

t2=time.clock()
T=abs(t2-t1)

print "Time taken for execution of the program is", T, "seconds"

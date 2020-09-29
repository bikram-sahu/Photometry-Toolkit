#Author(s): Bikram Keshari Sahu (15051) and Parth Nayak (15118)
#Code under the project of the course PHY312 Numerical Methods and Programming


import time
t1=time.clock()

import numpy as np
import pyfits as pf
import crop_data as cd

print "Collecting all clean science frames..."

with open("clean.in") as clean_list:
    CL=[line for line in clean_list]

CL=[x.split("\n")[0] for x in CL]

print "Clean files collected are:"
for i in CL:
    print i
    
DL=[pf.getdata(x) for x in CL]
NL=[x.split(".fits")[0] for x in CL]

print ""
xl=100
xr=100
yt=0
yb=0
print ""
print "Applying crop now..."

CCL=[cd.crop(DL[i],xl,xr,yt,yb) for i in range(len(DL))]

print "Saving cropped frames in the directory Crop..."

for i in range(len(CCL)):
    pf.writeto('Crop/'+NL[i]+'_crop.fits', CCL[i], clobber=True)
    print NL[i]+'_crop.fits'

print "Cropped clean science frames saved successfully."

t2=time.clock()
T=abs(t2-t1)
print "Time taken for execution of the program is", T, "seconds."

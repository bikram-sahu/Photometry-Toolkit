#Author(s): Bikram Keshari Sahu (15051) and Parth Nayak (15118)
#Code under the project of the course PHY312 Numerical Methods and Programming

import time
t1=time.clock()

import pyfits as pf
import numpy as np

with open("crop.in") as crop_list:
    CRL=[line for line in crop_list]

CRL=[x.split("\n")[0] for x in CRL]
CDL=[pf.getdata(x) for x in CRL]
NL=[x.split(".fits")[0] for x in CRL]

# Please mention the path of the sci.in file with in the " " as shown 
with open("/Users/Bikram/Project/Raw/Obj/sci.in") as sci_list:
    #Please mention the path of the Obj directory with in the " " as shown
    DL=["/Users/Bikram/Project/Raw/Obj/"+line for line in sci_list]

DL=[x.split("\n")[0] for x in DL]

for i in range(len(DL)):
    hd_raw=pf.open(DL[i])[0].header
    hd_upd=pf.open(CRL[i])[0].header
    DoO=hd_raw['DATE-OBS']
    Ut=hd_raw['UT']
    ToE=hd_raw['EXPTIME']
    hd_upd.append(('DATE-OBS',DoO, 'Date of Observation'), end=True)
    hd_upd.append(('UT', Ut, 'Universal Time at the end of Exposure'), end=True)
    hd_upd.append(('EXPTIME', ToE, 'Exposure Time in miliseconds'), end=True)
    pf.writeto(NL[i]+'.fits',CDL[i], header=hd_upd, clobber=True)


dt=pf.open("J0901p3846_R.4578.0_clean_crop.fits")
#print type(dt)
hd=dt[0].header
#print type(hd)
print hd['EXPTIME']

t2=time.clock()
T=abs(t2-t1)
print "Time taken is:", T, "seconds"

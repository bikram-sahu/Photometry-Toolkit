#Author(s): Bikram Keshari Sahu (15051) and Parth Nayak (15118)
#Code under the project of the course PHY312 Numerical Methods and Programming

import time
t1=time.clock()

import pyfits as pf
import numpy as np
import photometry as pm
import sky 
from math import *

print "Collecting crops..."

with open("crop.in") as crop_list:
    UCL=[line for line in crop_list]

UCL=[x.split("\n")[0] for x in UCL]
NL=[x.split(".fits")[0] for x in UCL]

print "Crops collected are:"
for i in UCL:
    print i

print "\nCollecting coordinates..."

X=[]; Y=[] #list of X and Y coordinates of the stars
with open("coordinates.dat") as cd:
    for line in cd:
        X.append(float(line.split('\t')[0]))
        Y.append(float(line.split('\t')[1]))

outfile=open("light_curve_data.txt", "w") 
#output file for plotting the light curves
print "\nThe output is getting redirected to 'light_curve_data.txt' in the present working directory. This may take a while..."
outfile.write("#UT\tObs. Date\tStar 1\tStar 2\tStar 3\tS2-S1\tS3-S1\tS3-S2 (As in the order specified in 'coordinates.dat')\n")

for i in range(len(UCL)):
    data=pf.getdata(UCL[i])
    print UCL[i]
    hd=pf.open(UCL[i])[0].header
    t_exp=float(hd['EXPTIME'])/1000.
    date_obs=hd['DATE-OBS'].split(" ")[0]
    u_time=hd['UT']
    outfile.write(str(u_time)+"\t")
    outfile.write(str(date_obs)+"\t")
    mag=[]
    for j in range(len(X)):
        N_ap, A_ap =pm.photo(data,X[j],Y[j])
        S_sky=sky.base(data,X[j],Y[j])
        mI=-2.5*log((N_ap-A_ap*S_sky)/t_exp, 10.)
        mag.append(mI)
        outfile.write(str(mI)+"\t")
    dm1=mag[1]-mag[0]; dm2=mag[2]-mag[0]; dm3=mag[2]-mag[1]
    outfile.write(str(dm1)+"\t")
    outfile.write(str(dm2)+"\t")
    outfile.write(str(dm3)+"\n")

outfile.close()

print "SUCCESS: Output is saved as 'light_curve_data.txt'."

t2=time.clock()
T=abs(t2-t1)
print "Time taken for execution is", T, "seconds."

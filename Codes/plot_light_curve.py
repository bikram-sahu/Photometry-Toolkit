import time as tm
import datetime as dt
t1=tm.clock()

import matplotlib.pylab as plt
import matplotlib as mp
import numpy as np

fig=plt.figure()

lc_data=open("light_curve_data.txt","r")
lc_data.readline() #skipping the first line
dm1=[]; dm2=[]; dm3=[]
time=[]
for line in lc_data:
    l=line.split("\t")
    time.append(dt.datetime.fromtimestamp(tm.mktime(tm.strptime(l[0]+" "+l[1],"%H:%M:%S %Y-%m-%d")))) #+" "+l[0]
    dm1.append(float(l[5])); dm2.append(float(l[6])); dm3.append(float(l[7]))

ax1=fig.add_axes([0.15,0.05,0.8,0.25])#, ylim=(-1.5,1.5))
ax2=fig.add_axes([0.15,0.35,0.8,0.25], xticklabels=[])#, ylim=(-1.5,1.5))
ax3=fig.add_axes([0.15,0.65,0.8,0.25], xticklabels=[])#, ylim=(-1.5,1.5))

time = mp.dates.date2num(time)
#matplotlib.pyplot.plot_date(dates, values)

ax1.plot_date(time, dm1,"b-")
ax2.plot_date(time, dm2,"b-")
ax3.plot_date(time, dm3,"b-")

ax1.plot_date(time, dm1,"o-", color="green")
ax2.plot_date(time, dm2,"o-", color="blue")
ax3.plot_date(time, dm3,"o-", color="red")

ax1.set_xlabel('UT (HH:MM:SS)')
ax1.set_ylabel('S2 - S1')
ax2.set_ylabel('S3 - S1')
ax3.set_ylabel('S3 - S2')
ax3.set_title('Source: S1 = J0901+3846')
fig.text(0.04, 0.5, 'Differential Instrumental Magnitudes', va='center', rotation='vertical')

plt.show()



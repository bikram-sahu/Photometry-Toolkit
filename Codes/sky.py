#Author(s): Bikram Keshari Sahu (15051) and Parth Nayak (15118)
#Code under the project of the course PHY312 Numerical Methods and Programming

import numpy as np
from math import *
import pyfits as pf
from gaussfit import *
from Analysis import *
from statistics import *

def mask_sky(cdata, cx, cy, tx, ty, fwhm_x, fwhm_y):    
    # Applying mask for S_sky
    y2, x2 = np.ogrid[-cx:tx-cx, -cy:ty-cy]
    mask= x2**2 + y2**2 <= (81*(fwhm_x +fwhm_y)**2)/4.0
    cdata[mask]=None
    mask= x2**2 + y2**2 >= (144*(fwhm_x +fwhm_y)**2)/4.0
    cdata[mask]=None
    MD = []
    for i in cdata:
        for j in i:
            if j > 0.0:
                MD.append(j)
                
    S_sky = mode(MD)
    return S_sky , cdata

def base(A, x_coodinate, y_coordinate):
    (a,b) = nearest_peak(A, x_coodinate, y_coordinate)   #function in Analysis module
    #print (a,b) 
    ax = plt.axes(projection= '3d')    
    x_st = a-55 ; x_en = a+55
    y_st = b-55 ; y_en = b+55
    z = []
    for i in range(y_st, y_en+1, 1):
        temp = []
        for j in range(x_st, x_en+1, 1):
            temp.append(A[i][j])
        z.append(temp)
    x = np.linspace(x_st, x_en, (x_en - x_st) + 1)
    y = np.linspace(y_st, y_en, (y_en - y_st) + 1)
    Xin, Yin = np.meshgrid(x, y)
    z = np.array(z)
    data = z
    cdata = data
    params = fitgaussian(data)
    fit = gaussian(*params)
    (height, x, y, width_x, width_y, base) = params
    fwhm_x = 2*sqrt(log(2.0))*width_x
    fwhm_y = 2*sqrt(log(2.0))*width_y
    S_sky , cdata = mask_sky(cdata, 54, 55, 111, 111, fwhm_x, fwhm_y)
    ax.scatter(Xin, Yin, cdata)
    return S_sky
    
if __name__ == '__main__':   
    A = pf.getdata("J0901p3846_R.4578.0_clean_crop.fits")
    print base(A, 960, 150)
    plt.show()
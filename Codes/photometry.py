#Author(s): Bikram Keshari Sahu (15051) and Parth Nayak (15118)
#Code under the project of the course PHY312 Numerical Methods and Programming

import numpy as np
from math import *
import matplotlib.pylab as plt
import pyfits as pf
from mpl_toolkits import mplot3d
from gaussfit import *
from Analysis import *
from statistics import *

def mask1(z, cx, cy, tx, ty, fwhm_x, fwhm_y):   
    # Applying mask for N_ap and A_ap
    y2, x2 = np.ogrid[-cx:tx-cx, -cy:ty-cy]
    mask = x2**2 + y2**2 >= 4*(fwhm_x +fwhm_y)**2
    z[mask] = None
    
    A_ap = 0.0
    N_ap = 0.0
    for i in z:
        for j in i:
            if j > 0.0:
                A_ap +=1
                N_ap +=j
                
    return (N_ap, A_ap, z) 

# This function will take Clean science frames and, the x and y coordinates of the star as defined below and return Star count in the aperture and Area of the aperture in pixels in the order as (N_ap, A_ap)
def photo(A, x_coodinate, y_coordinate):
    ax = plt.axes(projection = '3d')
    (a,b) = nearest_peak(A, x_coodinate, y_coordinate)   #function in Analysis module
    print (a,b)     
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
    (N_ap , A_ap, z) = mask1(z, 54, 55, 111, 111, fwhm_x, fwhm_y)
    ax.scatter(Xin, Yin, z)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('pixel count')
    
    
    return N_ap, A_ap 


if __name__ == '__main__':   
    A = pf.getdata("J0901p3846_R.4578.0_clean_crop.fits")
    print photo(A, 960, 150)
    plt.show()
         
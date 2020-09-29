#Author(s): Bikram Keshari Sahu (15051) and Parth Nayak (15118)
#Code under the project of the course PHY312 Numerical Methods and Programming


import numpy as np
from math import *
import matplotlib.pylab as plt
import pyfits as pf
from mpl_toolkits import mplot3d
from gaussfit import *
from Analysis import *

def plot_all_star(A):
    L = all_peaks(A)
    for h in range(len(L)):
        ax = plt.axes(projection='3d')
        (a, b) = L[h]
        x_st = a-25 ; x_en = a+25
        y_st = b-25 ; y_en = b+25
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
        plt.matshow(data, cmap=plt.cm.gist_earth_r)
        params = fitgaussian(data)
        fit = gaussian(*params)
        p =ax.plot_surface(Xin, Yin, fit(*np.indices(data.shape)), cmap=plt.cm.copper)
        ax.scatter(Xin, Yin, z, marker = '.')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.colorbar()
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('pixel count')
        ax = plt.gca()
        (height, x, y, width_x, width_y, base) = params
        fwhm_x = 2*sqrt(log(2.0))*width_x
        fwhm_y = 2*sqrt(log(2.0))*width_y
        print 'Coordinates of the target Object',(a,b)
        #print 'FWHM-X =', fwhm_x, '\nFWHM-Y =', fwhm_y
        print 'Sky base =' , base
        print 'Peak value =', height
        print 'Mean (x,y) =', (x,y)
        plt.show()
        
    return None
if __name__ =='__main__':
    A = pf.getdata("J0901p3846_R.4578.0_clean_crop.fits")
    plot_all_star(A)
    
        

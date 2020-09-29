#Author(s): Bikram Keshari Sahu (15051) and Parth Nayak (15118)
#Code under the project of the course PHY312 Numerical Methods and Programming

from matplotlib.pylab import *
import pyfits as pf
from math import *


def local_peak(A, y, x, ar):
    c = 0
    for i in range(y-ar, y+ar):
        for j in range(x-ar, x+ar):
            if A[i][j] > A[y][x]:
                c +=1
    return c 


def crude(A, x, y):
    ar = 1
    threshold = 10000.0
    z = []
    for i in y:
        for j in x:
            if A[i][j] > threshold:
                if local_peak(A, i, j, ar) == 0:
                    z.append((j,i))
    return z
              


def pk(A, z, ar):
    P = []
    for (j,i) in z:
        if local_peak(A, i, j, ar) ==0:
            P.append((j,i))
    return P

def regional_peaks(A, x_start, x_end, y_start, y_end):
    x = []
    y = []
    for i in range(x_start, x_end):
        x.append(i)
    for j in range(y_start, y_end):
        y.append(j)
    
    z = crude(A, x, y)
    L = z
    for ar in range(2, 15, 4):
        L = pk(A, L, ar)
    return L

def all_peaks(A):
    x_start = 50
    y_start = 50
    x_end = len(A[0]) -50
    y_end = len(A) - 50
    x = []
    y = []
    for i in range(x_start, x_end):
        x.append(i)
    for j in range(y_start, y_end):
        y.append(j)
    
    z = crude(A, x, y)
    L = z
    for ar in range(2, 15, 4):
        L = pk(A, L, ar)
    return L

def nearest_peak(A, x, y):
    L = all_peaks(A)
    (a1, b1) = L[0]
    d1 = sqrt((x-a1)**2 + (y-b1)**2)
    for i in range(1, len(L)):
        (a,b) = L[i]
        d = sqrt((x-a)**2 + (y-b)**2)
        if d < d1:
            d1 = d
            (a1, b1) = (a, b)
    return (a1,b1)

    

if __name__ == '__main__':
    A = pf.getdata("J0901p3846_R.4578.0_clean_crop.fits")
    #k = peaks(A, 900, 980, 100, 200)
    k = all_peaks(A)
    print k
    X = []
    Y = []
    for (j, i) in k:
        print A[i][j]
        X.append(j)
        Y.append(i)
    
    scatter(X,Y, marker = '.')
    show()


    
            
            
        
        

        
            
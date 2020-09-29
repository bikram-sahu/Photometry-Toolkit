#Author(s): Bikram Keshari Sahu (15051) and Parth Nayak (15118)
#Code under the project of the course PHY312 Numerical Methods and Programming

import numpy as np
import pyfits as pf

def crop(A, xl , xr, yu, yd):
    B = []
    n = len(A)
    m = len(A[0])
    for i in range(yu , n-yd):
        t = []
        for j in range(xl, m-xr):
            t.append(A[i][j])
        B.append(np.array(t))
    B = np.array(B)
    return B
    
C = pf.getdata("J0901p3846_R.4577.0_clean.fits")
G = crop(C, 100, 100, 0, 0)
pf.writeto("J0901p3846_R.4577.0_clean_crop.fits", G, clobber=True)
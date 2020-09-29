#Author(s): Bikram Keshari Sahu (15051) and Parth Nayak (15118)
#Code under the project of the course PHY312 Numerical Methods and Programming


################### MODULE FOR STATISTICS#############################

import numpy as np

# To find the median of a list of numbers
def med(A):
    for i in range(len(A)):
        for j in range(i,len(A)):
            if A[j] < A[i]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    l = len(A)
    if l%2 != 0:
        m = A[(l-1)/2]
    elif l%2 == 0:
        m = 0.5*(A[l/2] + A[(l/2)-1])
    return m
    
    
# To return a 2D Array with median values at each pixel.
def median_arrays(a):
    A = []
    n = len(a)
    for i in range(len(a[0])):
        t = []
        for j in range(len(a[0][i])):
            x = []
            for k in range(n):
                x.append(a[k][i][j])
            for g in range(len(x)):
                for h in range(i,len(x)):
                    if x[h] < x[g]:
                        temp = x[g]
                        x[g] = x[h]
                        x[h] = temp
            l = len(x)
            if l%2 != 0:
                m = x[(l-1)/2]
            elif l%2 == 0:
                m = 0.5*(x[l/2] + x[(l/2)-1])
            
            t.append(m)
        A.append(np.array(t))
    A = np.array(A)   
    return A


# To find the mean of a two dimensional array.
def avg(A):
    n = []; s = 0.0; k = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            s = s + A[i][j]
            k = k+1
    m = s/k
    return m

# To return a 2D array with mean values at each pixel.

def mean_arrays(a):
    A = []
    n = len(a)
    for i in range(len(a[0])):
        t = []
        for j in range(len(a[0][i])):
            x = []
            for k in range(n):
                x.append(a[k][i][j])
            s = 0.0
            for g in range(len(x)):
                s = s + x[g]
            m = s/len(x)
            t.append(m)
        A.append(np.array(t))
    A = np.array(A)   
    return A

# To return mode of a one dimensional list   
def mode(a):
    b=[a]
    return 3*med(a)-2*avg(b)

                
    
    
    
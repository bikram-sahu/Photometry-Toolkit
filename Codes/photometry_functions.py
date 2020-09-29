#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:49:26 2019

@author: Parth Nayak
"""

import numpy as np

def circular_sum(data, center, radius):
    X       = center[0]
    Y       = center[1]
    x       = np.arange(data.shape[1])
    y       = np.arange(data.shape[0])
    circle  = (x - X)**2 + (y - Y)**2 <= radius**2
    data    = data[circle]
    total   = np.sum(data)
    return total

def gaussian(height, center_x, center_y, width_x, width_y, base):
    #Returns a gaussian function with the given parameters
    width_x = float(width_x)
    width_y = float(width_y)
    return lambda x,y: base +height*np.exp(
                -(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2)/2)

def moments(data):
    #Returns (height, x, y, width_x, width_y, base ) the gaussian parameters of a 2D distribution by calculating its moments
    total = data.sum()
    base = 2725
    X, Y = np.indices(data.shape)
    x = (X*data).sum()/total
    y = (Y*data).sum()/total
    col = data[:, int(y)]
    width_x = np.sqrt(np.abs((np.arange(col.size)-y)**2*col).sum()/col.sum())
    row = data[int(x), :]
    width_y = np.sqrt(np.abs((np.arange(row.size)-x)**2*row).sum()/row.sum())
    height = data.max()
    return height, x, y, width_x, width_y, base

def fitgaussian(data):
    #Returns (height, x, y, width_x, width_y, base) the gaussian parameters of a 2D distribution found by a fit
    from scipy import optimize
    params = moments(data)
    errorfunction = lambda p: np.ravel(gaussian(*p)(*np.indices(data.shape)) -
                                 data)
    p, success = optimize.leastsq(errorfunction, params)
    return p
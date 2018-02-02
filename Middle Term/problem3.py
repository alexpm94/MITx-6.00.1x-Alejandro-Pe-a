#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:37:37 2017

@author: alexpm94
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    exponent=0
    while True:
        x=base**exponent
        if x>num:
            h=x-num
            l=num-base**(exponent-1)
            if min(h,l)==l:
                return exponent-1
            else:
                return exponent
        exponent+=1
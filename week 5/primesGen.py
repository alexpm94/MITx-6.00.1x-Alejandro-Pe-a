#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:07:34 2017

@author: alexpm94
"""

def genPrimes():
    '''
        Generator for prime numbers
    '''
    next=2
    primes=[2]
    while True:
        next+=1
        for p in primes:
            if (next%p)==0:
                break
        else:
            yield primes[-1]
            primes.append(next)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:10:54 2018

@author: alexpm94
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    newL=[-1]+sorted(L)
    count=1
    nd={}
    for i in range(len(newL)-1):
        if newL[-1-i]==newL[-2-i]:
            count+=1
        else:
            nd[newL[-1-i]]=count
            print(nd)
            if count&1:
                return newL[-1-i]
            count=1
    return None

L=[3, 0, 5, 3, 5, 3]
print(largest_odd_times(L))
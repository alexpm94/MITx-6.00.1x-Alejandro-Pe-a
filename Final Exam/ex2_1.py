#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:37:16 2018

@author: alexpm94
"""
L=[3, 9,9, 5, 3, 5,1,9]

def largest_odd_times(L):
    
    newL=[-1]+sorted(L)
    count=1
    for i in range(len(newL)-1):
        if newL[-1-i]==newL[-2-i]:
            count+=1
        else:
            if count&1:
                return newL[-1-i]
            count=1
    return None

print(largest_odd_times(L))
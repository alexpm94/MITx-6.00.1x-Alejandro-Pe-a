#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 12:03:48 2017

@author: alexpm94
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
    keyList=[]
    for k in aDict:
        if aDict[k]==target:
           keyList.append(k)
    return keyList
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:58:18 2017

@author: alexpm94
"""
#This function returns the substrins in a list with fewer tha 4 characters
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    b=[]
    for sub in aList:
        if len(sub)<4:
            b.append(sub)
    return b
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:07:47 2018

@author: alexpm94
"""
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

def f(a,b):
    return a+b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    nd1={}
    nd2={}
    for i in d1:
        if i in d2:
            nd1[i]=f(d1[i],d2[i])
        else:
            nd2[i]=d1[i]
            
    for i in d2:
        if not i in d1:
            nd2[i]=d2[i]
    
    return (nd1,nd2)
    
print(dict_interdiff(d1, d2))
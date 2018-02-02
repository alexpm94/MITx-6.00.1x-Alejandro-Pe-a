#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:07:47 2018

@author: alexpm94
"""
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}

def f1(a,b):
    return a>b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    nd1={}
    nd2={}
    ks=sorted(sorted(d1)+sorted(d2))+[-1]#keys sorted
    count=1
    for i in range(len(ks)-1):
        if ks[i]==ks[i+1]:
            nd1[ks[i]]=f1(d1[ks[i]],d2[ks[i]])
            count+=1
        else:
            if count<2:
                if d1.get(ks[i],0)!=0:                
                    nd2[ks[i]]=d1[ks[i]]
                else:
                    nd2[ks[i]]=d2[ks[i]]
            count=1
    return (nd1,nd2)
    
print(type(dict_interdiff(d1,d2)))
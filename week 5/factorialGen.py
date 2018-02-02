#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:07:34 2017

@author: alexpm94
"""

def genFact():
    '''
        Generator for factorial function
    '''
    x=1
    next=1
    while True:
        next*=x
        yield next
        x+=1
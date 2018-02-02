#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 12:26:47 2017

@author: alexpm94
"""
def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    Lcopy=L[:]
    for sub in Lcopy:
        if f(sub)==False:
            L.remove(sub)
    return len(L)

L = ['a?']
print (satisfiesF(L))
print (L)
print(f(L))
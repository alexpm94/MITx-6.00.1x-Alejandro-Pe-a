#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:52:45 2018

@author: alexpm94
"""

class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        #FILL THIS IN
        self.repr=[]
        
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        #FILL THIS IN
        try:
            self.delete(k)
            return self.repr.append((k,v))
        except KeyError:
            return self.repr.append((k,v))
        
        
    def getval(self, k):
        """ k, immutable object  """
        #FILL THIS IN
        for i in self.repr:
            if i[0]==k:
                return i[1]
        raise KeyError
        
    def delete(self, k):
        """ k, immutable object """   
        #FILL THIS IN
        for i in self.repr:
            if i[0]==k:
                return self.repr.remove(i)
        raise KeyError
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 03:13:41 2022

@author: anurag
"""

def bin_search(nums, t):
    
    l = 0
    r = len(nums) - 1
    
    while l<=r:
       mid = (l+r)//2
       num = nums[mid]
       
       if num == t:
           return mid
       elif num < t: 
           l = mid+1
       elif num > t:
           r = mid-1
           
    return -1
      
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:37:52 2022

@author: anurag
"""
import numpy as np

def outlier_removal(nums):
    nums = sorted(nums)
    nums2 =[]
    iq1 = np.quantile(nums, 0.25)
    iq3 = np.quantile(nums, 0.75)
    
    iqr = iq3 - iq1
    
    upper_bound = iq3 + 1.5*iqr
    lower_bound = iq1 - 1.5*iqr
    
    print('Inter-Quartile-Range: ',iqr)
    print('upper-bound: ',upper_bound)
    print('lower-bound: ',lower_bound)
    
    for i in range(len(nums)):
        if nums[i] < upper_bound and nums[i]>lower_bound:
            nums2.append(nums[i])
        else:
            continue
    
    return nums2
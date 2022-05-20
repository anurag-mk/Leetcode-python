#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 02:07:01 2022

@author: anurag
"""

def dest_city(paths):
    out_cnt = {}
    
    for i in paths:
        city_a, city_b = i
        out_cnt[city_a] = out_cnt.get(city_a,0) + 1
        out_cnt[city_b] = out_cnt.get(city_b,0)

    for city in out_cnt:
        if out_cnt[city] ==0:
            return city
        
        
def to_set():
    
    list1 = ['SF','LA']
    list2 = ['MN','SF']
    
    set1 = set(list1)
    set2 = set(list2)
    
    return (set1 - set2)
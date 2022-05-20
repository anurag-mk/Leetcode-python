#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 01:55:03 2022

@author: anurag
"""
def interpret(command):
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        
        return print(command)
        
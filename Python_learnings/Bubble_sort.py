#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: trying.py
# Created: Monday, 30th May 2022 1:34:31 pm
# Author: Azwad Aziz (azwad.a02@hotmail.com)
# -----
# Last Modified: Monday, 30th May 2022 9:50:44 pm
# Modified By: Azwad Aziz (azwad.a02@hotmail.com)
# -----
# Copyright (c) 2022 Dreams
###



# Bubble sort

a = [2,4,1,5,6,3]

for j in range(len(a)):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:


            a[i] , a[i+1] = a[i+1] , a[i]

        else:
            continue


print(a)


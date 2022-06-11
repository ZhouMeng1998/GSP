#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# logging flags
print_info_progress = 1
print_info = 0

# action flags
conduct_unit_tests = 0
conduct_experiments = 1

# datasets parameters
data_ind = 2
data_sources = ['For Bike', 'For Leviathan', 'For Retail']
dname = data_sources[data_ind]

# gsp parameters
minsup = 0.45
wSize = 0
minGap = 0
maxGap = float('inf')

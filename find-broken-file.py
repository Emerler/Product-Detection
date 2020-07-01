# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 21:16:00 2020

@author: Emerl2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
import tensorflow as tf

train_path = r'C:\Users\Emerl2\shopee-product-detection-student\train\train\train\\'
test_path = r'C:\Users\Emerl2\shopee-product-detection-student\test\test\test\\'

broken_fnames = []
for label in os.listdir(train_path):
    label_path = train_path + label
    for filename in os.listdir(label_path):
        if len(filename) > 36:
            print(label_path + filename)
            broken_fnames.append(label_path + filename)
            
print()
for filename in os.listdir(test_path):
    if len(filename) > 36:
        print(test_path + filename)
        broken_fnames.append(test_path + filename)
        
f = open('broken-file-names.txt', 'w')
f.write('\n'.join(broken_fnames))
f.close()
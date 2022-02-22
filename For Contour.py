# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:38:26 2022

@author: Student
"""

import numpy as np
import pandas as pd
import os
import fnmatch
import matplotlib.pyplot as plt
import re

file = r'C:\Users\Student\OneDrive - University of Tennessee\Desktop\Research\MPS (M = Cr, Mn)\MnPS3\Amal\1_28_2016_Amal_variable_temp_MnPS3\python'
os.chdir(file)
cwd = os.getcwd()
print(cwd)
list = os.listdir(file)
print(list)

Contour_data = np.empty([356,3])


for k in range(len(list)):
    if fnmatch.fnmatch(list[k],'*.asc*'):
        filename = list[k]
        regex = re.compile(r'\d+')
        temp_name = regex.findall(filename)
        for item in temp_name:
            float(item)
            
        Contour = np.empty([356,3])
        Contour[:,0] = item
              
        pd_data = pd.read_csv(list[k])
        np_data = pd_data.to_numpy()
        
        Contour[:,1] = np_data[:,2]
        Contour[:,2] = np_data[:,5]
        
        Contour_data = np.append(Contour_data,Contour,axis=0)
        pd_contour_data = pd.DataFrame(Contour_data,columns=['Temperature','Energy (eV)','Absorption'])
pd_contour_data.to_csv('Contour Data.txt',index=False)

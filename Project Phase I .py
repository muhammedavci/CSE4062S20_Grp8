# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:30:42 2020

@author: Furkan
"""

import numpy as np
import pandas as pd


df=pd.read_excel("Project.xlsx")


print(df.head(100))
for items in df.columns:
    print("Type of the ",items,"column"," is :",df[items].dtype)

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:08:10 2023

@author: Dipsha
"""
import pandas as pd
from centralTendency import centralTendancy as CT

read_data = pd.read_csv("D:/CODE/python/iris/iris.data", sep = ',', header=None)
# print(read_data)

"""
7. Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      -- Iris Setosa
      -- Iris Versicolour
      -- Iris Virginica

"""
column_names = ["SepalLength_in_cm", "SepalWidth_in_cm", "PetalLength_in_cm", "PetalWidth_in_cm", "Class"]
read_data.columns = column_names

CT_obj = CT()

for i in column_names[:-1]:
    print("Description of ", i, " column")
    list1 = read_data[i].tolist()
    CT_obj.describe(list1, class_interval=0.5, roundVal=3)
    print()

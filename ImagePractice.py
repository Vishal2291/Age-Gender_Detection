# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 10:41:00 2018

@author: Vishal
"""


import numpy as np
from PIL import Image
import os
path = r"G:\ML Project\PreRequisites\Resizing\New"
alphaArray = []
ages = []
for image_path in os.listdir(path):
    age = int((image_path.split("_")[1]).split(".")[0])
    ages.append(age)
    input_path = os.path.join(path, image_path)
    img = Image.open(input_path)
    arr= np.array(img)
    arr = arr.ravel()
    arr = list(arr)
    alphaArray.append(arr)
    
print(ages)
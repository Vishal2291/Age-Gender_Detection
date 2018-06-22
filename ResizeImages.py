# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 21:00:50 2018

@author: Vishal
"""


import PIL
from PIL import Image
import os
outPath = r"G:\ML Project\New"
path = "G:\ML Project\TestImages"

for image_path in os.listdir(path):
    dob = int(image_path.split('_')[1].split('-')[0])
    yearTaken = int(image_path.split('_')[2][0:4])
    input_path = os.path.join(path, image_path)
    img = Image.open(input_path)
    newres = 120
    wpercent = (newres / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((newres, hsize), PIL.Image.ANTIALIAS)
    fullpath = os.path.join(outPath, image_path.split('_')[0]+'_'+str(yearTaken-dob)+'.jpg')
    img.save(fullpath)
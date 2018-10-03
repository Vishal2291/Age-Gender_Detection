# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 10:41:00 2018

@author: Vishal
"""


import numpy as np
from PIL import Image
import os
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder

def decode(l):
    l1 = []
    for i in l:
        inverted = label_encoder.inverse_transform(i)
        l1.append(inverted)
    return l1
path = r"G:\ML Project\PreRequisites\Resizing\New"
alphaArray = []
ages = []
for image_path in os.listdir(path):
    age = (image_path.split("_")[1]).split(".")[0]
    ages.append(age)
    input_path = os.path.join(path, image_path)
    img = Image.open(input_path)
    arr= np.array(img)
    arr = arr.ravel()
    arr = list(arr)
    alphaArray.append(arr)
label_encoder = LabelEncoder()
ages_enc = label_encoder.fit_transform(ages)
print(ages_enc)
clf = tree.DecisionTreeClassifier()
clf.fit(alphaArray, ages_enc)
#testArray = np.array(Image.open(r"G:\ML Project\PreRequisites\Resizing\7000810_Young.jpg")).ravel()
Testpath = r"G:\ML Project\PreRequisites\Resizing\TrainNew"
ages_original = []
ages_predicted = []
for image_path in os.listdir(Testpath):
    testArray = np.array(Image.open(os.path.join(Testpath,image_path))).ravel()
    predictedAge = clf.predict([testArray])
    ages_predicted.append(predictedAge[0])
    ages_original.append((image_path.split("_")[1]).split(".")[0])

l1 = decode(ages_predicted)
l2 = label_encoder.fit_transform(ages_original)
print(l1)
print(l2)
print(confusion_matrix(l2,ages_predicted))
    

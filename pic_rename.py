# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 13:14:17 2023

@author: uid0555
"""

import cv2
import os
import time
import pandas as pd
import shutil

#%%
image_path=r'C:\Users\uid0555\Desktop\博世\GT\rawdata'
target_path=r'C:\Users\uid0555\Desktop\博世\GT\raw'
i=1
for pics in os.listdir(image_path):
    # name = os.path.basename(image_path)#读取原文件文件名
    # filename = name.split('.')[0]
    
    filefullname=os.path.join(image_path,pics)
    # filename = pics.split('.')[0]
    # print(filename)
    
    shutil.copy(filefullname, os.path.join(target_path,str(i)+'.jpg'))
    i+=1
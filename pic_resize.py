# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:45:58 2024

@author: uid0555
"""


import cv2
import os
 
# 读取原始图片
def pic_resize(input_path,output_path):

# image = cv2.imread('original_image.jpg')
    image = cv2.imread(input_path)
    height, width, channels = image.shape
    image_name=os.path.basename(input_path)
    image_fullname=os.path.join(output_path,image_name)
    print(image_fullname)
    try:
        if height<500:
            # 定义目标尺寸
            new_width = 500
            new_height = 500
             
            # 修改图片尺寸
            resized_image = cv2.resize(image, (new_width, new_height))
            print('尺寸修改完成')
             
            # 保存修改后的图片
            cv2.imwrite(image_fullname, resized_image)
        else:
            cv2.imwrite(image_fullname, image)
    except:
        pass

if __name__ == "__main__":
    import string
    result = list(string.ascii_uppercase) #所有英语字母
    # print(result)
    for letters in result:
        print(letters)
        path1=os.path.join(r'C:\Users\uid0555\Desktop\Vanes',letters)
        path2=os.path.join(r'C:\Users\uid0555\Desktop\Vanes_resize',letters)
        if not os.path.exists(path2):  #输出文件夹不存在则创建
            os.mkdir(path2)
        for pics in os.listdir(path1):
            print(pics)
            filename_pic=os.path.join(path1,pics)
            pic_resize(filename_pic,path2)
#%%
# for pics in os.listdir(image_path):
#     filefullname=os.path.join(image_path,pics)
#     input_path.append(filefullname)
image = cv2.imread(r'C:\Users\uid0555\Desktop\Vanes\A\abkh000002.jpg') 
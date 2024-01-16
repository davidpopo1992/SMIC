# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 09:44:09 2022

@author: uid0555
"""

import cv2
import os
import time
from natsort import natsorted

#解决无法将图片保存到中文路径的问题
def save_image(img_path,img):
    #{img_path:图片路径,img:图片对象}    
    cv2.imencode('.png', img)[1].tofile(img_path)

#将视频切片为图片
def video2images(Video_Dir,freq,output_dir):
     #{Video_Dir:视频路径,freq:每几帧抽一次图片,output_dir:输出图片路径}  
    cap = cv2.VideoCapture(Video_Dir)
    c = 1  # 帧数起点
    index = 1  # 图片命名起点，如1.jpg
 
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
 
    while True:
        # 逐帧捕获
        ret, frame = cap.read()
        # print('目前进到到第%d帧:'%c)
        # 如果正确读取帧，ret为True
        if not ret:
            print("未正确读取或读取已结束")
            # print("Can't receive frame.")
            break
        # freq:设置每x帧取一次图片，若想逐帧抽取图片，可设置c % 1 == 0
        if c % freq == 0:
            # 图片存放路径，即图片文件夹路径
            filename=os.path.join(output_dir, os.path.basename(Video_Dir).replace(".mp4","").replace(".avi","").replace(".mkv","").replace(".h264","")+"_"+str(index) + '.png')
            # filename=os.path.join(output_dir, os.path.basename(Video_Dir).replace(".h264","")+"_"+str(index) + '.png')
            # cv2.imwrite(filename, frame)
            save_image(filename,frame)
            index += 1
        c += 1
        cv2.waitKey(1)
        # 按键停止
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
 
#批量处理视频
def batch_video_process(path,freq,output_dir):
    #{path：视频路径,freq：每几帧抽一次图片，output_dir：输出图片路径}
    if not os.path.exists(output_dir):  #输出文件夹不存在则创建
        os.mkdir(output_dir)
    for each_video in os.listdir(path):
        if os.path.splitext(path)[-1]=='.mp4':
        # if os.path.splitext(path)[-1]=='.ts':
            time_start=time.time()
            print('正在处理的视频为: %s ......'%each_video)
            video_fullname=os.path.join(path,each_video)
            video2images(video_fullname,freq,output_dir)
            print('******该视频抽帧完成')
            time_end=time.time()
            print('处理时长为%.2f分钟'%((time_end-time_start)/60))

#图像转成视频
def makeVideo(path, size):
    #{path：视频路径,size：视频尺寸}
    filelist = os.listdir(path)
    fileist_sort=natsorted(filelist)
    filelist2 = [os.path.join(path, i) for i in fileist_sort]
    # print(filelist2)
    fps = 30  # 我设定位视频每秒1帧，可以自行修改
    # size = (1920, 1080)  # 需要转为视频的图片的尺寸，这里必须和图片尺寸一致
    # video = cv2.VideoWriter(path + "\\Video.mp4", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps,
    #                         size)
    video = cv2.VideoWriter(path + "\\Video.mp4", cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'), fps,
                            size) 

    for item in filelist2:
        print(item)
        # if item.endswith('.jpg'):
        if item.endswith('.png'):
            print(item)
            img = cv2.imread(item)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()
    print('******图片合成视频完成')

#%%
# path=r'C:\shangtang\mp4s\14_19_mask_pics\7'
# size = (1280, 960)  # 需要转为视频的图片的尺寸，这里必须和图片尺寸一致
# makeVideo(path, size)

#%%
if __name__ == "__main__":
    # input_path=[r'C:\工作\2023业务\中汽协示范应用\小鹏\blur1.mp4'
                
                
    #             ]
    image_path=r'C:\工作\2023业务\中汽协示范应用\小鹏\blur2_video'
    input_path=[]
    for pics in os.listdir(image_path):
        filefullname=os.path.join(image_path,pics)
        input_path.append(filefullname)

    print(input_path)
    video_num=len(input_path)
    
    
    output_path=[        
                  r'C:\工作\2023业务\中汽协示范应用\小鹏\blur2'
                  
                  ]  * video_num    
    freq=60
    for i in range(len(input_path)):
        path1=input_path[i]
        path2=output_path[i]
        print(path1,'正在处理...')
        if not os.path.exists(path2):  #输出文件夹不存在则创建
            os.mkdir(path2)
            video2images(path1,freq,path2)
        else:
            video2images(path1,freq,path2)
#     # path=r'C:\Users\uid0555\Desktop\out2'
#     # size=(1920,1080)
#     # makeVideo(path, size)


#%%
# if __name__ == "__main__":
#     for i in range(1,7,1):
#         path=r'C:\Users\uid0555\Desktop\zhiji\1692702300219245_1692702248920481_30_LSJWL4093NS118836\image'
#         filename=str(i)+'.h264'
#         input_path=os.path.join(path,filename)
#         freq=30 
#         output_folder=r'\blur'+str(i)
#         output_path=r'C:\Users\uid0555\Desktop\zhiji\1692702300219245_1692702248920481_30_LSJWL4093NS118836\image'+output_folder
#         if not os.path.exists(output_path):  #输出文件夹不存在则创建
#             os.mkdir(output_path)
#             video2images(input_path,freq,output_path)
#         else:
#             video2images(input_path,freq,output_path)
#         i+=1
# #     # path=r'C:\Users\uid0555\Desktop\out2'
# #     # size=(1920,1080)
# #     # makeVideo(path, size)

#%%
# if __name__ == "__main__":
#     path1=r'C:\工作\2023业务\汽车城匿名化试测\博园路-墨玉南路20230921085428-20230921090928-脱敏.mp4'
#     freq=20
#     output_dir=r'C:\工作\2023业务\汽车城匿名化试测\pics'
#     video2images(path1,freq,output_dir)
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:14:06 2023

@author: uid0555
"""

import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment


def clip_video(source_file, target_file, start_time, stop_time):
  """
  利用moviepy进行视频剪切
  :param source_file: 原视频的路径，mp4格式
  :param target_file: 生成的目标视频路径，mp4格式
  :param start_time: 剪切的起始时间点（第start_time秒）
  :param stop_time: 剪切的结束时间点（第stop_time秒）
  :return:
  """
  validate_file(source_file)
  source_video = VideoFileClip(source_file)
  video = source_video.subclip(int(start_time), int(stop_time)) # 执行剪切操作
  video.write_videofile(target_file) # 输出文件


def clip_audio(source_file, target_file, start_time, stop_time):
  """
  利用pydub进行音频剪切。pydub支持源文件为 mp4格式，因此这里的输入可以与视频剪切源文件一致
  :param source_file: 原视频的路径，mp4格式
  :param target_file: 生成的目标视频路径，mp4格式
  :param start_time: 剪切的起始时间点（第start_time秒）
  :param stop_time: 剪切的结束时间点（第stop_time秒）
  :return:
  """
  validate_file(source_file)
  audio = AudioSegment.from_file(source_file, "mp4")
  audio = audio[start_time * 1000: stop_time * 1000]
  audio_format = target_file[target_file.rindex(".") + 1:]
  audio.export(target_file, format=audio_format)


def combine_video_audio(video_file, audio_file, target_file, delete_tmp=False):
  """
  利用 ffmpeg将视频和音频进行合成
  :param video_file:
  :param audio_file:
  :param target_file:
  :param delete_tmp: 是否删除剪切过程生成的原视频/音频文件
  :return:
  """
  validate_file(video_file)
  validate_file(audio_file)
  # 注：需要先指定音频再指定视频，否则可能出现无声音的情况
  command = "ffmpeg -y -i {0} -i {1} -vcodec copy -acodec copy {2}".format(audio_file, video_file, target_file)
  os.system(command)
  if delete_tmp:
    os.remove(video_file)
    os.remove(audio_file)


def clip_handle(source_file, target_file, start_time, stop_time, tmp_path=None, delete_tmp=False):
  """
  将一个视频文件按指定时间区间进行剪切
  :param source_file: 原视频文件
  :param target_file: 目标视频文件
  :param start_time: 剪切的起始时间点（第start_time秒）
  :param stop_time: 剪切的结束时间点（第stop_time秒）
  :param tmp_path: 剪切过程的文件存放位置
  :param delete_tmp: 是否删除剪切生成的文件
  :return:
  """
  # 设置临时文件名
  if tmp_path is None or not os.path.exists(tmp_path):
    # 如果没有指定临时文件路径，则默认与目标文件的位置相同
    tmp_path = target_file[: target_file.rindex("/") + 1]
  target_file_name = target_file[target_file.rindex("/") + 1: target_file.rindex(".")]
  tmp_video = tmp_path + "v_" + target_file_name + ".mp4"
  tmp_audio = tmp_path + "a_" + target_file_name + ".mp4"

  # 执行文件剪切及合成
  clip_video(source_file, tmp_video, start_time, stop_time)
  clip_audio(source_file, tmp_audio, start_time, stop_time)
  combine_video_audio(tmp_video, tmp_audio, target_file, delete_tmp)


def validate_file(source_file):
  if not os.path.exists(source_file):
    raise FileNotFoundError("没有找到该文件：" + source_file)


#C:\Users\uid0555\Desktop\QVE视频压缩\赵剑_课时9座舱数据不出车和匿名化处理(3).mp4

def test_example():
  """
  测试例子
  :return:
  """
  root_path = r'C:/工作/2023业务/匿名化测试/吉利/'
  video_name = "renlian2.mp4"
  source_file = root_path + video_name
  start_time = 0
  stop_time = 20

  # 设置目标文件名
  target_name = str(start_time) + "_" + str(stop_time)
  target_file = root_path + "_1" + target_name + ".mp4"
  # 处理主函数
  clip_handle(source_file, target_file, start_time, stop_time)


if __name__ == "__main__":
  test_example()
  
  
#%%
#课时_3_数据安全法规解读（中）_1
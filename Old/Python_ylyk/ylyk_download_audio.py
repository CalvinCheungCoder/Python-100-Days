import urllib.request
import json
import ssl
import pymysql
import os
import re

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = 'zhang051109',
                             database = 'ylyk',
                             charset = 'utf8')

cursor = connection.cursor()
context = ssl._create_unverified_context()
# 音频下载
def downloadaudio(audioname, pathname, audiourl):
    audioname = audioname.replace('/','or')
    path = '/Users/zhangdinghao/Downloads/ylyk/' + pathname
    filename = path + '/' + audioname
    folder = os.path.exists(filename)
    if not folder:
        print(' \n音频名称：{0} \n 音频链接：{1}\n 课程名称：{2}'.format(audioname,audiourl,pathname))
        req = urllib.request.Request(audiourl)
        with urllib.request.urlopen(req, context=context) as response:
            audiodata = response.read()
            # 创建课程对应的文件夹
            folder = os.path.exists(path)
            if not folder:
                os.mkdir(path)
            with open(filename,'wb') as f:
                f.write(audiodata)

# 查询课程详情并更新音频链接
sql = 'select *from ylyk_sourse'
cursor.execute(sql)
result_set = cursor.fetchall()
for row in result_set:
    album_name = row[1] # 课程名称
    audio_name = row[2] # 单节课程名
    langurl = row[6]    # 讲解版 URL
    shorturl = row[7]   # 朗读版 URL
    if len(shorturl) > 8:
        audio_name_two = audio_name + '_讲解版.mp3'
        audio_name_three = audio_name + '_朗读版.mp3'
        downloadaudio(audioname=audio_name_two,pathname=album_name,audiourl=langurl)
        downloadaudio(audioname=audio_name_three,pathname=album_name,audiourl=shorturl)
    else:
        audio_name_two = audio_name + '_讲解版.mp3'
        downloadaudio(audioname=audio_name_two,pathname=album_name,audiourl=langurl)
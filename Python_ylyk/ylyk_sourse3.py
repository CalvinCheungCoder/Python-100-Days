# 根据课程的信息拉取课程列表数据
import urllib.request
import json
import ssl
import pymysql

import os
import re

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '123456',
                             database = 'ylyk',
                             charset = 'utf8')

cursor = connection.cursor()
context = ssl._create_unverified_context()

sql = 'select *from ylyk_sourselist'
cursor.execute(sql)
result_set = cursor.fetchall()
for row in result_set:
    print('id：{0} - name：{1} '.format(row[0],row[1],row[2]))
    url = 'https://api.ylyk.com/v1/course/{0}?page=1&size=2000&ischeck=0&order=asc'.format(row[0])
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req,context=context) as response:
        detail_data = response.read()
        json_data = detail_data.decode()
        jsonStr = json.loads(json_data)
        course_list = jsonStr['data'][0]['course_list']
        for course in course_list:
            course_id = course['course_id']
            album_id = course['album_id']
            album_name = course['album_name']
            name = course['name']
            cover_url = course['cover_url']
            teacher_name = course['teacher_name']
            value = (album_id,album_name,name,course_id,teacher_name,cover_url)
            sql = "INSERT INTO ylyk_sourse (album_id, album_name, name, course_id, teacher_name, cover_url) values(%s, '%s', '%s', %s, '%s', '%s')" % value
            try:
                cursor.execute(sql)
                connection.commit()
                print('插入成功\n')
            except:
                connection.rollback()
                print('插入错误\n')
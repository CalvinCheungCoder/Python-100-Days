# 根据课程列表数据拉取每个课程的详情数据
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

sql = 'select *from ylyk_sourse'
cursor.execute(sql)
result_set = cursor.fetchall()
for row in result_set:
    course_id = row[3]
    url = 'https://api.ylyk.com/v1/course/{0}/read'.format(course_id)
    print(url)
    req = urllib.request.Request(url)
    json_data = ''
    with urllib.request.urlopen(req,context=context) as response:
        detail_data = response.read()
        json_data = detail_data.decode("UTF-8")
        json_str = json.dumps(json_data,ensure_ascii=False)

        twosql = "UPDATE ylyk_sourse set detailjson = {0} where course_id = {1}".format(json_str,course_id)
        try:
            cursor.execute(twosql)
            connection.commit()
        except:
            print('sql语句：{0}'.format(twosql))
            connection.rollback()

# 查询课程详情并更新音频链接
sql = 'select *from ylyk_sourse'
cursor.execute(sql)
result_set = cursor.fetchall()
for row in result_set:
    course_id = row[3]
    jsonstr = row[8]
    if jsonstr != None:
        str = json.loads(jsonstr)
        audioarr = str['data'][0]['audio']
        langstr = ''
        shortstr = ''
        if len(audioarr) > 1:
            langstr = audioarr[0]['url']
            shortstr = audioarr[1]['url']
        else:
            langstr = audioarr[0]['url']
            shortstr = None
        sql = "UPDATE ylyk_sourse set langurl = '{0}', shorturl = '{1}' where course_id = {2}".format(langstr, shortstr, course_id)
        try:
            cursor.execute(sql)
            connection.commit()
            print('更新成功\n')
        except:
            connection.rollback()
            print('更新错误\n')
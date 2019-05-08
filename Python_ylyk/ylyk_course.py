# 根据课程列表数据拉取每个课程的详情数据(已存在数据略过)
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

sql = 'select *from ylyk_sourse'
cursor.execute(sql)
result_set = cursor.fetchall()
for row in result_set:
    name = row[2]
    course_id = row[3]
    detail_json = row[8]
    if detail_json:
        print("%s 已存在",name)
    else:
        headers = {"User-Agent": "ylyk/3.5.4 (iPhone; iOS 12.1.4; Scale/3.00)",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Accept-Language": "zh-Hans",
                   "Connection": "keep-alive",
                   "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7",
                   "Authorization": "ZVc5MWJHbHVlVzkxYTJVekxqQT06NVhpaDk1Q28xa2x4RFF2NHd0TmFZNDFxM1Y5NzhzY0k6MjA2MjUw",
                   "source":"phone",}

        url = 'https://api.ylyk.com/v1/course/{0}/read'.format(course_id)
        print(url,name)
        req = urllib.request.Request(url,headers=headers)
        json_data = ''
        with urllib.request.urlopen(req,context=context) as response:
            detail_data = response.read()
            json_data = detail_data.decode("UTF-8")
            json_str = json.dumps(json_data,ensure_ascii=False)

            twosql = "UPDATE ylyk_sourse set detailjson = {0} where course_id = {1}".format(json_str,course_id)
            try:
                cursor.execute(twosql)
                connection.commit()
                print('保存成功 %s', name)
            except:
                print('sql语句：{0}'.format(twosql))
                connection.rollback()

# 查询课程详情并更新音频链接
# sql = 'select *from ylyk_sourse'
# cursor.execute(sql)
# result_set = cursor.fetchall()
# for row in result_set:
#     # print('course_id：{0} - name：{1} - jsonstr:{2}'.format(row[3],row[1],row[8]))
#     course_id = row[3]
#     langurl = row[6]
#     jsonstr = row[8]
#     if (jsonstr != None) & (langurl == None):
#         str = json.loads(jsonstr)
#         audioarr = str['data'][0]['audio']
#         langstr = ''
#         shortstr = ''
#         if len(audioarr) > 1:
#             langstr = audioarr[0]['url']
#             shortstr = audioarr[1]['url']
#         else:
#             langstr = audioarr[0]['url']
#             shortstr = None
#         sql = "UPDATE ylyk_sourse set langurl = '{0}', shorturl = '{1}' where course_id = {2}".format(langstr, shortstr, course_id)
#         try:
#             cursor.execute(sql)
#             connection.commit()
#             print('更新成功\n')
#         except:
#             connection.rollback()
#             print('更新错误\n')
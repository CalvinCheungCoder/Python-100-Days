# 根据课程 ID 拉取该课程下的列表数据并存储到数据库（已储存的跳过）
import urllib.request
import json
import ssl
import pymysql

import os
import re

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '123',
                             database = 'ylyk',
                             charset = 'utf8')

cursor = connection.cursor()
context = ssl._create_unverified_context()

with open('ylyk.json','r') as f:
    data = json.load(f)
    data_listArr = data['data']
    for data_detail in data_listArr:
        children_arr = data_detail['children']
        # print(children_arr)
        for children in children_arr:
            children_id = children['id']
            children_classname = children['class_name']
            url = 'http://api.ylyk.com/v1/album/classalbums/{0}'.format(children_id)
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req,context=context) as response:
                detail_data = response.read()
                json_data = detail_data.decode()
                jsonStr = json.loads(json_data)
                jsonDataArr = jsonStr['data']
                for listdata in jsonDataArr:
                    id = listdata['id']
                    name = listdata['name']
                    desc = listdata['desc']
                    cover_url = listdata['cover_url']
                    goods_id = listdata['goods_id']
                    paytype_id = listdata['paytype_id']

                    seleSql = "SELECT *FROM ylyk_sourselist WHERE id = %s" % id
                    try:
                        cursor.execute(seleSql)
                        results = cursor.fetchall()
                        if len(results) > 0:
                            print(len(results))
                            print('该课程已存在')
                        else:
                            value = (id,name,desc,cover_url,goods_id,paytype_id)
                            sql = "INSERT INTO ylyk_sourselist (id, name, des, coverurl, goods_id, paytype_id) values(%s, '%s', '%s', '%s', %s, %s)" % value
                            try:
                                cursor.execute(sql)
                                connection.commit()
                                print('插入成功\n')
                            except:
                                connection.rollback()
                                print('插入错误\n')
                                break
                    except:
                        connection.rollback()
                        print('查询错误')
                        break

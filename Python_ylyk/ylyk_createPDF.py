# 根据课程详细数据生成对应的 PDF 文件
import json
import pdfkit
import pymysql
import os
import re

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '123',
                             database = 'ylyk',
                             charset = 'utf8')

cursor = connection.cursor()

def createPDF(jsonstr):
    jsonstrtwo = json.loads(jsonstr)
    name = jsonstrtwo['data'][0]['basic']['name']
    name = name.replace('/','or')
    album_name = jsonstrtwo['data'][0]['basic']['album_name']
    teacher = jsonstrtwo['data'][0]['basic']['teacher']
    content = jsonstrtwo['data'][0]['basic']['content']
    # 标题和作者
    paragraphstr = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>{0}{1}</title></head><body><h1 style="font-family:Tahoma;color:black;font-size:24px;text-align:center">{2} / {3}</h1><div style="font-family:Tahoma;color:black;font-size:18px;text-align:center">{4}</div>'.format(
        album_name,name,album_name,name,teacher)
    # 课程导读
    if len(content) > 4:
        paragraphstr += '<br><p style="font-family:Tahoma;color:black;text-align:center;font-size:20px;background-color:rgb(230,230,230);width: 90px">课程导读</p>'
        content = content.replace('\n','<br>')
        content = '<p style="font-family:Tahoma;color:rgb(30, 30, 30);line-height:1.8">' + content + '</p>'
        paragraphstr += content;
    # 英文原文
    paragraphstr += '<br><p style="font-family:Tahoma;color:black;text-align:center;font-size:20px;background-color:rgb(230,230,230);width: 90px">英文原文</p>'
    paragraphArr = jsonstrtwo['data'][0]['explain_info']['paragraph']
    for paragraphdata in paragraphArr:
        paragraphtype = paragraphdata['type']
        paragraphcontent = paragraphdata['content']
        paragraphcontent = paragraphcontent.replace('\n','<br>')
        # 图片内容
        if paragraphtype == 'image':
            paragraphcontent = '<img src="' + paragraphcontent + '" style="width:auto;height:auto;max-width:70%;">' + '<br>'
        else:
            # 文本内容
            paragraphcontent = '<p style="font-family:Tahoma;color:rgb(30, 30, 30);line-height:2.0">' + paragraphcontent + '</p>' + '<br>'
        paragraphstr += paragraphcontent;
    # 生成 PDF 文件
    path = '/Users/zhangdinghao/Downloads/ylyk_note/' + album_name
    filepath = path + '/' + name + '.pdf'
    folder = os.path.exists(filepath)
    if not folder:
        # print('{0}\n\n'.format(jsonstr))
        foldertwo = os.path.exists(path)
        if not foldertwo:
            os.mkdir(path)

        filepathtwo = path + '/' + name
        pdfkit.from_string(paragraphstr, '{0}.pdf'.format(filepathtwo))
        print(filepathtwo)

# 查询课程列表并获取课程详情
sql = 'select *from ylyk_sourse'
cursor.execute(sql)
result_set = cursor.fetchall()
for row in result_set:
    course_id = row[3] # 课程 ID
    jsonstr = row[8]   # 原始数据
    createPDF(jsonstr)
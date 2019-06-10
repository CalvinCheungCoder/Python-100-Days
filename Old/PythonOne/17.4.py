import pymysql

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = 'zhang051109',
                             database = 'mydb',
                             charset = 'utf8')

try:
    # 2. 创建游标对象
    with connection.cursor() as cursor:

        # 3. 执行SQL操作
        sql = 'select *from user'
        cursor.execute(sql)
        # 4. 提取结果集
        result_set = cursor.fetchall()
        for row in result_set:
            print('userid：{0} - name：{1} - age:{2}'.format(row[1], row[0],row[2]))

        # 插入数据
        sql = "INSERT INTO user (userid,name ,age) VALUES (6, 'Mohan', 20)"
        cursor.execute(sql)

        sql = 'select *from user'
        cursor.execute(sql)
        result_set = cursor.fetchall()
        print('------------------------------')
        for row in result_set:
            print('userid：{0} - name：{1} - age:{2}'.format(row[1], row[0], row[2]))

        # 更新数据
        sql = "UPDATE user SET age = 16 WHERE name = 'Jack'"
        cursor.execute(sql)

        sql = 'select *from user'
        cursor.execute(sql)
        result_set = cursor.fetchall()
        print('------------------------------')
        for row in result_set:
            print('userid：{0} - name：{1} - age:{2}'.format(row[1], row[0], row[2]))

        # 删除数据
        sql = "DELETE FROM user WHERE name = 'Jack'"
        cursor.execute(sql)

        sql = 'select *from user'
        cursor.execute(sql)
        result_set = cursor.fetchall()
        print('------------------------------')
        for row in result_set:
            print('userid：{0} - name：{1} - age:{2}'.format(row[1], row[0], row[2]))

    # with代码块结束 5. 关闭游标

finally:
    # 6. 关闭数据连接
    connection.close()
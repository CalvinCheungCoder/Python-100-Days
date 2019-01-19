f_name = r'/Users/zhangdinghao/Documents/test.txt'
try:
    f = open(f_name)
except OSError as e:
    print('打开文件失败')
else:
    print('打开文件成功')
    try:
        content = f.read()
        print(content)
    except OSError as e:
        print('处理 OSError 异常')
    finally:
        f.close()

with open(f_name,'r') as  f:
    content = f.read()
    print(content)

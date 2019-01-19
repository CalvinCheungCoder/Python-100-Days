import os.path

from datetime import datetime

f_name = r'/Users/zhangdinghao/Documents/test.txt'
af_name = r'/Users/zhangdinghao/Documents/test.txt'

# 返回路径中基础名部分
basename = os.path.basename(af_name)
print(basename)

# 返回路径中目录部分
dirname = os.path.dirname(af_name)
print(dirname)

# 返回文件的绝对位置
print(os.path.abspath(f_name))

# 返回文件的大小
print(os.path.getsize(f_name))

# 返回最近访问时间
atime = datetime.fromtimestamp(os.path.getatime(f_name))
print('文件最近访问时间:',atime)

# 返回创建时间
ctime = datetime.fromtimestamp(os.path.getctime(f_name))
print('文件创建时间:',ctime)

# 返回修改时间
mtime = datetime.fromtimestamp(os.path.getmtime(f_name))
print('文件修改时间:',mtime)

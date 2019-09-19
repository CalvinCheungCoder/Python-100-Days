"""
扩展性系统性能
- 垂直扩展 - 增加单节点处理能力
- 水平扩展 - 将单节点变成多节点（读写分离/分布式集群）
并发编程 - 加速程序执行 / 改善用户体验
耗时间的任务都尽可能独立的执行，不要阻塞代码的其他部分
- 多线程
1. 创建Thread对象指定target和args属性并通过start方法启动线程
2. 继承Thread类并重写run方法来定义线程执行的任务
3. 创建线程池对象ThreadPoolExecutor并通过submit来提交要执行的任务
第3种方式可以通过Future对象的result方法在将来获得线程的执行结果
也可以通过done方法判定线程是否执行结束
- 多进程
- 异步I/O
"""

import glob
import os
import time

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from PIL import Image

def gen_thumbnail(infile):
    file, ext = os.path.splitext(infile)
    filename = file[file.rfind('/') + 1:]
    for size in (32, 64, 128):
        outfile = f'thumbnails/{filename}_{size}_{size}.png'
        image = Image.open(infile)
        image.thumbnail((size, size))
        image.save(outfile, format='PNG')

def main():
    pool = ThreadPoolExecutor(max_workers=30)
    futures = []
    start = time.time()
    for infile in glob.glob('images/*'):
        future = pool.submit(gen_thumbnail, infile)
        futures.append(future)
    for future in futures:
        future.result()
    end = time.time()
    print(f'耗时: {end - start}秒')
    pool.shutdown()

if __name__ == '__main__':
    main()
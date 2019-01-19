import threading
import time

value = 0

def thread_body():
    global value
    print('ThreadA 开始。。。')
    for n in range(2):
        print('ThreadA 执行。。。')
        value += 1
        time.sleep(1)

    print('ThreadA 结束。。。')


def main():
    print('主线程 开始。。。')
    t1 = threading.Thread(target=thread_body(), name='ThreadA')
    t1.start()

    t1.join()
    print('value = {0}'.format(value))
    print('主线程 结束。。。')


if __name__ == '__main__':
    main()
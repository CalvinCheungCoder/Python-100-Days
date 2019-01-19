import threading
import time

isruning = True

def thread_body():
    while isruning:
        print('下载中。。。')
        time.sleep(5)
    print('执行完成...')

def main():
    t1 = threading.Thread(target=thread_body)
    t1.start()

    command = input('请输入停止指令：')
    if command == 'exit':
        global isruning
        isruning = False


if __name__ == '__main__':
    main()
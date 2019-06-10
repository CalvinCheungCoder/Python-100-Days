import threading
import time

def thread_body():
    t = threading.current_thread()
    for n in range(5):
        print('第 {0} 次执行线程 {1}'.format(n, t.name))
        time.sleep(1)

    print('线程 {0} 执行完成！'.format(t.name))


def main():
    t1 = threading.Thread(target=thread_body())
    t1.start()

    t2 = threading.Thread(target=thread_body(),name='MyThread')
    t2.start()

if __name__ == '__main__':
    main()
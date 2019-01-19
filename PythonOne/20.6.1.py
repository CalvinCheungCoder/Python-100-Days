import threading
import time

# 创建条件变量对象
condition = threading.Condition()


class Stack:
    def __init__(self):
        # 堆栈指针初始值为0
        self.pointer = 0
        # 堆栈有5个数字的空间
        self.data = [-1, -1, -1, -1, -1]

    # 压栈方法
    def push(self, c):
        global condition
        condition.acquire()
        # 堆栈已满，不能压栈
        while self.pointer == len(self.data):
            # 等待其它线程把数据出栈
            condition.wait()
        # 通知其他线程把数据出栈
        condition.notify()
        # 数据压栈
        self.data[self.pointer] = c
        # 指针向上移动
        self.pointer += 1
        condition.release()

    # 出栈方法
    def pop(self):
        global condition
        condition.acquire()
        # 堆栈无数据，不能出栈
        while self.pointer == 0:
            # 等待其他线程把数据压栈
            condition.wait()
        # 通知其他线程压栈
        condition.notify()
        # 指针向下移动
        self.pointer -= 1
        data = self.data[self.pointer]
        condition.release()
        # 数据出栈
        return data

# 创建堆栈 stack 对象
stack = Stack()

# 生产者线程体函数
def producer_thread_body():
    global stack # 声明为全局变量
    for i in range(0, 10):
        # 把数字压栈
        stack.push(i)
        print('生产：{0}'.format(i))
        time.sleep(1)


# 消费者线程体函数
def customer_thread_body():
    global stack
    for i in range(0, 10):
        x = stack.pop()
        print('消费：{0}'.format(x))
        time.sleep(1)

def main():
    producer = threading.Thread(target=producer_thread_body)
    producer.start()

    customer = threading.Thread(target=customer_thread_body)
    customer.start()

if __name__ == '__main__':
    main()
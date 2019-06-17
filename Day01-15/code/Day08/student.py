# 定义和使用学生类

def _foo():
    print('test')


class Student(object):
    # __init__ 对象初始化，并给学生对象绑定 name 和 age 两个属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s 正在学习 %s.' % (self.name, course_name))

    def watch_av(self):
        if self.age < 18:
            print('%s 只能观看《熊出没》.' % self.name)
        else:
            print('%s 可以观看岛国片，欧美片.' % self.name)


def main():
    stu1 = Student('Calvin', 22)
    stu1.study('Python 100 Days 从小白到大牛')
    stu1.watch_av()

    stu2 = Student('小明', 12)
    stu2.study('思想品德')
    stu2.watch_av()


if __name__ == '__main__':
    main()
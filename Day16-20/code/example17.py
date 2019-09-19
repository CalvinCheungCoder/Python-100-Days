"""
多重继承 - 一个类有两个或者两个以上的父类
MRO - 方法解析顺序 - Method Resolution Order
当出现菱形继承（钻石继承）的时候，子类到底继承哪个父类的方法
Python 2.x - 深度优先搜索
Python 3.x - C3算法 - 类似于广度优先搜索
"""

class A():

    def say_hello(self):
        print('hello, A')

class B(A):
    pass

class C(A):
    def say_hello(self):
        print('hello, C')

class D(B, C):
    pass

class SetOnceMappingMixin():
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)

class SetOnceDict(SetOnceMappingMixin, dict):
    pass

def main():
    print(D.mro())
    D().say_hello()
    print(SetOnceDict.__mro__)
    my_dict = SetOnceDict()
    my_dict['username'] = 'jack Ma'
    my_dict['username'] = 'Tony Zhang'

if __name__ == '__main__':
    main()
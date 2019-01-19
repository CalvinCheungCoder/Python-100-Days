print('hello world')
a = (21,22,23,24)
for i, item in enumerate(a):
    print('{0} - {1}'.format(i,item))

b = 'hello '
print(len(b))


def rectangle_area(width,height):
    area = width * height
    return area


print(rectangle_area(10,10))


def make_coffee(name = "卡布奇诺"):
    return "制作一杯{0}咖啡".format(name)


print(make_coffee("拿铁"))
print(make_coffee())

# 无返回值函数


def sum(*numbers,multiple=1):
    total = 0.0
    for number in numbers:
        total += number
    return total * multiple


print(sum(100,200,300))
double_tuple=(50,20,30)
print(sum(100,23,*double_tuple))
print(sum(100,100,multiple=2))


def show_info(sep=':',**info):
    print('\n-----info-----')
    for key, value in info.items():
        print('{0} {2} {1}'.format(key,value,sep))


print(show_info('->',name='Tony',age=18,sex=True))
stu_dict = {'name' : 'calvin','age' : 18}
# ** 是为了拆包，将 stu_dict 拆包成为 key=value 对的形式
print(show_info(**stu_dict,sex=True,sep='='))

# 多返回值函数


def position(dt,speed):
    posx = speed[0] * dt
    posy = speed[1] * dt
    return (posx,posy)


move = position(60.0,speed=(10,-5))
print("\n物体位移：({0},{1})".format(move[0],move[1]))

# 函数变量作用域，全局变量和局部变量
x = 20


def print_value():
    x = 10
    print("函数中x = {0}".format(x))


print(print_value())
print("全局变量中x = {0}".format(x))

# 局部变量修改全局变量


def print_value2():
    global x
    x = 10
    print("函数中x = {0}".format(x))


print(print_value2())
print("全局变量中x = {0}".format(x))

# 10.5 生成器，生成器函数是通过 yield 返回数据，与 return 不同的是：return 语句一次返回所有数据，函数调用结束；而 yield 语句只返回一个元素数据，
# 函数调用不会结束，只是暂停，直到 _next_() 方法被调用，程序继续执行 yield 语句之后的语句代码。
# 生成器特别适合用于遍历一些大序列对象，它无需将对象的所有元素都载入内容才开始操作，而是仅在迭代至某个元素时才会将元素载入内存


def square(num):
    n_list = []
    for i in range(1,num + 1):
        yield i * i


for i in square(5):
    print(i,end=' ')

# 嵌套函数，所示，作用域在嵌套函数内部，外部函数之外直接访问嵌套函数会发生错误


def calculate(n1,n2,opr):
    multiple = 2

    # 定义相加函数
    def add(a,b):
        return (a + b) * multiple
    # 定义相减函数
    def sub(a,b):
        return (a - b) * multiple
    if opr == '+':
        return add(n1,n2)
    else:
        return sub(n1,n2)


print("\n\n嵌套函数执行结果={0}".format(calculate(10,5,'+')))

number_list = range(1,21)
numberfilter = filter(lambda it : it % 2 == 0,number_list)
print(list(numberfilter))

name_list = ["TOM","TONY","BEN","ALEX"]
nameList = map(lambda u : u.lower(),name_list)
print(list(nameList))


from functools import reduce


a = (1,1,1,1,2)
a_reduce = reduce(lambda acc,i : acc + i,a)
print(a_reduce)
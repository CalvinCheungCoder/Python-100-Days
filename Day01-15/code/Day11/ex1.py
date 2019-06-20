# 异常机制 - 处理程序在运行时可能发生的状态

input_again = True
while input_again:
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        print('%d / %d = %f' % (a, b, a / b))
        input_again = False
    except ValueError:
        print('请输入整数')
    except ZeroDivisionError:
        print('除数不能为0')
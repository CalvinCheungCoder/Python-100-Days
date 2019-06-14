'''
找出 100-999 之间所有的水仙花数
水仙花数是各位立方和等于这个数本身的数
如：153 = 1**3 + 5**3 + 3**3
'''

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print('水仙花数:',num)
        print('')

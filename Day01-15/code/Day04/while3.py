# 用 while 循环实现 1~100 之间的偶数和

sum, num = 0, 2
while num <= 100:
    sum += num
    num += 2
print(sum)
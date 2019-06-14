'''
Craps 赌博游戏
玩家摇两颗色子 如果第一次摇出 7 点或 11 点 玩家胜
如果摇出 2 点 3 点 12 点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出 7 点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有 1000 元的赌注 全部输光游戏结束
'''

from random import randint

money = 1000
while money > 0:
    print('你的资产为：',money)
    needs_to_go = False
    while True:
        debt = int(input('请下注：'))
        if debt > 0 and debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜！')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜！')
        money -= debt
    else:
        needs_to_go = True

    while needs_to_go:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜！')
            money -= debt
            needs_to_go = False
        elif current == first:
            print('玩家胜！')
            money += debt
            needs_to_go = False

print('你破产了，游戏结束!')

# coding=utf-8

import enum


class WeekDays(enum.IntEnum):
    # 枚举常量列表
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5


day = WeekDays.FRIDAY

print(day)
print(day.value)
print(day.name)

if day == WeekDays.MONDAY:
    print("学习使我快乐")
elif day == WeekDays.FRIDAY:
    print("工作使我快乐")

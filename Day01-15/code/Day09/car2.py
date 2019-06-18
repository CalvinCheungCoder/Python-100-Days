'''
属性的使用
- 使用已有方法定义访问器/修改器/删除器
'''

class Car(object):
    __slots__ = ('_brand', '_max_speed')

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_max_speed(self):
        return self._max_speed

    def set_max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car:[品牌 = %s, 最高时速 = %s]' % (self._brand, self._max_speed)

    # 用已有的修改器和访问器定义属性
    brand = property(get_brand, set_brand)
    max_speed = property(get_max_speed, set_max_speed)

car = Car('QQ', 120)
print(car)
car.max_speed = 320
car.brand = 'Benz'
print(car)
print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)
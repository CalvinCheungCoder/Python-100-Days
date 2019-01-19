class Animal(object):

    def __init__(self,age,sex = 1,weight = 0.0):
        self.age = age
        self.sex = sex
        self.weight = weight

    def eat(self):
        self.weight += 0.05
        print('eat...')

    def run(self):
        self.weight -= 0.01
        print('run...')


animal = Animal(2,1,10.0)
print("年龄：{0}".format(animal.age))
print("性别：{0}".format(animal.sex))
print("体重：{0:0.2f}".format(animal.weight))
animal.run()
print("体重：{0:0.2f}".format(animal.weight))
animal.eat()
print("体重：{0:0.2f}".format(animal.weight))


# 类方法
class Account:
    interest_rate = 0.0668

    def __init__(self,owner,amount):
        self.owner = owner
        self.amount = amount

    # 类方法
    @classmethod
    def interest_by(cls,amt):
        return cls.interest_rate * amt

    # 静态方法
    @staticmethod
    def interest_with(amt):
        return Account.interest_by(amt)


interest1 = Account.interest_by(100000.0)
print('计算利息：{0:.2f}元'.format(interest1))
interest2 = Account.interest_with(100000.0)
print('计算利息：{0:.2f}元'.format(interest2))
# 私有方法和私有变量是在方法或者变量名前加 __，例如 __weight, __run


# 继承，子类继承父类只是继承父类中公有的成员变量和方法，私有的成员变量和方法不能继承
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        template = 'Person [name = {0},age = {1}]'
        return template.format(self.name,self.age)


class Student(Person):
    def __init__(self,name,age,school):
        super().__init__(name,age)
        self.school = school


# 重写方法，如果子类方法名与父类方法名相同，而且参数列表也相同，只是方法体不同，那么子类重写（Override）了父类的方法，子类重写父类 eat 方法
class Dog(Animal):
    def eat(self):
        self.weight += 0.1
        print("狗狗吃...")


a1 = Dog(2,0,10.0)
a1.eat()


# 多继承，大部分计算机语言，如 Java，Swift 只支持单继承，Python 支持多继承，为了解决方法名字冲突，Python 给出如下方案
# 当子类实例调用一个方法时，先从子类中查找，如果没有查找到则查找父类。父类的查找顺序是按照子类声明的父类列表从左至右查找，如果没有找到再找父类的父类，依次查找下去
class ParentClass1:
    def run(self):
        print('PersentClass1 run...')


class ParentClass2:
    def run(self):
        print('PersentClass2 run...')


class SubClass1(ParentClass1,ParentClass2):
    pass


class SubClass2(ParentClass1,ParentClass2):
    pass


class SubClass3(ParentClass1,ParentClass2):
    def run(self):
        print('SubClass3 run...')


sub1 = SubClass1()
sub1.run()
sub2 = SubClass2()
sub2.run()
sub3 = SubClass3()
sub3.run()


# 几何图形
class Figure:
    def draw(self):
        print("绘制 Figure...")


# 椭圆形
class Ellipse(Figure):
    def draw(self):
        print("绘制 Ellipse...")


# 三角形
class Triangle(Figure):
    def draw(self):
        print("绘制 Triangle...")


f1 = Figure() # 没有发生多态
f1.draw()
f2 = Ellipse() # 发生多态
f2.draw()
f3 = Triangle() # 发生多态
f3.draw()


# Python 根类 - Object 和对象比较
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        template = 'Person [name={0},age={1}]'
        return template.format(self.name,self.age)

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False


p1 = Person('Tony',18)
p2 = Person('Tony',18)
print(p1 == p2)

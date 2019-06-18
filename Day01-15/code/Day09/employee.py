'''
抽象类 / 方法重写 / 多态
实现一个工资结算系统 公司有三种类型的员工
- 部门经理固定月薪 12000 元/月
- 程序员按本月工作小时数每小时 100 元
- 销售员 1500 元/月的底薪加上本月销售额 5% 的提成
输入员工的信息 输出每位员工的月薪信息
'''

from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):

    def __init__(self, name):
        super().__init__(name)

    def get_salary(self):
        return 12000

class Programmer(Employee):

    def __init__(self, name):
        super().__init__(name)

    def set_working_hour(self, work_hour):
        self._work_hour = work_hour

    def get_salary(self):
        return 100 * self._work_hour

class Salesman(Employee):

    def __init__(self, name):
        super().__init__(name)

    def set_sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1500 + self._sales * 0.05


if __name__ == '__main__':
    emps = [Manager('Calvin'), Programmer('Calvin2'), Salesman('Calvin3')]

    for emp in emps:
        if isinstance(emp, Programmer):
            working_hour = int(input('请输入 %s 本月的工作时间:' % emp.name))
            emp.set_working_hour(working_hour)
        elif isinstance(emp, Salesman):
            sales = float(input('请输入 %s 本月销售额：' % emp.name))
            emp.set_sales(sales)
        print('%s 本月薪水为：￥%.2f 元' % (emp.name, emp.get_salary()))
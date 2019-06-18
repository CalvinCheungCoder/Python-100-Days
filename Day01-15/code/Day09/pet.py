from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickName):
        self._nickname = nickName

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):

    def make_voice(self):
        print('%s: 汪汪汪。。。' % self._nickname)

class Cat(Pet):

    def make_voice(self):
        print('%s: 喵喵喵。。。。' % self._nickname)

def main():
    pets = [Dog('旺财'), Cat('Kittey'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()
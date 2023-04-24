class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplemented('구현안됨')


class Cat(Animal):
    def talk(self):
        return 'Meow!'


class Cat2(Animal):     #직접 Animal을 호출해서 한다면 이렇게
    def __init__(self, name):
        super().__init__(name)
        # Animal.__init__(self, name)  같은녀석 클래스를 호출해서 사용하기 때문에 self가 필요함. 가독성이 좋다.

    def talk(self):
        return 'Meow!'


class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


Missy = Cat('Missy')        #디버깅한다면 변수로 바꾸로 돌리면 수월하다.
animals = [Missy, Cat('Mr.'), Dog('Lassie')]

for Animal in animals:
    print(Animal.name, ':', Animal.talk())
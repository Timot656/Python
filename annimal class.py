from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        print("I can walk and run")
        class Snale(Animal):
            def move(self):
                print("I can crawl")
            class Dog(Animal):
                def move(self):
                    print("I can bark")
            class Lion (Animal):
                def move(self):
                    print("I can roar")
R = Human()
R.move()
K = Snale()
K.move()
K = Lion()
K.move
from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print("Passed Value: ", x)
@bstractmethod
def task(self):
    print("We are inside Abstract Methond")
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")
test_obj = test_class
test.task()
test_obj.print(100)
from abc import ABC, abstractmethod

class Students(ABC):
    @abstractmethod
    def grade(self):
        pass

class Ruf(Students):
    def grade(self):
        return 12

p1 = Ruf()

print(p1.grade())
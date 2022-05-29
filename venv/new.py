from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop (Computer):
    def process(self):
        print("it is running")
class Whiteboard(Computer):
    def process(self):
        print("it is writing")

class Programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()

#com= Computer()
com1= Laptop()
com2 = Whiteboard()
#com.process()
prog1=Programmer()
prog1.work(com1)
prog1.work(com2)
#com1.process()
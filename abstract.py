from abc import ABC,abstractmethod
class TimeTable(ABC):
    @abstractmethod
    def Breakfast(self):
        pass
    @abstractmethod
    def Lunch(self):
        pass
    @abstractmethod
    def Dinner(self):
        pass
class Aman(TimeTable):
    def Breakfast(self):
        print("bread and butter")
    def Lunch(self):
        print("Chicken Biryani")
    def Dinner(self):
        print("roti and sabzi")
aman=Aman()
aman.Breakfast()
aman.Lunch()
aman.Dinner()
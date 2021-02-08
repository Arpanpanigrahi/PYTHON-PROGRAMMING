#1. Design a dummy game like clash of clans

from abc import ABC, abstractmethod
class Soldier(ABC):
    def gather(self):
        print("Gather")
    @abstractmethod
    def attack(self):
        pass
        
class Refillable(ABC):
    @abstractmethod
    def refil(self):
        pass
    
class TimeBasedRefil(Refillable):
    def refil(self):
        print("Time based refil")
        
class WeaponBasedRefil(Refillable):
    def refil(self):
        print("Weapon based refil")
        
class Archer(Soldier):
    def attack(self):
        print("Archer attack")

    def refil(self):
        return TimeBasedRefil().refil()
        
class SpearMan(Soldier):
    def attack(self):
        print("Spearman attack")
        
a1 = Archer()
a1.gather()
a1.attack()
a1.refil()
s=Soldier()

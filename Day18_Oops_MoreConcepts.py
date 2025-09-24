'''
#POLYMORPHISM
class Animal:
    def voice(self):
        print("All Animals Have voice to make Noise!!")



class Cat(Animal):
    def voice(self): #Overriding the parent class method
        print("Meow")


an = Animal()
an.voice()

ca = Cat()
ca.voice()'''

# Class and Object
'''Encapsulation -> Wrapping variables and methods inside a class
                -> Restricting direct access to some of the objects's components 
                ''' 
'''
class Account:
    def __init__(self,balance):
        self.__balance = balance

    def check_balance(self):
        return self.__balance

    def withdrawl(self,amount):
        self.__balance-=amount

ac1 = Account(50000)
ac1.withdrawl(1000)
print(ac1.check_balance())
#print(ac1.__balance) # ERROR because it is Private using __'''

#Inheritance

#Polymorphism --> Overriding (No Overloading in Python)
#Abstraction --> Hiding Internal details and displaying essential/required features

from abc import ABC, abstractmethod
'''abc -> abstract base class module
   ABC -> used to define an abstract class
   @abstractmethod -> make a method as abstract, method will have no body
                       in parent class and must be implemented in a child class
 '''

'''
class Animal(ABC):
    @abstractmethod  
    def voice(self):
        pass

class Cat(Animal):
    def voice(self):
        print("Cat Meowed!!")

c = Cat()
c.voice()'''













































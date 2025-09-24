'''
Object Oriented Programming Langugage -- OOP
Everything in Python is Object
Class Id Data Type
'''
'''
# class creation
class Student:
    name = "NA"
    age = 0

s1 = Student() #object creation
s2 = Student()

s1.name = 'John'
s1.age = 21

print(s1.name)
print(s2.name)
print(s1.age)
print(s2.age)'''


'''
__init__() -> Initializer
1) __init__() method is automatically called when a new object is created.
2) It is an Initializer
3) one fixed argument is used as first argument/parameter to assign object.
'''

'''
class Student:
    def __init__(me,name,age):
        #print(me)
        me.myname = name
        me.myage = age

s1 = Student('John',21)
print(s1.myname,s1.myage)
s2 = Student('Harry',20)
print(s2.myname,s2.myage)'''

'''
#class with method
class Student:
    def __init__(me,name,age):
        #print(me)
        me.myname = name
        me.myage = age

    def hobby(me,hob):
        print(me.myname,me.myage)
        print('Hobby: ',hob)
        
        

s1 = Student('John',21)
s2 = Student('Harry',20)
s1.hobby('Painting')
s2.hobby('Dancing')'''



# Create 3 objects car1,car2,car3 of the Car class with brand and year.
# Create a book class having title, price and author, and create 3 objects.


'''Create a class with methods showing 3 employee names and salary, name and salary
should be taken from user.'''

# Create a class Rectangle to find the area.
# Create a class Circle with radius and method to calculate circumference and area.


























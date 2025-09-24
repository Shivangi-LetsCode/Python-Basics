'''
# HIERARCHICAL INHERITANCE
class Parent:
    def show(self):
        print("I am Parent")

class Child1(Parent):
    def child1_fun(self):
        print("I am John")

class Child2(Parent):
    def child2_fun(self):
        print("I am Harry")


John = Child1()
Harry = Child2()

John.show()
John.child1_fun()

Harry.show()
Harry.child2_fun()'''


'''
SCHOOL MANAGEMENT SYSTEM

USE ALL 4 INHERITANCE

Class Names: Person(name, age)
Student(student_id)
SchoolStudent(grade)
Sports(sport_name)
SportsStudent  --> object
Teacher(subject) --> object

output: Sports Students details --> Name, Age, student_id, grade, sport_name
        Teacher Details--> Name,age,Subject

'''




'''
PROJECT -> PASSWORD STRENGTH CHECKER
import string  -> string.puntuation
condition: length>8, capital, lower, digit, special character
score variable
score <=2 : weak
score 3 to 4 : Moderate
score else: Strong
'''




























'

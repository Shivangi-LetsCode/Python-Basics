'''
#INHERITANCE
Defining new class with the help of old class

Parent/Base/Super
Child/Derived/Sub

Types of Inheritance:
1) Single Inheritance
2) Multiple Inheritance
3) Multilevel Inheritance
4) Hierarchical Inheritance
'''

'''
class1:

class2(class1):
Everything availabale in class1 will be by default available in class2 +
Extra features of class2
'''

#SINGLE INHERITANCE
class Person:
    def __init__(self,name,age):
        self.person_name = name
        self.person_age = age

    def Show(self):
        print(self.person_name)
        print(self.person_age)


class Student(Person):
    def __init__(self,person_name,person_age,subject,grade):
        super().__init__(person_name,person_age)
        #Person.__init__(self,person_name,person_age)
        self.student_subject = subject
        self.student_grade = grade

    def ShowSubjectGrade(self):
        print(self.student_subject)
        print(self.student_grade)

John = Student('John',24,'Python','A')
John.Show()
John.ShowSubjectGrade()


'''
Create a Parent class as Person class which is Inherited by Employee class.
Employee should have name, salary, Department, Year_Experience and Designation
also show Employee Details.
'''






    
    
        













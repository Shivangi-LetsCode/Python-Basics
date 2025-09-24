
'''#2) Multilevel Inheritance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Person Details: {self.name},{self.age}")

class Employee(Person):
    def __init__(self,name,age,emp_id):
        super().__init__(name,age)
        self.emp_id = emp_id
        print(f"Employee Details: {self.emp_id}")
    

class Developer(Employee):
    def __init__(self,name,age,emp_id,skills):
        super().__init__(name,age,emp_id)
        self.skills = skills
        print(f"Developer Details: {self.skills}")

class Freelancer:
    def __init__(self,hourly_rates):
        self.hourly_rates = hourly_rates
        self.projects = []
        print(f"Freelancer Details: ${self.hourly_rates}/hr")

    def add_project(self,project):
        self.projects.append(project)

    def total_income(self,hours):
        return self.hourly_rates * hours

class FreelancerDeveloper(Developer, Freelancer):
    def __init__(self,name,age,emp_id,skills,hourly_rates):
        Developer.__init__(self,name,age,emp_id,skills)
        Freelancer.__init__(self,hourly_rates)

    def profile(self):
        print(f"{self.name}(ID: {self.emp_id}) is a skilled freelancer developer in {', '.join(self.skills)}.")
        print(f"Current Projects: {self.projects}")
        print(f"Hourly Rate: ${self.hourly_rates}/hr")


        
John = FreelancerDeveloper("John",29,"E101",['Python','REST API','Django','Flask'],40)
John.add_project("Ecommerce Website")
John.add_project("App Development")
John.profile()

print("Total Income for 40 hours:", John.total_income(40))'''




'''
# MRO-> METHOD RESOLUTION ORDER
#3) Multiple Inheritance
class Father:
    def skills(self):
        print("Driving, Singing")
        super().skills() # Goes to the next class in MRO

class Mother:
    def skills(self):
        print("Cooking, Dancing")

class Child(Father,Mother):
    def more_skills(self):
        super().skills()

Jack = Child()
Jack.more_skills()
print(Child.__mro__)'''






















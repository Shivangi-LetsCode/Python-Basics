'''Student Grade Checker
name, math, science, english, cal average, passed or not, if average
is more than 35 then passed otherwise failed, if passed and average >=90 then A+
and so on, store grades into same variable, top_grades=['A+','A'], is_topper,
show the results(name,total marks, average, pass/fail, grade),
if student is topper then congratulate him/her.'''

# METHOD 1

x,y,z,q=input("enter your Name :"),int(input("Enter your maths score :")),int(input("Enter your Science score :")),int(input("Enter english score :"))
u=(y+z+q)/3
print("Percatange is :",u)
if u>=35:
    print("pass")
else:
    print("Fail")

if u>=90:
    print("Congratulation",x ,"for securing",u,"percentage and A+ grade")
elif u>=85:
    print("Congratulation",x ,"for securing",u,"percentage and A grade")
elif u>=80:
    print(x,u,"you have scored B+")
elif u>=75:
     print(x,u,"you have scored B")
elif u>=70:
     print(x,u,"you have scored C+")
elif u>=65:
     print(x,u,"you have scored C")
elif u>=60:
     print(x,u,"you have scored D")
elif u>=55:
     print(x,u,"you have scored D-")
elif u>=35:
     print(x,u,"you have scored E")
else:
     print(x,u,"you have scored F")
    
    
    



# METHOD 2


name,math,science,english=input("enter your Name :"),int(input("Enter your maths score :")),int(input("Enter your Science score :")),int(input("Enter english score :"))
# Arithmetic operator
total = math+science+english
average= total/3
print("Percatange is :",u)

#Relational and logical
passed = (math>=35) and (science>=35) and (english>=35)

if passed and average>=90:
    grade='A+'
elif passed and average>=75:
    grade='A'
elif passed and average>=60:
    grade='B'
elif passed:
    grade='C'
else:
    grade = 'Fail'

#Membership operator
top_grades = ['A+','A']
is_topper = grade in top_grades
if is_topper:
    print('========================================================')
    print('Congratulation!! You are among the top students.')
    print('========================================================')


#Result
print("--- Student Report ---")
print("Name: ",name)
print("Total Marks: ",total)
print("Result: ","Pass" if passed else "Fail")










    













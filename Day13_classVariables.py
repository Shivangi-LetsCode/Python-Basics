'''class Student:
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
s2.hobby('Dancing')

#del s2.age
#print(s2.age)

#del s2
#print(s2.name)'''

'''
#pass
def f1():
    pass

class S:
    pass'''

''' Types Of Variables
1) Instance variables--> Object specific
2) static variables --> class specific, single time, access with class name
3) Local variables
4) Global variables
'''
'''
same bank
savings Account : 3%
Salary Account: 5%
Current Account: 7%

A/c holder name: instance variable
A/c Number: instance
Mobile numer: instance
interest: static variable'''

'''
# instance and static variables
class Account:
    interest = 3 # static variable
    def __init__(self,acc,bal):
        self.acc_no = acc
        self.balance = bal

print(Account.interest)
# print(Account.acc_no) ERROR
john = Account(101,50000)
print(john.interest,john.acc_no,john.balance)'''

'''
#Local Variable
def f1():
    x = 5 # local variable
    print(x)
f1()
#print(x) #ERROR'''
'''
#GLOBAL VARIABLE
y = 3 #Global variable
def f2():
    print(y)
f2()
print(y)


y = 3 #Global variable
def f2():
    y=6; #olocal variable
    print(y)
f2()
print(y)'''


'''
y = 3 #Global variable
def f2():
    #y=6 #local variable
    global y
    print(y)
f2()
print(y)'''

'''
y=3
def f3():
    y = 6 # local
    print(globals() ['y']) # global
    print(y) #local

f3()
print(y)
'''

'''
class A:
    myvar = 100

class B(A):
    pass

B.myvar+=50
print(A.myvar)
print(B.myvar)'''

'''
class Collector:
    items = []
    def __init__(self,item):
        Collector.items.append(item)

c1 = Collector('item1')
c2 = Collector('item2')
print(Collector.items)'''



































































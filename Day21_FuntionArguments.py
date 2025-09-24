'''def sum1(a,b):
    s = a+b
    print("Sum is: ",s)

sum1(10,20)
#sum1(10,20,30) #ERROR'''

'''
#DEFAULT ARGUMENTS
def sum1(a,b,c=0):
    s = a+b+c
    print("Sum is: ",s)

sum1(10,20)
sum1(10,20,30)
'''

'''
If we are declaring first argument as default argument
then all arguments should be default
'''

''' ERROR
def sum1(a=0,b,c):
    pass

sum1(1,3)
'''
'''
def sum2(a=2,b=2,c=0):
    s = a+b+c
    print("Sum is: ",s)

sum2() #4
sum2(10) #12
sum2(10,20) #30
sum2(10,20,30) #60'''

'''
#KEYWORD ARGUMENTS
def f1(a,b):
    print("a: ",a,"b: ",b)

f1(10,20) #a:10 and b:20
f1(20,10) #a:20 and b:10'''
'''we want b should be 20, doesn't matter the position'''
'''
f1(a=10,b=20)
f1(b=20,a=10)
f1(10,b=20) #10 is positional  and 20 is keyword argument
#f1(a=10,b) #ERROR
#f1(10,a=10) #ERROR
#f1(a=10,a=20) #ERROR'''


'''
If we are declaring first argument as Keyword argument
then all arguments should be keyword arguments
'''
'''
#VARIABLE LENGTH ARGUMENT
def vla(*a):
    print(a,type(a))

vla(10,20,30,40,50,60,"Hello")'''

#find average of numbers using variable length arguments
#Count points for each player
'''
countpoints('John',2,3,4)
countpoints('Harry',4,5,3)'''


"""
#VARIABLE LENGTH KEYWORD ARGUMENT
def f1(**k):
    print("Person Information")
    print(k)
    '''for key,value in k.items():
        print(key,"-",value)'''


f1(name="John",age=22)
f1(name="Harry",age=24,marks=28)
f1(name="Rich",age=27,marks=48,salary=30000)"""




























    

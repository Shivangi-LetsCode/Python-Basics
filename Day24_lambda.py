'''
lambda function --> function without name/anonymous function
syntax: lambda arguments: expressions
'''
'''
def value(a):
    print(a+5)

value(2)


value = lambda a: a+5
print(value(2))

#take 2 inputs from user and apply multiplication
a = int(input("Enter a: "))
b = int(input("Enter b: "))
result = lambda a,b: a*b
print(result(a,b))'''



'''
#lambda with multiple statements
a = int(input("Enter a: "))
b = int(input("Enter b: "))
result = lambda a,b: (a*b, a+b)
print(result(a,b))'''

'''
# lambda with list

result = [lambda num=x:num*2 for x in range(1,5)]
print(result)
for i in result:
    print(i())'''
'''
#returning lambda
def f1(y):
    print(y)
    return lambda x:x*y


multiply_it = f1(2)
print(multiply_it(3))

#x = 3, y = 2

extra_multiply_it = f1(5)
print(extra_multiply_it(4))'''

'''
#lambda with condition
check_even_odd = lambda x: "Even" if x%2 == 0 else "Odd"
print(check_even_odd(9))'''

'''
# lambda with dictionaries values
operations ={
'add':lambda x,y:x+y,
'sub':lambda x,y:x-y
    }

print(operations['add'](4,9))
print(operations['sub'](4,9))


#nested lambda
nestedlambda = lambda x: (lambda y: x+y)
value = nestedlambda(5)
print(value(6))'''

add = lambda x: (lambda y: x+y)
print(add(3)(9))





#lambda function to capitalize a string.
#lambda function to check inputed is even or odd.
#lambda function to check inputed number is positive, negative or zero.
#find maximum of 2 numbers using lambda.
#sort a list of strings by their length
#check if string starts with s.
#return max and absolute difference of two numbers
#use lambda to return both upper and lower case of a string
#lambda that multiplies 3 numbers using nesting
# nested lambda that checks if sum of two numbers is even
#create power function using lambda
#concatenate 2 strings using lambda

























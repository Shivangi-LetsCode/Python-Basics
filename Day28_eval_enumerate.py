'''
eval() evaluates a string as a python expressions and returns the result.
'''
'''
a = eval("2+4")
print(a)


x = 10
y = 20
print(eval("x*y"))

print(eval("[i*2 for i in range(5)]"))

exp = "2+8*6"
print(exp)
print(eval(exp))

exp = input("Enter any expression: ")
print(eval(exp))


x = 15
print(eval("x>10 and x<20"))

exp = "x + y"
print(eval(exp,{"x":4, "y":3}))


def greet(name):
    return f"Hello, {name}"

print(eval("greet('John')"))


num = 10
print(eval("num%2 == 0"))


a = 8
b = 3
op = "-"
print(eval("a "+ op + " b"))



# dynamic function calling
def square(x):
    return x*x

def cube(x):
    return x*x*x

func = "square"
print(eval(f"{func}(4)"))'''

'''
#enumerate() --> to get both the index and the value while looping
fruits = ['Apple','Mango','Grapes','Papaya']
for index, fruit in enumerate(fruits):
    print(index,fruit)



fruits = ['Apple','Mango','Grapes','Papaya']
for index, fruit in enumerate(fruits, start=1):
    print(index,fruit)


for index, charac in enumerate("Apple"):
    print(index, charac)
    

num = [10,20,30,40,50]
search = 30
for i,num in enumerate(num):
    if num == search:
        print(f"{search} found at index {i}")

'''
'''
enumerate:
1) create a list having a,b,c,d,e characters and
Change element at odd indices to Uppercase.

2) Track word position in a sentence. -> we are learning python

3) Print every second element using enumerate.

4) Print list characters in reverse order using enumerate.


eval():
1) Evaluate 5*(4+2) using eval

2) input x from user and check whether x value is greater then 20.

3) Enter a lambda expression in input() and convert it into expression using eval.

'''


expr = input("Enter safe Arithmetic expression only")
if any(word in expr for word in ['import','os','exec']):
    print("Unsafe Expression Detected")
else:
    print(eval(expr))














































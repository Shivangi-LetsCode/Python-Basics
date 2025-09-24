'''
Walrus Operator: Assign and use a value in a single line
syntax: variable := expression
'''
'''
name = input("Enter name: ")
while name!= "exit":
    print(name)
    name = input("Enter name: ")

#using Walrus
while(name:=input("Enter name: ")) != "exit":
    print(name)


if (n:= input("Name: ")) and len(n)>5:
   print(f"Very Long : {n}")'''

'''
1) Use walrus operator in a while loop tp keep asking
for a number until user enters 0.

2) Print numbers from 1 to 5 using input() and walrus.

3) Filter positive numbers using list comprehension and walrus

4) Print all even numbers until 0 is entered.
















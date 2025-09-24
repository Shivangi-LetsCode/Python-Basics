'''
Function calls itself to solve a smaller part of the problem.
1. Base Case : Stop the recursion
2. Recursive case : Calls the function again with a input
'''
'''
# countdown timer
def count(num):
    if num<=0:  # base case
        print("Over!!")
    else:
        print(num)
        count(num-1) #recursive case
count(5)'''
'''

# factorial using recursion
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1) 
print(factorial(5))'''

'''
#sum of digit
def sumdigit(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sumdigit(num//10)

print(sumdigit(1278))'''
'''

#reverse a string
def reversestring(text):
    if len(text) == 0:
        return text
    else:
        return text[-1] + reversestring(text[:-1])

print(reversestring("python"))'''

'''
#Sum of n natural numbers
def sum_natural(num):
    if num == 1:
        return 1
    else:
        return num + sum_natural(num-1)

print(sum_natural(5))'''

'''
#power
def power(a,b):
    if b == 0:
        return 1
    else:
        return a * power(a,b-1)
        

print(power(2,6))'''

'''
def binarysearch(arr, low, high, element):
    if low>high:
        return -1 # element not found
    mid = (low + high)//2
    if arr[mid] == element:
        return mid
    elif element<arr[mid]:
        return binarysearch(arr,low,mid-1,element)
    else:
        return binarysearch(arr,mid+1,high,element)
        

arr = [1,3,5,7,9,11,13,15,17,19]
print(binarysearch(arr,0,len(arr)-1,11))'''

'''
# print numbers from N to 1.
# Count number of digits in a number.
# Check if a string is palindrome.
# Find product of elements in a list.
# Count vowels in a string.
# count even numbers in a list.
# find maximum and minimum element in a list.
'''






































































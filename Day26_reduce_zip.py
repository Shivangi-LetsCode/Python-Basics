from functools import reduce
nums = [1,2,3,4,5,6,7,8,9,10]
result = reduce(lambda x,y: x+y, nums)
print(result)
result = reduce(lambda x,y: max(x,y), nums)
print(result)


num = [2,7,5,8,9,1]
max_number = reduce(lambda x,y: x if x>y else y, num)
print("Maximum:", max_number)

min_number = reduce(lambda x,y: x if x<y else y, num)
print("Minimum:", min_number)


words = ['We', 'are', 'Learning', 'Python']
sentence = reduce(lambda x,y: x+' '+y,words)
print(sentence)


s = 'Python'
reversedtext = reduce(lambda x,y: y+x, s)
print(reversedtext)

nums = [1,2,3,4,5,6,7,8,9,10]
multi_even = reduce(lambda x,y: x*y, filter(lambda x:x%2 == 0, nums))
print(multi_even)

fruit = "Banana"
count_a = reduce(lambda x,y: x+1 if y == 'a' else x, fruit, 0)
print("A: ",count_a)


# zip: to combine two or more iterables
names = ['John','Harry','Peter','Daniel']
marks = [30,65,22,65]
result = zip(names,marks)
print(list(result))


names = ['John','Harry','Peter','Daniel']
marks = [30,65,22]
result = zip(names,marks)
print(list(result))





names = ['Harry','Peter','Daniel']
marks = [30,65,22,65]
result = zip(names,marks)
print(list(result))


zipped = [('John', 30), ('Harry', 65)]
a,b = zip(*zipped)
print(a)
print(b)

keys = ['name','age','city']
values = ['John',34,'Pune']

d = dict(zip(keys,values))
print(d)



names = ['John','Harry','Peter','Daniel']
marks = [30,65,22,65]
for name,mark in zip(names,marks):
    print(f"{name} scored {mark}")


from itertools import zip_longest
names = ['John','Harry','Peter','Daniel']
marks = [30,65,22]
result = zip_longest(names,marks, fillvalue=0)
print(list(result))


fruits = ['Apple','Banana','Mango']
prices = [100,30,50]
zipped = zip(prices,names)
sortedprice = sorted(zipped)
print(list(zipped))


'''
reduce:
1) Sum of squares of all numbers in list

2) Find factorial of a number using reduce

3)Convert list of digits to actual number

zip:

1) Add corresponding elements of two lists

2) Compare two lists element-wise

3) Unzip a list of tuples

4) Check if two lists are reverse of each other
'''

    










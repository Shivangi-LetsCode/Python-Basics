'''
filter() filters elements of an iterable based on condition provided by function.
'''
def odd(n):
    return n%2 != 0

numbers = [1,2,3,4,5,6,7,8,9]
print(list(filter(odd,numbers)))


#with lambda
print(list(filter(lambda a:a%2!=0, numbers)))


#ternary with filter lambda
print(list(filter(lambda a: True if a%2!=0 else False, numbers)))

#ternary with map lambda
print(list(map(lambda a: print(a,' is odd') if a%2!=0 else print(a,' is even'), numbers)))




greatherthan5 = list(filter(lambda a: a>5,numbers))
print(greatherthan5)


num = [0,23,0,6,5,3,0,12,0,0]
print(list(filter(lambda a: a!=0, num)))

numbers = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda a:a**2,filter(lambda a: a%2 == 0,numbers))))

print(list(filter(lambda a: a%2 == 0,map(lambda a:a**2,numbers))))

'''
# Convert names starting with A in uppercase in a list usinf filter and map
# cube of all positive numbers using map and filter
# Append # to emails ending with .com
ex: ['xyz@gmail.com','psd@gmail.in','jhgj@yahoo.com']
ex: ['xyz@gmail.com#','jhgj@yahoo.com#']'''



'''
map function is a function that executes a function for each item inan iterable
like list, tuple etc.

map takes 2 arguments:
1) function -> what to do with data
2) iterable -> with what data to do
'''
'''
colors = ('Red', 'Orange','Yellow','green')
print(colors)
print(len(colors))


def colorslength(color):
    return len(color)

length = map(colorslength,colors)
print(list(length))

for i in colors:
    print(len(i))
    '''
'''
colors = ('Red', 'Orange','Yellow','green')
fruits = ('Apple','Orange','Banana','Melon')
print(colors+fruits)

def fruit_color(fruit,color):
    return fruit + color

fc = list(map(fruit_color,fruits,colors))
print(fc)'''

# map with lambda
mylist = [10,20,30,40]
result = list(map(lambda a: a*2, mylist))
print(result)


# sum of elements of two lists
#method 1
l1 = [1,4,7]
l2 = [2,3,6]
def calsum(l1,l2):
    return l1+l2

cal = list(map(calsum,l1,l2))
print(cal)

# method 2
print(list(map(lambda a,b: a+b, l1,l2)))


'''
# convert each list element into capital using map
# Remove extra spaces using map ex: [' Red   ',' green       ']
# Multiply 2 list using map
# convert a list of Integers into String -> [10,20,30] --> ["10","20","30"]
#Create a dictionary having fruits with prices, using map provide
10% discount on each fruit

#Convert temperature from celcius to farenheit using map
#Extract first letter of each word in list
'''
























































'''
import math
print(math.sqrt(16))
print(math.factorial(4))
print(math.pow(2,4))
print(math.floor(34.7))
print(math.ceil(34.7))

'''

import random as r
'''
print(r.random())  # 0.0 to 1.0
print(r.randint(1,6)) # int 1 to 6
print(r.uniform(1,6)) #float 1 to 6

data = ['apple','mango','banana','papaya','orange']
print(r.choice(data))
print(r.choices(data, k=3))
print(r.sample(data,k=2))

r.shuffle(data)
print(data)

r.seed(7)
print(r.randint(1,100))

# dice rolling
def roll_dice():
    return r.randint(1,6)

for i in range(5):
    print("Dice Rolled: ",roll_dice())'''

print(r.gauss(0,1))

from collections import Counter
print(Counter("fnwdkjfnewkjfnnm"))


fruits = ['apple','mango','banana','apple','orange','papaya','orange','apple','apple','papaya','papaya']
c = Counter(fruits)
print(c)
print(c.most_common(3))







































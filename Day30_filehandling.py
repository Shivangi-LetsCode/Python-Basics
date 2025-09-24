#File handling
'''
To store data permanently
Types of files:
  Text file(.txt)
  Binary file


STEPS:
1) Open
2) Process
3) Close

Mode:
r --> read only
    if file doesn't exists then FileNotFoundError

w --> write only (no reading)
    if file doesn't exists then new file will be created.
    If  file already exists with data, it will remove all previous content from the file
    and starts writing from the starting

a --> append only(no reading)
    if file doesn't exists then new file will be created.
    If file already exists with data,it will continue writing from last
    character occurance.

x --> Exclusive write mode
       Fresh writing only
       If file exists it will provide error.
       if file doesn't exists then new file will be created.


r+ --> reading/writing/modify
        if file doesn't exists then FileNotFoundError
        Pointer/cursor points starting character, after reading full content starts
        writing
        

w+ --> reading/writing
        if file doesn't exists then new file will be created.
        will erase previous data and starts writing from starting

a+ --> reading/writing
        if file doesn't exists then new file will be created.
        If file already exists with data,it will continue writing from last
        character occurance.

'''
'''
f = open('textfile.txt','r')
print(f.name)
print(f.mode)
#print(f.read())
#print(f.readline())
print(f.read(4))
f.close()'''
'''
f = open('textfile.txt','r')
for text in f:
    print(text)
'''
'''
f = open('textfile.txt','w')
text = input("What you want to write?")
f.write(text)
f.close()'''
'''
f = open('textfile.txt','a')
text = input("What you want to write?")
f.write(text)
f.close()'''
'''
f = open('textfile1.txt','a')
l = ['Apple\n','Orange\n','Mango\n']
f.writelines(l)
f.close()
'''
'''
f = open('textfile.txt','x')
text = input("What you want to write?")
f.write(text)
f.close()'''

'''
#PERSONAL DIARY APP
1) Add a new diary entry
2) View entries by date
3) Delete entries

menu: add entry, view entry, delete entry, close entry, choice, if elif'''
import os
from datetime import datetime






























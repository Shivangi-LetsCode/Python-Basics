'''
EXCEPTION HANDLING
Syntax error and Logical Error(Exception)
1) Python raises exception, Python Handles
2) Python raises exception, Developer Handles
3) Developer raises exception, Python Handles
4) Developer raises exception, Developer Handles
'''
'''
try, except, raise, finally
'''
'''
#Syntax error:
#print("Hello" #error
# print("Hello") #error

#1) Python raises exception, Python Handles
#print(9/0)  #ZeroDivisionError
#print(x) #NameError

x = 10
y =  '20'
#print(x+y) #TypeError

l = [10,20,30]
print(l[3]) #IndexError


#2) Python raises exception, Developer Handles
try:
    print(9/0)
except:
    print('Please do not divide by Zero')



try:
    num = int(input("Enter numerator"))
    den = int(input("Enter denomenator"))
    print(num/den)
except:
    print('Please do not divide by Zero')



try:
    num = int(input("Enter numerator"))
    den = int(input("Enter denomenator"))
    print(num/den)
except ValueError:
    print('Please provide Integer only')


try:
    num = int(input("Enter numerator"))
    den = int(input("Enter denomenator"))
    print(num/den)
except ValueError:
    print('Please provide Integer only')
except ZeroDivisionError:
    print("Do not divide by zero")

try:
    num = int(input("Enter numerator"))
    den = int(input("Enter denomenator"))
    number = float(input("Enter number: "))
    print(num/den)
    print(num + number)
except ZeroDivisionError:
    print("Do not divide by zero")
except ValueError:
    print('Please provide Integer only')
except TypeError:
    print("Provide expected Type")
else:
    print("Everything Is Fine!!")


try:
    num = int(input("Enter numerator"))
    den = int(input("Enter denomenator"))
    number = float(input("Enter number: "))
    print(num/den)
    print(num + number)
except ZeroDivisionError:
    print("Do not divide by zero")
except ValueError:
    print('Please provide Integer only')
except TypeError:
    print("Provide expected Type")
else:
    print("Everything Is Fine!!")
finally:
    print("Hi!! I am Finally!")'''



'''
try:
    int(input("Enter Number: "))
    result  = "5" + 5
    list1 = [1,2,4]
    print(list1[6])

except(ValueError,TypeError):
    print("Something Wrong!!")
except IndexError:
    print("No Value Found!!")
finally:
    print("Hi! I am finally!!")

try:
    num = int(input("Enter numerator"))
    den = int(input("Enter denomenator"))
    print(num/den)
except Exception as e:
    print(e)'''



'''
function --> student_register(name, age)
name mandatory, age should be more than 15(valueError)

'''
help(Exception)








































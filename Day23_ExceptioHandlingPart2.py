'''
#3) Developer raises exception, Python Handles
num = int(input("Enter Numerator"))
den = int(input("Enter Denomenator"))
if den == 0:
    raise ZeroDivisionError("Denomenator can not be Zero!")
print(num/den)'''

'''
#4) Developer raises exception, Developer Handles
try:
    num = int(input("Enter Numerator"))
    den = int(input("Enter Denomenator"))
    if den == 0:
        raise ZeroDivisionError("Denomenator can not be Zero!")
    print(num/den)
except ValueError:
    print("Wrong value type")
except ZeroDivisionError as z:
    print(z)'''

'''
#NESTED TRY CATCH
try:
    print(10/2)
    try:
        num = int(input("Enter Numerator"))
        den = int(input("Enter Denomenator"))
        print(num/den)
    except ZeroDivisionError:
    print("You can not divide by Zero!!")
except ValueError:
    print("You have a value error")'''


#Nested try catch using Developer raises exception, Developer Handles


#Mini Project
class InvalidPin(Exception):
    def __init__(self,message):
        self.msg = message

actual_pin = 1234
entered_pin = int(input("Enter Pin: "))
try:
    if entered_pin != actual_pin:
        raise InvalidPin("Wrong Pin Entered!!")
except InvalidPin as I:
    print(I.msg)
else:
    print("Pin is Validated Successfully!!")
        


'''ATM Simulator:
User enters pin and performs check balance, withdrawl,
deposit and handle wrong inputs and exceptions.'''

    









#1: ARITHMETIC OPERATORS
print("Arithmetic operators")
print("Addition: 7+9=", 7+9)
print("Subtraction: 7-12=", 7-12)
print("Multiplication: 7*9=", 7*90)
print("Division: 16/4=", 16/4)
print("Integer division: 16/4=", 16/4)

#2: BOOLEAN OPERATORS
# x and y: if x is false → returns x, otherwise returns y
# x or y: if x is true → returns x, otherwise returns y
# Anything non-zero number = True
print("7 or 20=", 7 or 20)
print("7 and 20=", 7 and 20)
print((7-7) or False or 21/3 or 16)
# 0 not true, false not true, so it prints 21/3 = 7
print(7 and None and 22)
# 7 is true, none is not true, so prints none

## Not AlWAYS returns True or False
# Is 7 truthy? Yes — any non-zero number is True.
print(not 7)
print(not True)
print(not 0)


print("7 < 20=", 7 < 20)
print("7 > 20=", 7 > 20)
print("7 <= 7=", 7 <= 7)
print("7 == 7=", 7 == 7)
print("7 != 7=", 7 != 7)
print(0 == 0.0) #True
print(1 == True) #True
print(2 == True) #False, because we already established True as 1
print(7 is 7) #Identity (= → checks value / is → checks identity (same memory object))
print(7 is not 8)

#3: VARIABLES
# LHS is a name we call the variable
# RHS is the value we associate with it, in this case, a float number

a = 10
speed = 20
time = 30
print("distance =", speed * time)

#4: GETTING INPUT
prompt = "what is your name?"
name = input(prompt)
if name == "Carlota":
    print("FU Carlota")
else:
    print("nice to meet you", name)

#5: CATCHING EXCEPTIONS
# Errors that happen during execution (not syntax). Examples in slides: NameError, ZeroDivisionError.
try:
    prompt2 = ("how old are you," + name + "?")
    age = input(prompt2)
    # convert to int
    age = int(age)
    print("you were born in,", 2025 - age)
except ValueError:
    print("sorry", name, "but that is not a number")
except NameError:
    print("sorry that is not a valid name for print")
except:
    print("all other exceptions go here!")
# Catches any other error not included above. MUST be last!
else:
    print("thank you for playing fair and square")
# The else runs ONLY if: No exception occurred. The try block completed successfully
# If an error happens, else doesn't run

#6: CONDITIONAL EXECUTION
try:
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
except ValueError:
    print("Please enter a valid integer.")


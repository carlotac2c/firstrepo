#1: OPERATORS
print(2 + 3)
print(6 / 2)
print(2 != 3)
print(5 or 6)
print(2 + 3 * 2 ** 2)

#2: VARIABLES
a = 2
b = 3
c = "abc"

print(a, b, c)
print(a, b, c, sep=",")

a += 2
print(a)
a -= 1
print(a)
a *= 3
print(a)
a /= 2
print(a)

#3: STRING OPERATIONS
print("bubu" * 2)

# Must convert 4/2 to int because it's float
print("bubu" * int(4/2))

# Will print the 3rd element. So element 1 = [0] / element 2 = [1]
print("abc"[2])

# “Split this string every time you see the letter 'a'.”
print("abcabcabc".split("a"))

#4: LIST BASICS
# [] creates a list
my_list = ["abc", 2]
print(my_list)

# len counts length of the list: how many elements are there?
print(len(["abc", 2]))

# append("John") adds "John" at the end of the list.
a = [1, 2, 3]
a.append("John")
print(a)

#5: INPUT + TYPE CONVERSION
num = input("Enter number: ")
print("You typed:", num)

num_int = int(input("Enter integer: "))
print("Double:", num_int * 2)

#6: EXCEPTIONS
# “Try to execute this code. If an error happens, don’t crash, handle it.
# Python immediately stops executing the try block: It jumps to the matching except
# input() returns a string / int() tries to convert it to an integer.
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    print("Result:", x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid number")

#7: CONDITIONALS
# If this condition is true, do something. Otherwise, do something else.”
number = int(input("Enter a number: "))

# % means remainder.
if number % 2 == 0:
    print("even")
else:
    print("odd")

#8: BOOLEAN OPERATORS
# Both sides must be True to get True
print(True and False)
# At least one side must be True
print(True or False)
# Reverse the value
print(not True)

#9: WHILE LOOP
# Keep repeating this code while the condition is True
# “Is n less than 5?” If YES → run the code inside / If NO → stop the loop
# Two things happen every time: 1. Print the current value of n / 2.Increase n by 1
# Stops at 4 because 5 =5
n = 1
while n < 5:
    print(n)
    n += 1

#10: FOR LOOP
# range(start, stop): starts at 1, stops at 10 (doesn't include 10)
# range(10) produces numbers from 0 to 9. ALWAYS excludes last number
for i in range(10):
    print(i)

for i in range(1, 4):
    print(i)

# Strings are sequences of characters. So Python reads: a,b,c one by one
for letter in "abc":
    print(letter)

#11: BREAK
for i in range(10):
    if i == 5:
        break
    print(i)
# break = immediately exit the loop completely. The moment i == 5, the loop exits, never prints 5

#12: CONTINUE
for i in range(5):
    if i == 2:
        continue
    print(i)
# continue = Skip the rest of THIS iteration, Go to the next loop cycle. Doesn't print 2.

# FULL PROGRAMME
a = 2
b = 3
c = "abc"

print(a, b, c)
print(a, b, c, sep=",")

a += 2
print(a)

print(c * (a - b))

# find searches for a substring inside a string. It returns: The index position where it first appears
# -1 if not found
d = c.find("b")
print(d)
print(d and b)
print(d == True)

e = str(a) + str(b) + str(c) + str(d)
print(e)
# SLICING = string[start : stop : step]
# Start at index 1. Take every 2nd character
print(e[1::2])
# No start, no stop. Step = -1. This reverses the string.
print(e + e[::-1])




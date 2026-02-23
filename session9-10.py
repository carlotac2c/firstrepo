#1: FILES
# opening a file METHOD 1
fp = open ("text.txt") #open for read is by default
print(fp.read()) #reads the content of the file
fp.close()

# opening a file METHOD 2
with open("text.txt") as fp:
    print(fp.read())

# reading a file line by line
with open("text.txt") as fp:
    for line in fp:
        print(line.capitalize().rstrip())
fp.close()

# writing to file
# "a" → append mode / write() does NOT add newline automatically / must manually add "\n"
fp = open("text.txt", "a")
print(fp)
line = input("Give me some text, don't be shy: ")
fp.write(line)
fp.write("\n")
fp.close()

#2: FUNCTIONS
# max = highest character (ascending order in alphabet). every character has a code in python.
print(max('Hello world'))
print(min('Hello world'))
print(len('Hello world'))
print(int(3.2))
print(float(7))
print(str(3+6))

#3: MATH FUNCTIONS
import math
# must import math. math.sin expects radians
print(math.sin(30 /360 * 2 * math.pi))
print(math.sin(45 /360 * 2 * math.pi))
print(math.sqrt(2)/2)
# help() shows documentation / dir() shows all functions
print(help(math.sinh))
print(dir(math))

#4: RANDOM MODULE
# random.random() → number between 0 and 1
import random
for i in range(10):
    x = random.random()
    print(x)

# randint(5,10) → integer between 5 and 10
print(random.randint(5, 10))
# choice(list) → random element
ppl = ["Jon", "Ana", "Maria", "Jim", "Florence", "George", "James"]
print(random.choice(ppl))

#5: CREATING FUNCTIONS
# def defines function.
# To call the function, use the name followed by the arguments between ().
# To print the docstring, use help() function
def greet():
    """
    Input: none
    This function just prints "Hello!"
    """
    print("Hello!")

# FUNCTION W/ ARGUMENT
def greet_name(name):
    """
    Input: name (string)
    This function prints "Hello, <Name>"
    """
    print("Hello,", str(name).capitalize())

# Call first function
greet()

# Show documentation
help(greet)

# Call second function
greet_name("james")

# FUNCTION W/ 3 ARGUMENTS
def sum_and_multiply(t1, t2, m):
    """
    :param t1: addition number1
    :param t2: addition number2
    :param m: multiplicator
    :return: prints (t1+t2)*m
    """
    print((t1+t2)*m)

sum_and_multiply(1,2,3)

# NAMED ARGUMENTS
def sum_and_multiply(t1, t2, m):
    print((t1+t2)*m)

sum_and_multiply(t2=1,m=2,t1=3)

# FUNCTIONS THAT RETURN VALUES
def sum_and_multiply(t1, t2, m):
    """
    :param t1: addition number1
    :param t2: addition number2
    :param m: multiplicator
    :return: prints (t1+t2)*m
    """
    return (t1+t2)*m

result = sum_and_multiply(1,2,3)
print("(1+2)*3 - 4 = ", result-4)
# return sends value back
# stored in variable result

# FUNCTIONS THAT CALL ANOTHER FUNCTION
# # bond() returns string. That string is passed into introduce().
def introduce(name):
    """
    :param name: a regular string :return: prints the name
    """
    print("The name is:", name)

def bond(first_name="james", last_name="bond"):
    """
    Cool function
    :param first_name: first name, default "james"
    :param last_name: last name, default "bond"
    :return: returns the cool introduction
    """
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return last_name+","+" "+first_name+" "+last_name

introduce(bond())

#5: LISTS
# A list is a sequence of values.
# As opposed to a string which is a sequence of only characters, a list can be a sequence of anything
a=[]
print(a)
a=[1,3,5,2,54]
print(a)
a=["me", "myself", "eye"]
print(a)
a = ["me", 2+3, "hey"+"you", -4.2, None]
print(a)

#6: MUTABLE LISTS
# A list is mutable because you can CHANGE the items inside the list after it was created.
# It was not possible with strings
lst = [1, 3, 5, 7, 9]
print(lst[1])

lst[1] = 11
print(lst)

lst[1] = lst[2]
print(lst)

#7: CODE SLICING
# like with range slice[start:end:step]
list = [1,2,3,4,5,6,7,8,9,10]
print(list[1:3])
print(list[:4])
print(list[4:])
print(list[::3])
print(list[::-1])

#8: LIST OPERATIONS
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

print([0] * 4)
print([1, 2, 3] * 3)

# The built in function len() will return the length of a list.
a = [1,3,5]*3
print(len(a))

# lists within a list
a = ["aa", 22, [1,2,3,4,5], ["one", "two", "three"]]
print(len(a))

# List is “iterable” so for can be used to get each element
for n in a:
    print(n)

#9: LIST METHODS
# append() adds a new element at the end of the list
t = ['a', 'b', 'c']
t.append('d')
print(t)

# extend() takes another list and appends it to the end
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

# sort() arranges the elements from low to high
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)

t = t.sort()
print(t)

#10: REMOVE METHODS
# pop() modifies the list and returns the element that was removed.
# If you don't provide an index, it deletes and returns the last element.
t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)

# del operator just removes the element(s),if you do not need it anymore
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)

# remove()d eletes an element when the element is known,but not the index.
# It returns None. Error if the element is not present in the list
t = ['a', 'b', 'c']
t.remove('b')
print(t)
#1: STRINGS
text = "Python"
name = 'Carlota'

#2: STRING INDEXING
# each string has a position (starting with 0)
print(text[0])   # P
print(text[4])   # o

# negative indexing, -1 is the last character
print(text[-1])  # n
print(text[-2])  # o

#3: STRING SLICING
# format= string[start:stop:step]
print(text[0:3])  # Pyt
print(text[2:5])  # tho
# omiting values
print(text[:3])   # Pyt
print(text[3:])   # hon
print(text[:])    # Python
# step slicing
print(text[::2])  # Pto
# reverse string
print(text[::-1])  # nohtyP

#4: IMMUTABILITY
text = "Python"
text = "J" + text[1:]
print(text)  # Jython

#5: LOOPING
# prints one letter per line. each iteration: ch becomes one character
for ch in text:
    print(ch)

#6: BUILDING A STRING W/ A LOOP
# if you want to modify a string, you must create a new string step-by-step.
text = "Hello World"
new_text = ""

for ch in text:
    if ch != " ":
        new_text += ch

print(new_text)  # HelloWorld

#7: STRING METHODS
text = "Python"
# len = returns the number of characters (spaces count)
print(len(text))  # 6

# lower/upper = convert to lower/upper case
print(text.lower())  # python
print(text.upper())  # PYTHON

# strip = removes spaces from beginning and end
text = "  hello  "
print(text.strip())  # hello

text = "Python"
# find = searches for a substring (index if found, -1 if not found)
print(text.find("t"))  # 2 because p(0) y(1) t(2)
print(text.find("z"))  # -1

# replace = replaces part of string
print(text.replace("P", "J"))  # Jython

# count = counts how many times something appears.
text = "banana"
print(text.count("a"))  # 3

# startswith/endswith = checks beginning or ending = gives Boolean values
text = "Python"
print(text.startswith("Py"))  # True
print(text.endswith("on"))    # True

# isdigit = checks if ALL characters are digits = gives Boolean values
text = "12345"
print(text.isdigit())  # True

# isalpha = checks if ALL characters are letters = gives Boolean values
text = "abc"
print(text.isalpha())  # True

# s.capitalize, s.center
text = "Hey my name is John"
print(text.capitalize())
print(text.center(30))

#8: MEMBERSHIP OPERATOR
# checks whether something exists inside something else
text = "Python"
print("th" in text)   # True
print("z" in text)    # False

#9: COMMON EXERCISES
# count vowels
text = "education"
count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print(count)

# reverse string manually
text = "Python"
reversed_text = ""

for ch in text:
    reversed_text = ch + reversed_text

print(reversed_text)

# check palindrome
text = input("Enter word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# sum digits
text = "12345"
total = 0

for ch in text:
    total += int(ch)

print(total)  # 15

# parsing strings
s = "http://google.com and then there could be http://yahoo.com or even a website"

start = 0

while True:
    start = s.find("http://", start)
    if start == -1:
        break

    end = s.find(" ", start)

    if end == -1:
        print(s[start:])
        break

    print(s[start:end])
    start = end
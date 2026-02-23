#1: TUPLES
#  A tuple is a sequence of values (much like a list!)
a = ()
print(a)

a = (1,3,5,2,54)
print(a)

a = ("me", "myself", "eye")
print(a)

a = ("me", 2+3, "hey"+"you", -4.2, None)
print(a)

# dif between int and tuple (comma makes it a tuple)
a = (5)
print(type(a))
a = (5,)
print(type(a))

#2: TUPPLES ARE IMMUTABLE
# You can not change them once they have been defined (opposed to lists)
a = tuple("Macarena")
print(a)
print(a[2])

# convert list into tuple
a = tuple([1,2,3,4,5])
print(a)

#3: TUPLE SLICING
# just like with the range() function, slicing is [start:end:step]
tpl = (1,2,3,4,5,6,7,8,9,10)
print(tpl[1:3])
print(tpl[:4])
print(tpl[4:])
print(tpl[::3])
print(tpl[::-1])
# can construct a new tuple)
tpl = (100,) + tpl[1:]
print(tpl)

#4: TUPLE OPERATIONS
a = (1, "one", None)
b = (3, 'seven')
print(a + b)

print(4*a)

print(len(tpl))

# tuple is iterable
for n in a:
    print(n)

# tuple unpacking
x, y = ["one", "two"]
print(x)
print(y)
x,y = y, x
print(x)
print(y)

#5: DICTIONARIES
# a more general type of list
# While in a list the indices are integers, in a dictionary they can be almost any immutable object.
# In the case of dictionaries, the index is called a “key”.
# Like indices, the “keys” need to be unique and each key maps to a value.
# Dictionaries are mutable!
# created with {}

d = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(d)
print(d["two"])

#6: DICTIONARY OPERATORS
print(len(d))

# for skips over keys
for n in d:
    print(n)

# adding/deleting elements
d= {'John': 7, 'Mary': 9, 'James': 4, 'Jane': 6, 'Jorge': 8}

d["Ana"] = 9
print(d)

del(d["Mary"])
print(d)

#7: DICTIONARY METHODS
# in can be used to check if a key is present in the dictionary
d= {'John': 7, 'Mary': 9, 'James': 4, 'Jane': 6, 'Jorge': 8}
print("Mary" in d)
print("mary" in d)
print(4 in d)

# The method keys returns an iterable that acts as a tuple of all the keys
print(d.keys())

# The method values returns an iterable that acts as a tuple of all the values
print(d.values())

# The method get takes a key and a default value to return if the key is not present
d= {'John': 7, 'Mary': 9, 'James': 4, 'Jane': 6, 'Jorge': 8}
print(d.get("Jane", 0))
# Returns default value → 0 if key not present
print(d.get("Janes",0))

#8: FULL FILE EXAMPLE
punctuation2 = ",.;:!?\"'()[]{}-*<>"

def common_words(file_name):
    fd = open(file_name, "r")
    d = {}
    for line in fd:
        for c in punctuation2:
            line = line.replace(c, " ")
        words = line.split()
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

    values = list(d.values())
    values.sort(reverse=True)
    common = []
    for numbers in values[:10]:
        for keys in d:
            if d[keys] == numbers:
                common.append((keys, numbers))

    print("the most common words are:")
    for i in common:
        print(i[0], i[1], "times")

# THIS IS WHAT MAKES IT RUN
common_words("text1.txt")
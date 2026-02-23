fp = open ("text.txt") #open for read is by default
print(fp.read()) #reads the content of the file
fp.close()

# this can also be done like this
with open("text.txt") as fp:
    print(fp.read())
    # the file is open in this context
# now i am no longer in the context
# read line by line and can also process it:
with open("text.txt") as fp:
    for line in fp: # use for to read line by line!
        # print(line.capitalize(), end="")
        print(line.capitalize().rstrip())
        # "bob".capitalize().replace("o", "i").center(100)



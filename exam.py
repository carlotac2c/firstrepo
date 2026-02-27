# Q1
import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

# Q2
print(2+3*6/2)

# Q3
#Define the function
def is_valid_url(url):

    # 1.Must be a string
    if type(url) != str:
        return False

    # 2.No spaces allowed
    if " " in url:
        return False

    # 3.Must start with http:// or https://
    if url.startswith("http://"):
        rest = url[7:]
    elif url.startswith("https://"):
        rest = url[8:]
    else:
        return False

    # 4.Must have something after the scheme
    if rest == "":
        return False

    # 5.Separate domain and path
    position = rest.find("/")

    if position == -1:
        domain = rest
        path = ""
    else:
        domain = rest[:position]
        path = rest[position:]

    # 6.Domain must contain a dot
    if "." not in domain:
        return False

    parts = domain.split(".")

    #No empty parts like example..com
    for part in parts:
        if part == "":
            return False

        #Check allowed characters in domain
        for ch in part:
            if not (
                ("a" <= ch <= "z") or
                ("A" <= ch <= "Z") or
                ("0" <= ch <= "9") or
                ch == "-"
            ):
                return False

    # 7.Validate path (if exists)
    if path != "":
        if path[0] != "/":
            return False

        for ch in path:
            if not (
                ("a" <= ch <= "z") or
                ("A" <= ch <= "Z") or
                ("0" <= ch <= "9") or
                ch == "-" or
                ch == "_" or
                ch == "." or
                ch == "~" or
                ch == "/"
            ):
                return False

    return True

# Example Tests
print(is_valid_url("https://www.example.com"))          # True
print(is_valid_url("http://example.com/blog"))         # True
print(is_valid_url("https://example.com/blog/page1"))  # True
print(is_valid_url("ftp://example.com"))               # False
print(is_valid_url("https://example"))                 # False
print(is_valid_url("https://example .com"))            # False

# Q4
#Define the function
def days_since_birthday():

    CURRENT_YEAR = 2026  # Change manually if needed

    birthday = input("Enter your birthday (DD-MM-YYYY): ")

    # 1.Check format
    parts = birthday.split("-")
    if len(parts) != 3:
        print("Invalid format")
        return

    # 2.Convert safely
    try:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
    except:
        print("Invalid date values")
        return

    # 3.Year validation
    if year >= CURRENT_YEAR or year < 0:
        print("Invalid year")
        return

    # 4.Month validation
    if month < 1 or month > 12:
        print("Invalid month")
        return

    # 5.Determine max days in month
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max_days = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30
    else:  # February
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_days = 29
        else:
            max_days = 28

    # 6.Day validation
    if day < 1 or day > max_days:
        print("Invalid day")
        return

    # 7.Calculate full years only
    total_days = 0

    for y in range(year + 1, CURRENT_YEAR):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            total_days += 366
        else:
            total_days += 365

    print("Days passed (whole years only):", total_days)

# Call the function
days_since_birthday()

# Q6
a = 10
a = a + 2
print(a*2)

a = 19
print(a+3)

a = a // 2
print(a)

# Q7
import random  #Import "random" to generate random numbers

random_numbers = []  #Create empty list to store the random numbers

#Generate 10 random numbers between 1 and 100
for i in range(10):
    #random.randint(1, 100) generates a random integer from 1 to 100
    random_numbers.append(random.randint(1, 100))
    #append() adds the generated number to the list

#Go through the list using index so that we can modify elements
for i in range(len(random_numbers)):

    number = random_numbers[i]
    #Store the current element in a variable

    #If the number is greater than 80 (n>80)
    if number > 80:
        #Replace it with its negative value (-number)
        random_numbers[i] = -number

    #If the number is lower than 40 (n<40)
    elif number < 40:
        #Convert the number to a string to access each digit (str(n))
        digits = str(number)

        digit_sum = 0  #Variable to store the sum of digits

        #Loop through each character (digit) in the string
        for d in digits:
            #Convert digit back to integer and add to total
            digit_sum += int(d)

        #Replace the original number with the sum of its digits
        random_numbers[i] = digit_sum

#Print the final list
print(random_numbers)

# Q8
#STEP 1 = define the function
def longest_word_starting_with_c(textforQ8):
    #Open the file in read mode
    fp = open(textforQ8, "r")

    longest_word = ""  #Variable to store the longest word found

    #Read the file line by line
    for line in fp:

        #Split the line into words
        words = line.split()

        #Go through each word in the line
        for word in words:

            #Check if word starts with "c"
            #Word[0] gives the first character
            if len(word) > 0 and word[0] == "c":

                #Compare lengths
                if len(word) > len(longest_word):
                    longest_word = word

    #Close the file
    fp.close()

    #Return the result
    return longest_word

#Print the result
result = longest_word_starting_with_c("textforQ8")
print(result)

# Q9
l = ['c', 'a', 'r', 'l', 'o', 't', 'a']
l[4] = 'i'
print(l)

# Q10
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("9847255590886266818998186626880955527489"))

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("6892149109325320763773670235239019412986"))

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("6800923757255865070000705685527573290086"))

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("1414884937242655719669145562427394884141"))



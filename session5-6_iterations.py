#7: ITERATIONS/LOOPS
# Repeating code = iteration/loop. Two main types: while and for

# WHILE LOOP: unknown number of iterations
n = 1
result = 0
while n < 10:
    result += n
    n += 1
print("The sum of the first 9 numbers is", result)

# Infinite loop + break/continue
# break exits the loop completely / continue skips to the next iteration
while True:
    num = input("Give me a number (type quit to exit): ")
    num2 = input("Give me another number (type quit to exit): ")
    if num == "quit" or num2 == "quit":
        break
    num = int(num)
    num2 = int(num2)
    if num2 == 0:
        print("Can not divide by zero")
        continue
    print("The division result is", num / num2)

# FOR LOOP: definite loop: known finite steps
# Looping with a range
# range(start, stop[, step]
result = 0
for i in range(0, 10):
    result += i
print("The sum of the first 9 numbers is", result)

# Looping through a string
result = 0
text = "1234567890"
for ch in text:
    result += int(ch)
print(result)
# Python goes through each character one by one, but has to convert characters into integers

# for: known number of iterations, uses iterables
# while: unknown number, must manage condition (and often counters)

# HOMEWORK
try:
    gross = float(input("Gross salary: "))
    children = int(input("Number of children: "))

    # base tax rate by bracket
    if gross < 1000:
        tax_rate = 0.10
    elif gross < 2000:
        tax_rate = 0.12
    elif gross < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18

    # child tax cut
    if gross < 2000:
        tax_rate -= 0.01 * children
    else:
        tax_rate -= 0.005 * children

    # prevent negative tax (optional safety)
    if tax_rate < 0:
        tax_rate = 0

    net = gross * (1 - tax_rate)
    print("Net salary:", net)

except ValueError:
    print("Invalid input. Please enter numbers.")

# EXERCISES
#1
divisor = 3
for num in range(0, 12, 3):
    print(num/divisor)

#2
num = 0
while num <= 5:
    print(num)
    num += 2

print("Out")
print(num)

#3
num = 0
count = 0

while num <= 19:
    if num % 3 == 0:
        count += 1
    num += 1

print("Numbers divisible by 3:", count)

#4
for letter in 'Ahola':
    print(letter)
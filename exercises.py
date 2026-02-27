def letters():
    while True:
        try:
            num = int(input("Please give me a grade from 0 to 100: "))
        except ValueError:
            print("I need a number")
            continue

        if num < 0 or num > 100:
            print("Grade must be between 0 and 100.")
            continue

        if num >= 90:
            return "A"
        elif num >= 80:
            return "B"
        elif num >= 70:
            return "C"
        elif num >= 60:
            return "D"
        else:
            return "E"

print(letters())

# LOOPS
num = 0
while num < 10:
    print(num)
    num += 1

total = 0

# LOOPS
for num in range(1, 101):
    if num % 2 == 0:
        total += num

print("The sum of even numbers between 1 and 100 is:", total)

# LOOPS
def palindrome_check():
    text = input("Enter text: ")

    punctuation = ".,!?;:\"'()"

    # Remove punctuation
    for c in punctuation:
        text = text.replace(c, "")

    text = text.lower().replace(" ", "")

    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")

palindrome_check()

# LOOPS
def characters():
    text = "education"
    count = 0

    for ch in text:
        if ch in "abcdefghijklmnopqrstuvwxyz":
            count += 1

    return count

print(characters())

# TEXT ANALYSER
def text_analyzer(file_name):
    punctuation = ",.;:!?\"'()[]{}-*<>"

    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found.")
        return

    word_count = {}

    for line in file:
        line = line.lower()

        # remove punctuation
        for p in punctuation:
            line = line.replace(p, " ")

        words = line.split()

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    file.close()

    # total unique words
    print("Total unique words:", len(word_count))

    # sort words by frequency
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    print("\nTop 5 words:")
    for word, count in sorted_words[:5]:
        print(word, "-", count)


# run it
text_analyzer("text.txt")

grades = {"John":7, "Mary":9, "Ana":6}

# Print average grade
total = 0
for student in grades:
    total += grades[student]

average = total / len(grades)
print("Average grade:", average)

# Print highest student
max_grade = -1
top_student = ""

for student in grades:
    if grades[student] > max_grade:
        max_grade = grades[student]
        top_student = student

print("Highest student:", top_student)

# Add new student
grades["James"] = 8

print("Updated grades:", grades)
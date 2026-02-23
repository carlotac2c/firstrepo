print(type(2+3))
print(type(6/2))
print(type(2 != 3))
print(type( 5 or 6))
print(type(print))
print(type(print(2*2)))
print(type("abc".find))
print(type("bubu"*2))
print(type(["abc", 2]))
print(type("abc"[2]))

a = 2
b = 3
c = "abc"

print(a, b, c)
print(a, b, c, sep=",")

# a = a + 2
a += 2
a == 5

print(a)
print(c * (a - b))

d = c.find("b")
print(d)

print(d and b)
print(d == True)

e = str(a) + str(b) + str(c) + str(d)
print(e)

print(e[1::2])
print(e + e[::-1])

# FUNCTION 1
# r tells python to open a file = read mode
# lower().startswith("b") makes it work for Bat, BAT, bat, etc.
# w_clean keep only letters, remove punctuation around the word
def print_b_three_letter_words(file_name):
    fp = open(file_name, "r")

    for line in fp:
        words = line.split()
        for w in words:
            w_clean = w.strip(",.;:!?\"'()[]{}-*<>")

            if len(w_clean) == 3 and w_clean.lower().startswith("b"):
                print(w_clean)

    fp.close()

print_b_three_letter_words("text2.txt")

# FUNCTION 2
def divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

print(divisors(21))

# n % i = i divides n with no remainder

# FUNCTION 3
def force_multiple_6():
    """
    :return: int
    """
    while True:
        num = input("Please give me a multiple of 6:")
        try:
            num = int(num)
            if num % 6 == 0:
                return num
            else:
                print("At least you gave me a number. Try again, it needs to be a multiple of 6")
        except ValueError:
            print("I need a number")
print(force_multiple_6())

# FIND WORDS FROM BOOK
pip install requests
import requests

def download_book(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    with open("book.txt","w", encoding="utf-8") as f:
        f.write(response.text)

download_book("https://www.gutenberg.org/files/64317/64317-0.txt")


def find_3_letter_words(book_name):
    unique_words = []
    special_chars = ",.?!;`"

    with open(book_name, "r", encoding="utf-8") as f:
        for line in f:
            for c in special_chars:
                line = line.replace(c, "")
            words = line.split()

            for word in words:
                if (
                    word.lower().startswith("b")
                    and len(word) == 3
                    and word.lower() not in unique_words
                ):
                    unique_words.append(word.lower())

    print(unique_words)

find_3_letter_words("book.txt")
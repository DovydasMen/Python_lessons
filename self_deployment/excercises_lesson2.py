# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning


# sentence = "Code Academy ju lo me"
#  #          0123456789

# print(sentence[5])
# print(sentence[-2]) # is kito galo skaiciuoja
# print(sentence[5:10]) # skaiciuoja tarpa, kuri isspelint.
# print(sentence[5:]) # nuo penkto elemento iki galo.
# print(sentence[0:4]) #nuo pirmo elemento iki 4
# print(sentence[5:12:1])
# print(sentence[5::2])# nuo penkto elemento iki galo, kas antr1 elementa renkantis.
# print(sentence[::-1])# atprintis atbulai
# print(sentence.split()) #sukala i lista
# print(sentence.replace("C", "k")) # pakeis tik didziasias raides, mazosios liks tokios pacios.
# print(sentence.replace("Code", "Music"))

# print(sentence[-1])
# print(sentence.upper())
# print(sentence.translate("C"))

# greeting = "Hello, my name is"
# name = "Dovydas"

# completed_greeting = greeting + " " + name

# print(completed_greeting)

# number_as_a_string = "55"
# flooat_number = float(number_as_a_string)
# int_number = int(number_as_a_string)

# print(flooat_number)
# print(int_number)

# string_it_self = "Hello"
# string_is_number = str(string_it_self)
# print(string_is_number)
# print(string_is_number.__class__) #Visvien stringas




"""Sukurkite programą, leidžiančią vartotojui įvesti savo vardą ir amžių
Apskaičiuoti metus, kuriais vartotojas gimė
Išspausdinti atsakymą į terminalą
"""
# user_name = input("Please enter your name: ")
# it_was_a_birthday = input("Have you selabrated your birthday this year? Y/N?")
# user_age = int(input("Please enter your age :"))


# def years_of_born(name: str, birtday_input: str, age: int) -> str:
#     birtday = birtday_input.lower()
#     if birtday == "y":
#         return f"Hello {name}, you are born on {2023 - age}"
#     else:
#         return f"Hello {name}, you are born on {2022 - age}"

# print(years_of_born(user_name, it_was_a_birthday, user_age))


"""
Create a program that allows user to enter a full sentence
print the sentence backwards
print every second letter in the sentence
"""

# user_input_sentence = input("Please write your sentence:")

# def sentence_slicing(sentence: str) -> str:
#     print(sentence[::-1])
#     print(sentence[::2])
    

# sentence_slicing(user_input_sentence)

"""
Create a program that expects user to enter two numbers
multiply those numbers and print the answer
Create similar programs with other signs.
"""
# number_one, sign, number_two = input("Please define your matematical expretion:").split()

# def calculator (entered_number_one: str, entered_sign: str, entered_number_two: str) -> float:
#     first_number = float(entered_number_one)
#     secound_number = float(entered_number_two)
#     if entered_sign == "+":
#         return first_number + secound_number
#     elif entered_sign == "-":
#         return first_number - secound_number
#     elif entered_sign == "*":
#         return first_number * secound_number
#     else:
#         return first_number / secound_number
    

# print(calculator(number_one, sign, number_two))
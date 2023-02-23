#Create at least 5 different functions by your own and test it.

# name_list = []

# def lords_name(name : str) -> str:
#      name = input(str("Please insert your name: ")).split(" ")
#      return name


# imported_name = lords_name(str)

# name_list.append(imported_name)

# print(name_list)


# def sum_calculator(num1 : int, num2 :int) -> int:
#     return num1 +  num2


# def age_allowance(age: int) -> int:
#     if age >= 21:
#         print("You are old enought to enter")
#     else:
#         print("Your are not allowed to enter")


# age_allowance(13)

# def number_to_the_list(x: int, y: int, z: int)-> int:
#     new_list = [x,  y, z]
#     return new_list

# a = number_to_the_list(1, 2, 7)

# print(a)

# x, sign, y = input("Nurodykite reiksmes: ").split(" ")
# x = float(x)
# y = float(y)

# def calculator(x: float, y: float, sign: str) -> float:
#     if sign == "+":
#         result = x + y
#     elif sign == "-":
#         result = x + y
#     elif sign == "*":
#         result = x * y
#     else:
#         result = x / y
#     return result



# result_1 = calculator(x, y, sign)

# print(result_1)

# from typing import Tuple

# def add_two_numbers(a: int, b: int)-> Tuple[int, int, float, int]:
#     return a+b, a-b, a/b, a*b 

# first_integer = int(input("Add first integer: "))
# secound_integer = int(input("Enter secound integer: "))

# sum, sub, div, mult = add_two_numbers(first_integer, secound_integer)
# print(f" Suma = {sum}, atimtis = {sub} , dalyba = {div}, daugyba = {mult}")




#Create a function that adds a string ending to each member in a list.

# from typing import List

# user_string = input("Enter your string: ")

# str_list = ["Myliu", "Myliu", "Myliu", "Myliu", "Myliu"]
# def add_str(my_list: List[str], my_string: str) -> List[str]:
#     str_added = []
#     for items in my_list:
#         str_added.append(items + my_string)
#     return   str_added 


# a = add_str(str_list,  user_string)
# print(a)


#Create a function that returns only strings with unique characters.

# from typing import List

# strings_list = ["Tomas", "Tadas", "Vytautas", "medis", "Meras", "ananasas"]

# def unique_values(str_list: List[str]) -> List[str]:
#     new_str_LIST = []
#     for value in str_list:
#         if len(set(value)) == len(value):
#             new_str_LIST.append(value)
#     return new_str_LIST

# unique = unique_values(strings_list)

# print(unique)
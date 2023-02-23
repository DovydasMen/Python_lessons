# Create at least 5 different functions and try to handle at least 5 built-in Python Exceptions.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def append_int_to_set_value(i: int)-> None:
#     i= 1
#     i.append(2)
# #int objektas neturi galimybes prie jo kazka prid4eti

# try:
#     append_int_to_set_value(2)
# except AttributeError:
#     print("You can't add number here")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# from typing import Optional, Union

# def div_two_integers(number1: Union[float, int], number2: Union[float, int]) -> float:
#     div = number1/number2
#     return div


# try:
#     div_two_integers(number1 = 2, number2 = 0)
# except ZeroDivisionError:
#     print(f" Why do you want to divide from zero?")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# employer_dict = {"Name": "Dovydas", "ID": 256}

# try:
#     employer_id = employer_dict["ID"]
#     print(employer_id)

#     emp_role = employer_dict["Role"]
#     print(emp_role)
# except KeyError as e:
#      print(f"Key Not Found in Employee Dictionary: {e}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 4 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# from typing import Union


# def division_of_two_digits(number_one: Union[int,float], number_two: Union[int, float])-> float:
#     assert number_two!=0,"Cannot divide by 0"
#     return number_one / number_two

# try:
#     print(division_of_two_digits(number_one = 5.3, number_two = 0))

# except AssertionError:
#     print("Division from 0 is not possible")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ task 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Program to check if a number is prime or not
# from typing import Union
# def prime_number_or_not(num: Union[int, float]) -> bool:
#     flag = False
#     if num == 1:
#      print(num, "is not a prime number")
#     elif num > 1:
#     # check for factors
#      for i in range(2, num):
#         if num % i == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

#     # check if flag is True
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")


# try:
#     prime_number_or_not(9)
# except ValueError:
#    print(f" Please insert str or float value")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ task 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# """Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication. Handle all possible errors that may occur."""
# from typing import Union


# def calculator_with_user_input(input_number_one: Union[int, float], input_number_two: Union[int, float]) -> dict[str, Union[int, float]]:
#     sum = input_number_one + input_number_two
#     substract = input_number_one - input_number_two
#     division = input_number_one / input_number_two
#     multiplication = input_number_one * input_number_two
#     calc_result = {"Sum of two numbers": sum, "Substraction of two numbers": substract,
#                    "Division of two numbers": division, "Multiplication of two numbers": multiplication}
#     return calc_result


# def beaty_print_dict(calc_result: dict[str, Union[int, float]]) -> None:
#     for key, value in calc_result.items():
#         print(f"{key} : {value}")


# try:
#     input_number_one = float(input("Please nominate number: "))
#     input_number_two = float(input("Please nomine secound number: "))
#     result = calculator_with_user_input(input_number_one, input_number_two)
#     print(beaty_print_dict(result))
# except ZeroDivisionError:
#     print("Never divine by zero")
# except ValueError:
#     print("You didin't entered value")

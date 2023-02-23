# a = 5
# b = 2


# def addition(number1, number2):
#     sum = number1 + number2
#     return sum


# c = addition(a, b)  # gali b8ti ir ne kintamieji, o bet kokie skaiciai.

# print(c)


# def print_something():
#     print("Hello world!")  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# print_something


# my_list = [1, 2, 3,]

# my_list.append(4) # grazins none my_list = my_list.append(4)

# print(my_list)

# import random

# def get_random_number():
#     print(random.randint(0, 10))

# # funkcija nieko negrazina

# print(get_random_number())

# def __get_something():
#     print("Hello world")

# __get_something

# def find_sum(num1, num2):
#     """Returns the sum of num1 and num 2"""
#     sum_nums = num1 + num2
#     return sum_nums #po returno galime veiksmus rasyti, jie gris.

# print(find_sum (5, 10))

# def even_ood(num): # tikrina ar skaicius lyginis.
#     if num % 2 == 0:
#         return "even"
#     else:
#             return "odd"
   

# print(even_ood(7))

# def find_sum(num1, num2=50): # 50 bus kaip default, jeigu antro skaiciau nenurodys.
#     sum_nums = num1 + num2
#     return sum_nums

# print(find_sum(5, 11))

# def find_substractiion(num1,num2  = 50, print_result = False): # default reiksmes negalime deti i prieki, tik gale.
#     sub_nums = num1 - num2
#     if print_result:
#         print(sub_nums)
#     return sub_nums

# print(find_substractiion(5, 10, True)) # jeigu ant
# ro skaiciau nepaduosime, reiktu rasyti visa funkcija print_result=True

# def aadd_two_int_numbers(a : int, b : int) -> int:
#     return a + b

# number1 = aadd_two_int_numbers(5.5, 50)
# print(number1)

# type_annotation_int: int = 43
# type_annotation_float: float = 2.75
# type_annotation_string: str = "cold"
# type_annotation_bool:  bool = True

# import random

# from typing import List, Tuple, Union, Dict, Optional
# Dicttype_annotation_tuple: Tuple[str] = ("1", "2", "3")
# type_annotation_list: List[str] = ["a", "b", "c"]
# type_annotation_dict: Dict[str, int] = { "a": 1 , "b" : 2}


# def get_random_object()-> Union[int, str, List[str]]:
#     number = random.randint(0, 3)
#     if number == 0:
#         return 0
#     elif number == 1:
#         return "str"
#     else:
#         return ["1", "2", "3"] 

# def another_funcios(number: int)-> Optional[int]:
#     if number > 10:
#         return number

# number1: int = another_funcios(1)
# print(number1)


# from typing import Tuple, Optional, Union, List



# def the_func(x: Union[int, float], y: List[str], z: Optional[float] = None) -> str: #optional gali paduopti ir nepaduoti.
#     return "You called the_func with " + str(x) + str(y) + str(z)

# print(the_func(2, ["1", "2"]))
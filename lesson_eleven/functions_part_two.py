from typing import Any

# def check_arguments(mandatory, *args, **kwargs) -> None:
#     print(mandatory)
#     if args:
#         for argument in args:
#             print(args)
#     if kwargs:
#         print(kwargs)

# check_arguments(2, 3, 4,"something", name= "Dovydas", something = "1,2,3") #Kwargs - key words arguments.


# def check_argument(number1: int, number2: int, *args, default_settings=True, **kwargs) -> None:
#     print(number1 + number2)
#     if default_settings:
#             print(number1 + number2)
#     if args:
#         for argument in args:
#             print(argument)
#     if kwargs:
#         print(kwargs)

# a = 5

# check_argument(101, 102, "something", "something", default_settings=False)


# def multiply(x: int, y: int)-> int
#     return x * y

# print(multiply(2, 3))

# multiplication = lambda x,y: x * y
# print(multiplication(2,3))


# from typing import Callable # callable ka=koks dalykas, kur5 gali iskviesti.

# def get_sum(number1: int, number2: int)-> int:
#     return number1 + number2

# def get_something_else() -> str:
#     return "something else"



# def get_function(number: int) -> Callable:
#     if number > 1:
#         return get_sum
#     else:
#         return get_something_else
    
# print(get_function(2)(1, 2))

# suma = get_sum

# print(suma(5,5))

# from typing import Callable

# def my_func(n: int) -> Callable:
#     return lambda a: a * n

# my_doubler = my_func(2)
# print(my_doubler(11))

# multiplication = (lambda x, y: x * y)(2, 3)
# print(multiplication)

# from itertools import repeat

# number_list1 =  [1, 2 , 3, 4, 5]
# number_list2 = [0, -1, -2, -3, -4]


# def list_calculator(firs_list : list, secound_list: list) -> bool:
#     final_list = []
#     for element in range(len(firs_list)):
#         final_list.append(firs_list[element] + secound_list[element])
#     return all_elements_in_list_equal(final_list)
    



# def all_elements_in_list_equal(lst: list)-> bool:
#     if len(set(lst)) == 1:
#         return True
#     return False
    
# compared_list = list_calculator(number_list1, number_list2)

# print(compared_list)

#same excercise
from typing import List

item_list_1 = [5, 8, 5, 0, -1, 7]
item_list_2 = [0, -7, -4, 1, 2, -6]

def add_puzzle(item1: list[int], item2: List[int]) -> bool:
    c = []
    for x,y in zip(item1, item2):
        c.append(x + y)
    if len(set(c)) == 1:
        return  True
    return False

print(add_puzzle(item_list_1, item_list_2))






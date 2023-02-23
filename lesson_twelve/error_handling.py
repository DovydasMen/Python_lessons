""" 
Create a function that takes one parameter as number - age , other as name which is default 'Anatnas', and some args and keywords.
Print first Name with age;
And then print all arguments with key arguments.
"""

# def print_name_age_with_arguments(age:int, name:str = "Antanas", *args, **kwargs) -> None:
#     print(f"Your name is {name} and you are {age}")
#     print(f"Free arguments are: {args if args else 'There are no arguments'} and free key arguments {kwargs if kwargs else 'There are no key arguments'}")


# print_name_age_with_arguments(25, "Tom", 12 , "arguments", street = "Royal Avenue")
from typing import Optional, Union

# def divider(number: Union[float, int]) -> None:
#     return number/2 if isinstance(number, float) else number // 2 

# # try:
# #     my_divided_number = divider("as")
# #     print(my_divided_number)
# #     print(my_divided_number / 0)
# #     # print("Hello world") syntax error


# # except TypeError:
# #     print("We are f-*cked up !")
# # except ZeroDivisionError:
# #     print("Never delete with 0")

# try:
#     my_magic_number = 2
#     my_divided_number = divider(number = 20)
#     print(my_divided_number)
#     print(my_divided_number / my_magic_number)
# except ZeroDivisionError:
#     print("My specific message for that exception")
    
# except Exception as e: # kai nezinome ko tiketis.
#     print(f" Error : {e}")
#     # x I am going to do that
# else:
#     print("Success")
# finally:
#   print("\n I don't care: I am printred annyways")

"""
my_divided_number = divider("0")
print(my_divided_number)
Jeigu nebus Try: ir Except: tada tiesiog gausime klaida.
"""



# def physics_is_fun(temp_c: float, pressure_mba: float, time_utc: int, weight_kg: float)-> None:
#     pass

# physics_is_fun(temp_c= 55.48, pressure_mba= 26.84, time_utc= 125487, weight_kg = 458.3)


def divider(number: Union[float, int]) -> Optional(Union[float, int]):
    try:
        return number/2 if isinstance(number, float) else number // 2 
    except TypeError:
        print("Wrong type recieved")
    except Exception as e:
        print(f"Error : {e}")




# i = 0
# while i <= 10:
#     print(i)
#     i = i + 1

# print(10 == 55)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ LIST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# my_list = [1, 1, 2 ,3 ,4 ,5]
# print(my_list.count(1))
# my_list.insert(3, 177)
# print(my_list)
# my_list.remove(1)
# print(my_list)
# my_list.remove(177)
# print(my_list)
# my_list.remove(my_list[-2])
# print(my_list)

# print(len(my_list))
# print(max(my_list))
# print(min(my_list))

# my_list = [1, 2, 32, 4]
# my_list[2] = 1555
# for item in my_list:
#     print(item + 5)

# my_list = ["first", "secound", "third"]
# print(my_list[-1])
# print(my_list[:2])
# print(my_list[::2])
# print(my_list[::-1])

# print("first" in my_list) #bool gryzta true
# print("fourth" in my_list)# bool gryzta false

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TUPLE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# empty_tuple = ( )
# tuple_single_item = (1, )
# another_tuple = (1, 2, 3, )

# Note 
"""
another_tuple[0] = 500
Tuple is no modifyable !!!
"""

# my_list= [1, 5, 10 , 30]
# # print(sum(my_list))
# # print(my_list[0] * my_list[1] * my_list[2] * my_list[3])
# # print(max(my_list))
# # print(min(my_list))
# # print(len(my_list))

# # for item in my_list:
# #     print(item)
# #     print(item + 12)
# # my_list[2] = 5
# # print(my_list)
# print(my_list[-1])
# print(my_list[:2]) 
# print(my_list[::2])
# print(my_list[::-1])
# print(my_list[0:2])

my_list_two = [1, 2, 3]

print(1 in my_list_two) #boool, parodo ar toks elementas yra
#.....





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TASK 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Write a python program that sums up all items in the list (all items are integers or floats in list, create a list yourself)


"""

random_numbers_list = [1.1, 2, 44, 7, 8]
sum_of_list = sum(random_numbers_list)
print(sum_of_list)

multiplication_of_list = random_numbers_list[0] * random_numbers_list[1] * random_numbers_list[2] * random_numbers_list[3] * random_numbers_list[4]
print(multiplication_of_list)
print(max(random_numbers_list))


list_full_of_strings = ["Dukra", "Kita dukra", "Vyras", "Moteris", "Visi faini"]
one_str_of_list = ''.join(list_full_of_strings)
new_line_of_strings ='\n'.join(list_full_of_strings)
print(one_str_of_list)
print(new_line_of_strings)

one_list = [1, 2.2, 3]
two_list = [2, 4.4, 6]
three_list = one_list + two_list

print(three_list)
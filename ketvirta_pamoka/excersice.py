# Create a list of different types of python objects, and print all the types. The one who gets the the most unique types wins respect points:
# print all the items separated with "|"
# create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.
# Create a list with student names and sort them, print the result to the terminal.
# write a program that allows user to write in any float number and then round it.

# task 1
# my_list = ['a', 1, 1.2, 'Dovydas', True]

# for item in my_list:
#     print(type(item))

# print(type(my_list))

#task 2

# my_list2 = ['a', 1, 1.2, 'Dovydas', True]

# print(*my_list2, sep= '/')

#work around to get to the list

# my_list_three = ['alibaba', 2, 'Antanas']

# a, b, c = my_list_three

# print(a, b, c)

# for item in my_list2:
#     print(item, sep='|')



#3 task
# create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.
# float_list = [1.556, 2.3331, 4.1171]
# float_list2 = []

# for number in float_list:
#     number = round(number, 2)
#     float_list2.append(number)
#     print(float_list2)  

# print(float_list2)

#4 task 

#Create a list with student names and sort them, print the result to the terminal.
# student_list = ['Dijora', 'Dane', 'Neringa', 'Dovydas', 'Agne', 'Jurate']

# print(sorted(student_list))


#write a program that allows user to write in any float number with decimal in on entry and then round it and print them.

# float_number, decimals = input("enter a float and decimal points: ").split(",")
# print(round(float(float_number), int(decimals)))


# Create a program which would take 5 separate sentences containing 5 words.
# Make those sentences in separate lists and sort them out (reverse=False)
# Create 5 five new lists what would contain first, second  indexed elements from those lists. (first list containing
# all first elements of those five, second list second elements and so on).
# print the length of all list items and print the longest lenght list and shortest.

sentence_one = input("Write sentence with five words :") .split ()
# sentence_two = input("Write secound sentence with five words :") .split ()
# sentence_three = input("Write third sentence with five words :") .split ()
# sentence_four = input("Write third sentence with five words :") .split ()
# sentence_five = input("Write third sentence with five words :") .split ()

first_list = [sentence_one]
print(type(first_list))
print(sorted(first_list).reverse=False )
# print(sentence_two)
# print(sentence_three)
# print(sentence_four)
# print(sentence_five)

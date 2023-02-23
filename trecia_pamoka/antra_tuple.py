#Write a python program that multiplies all items in the list (all items are integers or floats in list, create a list yourself)
my_tuple = (3, 7, 5, 8, 9, 11, 20, 25)

x = 1

for number in my_tuple:
    x = number * x
    print(x)

print(x)
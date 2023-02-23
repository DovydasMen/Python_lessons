# Write a python program that sums up all items in the list (all items are integers or floats in list, create a list yourself)

my_list = [3, 7, 5, 8, 9, 11, 20, 25]
x= 0
for number in my_list:
    x = number + x
    print(x)

print(sum(my_list))
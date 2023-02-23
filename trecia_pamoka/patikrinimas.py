my_list=[1, 2, 3, 4,-15, 5, 6, 7, 8, 9, 1, 2, 3, 7, 1, 1,666, "Albert", print]


print(666 in my_list)
# atspausdins  true arba folse, jeigu skaicius egzisuotja liste. (loggika arba elemntas yra arba ne sarase)
print(20 in my_list)
print("Albert" in my_list)
#tikrina ir stringus
print(print in my_list)
#tikrina ir funkcijas
my_list[-1]("Hello World")
print(my_list.index(print))
#randa elemento vieta, siuo atveju nurodo funkcijos print vieta liste.
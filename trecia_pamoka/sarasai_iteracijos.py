my_list=[1, 2, 3, 4,-15, 5, 6, 7, 8, 9, 1, 2, 3, 7, 1, 1,666]

for number in my_list:
    print(number +1)
    
#atlieka veiksmus po viena elementa. 6iuoo atveju, paima is saraso 1 ir prideda 1 bei atprintina, tada ima kita elementa ir prideda viena bei ji atprintina ir t.t

print("loop is done")
my_list[-1]= 777
print(my_list)
#pakeičia paskutinį skaičiu į 777

my_list[-1] = my_list[-1] + 50
# prides prie paskutinio skaiciau 50
print(my_list)

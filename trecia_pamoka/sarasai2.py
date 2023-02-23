my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 7, 1, 1]
# I sarasa suvedame duomenis
print(my_list)
#suskaičuoja vienetukus sarase  !!! print(my_list.count (1))
my_list.append(500)
#Ideda i sarasa 500 skaiciu, jis idedamas i gala.
print(my_list)
my_list.insert(0,600)
#ides i pirma vieta 600
print(my_list)
#ides i 3 vieta 700
my_list.insert(3,700)
print(my_list)

my_list.remove(600)
#panaikinsime 600 is listo
my_list.remove(1)
my_list.remove(1)
my_list.remove(1)
#isima toki kieki 1 skaiciu kiek kartu nurodome. negalime kartu chainin my_list.remove(1).remove(1).remove(1).remove(1) ir t.t
print(my_list)


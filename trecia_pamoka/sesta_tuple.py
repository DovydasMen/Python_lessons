#Write a python program that asks user to enter 3 integers and find the highest value entered.
number1 = int(input("Nurodykite pirma skaiciu: "))
number2 = int(input("Nurodykite antrą skaičių: "))
number3 = int(input("Nurodykite trecia skaiciu: "))

my_tuple = (number1, number2, number3)
print(("Didžiausia reikšmė-"), max(my_tuple))
# Kableliu atskiriu dvi skirtingas reiksmes, kurias noriu, kad atspausdintu.
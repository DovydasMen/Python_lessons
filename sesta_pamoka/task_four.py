#Write a small calculator application, that allows user to enter two numbers and a symbol, given and then do the operation and print an answer.
# numb1 = int(input("Enter first number which you want to: "))
# numb2 = int(input("Enter secound number which you want to: "))
# math = input("Enter math symbol what you want to do: ")

# if math == "+":
#     x = numb1 + numb2
# elif math == "-":
#     x = numb1 + numb2
# elif math == "*":
#     x = numb1 * numb2
# elif math == "/":
#     x = numb1 / numb2
# elif math == "**":
#     x= numb1 ** numb2
# elif math == "//":
#     x= numb1 // numb2
#print(f"Your result : {x}")
number_one, operation, number_two = input("Enter condition:"). split()
number_a = int(number_one)
Number_b = int (number_two)
c = operation

if c == "+":
     x = number_a + Number_b
     print(f"Your result : {x}")
elif c == "-":
     x = number_a - Number_b
     print(f"Your result : {x}")
elif c == "*":
     x = number_a * Number_b
     print(f"Your result : {x}")
elif c == "/":
     x = number_a / Number_b
     print(f"Your result : {x}")
else:
    print("Don't expect me no more!")

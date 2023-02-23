#allow user to enter two numbers, print out which one is higher than the other, or are they equal?
numb1 = int(input("Enter your first number: "))
numb2 = int(input("Enter your secound number: "))

if numb1 > numb2 :
    print(f" Number {numb1} is higher than {numb2}")
elif numb1 < numb2 :
    print(f" Number {numb2} is higher than {numb1}")
else:
    print(f"Numbers {numb1} and {numb2} are equal")
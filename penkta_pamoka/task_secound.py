# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x):
# You can use input to receive the number. Example:
# n= 5 , output:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

entered_number = int(input("Please enter input to exponent: "))
generated_dictionary ={}
for items in range(1, entered_number+1) :
    generated_dictionary[items] = items * items

print(generated_dictionary)
#Write python program that asks user to enter name, surname, age. Put these values into a dictionary and print dictionary

name_input = str(input(" Please enter your name: "))
surname_input = str(input("Please enter your surname: "))
age_input = str(input("Please enter your age: "))

person_dictionary = {}
Updated_name = { "Name" : name_input}
person_dictionary.update(Updated_name)

updated_surname = {"Surname" : surname_input}
person_dictionary.update(updated_surname)

updated_age = {"Age" : age_input}
person_dictionary.update(updated_age)

print(person_dictionary)
# print(f"{name_input} {surname_input} yra tokio amziaus : {age_input}")
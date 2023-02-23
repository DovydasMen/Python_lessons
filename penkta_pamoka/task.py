# We have 3 dictionaries :  dic_one={1:10, 2:20} dic_two={3:30, 4:40} dic_three={5:50,6:60}
# Create one final dictionary from all those 3.

dictionary_one = {1: 10,
                  2: 20, }
dictionary_two = {3: 30,
                  4: 40, }
dictionary_three = {5: 50,
                    6: 60, }

dictionary_one.update(dictionary_two)
dictionary_one.update(dictionary_three)

print(dictionary_one)

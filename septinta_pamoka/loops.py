# i = 0

# while i < 10:
#     print(i)
#     i += 1

# import time #sustabdo executiona.

# while True:
#     print("Zalgiris")
#     time.sleep(1)


# apples = 0 
# while apples <= 10:
#     print(f"gathered apples so far {apples}") 
#     apples += 1  # prie sumos prideda vienetuka apples = apples + 1
# import Sys

# names = ["Dovydas" , "Dane", "Neringa", "DIjora"]
# print("Coonsumtion", sys.getsizeof(names))

# for name in names:
#     print(F"Greetings, {name}")
#     print(type(name))

# for letter in "Dovydas":
#     print(letter)

# my_dic={
#         "first_items" : 1,
#         "last_item" : 2,
#     }

# for key, item in my_dic.items()
#     if my_dic[key] == "",
        
# print (key, item)





# my_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # for number in my_number_list:
# #     print(number)

# for x in range(0, 10, 2): # trecias elementas nurodo zingsni, pagal kuri eina
#     print(x)
    

# for _ in range(0, 10, 2):
#     # doing something else
#     print
# ("Something else")


# import time


# secounds = 1
# while True:
#     print("Zalgiris")
#     time.sleep(0.5)
#     secounds += 1
#     if secounds == 3:
#         break

# my_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in my_number_list:
#     print(number)
#     if number >= 9:
#         break
    
# for _ in range(0, 5):
#     for number in my_number_list:  # break bus da=nai naudojamas.
#         print(number)
#         if number >= 9:
#             break


    
# my_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in my_number_list:
#     if number == 7:
#         continue # loopuose naudojamas daznai, kai iki 7 daejo, po continou, nieko neatliko, kai iskilo 8 vygde toliau cikla. Gri=kite i ciklo pradzia.
#     print(number)

i = 0 
while i < 6:
    i += 1 # i= i + 1
    print("Hey hoo")
    if i == 3:
        print("I am here")
        continue
    print(i)
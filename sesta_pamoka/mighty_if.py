# print (11>10) #atspasdins ar ture ar ne, pagall matematikos logiką.
# number = int(input("Enter your name:" ))


# if number >= 18 : #!= nelygu, > daugiau, < maziau,  >= daugiau arba lygu, <= naziau arba lygu.

#     print("You allow to enter")
# elif number == 5 :
#     print ("You entered 5! ")
# elif number < 5:
#     print(" Winner, your number is less than 5")
# else: #Jeigu neatitinka jokios salygos, ra6ome else ir nurodome.
#     print (f" you have entered {number}")
# #print("finishing program")

# fruit =  str(input("Name a fruit, we would check it if we can offer it to you: "))

# if fruit in ["orange", "pear","apple"]:
#     print(" Yes, it is in a list!")
# else:
#     print ("Sorry, it's not in a list")

# trumpesni if'ai

#

# The and keyword is a logical operator, and is used to combine conditional statements: Basically both conditions must be true for statement to return True:

# a = 200
# b = 400
# c = 500

# if c > a and c > b:

#     print("C is the greastest oof them all")

# The or keyword is a logical operator, and is used to combine conditional statements: Basically atleast one of the conditions must be true for statement to return True:

# a = 200
# b = 400
# c = 500
# if b > a or b > c:
#     print("B is at least greater than one of the values !")

#     x = 15
#     if x > 10:
#         print("Above ten,")
#         if x > 20:
#             print(" and also above 20!")
#         else:
#             print("but noot above 20")

# a = 50
# b = 80

# if b > a:
#     pass


# name = "Tom"

# if name == "Tom":
#     print(" Nice to see you Tom")
# else:
#     print("Welcome usser")


# user = "Johnny"
# privileg_users = ["Tom", "Albert", "Stepehen"]
# if user == privileg_users :
#     print(f"Welcome home {user}")
# else:
#     print("intruder , calling police")


# my_dict = {"name" : "Stephen", "Born" : "1995-10-28", "interests" : "apples"}
# if my_dict["name"] == "Stephen":
#     print ("This guuy does not like Windows")
# else:
#     print(" No clue who this is")

# name = "Dovydas"
# if not name:
#     print("Name was not entered")
# else:
#     print("Name was entered")


# my_list = [221]
# if my_list:
#    print(f"Items exist in list. It is {my_list}")
# else:
#    print("list is empty")

my_dict = {"name" : "Bill", "Born" : "1995-10-28", "interests" : "apples"}
if "Bill" in my_dict.values():
 print ("This guy hates apples")
else:
 print(" No clue who this is")
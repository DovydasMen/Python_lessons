# squares = []

# for number in range(400):
#     squares.append(number * number)

# print(squares)

# squares = [number * number for number in range(10) if number == 5]
# print(squares)

# def add_smth(nr : int):
#     return nr ** nr


# We have 5 names list, print all names which have les then 5 letters

# list_names = ["Dovydas", "Neringa", "Dane", "Dijora", "Vilkas"]
# names=[]
# for name in list_names:
#     if len(name) >= 5:
#         names.append(name)

# print(f" Names_list_one : {names} ")

# print([])  REIKIA PASIBAIGTI


# my_dick = {"i" : 1,
#            "Delta" : 2,
# }
# squares = {i : i * i for i in range(10) if i <= 6}
# print(squares)


# Create dictionary with 5 key:value pairs, Keys must be strings, value must be int doublke digits)
# Use dictionary comprahension to create a new dictionary where keys are the same as your current, but letter cappitals, and values are in revers order.
# team_score = {
#     "Zalgiris" : 81,
#     "Rytas" : 31,
#     "Prienai" : 74,
#     "Klaipėda" : 12,
#     "Mantinga" : 47,
# }
# new_dic = {}

# new_dic = {team.upper() : int(str(number)[::-1]) for (team, number) in team_score.items()}
# print(new_dic)


# for name, number in team_score.items():
#     new_dic[name.upper()] = int(str(number)[::-1])
# print(new_dic)

# enumerate

# values = ["a", "b", "c"]
# # Seth duomenu strukt8roje jis neveikia.
# for index, value in enumerate(values):
#     print(index, value)

list_names = ["Dovydas", "Neringa", "Dane", "Dijora", "Vilkas"]
list_new_names = {place : names for (place, names) in enumerate(list_names)} 

#jeigu su for ciklu, reikia dictionary susikurti tuscia.
# for place, names in enumerate(list_names):
#     list_new_names [place] = names

print(list_new_names)

#asfdasfdasd


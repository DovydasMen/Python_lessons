countries_and_capitals = {
    "Lithuania" : "Vilnius",
    "Poland" : "Warsaw",
    "Latvia" : "Ryga",
    "Estonia" : "Talinn",
    "Denmark" : {
             "capital" : "Kopenhaven",
             "population" : 2500000,
             "rich" : "poor",
    }
}

# print(countries_and_capitals["Denmark"])
# print(countries_and_capitals["Denmark"]["capital"])
# print(countries_and_capitals["Denmark"]["population"])
# # pra6ome isprinti, nurodome entry point, tada specifikuojame pirmajame lauztiniame skliauste, kury kay imame ir tada antruose skliaustuose renkiesi kokia info paleisti.
# print(countries_and_capitals.get("Denmark").get('population'))
# #su get opcija

# #print(list(countries_and_capitals.items()))
# #built in metodas, kuris dictionary isprintina  i lista.

# print(list(countries_and_capitals["Denmark"].keys()))

# print(list(countries_and_capitals.values()))

print(countries_and_capitals)
# countries_and_capitals.pop("Latvia") #ismeta key ir value .pop funkcija.
# print(countries_and_capitals)
new_country = {"Spain" : "Madrid"} 
countries_and_capitals.update(new_country) #pridedame nauja dictionary prie esamo.
print(countries_and_capitals)



















#keys nekeiciami

students = {
    "name" : "Antanas",
    "age" : 20,

}
print(students)

students["Surname"] = "Virgius"

print(students)

# student[[1, 2, 3,]] = "Vilnius" Negalima keisti key, bei turi b8ti stringas arba integeris.
print(students["age"])

del students["name"]
print(students)

print(students.get("age"))
# print(students.get("ag", "bet koks reiksme")), jeigu get pirmoje reiksmeje neranda tokio dalytko, tai vietoje none, grazins bet koks reiksme.
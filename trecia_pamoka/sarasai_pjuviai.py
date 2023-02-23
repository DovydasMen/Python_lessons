my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 7, 1, 1]

print(my_list[-1])
# is saraso paimsime ir atspausdinsime skaiciu pabaigoje
print(my_list[::2])
# is saraso paimsime ir atspausdinsime kas antra skaiciu.
my_list2=["Danielius", "Toomas", "Jonas", [1, 2, 3, ["find_me"]]]
print(my_list2[2])
#is saraso printins 2 daikta
print(my_list2[0][-4])
# atspausdins  danieliaus vardo viena lraide. print(my_list2[0][-4][1]) tokiu variantu gaunasi, kad neturime logikos, kadangi situo atveju is danieliau isimame l raide ir ten liek vienas slotas0 su l.
print(my_list2[-1][-1][0])
#my_list2=["Danielius", "Toomas", "Jonas", [1, 2, 3, ["find_me"]]]
# po pirmo -1, bus [1, 2, 3, ["find_me"]], tada dar vienas -1 lieka ["find_me"], tada pirma reiksme 0, nes ten pirmas oobjektas likes t.y sarasas "find_me"

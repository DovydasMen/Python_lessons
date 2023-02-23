#Create program that allows user to enter text
#Convert that text to Leet speak 1337
#print outcome

text = input("Įveskite tekstą, kurį perrašysime į Leet speek: ")
leet_speak = text.replace("A","∆").replace("a","∆").replace("B","|3").replace("b","|3").replace("C","©").replace("c","©").replace("D","|]").replace("d","|]").replace("E","£").replace("e","£").replace("F","ƒ").replace("f","ƒ").replace("G","6").replace("g","6").replace("H","#").replace("h","#").replace("I","!").replace("i","!").replace("J","√").replace("j","√").replace("K","|<").replace("k","|<").replace("L","|_").replace("l","|_").replace("M","м").replace("m","м").replace("N","п").replace("n","п").replace("O","Ø").replace("o","Ø").replace("P","|o").replace("p","|o").replace("Q","9").replace("q","9").replace("R","Я").replace("r","Я").replace("S","5").replace("s","5").replace("T","т").replace("t","т").replace("U","{_}").replace("u","{_}").replace("V","\/").replace("v","\/").replace("W","VV").replace("w","VV").replace("X","×").replace("x","×").replace("Y","\|/").replace("y","\|/").replace("Z","7_").replace("z","7_")
print(leet_speak)
from random import randint, choice

List1 = ["Nikita", "Timur", "Dima"]
Iq1 = randint(65,180)
Iq2 = randint(65,180)
Iq3 = randint(65,180)
List2 = [Iq1, Iq2, Iq3]

random1 = choice(List1)
random2 = choice(List2)
output1 = [random1, random2]
List1.remove(random1)

random3 = choice(List1)
random4 = choice(List2)
output2 = [random3, random4]
List1.remove(random3)

random5 = choice(List1)
random6 = choice(List2)
output3 = [random5, random6]






output4 = (output1, output2, output3)
print(output4)







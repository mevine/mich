####using built in modules######################
import random
######import choice as pick, randint as magic_number_chooser##
print(random .choice(["apple","orange","banana","grape"]))
print(random.randint(1,100))
print(random .shuffle(["apple","orange","banana","grape"]))


###########importing parts of a module##########
from random import choice,randint

print(choice(["apple","orange","banana","grape"]))
print(randint(1,100))
##or ussing shuffle
import random
fruit=["apple","orange","banana","grape"]
random.shuffle(fruit,random.random)
print(fruit)
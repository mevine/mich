#fuctions//#
def sing_happy_birthday():
    print("happy birthday to you")
    print("happy birthday to you")
    print("happy birthday dear mevine")
    print("happy birthday to you")

sing_happy_birthday()
#********************************************************#

#def square_of_8():
    #return 8**2
#result = square_of_8()
#print(result)
#*****************************************************#
from random import random
def flip_coin():
    #generate random no fro 0 to 1
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return"tales"
print (flip_coin())


def flip_coin():
    #generate random no fro 0 to 1
 
    if  random() > 0.5:
        return "HEAds"
    else:
        return"Tales"
print (flip_coin())
#*******************#
def square (num):
    return num*num
print (square(4))
print (square(6))

#******************************************#
#using exponentials
def exponent(num,power):
    """exponent raises a nomber to its power"""
    return num**power
print (exponent(2,3)) 
print(exponent(3,2))
print(exponent.__doc__) 

#****************************************************#
#**********************************************#
#documenting functions,we use """"  """" 
def say_hello ():
    """a simple function that returns a string hello""" 
    return"hello"  
print(say_hello.__doc__)



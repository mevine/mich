#rock papper scissor projo
print("Rock...")
print("Paper...")
print("Scissors...")
player1 = input("player1,make your move: ")
player2 = input("player2 ,make your move: ")
if player1 =="rock" and player2 =="scissors":
    print("player1 wins!")
elif player1 =="rock" and player2 =="papper":
    print("player2 wins!")
elif player1 =="papper" and player2 == "rock":
    print("player1 wins!")
elif player1 == "papper" and player2 == "scissors":
    print("player2 wins!") 
elif player1 =="scissors"  and player2 == "rock":
    print("player2 wins!")
elif player1 =="scissors" and player2 == "papper":
    print("player1 wins!")
elif player1 == player2:
    print("its a tie") 
else:
    print("something went wrong")  


#or 
print("Rock...")
print("Paper...")
print("Scissors...")
player1 = input("player1,make your move: ")
player2 = input("player2 ,make your move: ")
if player1 == player2:
    print("its a tie")
elif player1 == "rock":
    if player2 == "scissors":
       print("player1 wins")
    elif player2 =="papper" :
       print("player2 wins!") 
elif player1 == "papper":
    if player2 == "rock": 
       print("player1 wins!") 
    elif player2 == "scissors":
       print("player2 wins") 
elif player1 =="scissors":
    if player2 == "papper":
       print("player1 wins!")
    elif player2 == "rock":
       print("player2 wins")
 
else:
    print("something went wrong")            

#game with comp
import random
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "papper" 
else:
    computer = "scissors"  
print("computer")        


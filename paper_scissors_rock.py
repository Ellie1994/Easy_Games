import random
import time

player_1 = input("The first player enters a number of tosses: ")
player_2 = input("The second player enters a number of tosses: ")

tosses = ["toss..","toss..","toss.."]
for t in tosses:
    print(t)
    time.sleep(1)
    
variants = ["scissors", "paper", "rock"]    

player_1 = random.choice(variants)
player_2 = random.choice(variants)

print(player_1, " 'the first player'")
print(player_2, " 'the second player'")

if player_1 == "scissors" and player_2 == "paper":
    print("The scissors cut the paper! The first player won!")

elif player_1 == "paper" and player_2 == "scissors":
    print("The scissors cut the paper! The second player won!")
    
elif player_1 == "rock" and player_2 == "paper":
    print("The paper wraps up the rock! The second player won!")
    
elif player_1 == "paper" and player_2 == "rock":
    print("The paper wraps up the rock! The first player won!")

elif player_1 == "rock" and player_2 == "scissors":
    print("The rock smashes the scissors! The first player won!")
    
elif player_1 == "scissors" and player_2 == "rock":
    print("The rock smashes the scissors! The second player won!")
    
else:
   print("DRAW! :D")


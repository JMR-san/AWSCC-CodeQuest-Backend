import random

player_1 = input("Enter your move: ").lower()

moves = ["rock", "paper", "scissors"]
opponent = random.choice(moves)

print (f"Your move is {player_1} and computer's move is {opponent}!")
if player_1 == "rock" and moves == "rock":
    print("It's tie. Try again.")
elif player_1 == "paper" and opponent == "paper":
    print("It's tie. Try again.")
elif player_1 == "scissors" and opponent == "scissors":
    print("It's tie. Try again.")

elif player_1 == "rock" and opponent == "scissors":
    print ("You win!")
elif player_1 == "rock" and opponent == "paper":
    print ("You win!")

elif player_1 == "scissors" and opponent == "rock":
    print ("Computer wins!")
elif player_1 == "scissors" and opponent == "paper":
    print ("You win!")
    
elif player_1 == "paper" and opponent == "rock":
    print ("You wins!")
elif player_1 == "paper" and opponent == "scissors":
    print ("Computer wins!")


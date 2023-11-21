nameplayer_1 = input ("First player, what is your name? ")
nameplayer_2 = input ("Second player, what is your name? ")

player_1 = input (f"{nameplayer_1}, rock, paper or scissors? ")
player_2 = input (f"{nameplayer_2}, rock, paper or scissors? ")


if player_1 == "rock" and player_2 == "rock":
    print("It's tie. Try again.")
elif player_1 == "paper" and player_2 == "paper":
    print("It's tie. Try again.")
elif player_1 == "scissors" and player_2 == "scissors":
    print("It's tie. Try again.")

elif player_1 == "rock" and player_2 == "scissors":
    print (f"{nameplayer_1} wins!")
elif player_1 == "rock" and player_2 == "paper":
    print (f"{nameplayer_2} wins!")

elif player_1 == "scissors" and player_2 == "rock":
    print (f"{nameplayer_2} wins!")
elif player_1 == "scissors" and player_2 == "paper":
    print (f"{nameplayer_1} wins!")
    
elif player_1 == "paper" and player_2 == "rock":
    print (f"{nameplayer_1} wins!")
elif player_1 == "paper" and player_2 == "scissors":
    print (f"{nameplayer_2} wins!")
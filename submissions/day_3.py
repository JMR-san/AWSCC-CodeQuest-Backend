import time

playerName = input("Enter your name: ")
playerGen = input("Are you male or female? ")
dateGen = input("Are you attracted to male or female? ")
heart = "\u2764"
life = 2
affection = 0

#   define the date gender pronoun
if dateGen.capitalize() == "male" or "Male" or "M" or "m": 
    proGen = "him"
    proGen2 = "his"
else: 
    dateGen.capitalize() == "female" or "Female" or "F" or "f"
    proGen = "her"

dateName = input (f"What is {proGen} name? ")

#   Introducing the game
print (f"""Hello, {playerName}! Prom night is coming up, and you're planning to 
invite {dateName} as your date. Make {proGen} say yes!
You need 2/3 affection level before you can ask her as your date.
You have {life} lives:{heart} {heart}
Goodluck!!""")

#   First situation 1/3
approach = input (f"""You saw {dateName} walking on the hallway. 
Do you want to greet {proGen}? \nY / N: """)

if approach ==( 'Y' or 'y'):
    print (f"Good morning, {dateName}! How are you doing? ")
    time.sleep(1.5)
    helloD = input(f"""Good morning, {playerName}!! Have you heard the upcoming prom night?\n Y / N: """)
    if helloD == ('Y' or 'y'):
        ask = input ("Are you coming?\n Y / N: ")
        if ask == ('Y' or 'y'):
            affection += 1
            print (f"*{dateName} smiles* Really?! That's great. Ooops, the class is about to start, see you at the prom!")
            time.sleep(1)
            print (f"{dateName}'s affection increased: {affection}/3")
        else:
            print ("GAME OVER!") #  Ending 1
            exit()
    else:
        ask = input(f"Really?! There will be a prom night next week. You should come!")
        time.sleep(0.5)
        print ("(A) Sure!  \n(B) I'll think about it. \n(C) Sorry, I'm busy.")
        if ask.capitalize() == 'A':
            print (f"Great, can't wait to see you there {playerName}!")
            affection += 1
            print (f"{dateName}'s affection increased: {affection}/3")
        elif ask.capitalize() == 'B':
            print ("Oh, I see. Join if you can, it's fun!")
        elif ask.capitalize() == 'C':
            print (f"Oh, you won't be coming. Okay. *{dateName} leaves without saying good bye*")
            print ("GAME OVER!") #  Ending 2
            exit()

elif approach == ('N' or 'n'):
    print (f"{dateName} noticed you ignore {proGen}!")
    ignore = input("""Do you want to reconcile?\n Y / N: """)
    if ignore == ('Y' or 'y'):
        print (f"Good morning, {dateName}! How are you doing? ")
        time.sleep(1.5)
        helloD = input(f"""Good morning, {playerName}!! Have you heard the upcoming prom night?\n Y / N: """)
        if helloD == ('Y' or 'y'):
            ask = input ("Are you coming?\n Y / N: ")
            if ask == ('Y' or 'y'):
                affection += 1
                print (f"*{dateName} smiles* Reall, that's graet! Ooops, the class is about to start, see you at the prom!")
                time.sleep(1)
                print (f"{dateName} affection increased: {affection}/3")
            else:
                print ("GAME OVER!") #  Ending 3
                exit()
        else:
            ask = input(f"Really?! There will be a prom night next week. You should come!")
            time.sleep(0.5)
            print ("(A) Sure!  \n(B) I'll think about it. \n(C) Sorry, I'm busy.")
            if ask.capitalize() == 'A':
                print (f"Great, can't wait to see you there {playerName}!")
                affection += 1
                print (f"{dateName}'s affection increased: {affection}/3")
            elif ask.capitalize() == 'B':
                print ("Oh, I see. Join if you can, it's fun!")
            elif ask.capitalize() == 'C':
                print (f"Oh, you won't be coming. Okay. *{dateName} leaves without saying good bye*")
                print ("GAME OVER!") #  Ending 4
                exit()
    elif ignore == ('N' or 'n'):
        life -= 1
        print (f"You lost one life, you have remaining {life} lives: {heart} ")
if ask == ('Y' or 'y'): 
    inv = input(f"{dateName} is on {proGen2} way to class. \n Do you want to ask {proGen} as your date? ")
    time.sleep(1.5)



     


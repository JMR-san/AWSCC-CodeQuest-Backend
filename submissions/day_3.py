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
You need affection level 3 before you can ask {proGen} as your date.
You have {life} lives:{heart} {heart}
Goodluck!!""")
time.sleep(1)

#   First situation 1/3
approach = input (f"""You saw {dateName} walking on the hallway. 
Do you want to greet {proGen}? \nY / N: """)

if approach ==( 'Y' or 'y'):
    print (f"Good morning, {dateName}! How are you doing? ")
    time.sleep(1.5)
    helloD = input(f"""Good morning, {playerName}!! Have you heard the upcoming prom night?\nY / N: """)
    if helloD == ('Y' or 'y'):
        ask = input ("Are you coming?\nY / N: ")
        if ask == ('Y' or 'y'):
            affection += 1
            print (f"*{dateName} smiles* Really?! That's great. Ooops, the class is about to start, see you at the prom!")
            time.sleep(1)
            print (f"{dateName}'s affection increased: {affection}")
        else:
            print ("GAME OVER!") #  Ending 1
            exit()
    else:
        print (f"Really?! There will be a prom night next week. You should come!")
        time.sleep(1)
        ask = input ("(A) Sure!  \n(B) I'll think about it. \n(C) Sorry, I'm busy.\nAnswer: ")
        if ask.capitalize() == 'A':
            print (f"Great, can't wait to see you there {playerName}!")
            affection += 1
            print (f"{dateName}'s affection increased: {affection}")
        elif ask.capitalize() == 'B':
            print ("Oh, I see. Join if you can, it's fun!")
        elif ask.capitalize() == 'C':
            print (f"Oh, you won't be coming. Okay. *{dateName} leaves without saying good bye*")
            print ("GAME OVER!") #  Ending 2
            exit()

elif approach == ('N' or 'n'):
    print (f"{dateName} noticed you ignore {proGen}!")
    ignore = input("""Do you want to reconcile?\nY / N: """)
    if ignore == ('Y' or 'y'):
        print (f"Good morning, {dateName}! How are you doing? ")
        time.sleep(1.5)
        helloD = input(f"""Good morning, {playerName}!! Have you heard the upcoming prom night?\nY / N: """)
        if helloD == ('Y' or 'y'):
            ask = input ("Are you coming?\nY / N: ")
            if ask == ('Y' or 'y'):
                affection += 1
                print (f"*{dateName} smiles* Reall, that's graet! Ooops, the class is about to start, see you at the prom!")
                time.sleep(1)
                print (f"{dateName} affection increased: {affection}/3")
            else:
                print ("GAME OVER!") #  Ending 3
                exit()
        elif helloD == ('N' or 'n'):
            print (f"Really?! There will be a prom night next week. You should come!")
            ans = input ("(A) Sure!  \n(B) I'll think about it. \n(C) Sorry, I'm busy.")
            if ans.capitalize() == 'A':
                print (f"Great, can't wait to see you there {playerName}!")
                affection += 1
                print (f"{dateName}'s affection increased: {affection}/3")
            elif ans.capitalize() == 'B':
                print ("Oh, I see. Join if you can, it's fun!")
            elif ans.capitalize() == 'C':
                print (f"Oh, you won't be coming. Okay. *{dateName} leaves without saying good bye*")
                print ("GAME OVER!") #  Ending 4
                exit()
    elif ignore == ('N' or 'n'):
        life -= 1
        print (f"You lost one life, you have remaining {life} lives: {heart} ")
if affection <= 1 :
    inv = input(f"{dateName} is on {proGen2} way to class. \nDo you want to ask {proGen} as your date? \nY / N: ")
    if inv == ('Y' or 'y'):
            print (f"Hey, {dateName}! Do you want to be my date?")
            time.sleep(1)
            print (f"{playerName}, No.")
            life -= 1
            print (f"You lost one life, you have remaining {life} life: {heart} ")
    time.sleep(1.5)

#   Second Situation 2/3
print (f"It is now lunch time. Everyone is going to the cafeteria.\nYou saw {dateName} going same direction as you plan to.")
time.sleep(1)
eatL = input(f"Do you want to eat lunch with {proGen}? Y / N: ")
if eatL == ('Y' or 'y'): 
    print (f"*You run towards {proGen} and asked*")
    time.sleep(0.25)
    print(f"Hey, {dateName}. Do you want to eat lunch together?")
    if affection <= 1 :
        print("Sure! Let's go.")
        affection += 1
        print (f"{dateName} appreciates your invitation. \nAffection increased by 1!")
        if affection == 3:         #   Winning Condition
            inv = input(f"Do you want to ask {proGen} as your date?\nY / N: ")
            if inv == ('Y' or 'y'):
                    print (f"Hey, {dateName}! Do you want to be my date?")
                    time.sleep(1)
                    print (f"It would be a pleasure, {playerName}!")
                    time.sleep(1)
                    print (f"Congrats, {playerName}. You danced {dateName} during Prom Night. \nAnd won the King and Queen of the Night!")
        time.sleep(0.5)
        print ("You two are talking as you walk. And when you arrived...")
        food = input (f"Do you want to treat {dateName}? \nY / N: ")
        if food == ('Y' or 'y'):
            print(f"{dateName}, I'll pay for your lunch.")
            time.sleep(0.5)
            print(f"*{dateName} looked at you* Are you sure? I can pay for my own food.")
            print("Yes!")
            affection += 1
            print (f"{dateName} think you're sweet and nice. \nAffection increased by 1!")
            if affection == 3:         #   Winning Condition
                inv = input(f"Do you want to ask {proGen} as your date?\nY / N: ")
                if inv == ('Y' or 'y'):
                        print (f"Hey, {dateName}! Do you want to be my date?")
                        time.sleep(1)
                        print (f"It would be a pleasure, {playerName}!")
                        time.sleep(1)
                        if dateGen == ('M' or 'm'):
                            print (f"Congrats, {playerName}. You danced {dateName} during Prom Night. \nAnd won the Kings of the Night!")
                        elif dateGen == ('F'or'f'):
                            print (f"Congrats, {playerName}. You danced {dateName} during Prom Night. \nAnd won the King and Queen of the Night!")
    else:
        print(f"No. I'm meeting with my friends.*{dateName} left.*")
elif eatL == ('N' or 'n'):
    print ("TBC")
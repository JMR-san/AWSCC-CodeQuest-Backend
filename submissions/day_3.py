import time

playerName = input("Enter your name: ")
playerGen = input("Are you male or female? ")
dateGen = input("Are you attracted to male or female? ")
heart = "\u2764"
life = 3
affection = 0

#   define the date gender pronoun
if dateGen.capitalize() == "male" or "Male" or "M" or "m": 
    proGen = "him"
else: 
    dateGen.capitalize() == "female" or "Female" or "F" or "f"
    proGen = "her"

dateName = input (f"What is {proGen} name? ")

#   Introducing the game
print (f"""Hello, {playerName}! Prom night is coming up, and you're planning to 
invite {dateName} as your date. Make {proGen} say yes! 
You have {life} lives:{heart} {heart} {heart}
Goodluck!!""")

#   First situation 1/4
approach = input (f"""You saw {dateName} walking on the hallway. 
Do you want to greet {proGen}? 
Y / N: """)

if approach.capitalize() == 'Y' or 'y':
    print (f"Good morning, {dateName}! How are you doing? ")
    helloD = input(f"""Good morning, {playerName}!! """) 
elif approach.capitalize() == 'N' or 'n':
    print (f"{dateName} noticed you ignore {proGen}!")
    ignore = input("""Do you want to reconcile?
Y / N: """)
    if ignore.capitalize() == 'Y' or 'y':
        print (f"Good morning, {dateName}! How are you doing? ")
        time.sleep(1.5)
        helloD = input(f"""Good morning, {playerName}!! Have you heard the upcoming prom night?\n Y / N""")
        if helloD.capitalize() == 'Y' or 'y':
            ask = input ("Are you coming?\n Y / N")
            if ask.capitalize() == 'Y' or 'y':
                affection += affection
                print (f"*{dateName} smiles* Ooops, the class is about to start, see you to prom!")
                time.sleep(1)
                print (f"{dateName} affection increased: {affection}/3")
    else: 
        life - 1
        print (f"You lost one life, you have remaining {life} lives: {heart} {heart} ")
          
time.sleep(1.5)



     


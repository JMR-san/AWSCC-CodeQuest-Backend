playerName = input("What is your name? ")
print (f"Hello, {playerName}!")

answer = input("Can you help me find a shelter? (Y / N)")

if answer.capitalize() == 'Y':
    print ("The Police arived")
    pol = input ("Is the thief inside? (Y / N) ")

    if pol.capitalize() == "Y":
        print (f"The thief was caught, {playerName} wins!")
    elif pol.capitalize() != "Y":
        print (f"The thief escaped! {playerName} lose")

if answer.capitalize() != 'Y':
    print (f"The thief attacked {playerName}")
    atk = input ("Are you going to fightback? (Y / N)")

    if atk.capitalize() == "Y":
        print (f"The thief was defeated, {playerName} wins!")
    else:
        print (f"The thief escaped! {playerName} lose")


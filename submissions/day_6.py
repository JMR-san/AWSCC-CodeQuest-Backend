limit = int(input("Enter your number: \n"))

if limit >= 0:
    num = 1
    print(f"Limit: {limit} \n")
    while (num <= limit):
        buzz = num % 5
        fizz = num % 3
        if buzz == 0:
            print("Buzz")
        elif fizz == 0:
            print("Fizz")
        else:
            print(f"{num}")
        num += 1
else:
    print("INVALID")
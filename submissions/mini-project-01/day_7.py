shopping_list = []

action = 0
while action != 4:
    print("""\nOptions:
1. Add item to the shopping list1
2. View shopping list
3. Remove item fromt the shopping list
4. Quit""")
    action = int(input("Enter the number of your choice: "))
    if action == 1:
        item = input("Enter the item you want to add: ").capitalize()
        shopping_list.append(item)
        print(f"{item} has been added to your Shopping list.\n")
    elif action == 2:
        print("Your Shopping list:")
        for num, item in enumerate(shopping_list, start=1):
            print(f"\t{num}. {item}")
        print()
    elif action == 3:
        item = input("Enter the item you want to remove: ").capitalize()
        shopping_list.remove(item)
        print(f"{item} has been removed to your Shopping list.\n")
    elif action == 4:
        print("Goodbye!\n")
    else:
        print("Invalid\n")
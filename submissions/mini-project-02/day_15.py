import json
import os

def option_menu():
    menu = ["1 - Add Website, Username and Password",
            "2 - View",
            "3 - Search",
            "4 - Delete",
            "5 - Update",
            "6 - Close"]
    for num in menu: 
        print(f"{num}")

def manager_pass(menu_act):
    os.system('cls')
    with open('data.json', 'r') as file:
        data = json.load(file)

    if menu_act == '1':
        website = input ("Enter name of website: ")
        email = input ("Enter email: ")
        password = input ("Enter password: ")

        new_data = {
        website: [{
            'email': email,
            'password': password
            }]
        }
        os.system('cls')
        
        if website in data: 
            data[website].append({'email': email, 'password': password}) 
        else:
            data.update(new_data)

        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
            
        print("Successfully Added!")

    elif menu_act == '2':
            for website, website_data in data.items():
                print(f"Website: {website}")
                for entry in website_data:
                    print(f"    Email: {entry['email']} \n")
                    print(f"    Password: {entry['password']} \n")

    elif menu_act == '3':
        website = input("Enter website to search: ")
        if website in data:
            print("Website found!")
            data = json.load(f)
            for key, val in data.items():
                if key == website:
                    print(f"Website: {key}")
                    for i in range(len(val)):
                        print(f"    {i+1} Email: {val[i]['email']}")
                        print(f"      Password: {val[i]['password']}\n")
                    return True
        else:
            print("No website found!")

    elif menu_act == '4':
        website = input("Enter website to delete: ")
        with open('data.json', 'r') as file:
            data = json.load(file)
            if website in data:
                del data[website]

                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)
                print("Successfully Removed!")
                return True
            else:
                print("Website not found!")
            return

    elif menu_act == '5':
        website = input("Enter website to update: ")
        if website in data:
            updated = input(" 'EMAIL' or 'PASSWORD': ").lower()
            new_info = input(f"Enter your new {updated}: ")
            data[website][updated] = new_info

            with open('data.json', 'w') as f:
                json.dump(data, f, indent=5)

            print("Successfully updated!")

        else:
            print("No website found!")

    elif menu_act == '6':
        exit()

running = True

while running:
    print("=======>PASSWORD MANAGER<=======")
    option_menu()
    user_input = input("Enter a number: ")
    manager_pass(user_input)
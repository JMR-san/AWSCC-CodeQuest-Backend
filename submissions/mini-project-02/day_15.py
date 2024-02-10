import json
import os
from re import search

def option_menu():
    menu = {"1" : "Add Wesbite, Username and Password",
            "2" : "View",
            "3" : "Search",
            "4" : "Delete",
            "5" : "Update",
            "6" : "Close"}
    for num, func in menu: 
        print(f"{num} - {func}")

def manager_pass(menu_act, website):
    with open('data.json','r') as file:
        data = json.load(file)

    if menu_act == '1':
        website = input ("Enter name of website: ")
        email = input ("Enter email: ")
        password = input ("Enter password: ")

        if website in data:
            data[website].append({'email': email, 'password': password})
        else:
            data[website]= [{'email': email, 'password': password}]

        print("Successfully Added!")

    elif menu_act == '2':
        for num, funct in data.items():
            print(f"Website: {num}")
            for entry in funct:
                print(f"    Email: {entry['email']} \n")
                print(f"    Password: {entry['password']} \n")

    elif menu_act == '3':
        search_result = search(website, data)
        if not search_result:
            print("No website found!")

    elif menu_act == '4':
        search_result = search(website, data )
        if search_result:
            val = get_valid_index(data[website])
            data[website].pop(num)
            if len(data[website]) == 0:
                data.pop(website)
            print("Successfully removed.")

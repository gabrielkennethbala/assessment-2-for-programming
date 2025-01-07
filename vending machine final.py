# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:02:30 2025

@author: xplod
"""


import pyttsx3
engine = pyttsx3.init() 
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[0].id)
engine = pyttsx3.init()
engine.say("WELCOME TO GABRIELS VENDING MACHINE!!!!!! HOW MAY I SERVE YOU")
engine.runAndWait()


Main = ["pastries", "drinks", "snacks"]

pastries_dict = {
    1: {"name": "strawberry cake can", "price": 10.25},
    2: {"name": "chocolate banana cake", "price": 7.00},
    3: {"name": "zaatar croissant", "price": 2.00},
    4: {"name": "cheese croissant", "price": 2.00},
    5: {"name": "apple pie", "price": 5.50},
    6: {"name": "chocolate eclair", "price": 5.50}
}

drinks_dict = {
    1: {"name": "still water", "price": 10.50},
    2: {"name": "pepsi", "price": 7.50},
    3: {"name": "diet pepsi", "price": 2.75},
    4: {"name": "coca cola", "price": 2.75},
    5: {"name": "coke zero", "price": 5.75},
    6: {"name": "mountain dew", "price": 5.75},
    7: {"name": "diet mountain dew", "price": 10.50},
    8: {"name": "apple juice", "price": 7.50},
    9: {"name": "orange juice", "price": 2.50},
    10: {"name": "mixed cocktail juice", "price": 2.25}
}

snacks_dict = {
    1: {"name": "lays chips", "price": 10.25},
    2: {"name": "pringles chips", "price": 7.25},
    3: {"name": "chocolate cookies", "price": 2.25},
    4: {"name": "sour patch gummies", "price": 2.25},
    5: {"name": "coca cola gummy bears", "price": 5.50},
    6: {"name": "jawbreakers", "price": 5.50}
}

total = 0


def main_menu():
    while True:
        print("\nMain Menu:", Main)
        engine.say("CHOOSE YOUR CATEGORY")
        engine.runAndWait()
        x = input("CHOOSE YOUR CATEGORY :DDDDD(type 'exit' to finish): ").upper()
        if x == "PASTRIES":
            pastries_function()
        elif x == "DRINKS":
            drinks_function()
        elif x == "SNACKS":
            snacks_function()
        elif x == "EXIT":   
            checkout_function()
            break
        else:
            print("Invalid category. Please try again.")
            


def display_items(items_dict):
    print("\nAvailable items:")
    for key, value in items_dict.items():
        print(f"{key}: {value['name']} - ${value['price']:.2f}")


def pastries_function():
    global total
    while True:
        display_items(pastries_dict)
        engine.say("ENTER THE NUMBER YOU WANT")
        engine.runAndWait()
        pastries_input = input("ENTER THE NUMBER YOU WAAAAANT (or 'back' to return): ")
        if pastries_input.lower() == "back":
            break
        try:
            pastries_id = int(pastries_input)
            if pastries_id in pastries_dict:
                cost = pastries_dict[pastries_id]['price']
                total += cost
                print(f"Added {pastries_dict[pastries_id]['name']} for ${cost:.2f}. Total: ${total:.2f}")
                break
            else:
                print("YOU INPUTTED THE WRONG ID TRY AGAIN")
        except ValueError:
            print("WRONG, ENTER NEW NUMBER")


def drinks_function():
    global total
    while True:
        display_items(drinks_dict)
        engine.say("ENTER THE NUMBER YOU NEED")
        engine.runAndWait()
        drinks_input = input("ENTER THE NUMBER YOU NEEEED(or 'back' to return): ")
        if drinks_input.lower() == "back":
            break
        try:
            drinks_id = int(drinks_input)
            if drinks_id in drinks_dict:
                cost = drinks_dict[drinks_id]['price']
                total += cost
                print(f"Added {drinks_dict[drinks_id]['name']} for ${cost:.2f}. Total: ${total:.2f}")
                break
            else:
                print("you put in the wrong ID TRY AGAIN")
        except ValueError:
            print("NO, ENTER NEW NUMBER")


def snacks_function():
    global total
    while True:
        display_items(snacks_dict)
        engine.say("ENTER THE NUMBER YOU DESIRE")
        engine.runAndWait()
        snacks_input = input("ENTER THE NUMBER YOU DESIRE(or 'back' to return): ")
        if snacks_input.lower() == "back":
            break
        try:
            snacks_id = int(snacks_input)
            if snacks_id in snacks_dict:
                cost = snacks_dict[snacks_id]['price']
                total += cost
                print(f"Added {snacks_dict[snacks_id]['name']} for ${cost:.2f}. Total: ${total:.2f}")
                break
            else:
                print("you put in the wrojng id TRY AGAIN")
        except ValueError:
            print("NAH, ENTER NEW NUMBER")


def checkout_function():
    global total
    print(f"\nYour total is ${total:.2f}.")
    print("your coin input is = ", money)
    if money >= total:
        change = money - total
        engine.say("THANK YOU FOR YOUR PURCHASE, YOUR CHANGE IS")
        engine.runAndWait()
        print(f"THAAANK YOU FOR YOUR PURCHASE, YOUR CHANGE IS${change:.2f}.")
        total = 0
    else:
        print("Insufficient payment. Please try again.")


money = int(input("HELLO AND WELCOME TO THE VENDING MACHINE, HOW MUCH MONEY WOULD YOU LIKE TO ENTER?"))
verification = input(f"PLEASE CONFIRM IF THE COINS YOU ENTERED IS  {money} (yes or no): ").lower()
if verification == "yes":
    print("ENJOY YOUR SHOPPING AND CHOOSE WISELY")
    main_menu()
else:
    print("Reset the machine and enter your coins again.")
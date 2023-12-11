from entities import *

def main_menu():
    while True:        
        print("1- Créer une nouvelle partie")
        print("2- Charger une partie existante")
        print("3- Crédits")
        print("4- Quitter le jeu")
        menu = input()
        if menu == "1":
            new_game()
        elif menu == "2":
            load_game()
        elif menu == "3":
            credits()
        elif menu == "4":
            return False
                
                
def new_game():
    print ("test")

def save():
    print ("test2")

def load_game():
    print ("test3")

def credits():
    print ("test4")

def exit():
    return "You exited the game"





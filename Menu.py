import json
import time    
def main_menu():
    # Afficher les options
    print("MAIN MENU :")
    print("1. Création d'une nouvelle partie")                                          
    print("2. Charger une partie")
    print("3. Crédit")
    print("4. Fermer")

def introduction():
    print("Bienvenue dans le monde fantastique de Fantasia !")
    time.sleep(0.3)
    print(f"Vous incarnez Sir {player_name}, un vaillant chevalier chargé de protéger le royaume.")
    time.sleep(0.3)
    print("Depuis des siècles, des monstres terrifiants terrorisent les villages, semant le chaos et la destruction.")
    time.sleep(0.3)
    print("Votre quête est de pourchasser ces créatures maléfiques et de ramener la paix dans le royaume.")
    print("Préparez-vous, brave chevalier, l'aventure commence !")
    time.sleep(0.3)
    print("Vous vous tenez devant le château du roi, prêt à partir en quête.")
    time.sleep(0.3)
    print("Le roi vous a confié la mission de traquer les monstres qui menacent la sécurité du royaume.")
    time.sleep(0.3)
    print("Votre première destination est la sombre forêt d'Enigma, où les monstres ont été signalés en grand nombre.")
    time.sleep(0.3)
    print("Armez-vous de votre épée, mettez votre armure, et que la quête commence!")





# Charger la partie depuis le fichier JSON
def load_game():
    try:
        with open("save_game.json", "r") as file:
            saved_data = json.load(file)
            print("Partie chargée avec succès.")
            return saved_data
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
        return None

# Sauvegarder la partie dans un fichier JSON
def save_game(player_name):
    data_to_save = {"player_name": player_name}
    with open("save_game.json", "w") as file:
        json.dump(data_to_save, file)
        print("Partie sauvegardée avec succès.")


main_menu()

# Demander au joueur de choisir une option
choice = input("Entrer votre choix: ")

if choice == "1":
        print("Creation d'une nouvelle partie...")
        # Ajoutez ici le code pour créer une nouvelle partie
        player_name = input("Entrer le nom de votre personnage: ")
        print(f"Ravie de vous rencontrez {player_name}")
        time.sleep(0.3)
        introduction()
        # Sauvegarder la nouvelle partie
        save_game(player_name)
        
elif choice == "2":

        # Charger la partie existante
        saved_data = load_game()
        if saved_data:
            print(f"Partie chargée pour le joueur {saved_data['player_name']}.")
            main_menu()

elif choice == "3":
        print("Crédit")
        print("Réalisateur: Willy, Anthony, Imrane")
        print("Copyrigh 2024")
        main_menu()


elif choice == "4":
        print("Fermeture du jeu...")
        
else:
        print("Choix Invalide")
        main_menu()
        
        

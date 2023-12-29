
def main_menu():
  #Afficher les options
  print("MAIN MENU :")
  print("1. Création d'une nouvelle partie")
  print("2. Sauvegarde de la partie")
  print("3. Crédit")
  print("4. Fermer")

main_menu()
  #demander au joueur de choisir une option
choice = input("Entrer votre choix: ")
  
if choice == "1":
    print("Creation d'une nouvelle partie...")
    # Ajoutez ici le code pour créer une nouvelle partie
    player_name = input("Entrer le nom de votre personnage: ")
    print(f"Ravie de vous rencontrez {player_name}")

elif choice == "2":
    print("Sauvegarde de la partie...")
    # Ajoutez ici le code pour charger une partie sauvegardée

elif choice == "3":
    print("Crédit")
    print("Réalisateur: Willy, Anthony, Imrane")
    print("Copyrigh 2024")

elif choice == "4":
    print("Fermeture du jeu...")
    # Ajoutez ici le code pour quitter le jeu

else:
    print("Invalid choice. Please enter a valid option.")
  #Faire l'action choisie
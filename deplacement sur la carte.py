#liste bidimensionnelle pour la map
carte = [
    ['heaven', 'split', 'fracture', 'bind', 'ascent'],
    ['icebox', 'breeze', 'pearl', 'lotus', 'dust2'],
    ['mirage', 'mirage', 'nuke', 'cache', 'train'],
    ['overpass', 'cobblestone', 'inferno', 'agency', 'assault'],
    ['italy', 'office', 'feur', 'quoi', 'spawn']
]

# Mot secret pour permettre de se déplacer à nouveau
mot_secret = "bellobito"

# pour les event aleatoire de spawn de mobs et loots
def gerer_evenement(case):
    if case == 'quoi':
        print("un mob qui spawn boue")
    elif case == 'feur':
        print("ouaw un iphone 15 pro max 120hz")
    #...


# N E S O
def deplacer(direction, position_joueur):
    if direction == 'nord' and position_joueur[0] > 0:
        position_joueur[0] -= 1
    elif direction == 'est' and position_joueur[1] < len(carte[0]) - 1:
        position_joueur[1] += 1
    elif direction == 'sud' and position_joueur[0] < len(carte) - 1:
        position_joueur[0] += 1
    elif direction == 'ouest' and position_joueur[1] > 0:
        position_joueur[1] -= 1
    else:
        print("hop! hop!, tu ne peut pas allez dans un mur.")
        return False

    # pose actuelle
    case_actuelle = carte[position_joueur[0]][position_joueur[1]]

    # affichage
    print(f"Bienvenue à {case_actuelle}")
    print(f" {position_joueur}") #pour se reperer (a suppre)

    # Gérer l'événement pour la case actuelle
    gerer_evenement(case_actuelle)

    # Vérifier si le joueur a atteint la case spéciale
    if case_actuelle == 'office':
        mot_saisi = input("Vous avez atteint la sortie ! Entrez le mot secret pour pouvoir vous déplacer à nouveau : ")
        if mot_saisi != mot_secret:
            print("vous avez fuis")
            return False
    else:
        print("gg")
        return True

# les co du spawn
position_joueur = [4, 4]


historique_positions = [position_joueur.copy()]

# main while
while True:
    # while déplacement
    while True:
        # help
        direction = input("Entrez la direction (nord, est, sud, ouest): ").lower()

        # quitter deplacement pour entrer dans mode combat
        if direction == 'quitter':
            break

    

        # Copier les coordonnées actuelles du joueur
        ancienne_position = position_joueur.copy()

        # Mettre à jour les coordonnées du joueur
        deplacer(direction, position_joueur)
        
        


        # Ajouter la position actuelle à l'historique
        historique_positions.append(position_joueur.copy())
    
    #revenir apres le mode combat
    recommencer = input("Voulez-vous recommencer ? (oui/non) ").lower()
    if recommencer != 'oui':
        break











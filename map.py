#liste bidimensionnelle pour la map
carte = [
    ['heaven', 'split', 'fracture', 'bind', 'ascent'],
    ['icebox', 'breeze', 'pearl', 'lotus', 'dust2'],
    ['mirage', 'mirage', 'nuke', 'cache', 'train'],
    ['overpass', 'cobblestone', 'inferno', 'agency', 'assault'],
    ['italy', 'office', 'feur', 'quoi', 'spawn']
]

# les co du spawn
position_joueur = [4, 4]

#-----------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#


# pour les event aleatoire de spawn de mobs et loots
def gerer_evenement(case):
    if case == 'quoi':
        print("objet 2")
    elif case == 'feur':
        print("objet 1")
    #...

#-----------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#

# Mot secret pour permettre de se déplacer à nouveau
mot_secret = "motsecret"

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
        print("Tu a atteinte la limite de la map")
        return False

    # pose actuelle
    case_actuelle = carte[position_joueur[0]][position_joueur[1]]

    # affichage
    print(f"Bienvenue à {case_actuelle}")
    print(f" {position_joueur}") #pour se reperer, c les co (a suppre)

    # Gérer l'événement pour la case actuelle
    gerer_evenement(case_actuelle)

    # Vérifier si le joueur a atteint une case spéciale
    if case_actuelle == 'office':
        mot_saisi = input("Zone spéciale. Entrez le mot secret pour pouvoir vous déplacer à nouveau : ")
        if mot_saisi != mot_secret:
            print("Vous avez gagné !")
            return False
        else:
            global dans_boucle_deplacement
            dans_boucle_deplacement = False
    else:
        print("Lorem")
        return True





#-----------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#


#sauvegarde de la position du joueur
historique_positions = [position_joueur.copy()]


while True:
    # Boucle de déplacement
    while dans_boucle_deplacement:
        # dmd au joueur la direction
        direction = input("Entrez la direction (nord, est, sud, ouest: ").lower()

        # ff
        if direction == 'quitter':
            dans_boucle_deplacement = False
            break

        # Copier les coordonnées actuelles du joueur
        ancienne_position = position_joueur.copy()

        # Mettre à jour les coordonnées du joueur
        deplacement_reussi = deplacer(direction, position_joueur)

        #copier la position du joueur avant le combat
        if deplacement_reussi:
            historique_positions.append(position_joueur.copy())

    # Boucle de combat (à développer)

    # Demander à l'utilisateur s'il souhaite revenir à la boucle de déplacement
    recommencer = input("Voulez-vous revenir à la boucle de déplacement ? (oui/non) ").lower()
    if recommencer != 'oui':
        break

    # Réinitialiser la variable pour la prochaine itération
    dans_boucle_deplacement = True





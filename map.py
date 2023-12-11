from entities import *

# liste bidimensionnelle pour la map
carte = [
    ['heaven', 'split', 'fracture', 'bind', 'ascent'],
    ['icebox', 'breeze', 'pearl', 'lotus', 'dust2'],
    ['mirage', 'mirage', 'nuke', 'cache', 'train'],
    ['overpass', 'cobblestone', 'inferno', 'agency', 'assault'],
    ['italy', 'office', 'feur', 'quoi', 'spawn']
]

# les co du spawn
position_joueur = [4, 4]



# Variable pour indiquer si le joueur est dans la boucle de déplacement
dans_boucle_deplacement = True

# -----------------------------------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------#


# pour les event aleatoire de spawn de mobs et loots
def gerer_evenement(case):
    print(case)
    if case == 'quoi':
        print("Vous avez obtenu une potion de vie")
    elif case == 'feur':
        print("objet 1")
    # ...

# -----------------------------------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------#




# Nord Est Sud Ouest


def deplacer(direction, position_joueur):
    if direction == 'nord' and position_joueur[0] > 0:
        position_joueur[0] -= 1
    elif direction == 'est' and position_joueur[1] < len(carte) - 1:
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

    # Gérer l'événement pour la case actuelle
    gerer_evenement(case_actuelle)
    
# -----------------------------------------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------------------------------------#

# sauvegarde de la position du joueur
historique_positions = [position_joueur.copy()]


while True:
    # Boucle de déplacement
    while dans_boucle_deplacement:
        # dmd au joueur la direction
        direction = input("Entrez la direction nord, est, sud, ouest: ").lower()

        # ff
        if direction == 'ff':
            dans_boucle_deplacement = False
            quitter =input("etes vous sur de quitter ? la parti ne serra pas sauvegarder !!! (oui ou non) :")
            if quitter == "oui" :
                break
            elif quitter == 'non':
                dans_boucle_deplacement = True

        # Copier les coordonnées actuelles du joueur
        ancienne_position = position_joueur.copy()

        # Mettre à jour les coordonnées du joueur
        deplacement_reussi = deplacer(direction, position_joueur)

        # copier la position du joueur avant le combat
        if deplacement_reussi:
            historique_positions.append(position_joueur.copy())

    # Boucle de combat (à développer)


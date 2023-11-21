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

# pour les event aleatoire de spawn de mobs et loots
def gerer_evenement(case):
    if case == 'quoi':
        print("un mob qui spawn boue")
    elif case == 'feur':
        print("ouaw un iphone 15 pro max 120hz")
    #...

# while deplacement
while True:
    #help pour bouger
    direction = input("Entrez la direction (nord, est, sud, ouest): ").lower()
    
    # avoir les co pour verifier par la suite
    ancienne_position = position_joueur.copy()
    
    if direction == 'nord' and position_joueur[0] > 0:
        position_joueur[0] -= 1
    elif direction == 'est' and position_joueur[1] < len(carte[0]) - 1:
        position_joueur[1] += 1
    elif direction == 'sud' and position_joueur[0] < len(carte) - 1:
        position_joueur[0] += 1
    elif direction == 'ouest' and position_joueur[1] > 0:
        position_joueur[1] -= 1
    
    # verifier si le joueur a bouger
    if position_joueur != ancienne_position:
        
        # pour se reperer (a suppr)
        case_actuelle = carte[position_joueur[0]][position_joueur[1]]
        
        # affichage
        print(f"Bienvenue à {case_actuelle}")
        print(f" {position_joueur}") #pour se reperer (a suppre)
    else:
        print("Déplacement impossible. Choisissez une autre direction.")

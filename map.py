import simpleaudio as sa
from entities import *
from colorama import Fore, Back, Style


# liste bidimensionnelle pour la map
carte = [
    ["Glacier du Silence", "Temple des Souvenirs", "Porte des Étoiles", "Collines d'Azur", "Terres de Brume"],
    ["Plage des Songes", 'Terres de Fer', "Grottes de l'Abîme", "Chutes d'Ébène", "Jungle de l'Éclipse"],
    ["Falaises du Serpent", "Désert d'Ivoire", "Îles de l'Aurore", "Forêt d'Argent", "Marais des Ombres"],
    ["Cité des Vents", "Îles des Sirens", "Canyon de l'Écho", "Ruines d'Opale", "Lac des Mystères"],
    ["Château des Lamentations", "Plaines du Mirage", "Montagnes du Crépuscule", "Vallée d'Émeraude", "Volcan de l'Ombre"]
]

# les co du spawn
position_joueur = [4, 4]

# Variable pour indiquer si le joueur est dans la boucle de déplacement
dans_boucle_deplacement = True

# Chargez la musique de fond
background_music = sa.WaveObject.from_wave_file("backgroundMusic.wav")

#pour jouer la musique de fond
def play_background_music():
    global background_music
    play_obj = background_music.play()
    return play_obj

#pour arrêter la musique de fond
def stop_background_music(play_obj):
    play_obj.stop()

play_obj = play_background_music() # play

def Separe():
    print(Style.BRIGHT + "=================================================================================================================")

# -----------------------------------------------------------------------------------------------------------------#

# -----------------------------------------------------------------------------------------------------------------#

itemUtiliser = False

# pour les event aleatoire de spawn de mobs et loots
def gerer_evenement(case):
    
    global itemUtiliser

    if case == "Vallée d'Émeraude" and not itemUtiliser:
        print(Fore.MAGENTA + Style.BRIGHT + "Vous entrez dans la Vallée d'Émeraude, un sanctuaire magique caché entre les montagnes.")
        print("Des arbres aux feuilles émeraude diffusent une lueur apaisante, éclairant le sentier bordé de fleurs vibrantes.")
        input("Des papillons multicolores dansent dans l'air, créant une symphonie visuelle qui évoque la paix et la sérénité.\n...")

        print("\nEn franchissant l'arc de vigne qui marque l'entrée, une aura mystique vous accueille.")
        print("Autrefois le refuge d'une civilisation de magiciens, la Vallée d'Émeraude abritait un cristal d'une puissance incommensurable.")
        input("Pour protéger ce joyau, les habitants ont scellé le cristal dans une autre dimension, préservant ainsi la beauté et la magie de la vallée.\n...")

        print("\nAlors que vous avancez dans la Vallée d'Émeraude, vos yeux sont attirés par un éclat métallique caché parmi les fleurs.")
        print("En vous approchant, vous découvrez un coffre mystérieux, orné de motifs enchantés." + Fore.RESET + Style.RESET_ALL)

        choix_coffre = input(Fore.RED + Style.BRIGHT + "Voulez-vous ouvrir le coffre mystérieux ? (Oui/Non) \n>" + Fore.RESET + Style.RESET_ALL).lower()

        if choix_coffre == "oui":
            print(Fore.MAGENTA + Style.BRIGHT +"\nVous décidez d'ouvrir le coffre avec prudence. À l'intérieur, vous trouvez une potion de vie mystique, émettant une lueur curative.")
            print("Cette potion pourrait se révéler précieuse dans votre quête pour protéger la Vallée d'Émeraude."+ Fore.RESET + Style.RESET_ALL)
            print(Fore.GREEN + "Vous avez obtenu une potion de vie" + Fore.RESET)
            joueur.add_item(healpotion)
            print("     -- potion de vie +1")
            input("...")
            itemUtiliser = True
        else:
            print("\nVous choisissez de ne pas ouvrir le coffre mystérieux. Sa précieuse cargaison reste cachée, attendant peut-être d'être découverte par un aventurier futur.")

        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
    elif case == "Vallée d'Émeraude" and itemUtiliser:
        print("Rebonjour dans la Vallée d'Émeraude ! Vous vous souvenez du coffre mystérieux que vous avez découvert lors de votre première visite.")

    elif case == "Montagnes du Crépuscule" and not itemUtiliser:
        print(Fore.MAGENTA + Style.BRIGHT +"Vous atteignez les Montagnes du Crépuscule, une chaîne majestueuse de pics escarpés qui se dressent contre le ciel vespéral.")
        print("Les sommets sont éclairés par les dernières lueurs du jour, créant une toile de couleurs chaleureuses et éphémères.")
        print("Des sentiers sinueux serpentent entre les rochers, offrant une vue imprenable sur la vallée en contrebas.")
        input("Les murmures du vent entre les montagnes créent une atmosphère à la fois paisible et mystique.\n...")

        print("\nVous gravissez les sentiers escarpés qui serpentent à travers les Montagnes du Crépuscule.")
        print("Au sommet, vous découvrez un autel ancien baigné par les derniers rayons du soleil.")
        print("Une énergie mystique semble émaner de cet endroit, chargée d'histoire et de pouvoir.")
        input("Les anciennes légendes racontent que cet autel est le gardien d'un artefact légendaire, connu pour détenir une puissance céleste.\n...")

        print("\nSoudain, des bruits suspects attirent votre attention. Des ombres se profilent parmi les rochers.")
        print("Des bandits surgissent, armés et prêts à attaquer !")
        print("La voix mystique dans votre esprit vous implore : 'Oh non, des bandits nous attaquent ! Aidez-nous à défendre ces Montagnes du Crépuscule, héros !'"+ Fore.RESET + Style.RESET_ALL)

        choix_defense = input(Fore.RED + Style.BRIGHT + "Voulez-vous aider à défendre les Montagnes du Crépuscule des bandits ? (Oui/Non) " + Fore.RESET + Style.RESET_ALL).lower()

        if choix_defense == "oui":
            print("Vous vous préparez au combat, prêt à défendre les Montagnes du Crépuscule contre l'invasion des bandits.")
            itemUtiliser = True

        else:
            print("Vous choisissez de ne pas intervenir dans l'affrontement avec les bandits. La voix mystique exprime sa déception.")

    elif case == "Montagnes du Crépuscule" and itemUtiliser:
        print("Rebonjour dans les Montagnes du Crépuscule ! Vous vous souvenez des bandits qui ont attaqué lors de votre première visite.")
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
    Separe()
    print(f"                                     Bienvenue à {case_actuelle}")
    Separe()
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
        direction = input("Entrez la direction nord, est, sud, ouest: \n>").lower()
        # ff
        if direction == 'ff':
            dans_boucle_deplacement = False
            quitter = input("etes vous sur de quitter ? la partie ne sera pas sauvegardée !!! (oui ou non) \n> :")
            if quitter == "oui":
                print("GAME OVER")
                play_obj.stop()
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
                    
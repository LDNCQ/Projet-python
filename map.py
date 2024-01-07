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
position_joueur = [2, 2]

# Variable pour indiquer si le joueur est dans la boucle de déplacement
dans_boucle_deplacement = True

# Chargez la musique de fond
background_music = sa.WaveObject.from_wave_file("backgroundMusic.wav")

#pour jouer la musique de fond
def play_background_music():
    global background_music
    play_obj = background_music.play()
    return play_obj

# #pour arrêter la musique de fond
# def stop_background_music(play_obj):
#     play_obj.stop()

play_obj = play_background_music() # play

def Separe():
    print(Style.BRIGHT + "=================================================================================================================")

# -----------------------------------------------------------------------------------------------------------------#

# -----------------------------------------------------------------------------------------------------------------#

itemUtiliser1 = False
itemUtiliser2 = False
itemUtiliser3 = False
itemUtiliser4 = False
itemUtiliser5 = False
itemUtiliser6 = False
foretDargent = False
jungleDeLeclipse = False
TerresDeFer = False
TempleDesSouvenirs = False
PorteDesEtoiles = False
CollinesDazur = False

# pour les event aleatoire de spawn de mobs et loots
def gerer_evenement(case):
    
    global itemUtiliser1, itemUtiliser2, itemUtiliser3,itemUtiliser4, itemUtiliser5, itemUtiliser6, foretDargent, jungleDeLeclipse, TerresDeFer, TempleDesSouvenirs, PorteDesEtoiles, CollinesDazur

    if case == "Vallée d'Émeraude" and not itemUtiliser1:
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
            itemUtiliser1 = True
        else:
            print("\nVous choisissez de ne pas ouvrir le coffre mystérieux. Sa précieuse cargaison reste cachée, attendant peut-être d'être découverte par un aventurier futur.")

        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
    
    elif case == "Vallée d'Émeraude" and itemUtiliser1:
        print("Rebonjour dans la Vallée d'Émeraude ! Vous vous souvenez du coffre mystérieux que vous avez découvert lors de votre première visite.")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

    # -----------------------------------------------------------------------------------------------------------------#

    # -----------------------------------------------------------------------------------------------------------------#

    elif case == "Montagnes du Crépuscule" and not itemUtiliser2:
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
            itemUtiliser2 = True

        else:
            print("Vous choisissez de ne pas intervenir dans l'affrontement avec les bandits. La voix mystique exprime sa déception.")

        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

    elif case == "Montagnes du Crépuscule" and itemUtiliser2:
        print("Rebonjour dans les Montagnes du Crépuscule ! Vous vous souvenez des bandits qui ont attaqué lors de votre première visite.")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

    # -----------------------------------------------------------------------------------------------------------------#

    # -----------------------------------------------------------------------------------------------------------------#
        
    elif case == "Plaines du Mirage" and not itemUtiliser3:
        print(Fore.MAGENTA + Style.BRIGHT + "Vous pénétrez dans les vastes Plaines du Mirage, un paysage éthéré où le sol ondule comme une mer de lumière.")
        print("Des illusions subtiles créent des formes changeantes à l'horizon, défiant la réalité.")
        input("Des herbes scintillantes sous la lumière du soleil créent une atmosphère mystique. Un léger brouillard flotte au ras du sol, ajoutant une touche de magie à cette étendue enchanteresse.\n...")

        print("\nLes Plaines du Mirage cachent des secrets anciens et une énergie en constante fluctuation.")
        print("Au centre des plaines, une oasis magique est connue pour exaucer les vœux des voyageurs dignes.")
        print("Alors que vous explorez ce paysage éthéré, une silhouette floue apparaît à l'horizon, vous appelant à rejoindre l'oasis.")
        print("Une voix douce résonne dans l'air, révélant que l'oasis a été perturbée par des créatures de l'ombre.")
        input("Les illusions des Plaines du Mirage sont en danger, et votre présence est requise pour restaurer l'harmonie.\n..." + Fore.RESET + Style.RESET_ALL)
        itemUtiliser3 = True
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

    elif case == "Plaines du Mirage" and itemUtiliser3:
        print("Rebonjour dans les Plaines du Mirage ! Vous vous souvenez des illusions changeantes, de l'oasis magique, et de la menace des créatures de l'ombre.")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

    # -----------------------------------------------------------------------------------------------------------------#

    # -----------------------------------------------------------------------------------------------------------------#

    elif case == "Château des Lamentations" and not itemUtiliser4:
        print(Fore.MAGENTA + Style.BRIGHT + "Vous approchez du Château des Lamentations, une imposante forteresse qui se dresse au sommet d'une colline escarpée.")
        print("Les murs en ruine portent les stigmates du temps, et des vignes sauvages s'enroulent autour des pierres usées.")
        input("L'air est imprégné d'une aura sombre et mystérieuse, et le vent murmure des échos de chagrins passés.\n...")

        print("\nAlors que vous franchissez la porte du Château des Lamentations, des soupirs lointains résonnent dans les couloirs déserts.")
        print("Ce château, autrefois majestueux, est maintenant plongé dans l'oubli et le désespoir.")
        print("Des légendes racontent que des âmes tourmentées errent ici, cherchant la paix qui leur a été refusée.")
        print("Au cœur du château, une source de ténèbres semble grandir. Une voix sinistre murmure des avertissements dans votre esprit, révélant que l'équilibre entre les mondes est menacé.")
        input("Pour résoudre ce mystère, vous devrez affronter les chagrins passés qui hantent ces murs.\n...")

        print("\nAlors que vous explorez les sombres couloirs du Château des Lamentations, une horde de fantômes éthérés émerge des ombres.")
        print("Leurs lamentations résonnent dans les halls, témoignant de chagrins qui persistent même après la mort.")
        print("La voix sinistre dans votre esprit s'élève, vous avertissant que ces âmes tourmentées sont une manifestation des tourments qui hantent le château.")
        print("Vous êtes maintenant confronté à une décision difficile : affronter la horde de fantômes pour apaiser les âmes en peine ou tenter de contourner cette sinistre rencontre.")
        print("Que choisissez-vous ?" +Fore.RESET + Style.RESET_ALL)

        choix_affrontement = input(Fore.RED + Style.BRIGHT +"Voulez-vous affronter la horde de fantômes ? (Oui/Non) \n>"+Fore.RESET + Style.RESET_ALL).lower()

        if choix_affrontement == "oui":
            print("Vous décidez de faire face à la horde de fantômes. Votre lame coupe à travers les formes éthérées, dissipant les lamentations.")
            print("À mesure que la horde diminue, l'énergie sinistre qui imprègne le château commence à se dissiper.")
            print("Les âmes tourmentées semblent enfin trouver la paix. Le Château des Lamentations respire un sentiment de calme retrouvé.")
            itemUtiliser4 = True
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
        else:
            print("Vous choisissez de contourner la horde de fantômes, évitant un combat potentiellement dangereux.")
            print("Cependant, la voix sinistre murmure que les ombres continueront à hanter le château jusqu'à ce que la vérité soit révélée.")
            print("Votre décision aura des conséquences sur le destin du Château des Lamentations.")

            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
        
    elif case == "Château des Lamentations" and itemUtiliser4:
        print("Rebonjour dans le Château des Lamentations ! Vous vous souvenez des murs en ruine, des lamentations des âmes tourmentées, et de la horde de fantômes.")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
    # -----------------------------------------------------------------------------------------------------------------#

    # -----------------------------------------------------------------------------------------------------------------#
    elif case == "Volcan de l'Ombre" and not itemUtiliser5:

        print(Fore.MAGENTA + Style.BRIGHT + "Vous arrivez aux abords du redoutable Volcan de l'Ombre, une montagne de feu et de fumée qui domine l'horizon.")
        print("Les éruptions fréquentes projettent des cendres dans le ciel, obscurcissant le soleil et créant une atmosphère apocalyptique.")
        print("Des rivières de lave incandescente serpentent le long des flancs du volcan, émettant une lueur sinistre dans l'obscurité.")
        input("Des ombres dansent sur les parois rocheuses, témoignant de la présence d'une puissance ancienne et inquiétante.\n...")

        print("\nAlors que vous vous approchez du cratère fumant du Volcan de l'Ombre, un murmure profond se fait entendre.")
        print("Les légendes racontent que ce volcan renferme une forge mystique, alimentée par le feu des entrailles de la terre.")
        print("Des créatures de feu et d'ombre errent dans les profondeurs, protégeant les secrets enfouis sous la roche brûlante.")
        print("Une voix chuchote dans le vent, révélant que le Volcan de l'Ombre détient un artefact antique lié aux forces de l'ombre.")
        input("L'équilibre de la région est menacé, et votre quête vous conduit maintenant vers les entrailles de ce volcan redoutable.\n...")

        print("\nAlors que vous explorez les entrailles brûlantes du Volcan de l'Ombre, des créatures de feu surgissent de l'ombre.")
        print("Leurs formes ardentes dansent et tourbillonnent, défiant la chaleur extrême du volcan.")
        print("Ces ennemis de feu semblent protéger avec ferveur les secrets enfouis dans ce lieu maudit.")
        print("Vous êtes maintenant confronté à une bataille imminente. Leur flamme brûlante vacille à la moindre brise, mais leur pouvoir est redoutable.")
        input("Préparez-vous à affronter les créatures ardentes.\n..."+ Fore.RESET + Style.RESET_ALL)

        choix_combat_feu = input(Fore.RED + Style.BRIGHT +"Voulez-vous affronter les ennemis de feu ? (Oui/Non) "+ Fore.RESET + Style.RESET_ALL).lower()

        if choix_combat_feu == "oui":
            print("Vous vous engagez dans la bataille contre les ennemis de feu. Les flammes éclatent dans une danse furieuse.")
            print("À mesure que vous triomphez, les créatures laissent derrière elles des marques de cendres et de résistance brisée.")
            print("La voie vers l'avant s'ouvre, mais la chaleur du volcan s'intensifie.")
            itemUtiliser5 = True
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
        else:
            print("Vous choisissez de contourner les ennemis de feu, évitant un affrontement potentiellement périlleux.")
            print("Cependant, la voix sinistre murmure que votre chemin pourrait être semé d'autres dangers, car les ombres du volcan cachent bien des mystères.")
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

    elif case == "Volcan de l'Ombre" and itemUtiliser5:
        print("Rebonjour dans le Volcan de l'Ombre ! Vous vous souvenez des rivières de lave, des ombres dansantes, et de la rencontre avec les ennemis de feu.")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
    # -----------------------------------------------------------------------------------------------------------------#

    # -----------------------------------------------------------------------------------------------------------------#
    elif case == "Cité des Vents" and not itemUtiliser6:
        print(Fore.MAGENTA + Style.BRIGHT +"Vous atteignez la majestueuse Cité des Vents, perchée au sommet de hautes falaises.")
        print("Les bâtiments aux architectures élégantes se fondent avec les courants d'air tourbillonnants qui parcourent les rues étroites.")
        print("Des dômes translucides ornent les toits, capturant la lumière du soleil et projetant des reflets éthérés dans l'atmosphère.")
        input("Des ponts suspendus relient les différents niveaux de la cité, offrant une vue imprenable sur les vallées en contrebas.\n...")

        print("\nLa Cité des Vents est renommée pour abriter les artisans des airs, des maîtres de la manipulation des vents et des courants aériens.")
        print("Alors que vous explorez les quartiers animés, une rumeur se répand : des artefacts anciens, alimentés par les vents eux-mêmes, ont été dérobés.")
        print("Les vents capricieux tourbillonnent avec agitation, signe d'une perturbation dans l'équilibre de la cité.")
        print("Une figure mystérieuse vous aborde, révélant qu'un culte des ombres tente de corrompre les vents pour des desseins obscurs.")
        input("Votre quête vous conduit à travers les ruelles en spirale et les places aériennes de la Cité des Vents, où la danse des courants d'air cache des secrets millénaires.\n...")

        print("\nAlors que vous traversez les quartiers aériens de la Cité des Vents, des tourbillons d'air prennent forme.")
        print("Ces ennemis ressemblent à des tornades, déchirant tout sur leur passage avec une force dévastatrice.")
        print("Ils semblent être les manifestations corrompues des vents autrefois paisibles de la cité.")
        print("Vous êtes maintenant confronté à une tempête tourbillonnante. Leurs rugissements déchirent l'air, et leur danse destructrice bloque votre progression.")
        input("Préparez-vous à affronter ces ennemis en forme de tornade ou cherchez un moyen créatif de les contourner.\n..." +Fore.RESET + Style.RESET_ALL)

        choix_combat_tornade = input(Fore.RED + Style.BRIGHT +"Voulez-vous affronter les ennemis en forme de tornade ? (Oui/Non) "+ Fore.RESET + Style.RESET_ALL).lower()

        if choix_combat_tornade == "oui":
            print("Vous vous lancez dans la bataille contre les ennemis en forme de tornade. Leurs forces destructrices sont puissantes, mais votre détermination est inébranlable.")
            print("À mesure que vous triomphez, les tornades perdent de leur force et se dissipent dans les vents.")
            print("Les vents de la Cité reprennent leur calme, remerciant votre bravoure.")
            itemUtiliser6 = True
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

        else:
            print("Vous choisissez de contourner les ennemis en forme de tornade, évitant un affrontement potentiellement dévastateur.")
            print("Cependant, la voix sinistre murmure que la corruption dans les vents de la cité persiste, attendant d'autres occasions pour se manifester.")
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

    elif case == "Cité des Vents" and itemUtiliser6:
        print("Rebonjour dans la Cité des Vents ! Vous vous souvenez des quartiers aériens, des dômes translucides, et de la menace des vents corrompus.")
        print("Vous vous souvenez de la tempête tourbillonnante dans la Cité des Vents, des ennemis en forme de tornade déchirant tout sur leur passage, et de votre choix de les affronter ou de les contourner.")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
    # -----------------------------------------------------------------------------------------------------------------#

    # -----------------------------------------------------------------------------------------------------------------#
    elif case == "Forêt d'Argent" and not foretDargent:
        print(Fore.MAGENTA + Style.BRIGHT +"Vous pénétrez dans la Forêt d'Argent, un lieu magique où les arbres aux feuilles d'argent étincellent à la lueur de la lune.")
        print("Les rayons lunaires filtrent à travers les frondaisons, créant une symphonie de lueurs argentées.")
        input("Les murmures du vent entre les branches semblent révéler des secrets millénaires, tandis que des ruisseaux cristallins serpentent doucement entre les arbres.\n...")

        print("\nLa Forêt d'Argent est réputée pour abriter des créatures enchantées et des esprits sylvestres.")
        print("Cependant, une étrange obscurité semble s'insinuer entre les troncs anciens.")
        print("Des échos lointains signalent une perturbation dans l'équilibre naturel de la forêt.")
        print("Une nymphe solitaire vous approche, ses yeux reflétant la préoccupation.")
        print("Elle vous révèle que l'Arbre d'Argent, le gardien ancestral de la forêt, est en danger.")
        print("Une force maléfique tente de corrompre sa magie, menaçant la vie même de la Forêt d'Argent.")
        input("Votre quête vous appelle à explorer les profondeurs mystiques de cette forêt enchantée, à affronter les ombres qui s'y cachent, et à sauver l'Arbre d'Argent avant qu'il ne soit trop tard.\n...")

        print("\nAlors que vous progressez plus profondément dans la Forêt d'Argent, des phalènes géantes émergent des ombres.")
        print("Leurs ailes étincelantes battent dans un rythme hypnotique, éclairant la nuit de la forêt.")
        print("Ces créatures, habituellement paisibles, semblent être agitées par la perturbation qui touche la forêt.")
        input("Vous êtes maintenant confronté à une décision difficile : affronter les phalènes géantes pour restaurer la quiétude ou chercher un moyen de les apaiser sans combat.\n..."+Fore.RESET + Style.RESET_ALL)

        choix_combat_phalenes = input(Fore.RED + Style.BRIGHT +"Voulez-vous affronter les phalènes géantes ? (Oui/Non) "+ Fore.RESET + Style.RESET_ALL).lower()

        if choix_combat_phalenes == "oui":
            print("Vous décidez de faire face aux phalènes géantes. Leurs ailes chatoyantes se mêlent à votre combat, mais votre détermination l'emporte.")
            print("À mesure que vous triomphez, les phalènes retrouvent leur calme, contribuant à rétablir l'harmonie dans la Forêt d'Argent.")
            foretDargent = True
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
        else:
            print("Vous choisissez de ne pas combattre les phalènes géantes, optant plutôt pour une approche pacifique.")
            print("En utilisant votre sagesse, vous parvenez à communiquer avec les phalènes et à les apaiser.")
            print("Leur agitation diminue, et elles vous guident vers l'Arbre d'Argent, reconnaissantes de votre choix pacifique.")
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

    elif case == "Forêt d'Argent" and foretDargent:
        print("Rebonjour dans la Forêt d'Argent ! Vous vous souvenez des arbres aux feuilles d'argent étincelantes, des murmures du vent, et de la rencontre avec les phalènes géantes.")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

# -----------------------------------------------------------------------------------------------------------------#

# -----------------------------------------------------------------------------------------------------------------#
    elif case == "Jungle de l'Éclipse" and not jungleDeLeclipse:
        print(Fore.MAGENTA + Style.BRIGHT +"Vous pénétrez dans la mystérieuse Jungle de l'Éclipse, où la végétation dense crée un écheveau de lianes, de fougères géantes et d'arbres majestueux.")
        print("La lueur diffuse à travers les frondaisons crée une ambiance irréelle, évoquant une éclipse perpétuelle.")
        input("Des cris d'oiseaux exotiques et le bourdonnement des insectes emplissent l'air, masquant les secrets cachés au cœur de la jungle.\n...")

        print("\nLa Jungle de l'Éclipse est un lieu empreint de magie ancienne. On raconte que des artefacts puissants, liés aux phases lunaires et solaires, sont dissimulés dans les profondeurs de la jungle.")
        print("Une tribu locale vous approche, révélant que l'équilibre entre la lumière et l'ombre dans la jungle est menacé.")
        print("Ils vous parlent d'une éclipse imminente, dont les effets pourraient libérer une force sombre longtemps scellée.")
        print("Votre quête vous appelle à traverser les sentiers énigmatiques, à résoudre les énigmes lunaires, et à affronter les créatures éclipsées qui hantent la jungle.")
        input("Sauver l'équilibre délicat de la Jungle de l'Éclipse devient votre nouvelle mission. Oserez-vous percer les mystères de cette jungle ensorcelée?")

        print("\nAlors que vous progressez à travers les sentiers énigmatiques de la Jungle de l'Éclipse, des créatures éclipsées surgissent des ombres.\n...")
        print("Leurs formes exotiques et mystérieuses se fondent avec l'environnement de la jungle.")
        print("Ces créatures, habituellement paisibles, semblent agitées par la perturbation de l'équilibre naturel.")
        input("Vous êtes maintenant confronté à une décision cruciale : affronter ces créatures pour restaurer la quiétude ou tenter de les apaiser sans violence.\n..."+Fore.RESET + Style.RESET_ALL)

        choix_combat_jungle = input(Fore.RED + Style.BRIGHT +"Voulez-vous affronter les créatures de la Jungle de l'Éclipse ? (Oui/Non) "+ Fore.RESET + Style.RESET_ALL).lower()

        if choix_combat_jungle == "oui":
            print("Vous décidez de faire face aux créatures de la Jungle de l'Éclipse. Leurs mouvements gracieux et agiles créent une danse complexe, mais vous êtes prêt.")
            print("À mesure que vous triomphez, les créatures retrouvent leur calme, contribuant à rétablir l'équilibre dans la jungle.")
            jungleDeLeclipse = True
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
        else:
            print("Vous choisissez de ne pas combattre les créatures de la Jungle de l'Éclipse, optant plutôt pour une approche pacifique.")
            print("En utilisant votre empathie, vous parvenez à communiquer avec les créatures et à les apaiser.")
            print("La jungle résonne de sons apaisants, et les créatures vous guident vers la prochaine épreuve, reconnaissantes de votre choix pacifique.")
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

    elif case == "Jungle de l'Éclipse" and jungleDeLeclipse:
        print("Rebonjour dans la Jungle de l'Éclipse ! Vous vous souvenez de la végétation dense, des échos mystérieux, de l'éclipse perpétuelle, et de la rencontre avec les créatures éclipsées.")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
# -----------------------------------------------------------------------------------------------------------------#

# -----------------------------------------------------------------------------------------------------------------#
    elif case == "Terres de Fer" and not TerresDeFer:
        print(Fore.MAGENTA + Style.BRIGHT +"Vous pénétrez dans les Terres de Fer, un paysage austère et inhospitalier où des collines escarpées, parsemées de formations rocheuses abruptes, s'étendent à perte de vue.")
        print("La terre elle-même semble avoir absorbé la force du fer, donnant naissance à des teintes rouges et ocres.")
        input("Des vents violents balayent la surface, soulevant des tourbillons de poussière et ajoutant une aura de mystère à cette terre sauvage.\n...")

        print("\nLes Terres de Fer sont réputées pour être le domaine des forgerons légendaires, capables de manipuler le fer avec une maîtrise sans égale.")
        print("Cependant, des rumeurs parlent d'une ancienne forge oubliée au cœur des collines, renfermant des secrets oubliés depuis des siècles.")
        print("Alors que vous explorez ce territoire hostile, vous découvrez qu'une tribu ancestrale protège jalousement l'accès à la forge sacrée.")
        print("Une sentinelle solennelle s'approche de vous, évoquant des prophéties liées à un artefact ancien qui pourrait changer le destin des Terres de Fer.")
        print("Votre quête vous appelle à gravir les collines rocailleuses, à défier les vents furieux, et à affronter la tribu gardienne pour accéder à la forge légendaire.\n...")
        input("Serez-vous digne de manier le pouvoir du fer ancien enfoui dans les Terres de Fer?")

        print("\nAlors que vous gravissez les collines rocailleuses, la tribu gardienne des Terres de Fer se dresse devant vous.")
        print("Leurs guerriers portent des armures forgées avec une habileté remarquable, reflétant la maîtrise inégalée du fer par leur peuple.")
        print("Le chef de la tribu, une figure imposante, s'avance avec détermination, protégeant l'accès à la forge légendaire.")
        input("Vous êtes maintenant confronté à un choix difficile : affronter la tribu pour accéder à la forge ou chercher une solution pacifique.\n..."+Fore.RESET + Style.RESET_ALL)

        choix_combat_tribu = input(Fore.RED + Style.BRIGHT +"Voulez-vous affronter la tribu gardienne des Terres de Fer ? (Oui/Non) " + Fore.RESET + Style.RESET_ALL).lower()

        if choix_combat_tribu == "oui":
            print("Vous décidez de faire face à la tribu gardienne des Terres de Fer. Le combat est intense, chaque coup de lame résonnant dans les collines.")
            print("À mesure que vous triomphez, le respect et l'acceptation gagnent le cœur des guerriers de la tribu.")
            print("Le chef, admirant votre courage, vous accorde l'accès à la forge légendaire.")
            TerresDeFer = True
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

        else:
            print("Vous choisissez de ne pas combattre la tribu gardienne, optant plutôt pour une approche pacifique.")
            print("En utilisant votre diplomatie, vous parvenez à négocier un accord.")
            print("La tribu, impressionnée par votre sagesse, vous accorde l'accès à la forge sans violence.")
            print("Vous entrez dans la forge légendaire, portant le respect de la tribu comme un précieux trésor.")
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
    
    elif case == "Terres de Fer" and TerresDeFer:
        print("De retour dans les Terres de Fer, les collines rocailleuses et le souvenir de l'affrontement avec la tribu gardienne vous rappellent la maîtrise légendaire du fer.")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
# -----------------------------------------------------------------------------------------------------------------#

# -----------------------------------------------------------------------------------------------------------------#
    elif case == "Îles de l'Aurore":
        print("Vous êtes de retour sur les Îles de l'Aurore. Les plages familières, les arbres accueillants et le ciel aux teintes dorées vous rappellent le début de votre aventure.")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
# -----------------------------------------------------------------------------------------------------------------#

# -----------------------------------------------------------------------------------------------------------------#
    elif case == "Temple des Souvenirs" and not TempleDesSouvenirs:
        print(Fore.MAGENTA + Style.BRIGHT +"Le Temple des Souvenirs se dresse majestueusement au sommet d'une colline, ses colonnes anciennes et ses arches élégantes témoignant de sa grandeur passée.")
        print("L'air qui l'entoure semble imprégné de sagesse ancienne, et les murs de pierre racontent des histoires gravées par le temps.")
        input("Des lueurs mystiques flottent autour du temple, évoquant des souvenirs enfouis et des connaissances ancestrales.\n...")

        print("\nOn dit que le Temple des Souvenirs renferme une bibliothèque sacrée qui transcende le temps, où les souvenirs de chaque être vivant sont préservés.")
        print("Alors que vous franchissez les portes du temple, une énergie antique enveloppe votre esprit. Un gardien spectral, une entité éthérée, se présente à vous.")
        print("Le gardien vous informe que pour avancer dans votre quête, vous devez explorer les archives du temple et récupérer des fragments de mémoire dispersés.")
        print("Ces fragments renferment des indices cruciaux pour comprendre les énigmes à venir.")
        print("Aventurez-vous dans les couloirs du Temple des Souvenirs, découvrez les récits du passé, et dévoilez les mystères qui façonnent votre destin.")
        input("Serez-vous prêt à plonger dans les méandres du passé et à démêler les fils de la destinée dans ce lieu ancestral?\n...")

        print("\nAu fur et à mesure que vous explorez les archives du Temple des Souvenirs, une créature ancienne se réveille.")
        print("C'est une entité gardienne qui protège les secrets les plus profonds du temple.")
        print("Ses yeux brillent d'une lueur mystique, et son pouvoir semble connecté aux souvenirs et aux connaissances emmagasinés.")
        input("Vous êtes maintenant face à face avec cette créature éthérée, prête à défendre les mystères du temple.\n..."+Fore.RESET + Style.RESET_ALL)

        # Demande au joueur s'il veut affronter la créature du Temple des Souvenirs
        choix_combat_temple = input(Fore.RED + Style.BRIGHT +"Voulez-vous affronter la créature du Temple des Souvenirs ? (Oui/Non) "+ Fore.RESET + Style.RESET_ALL).lower()

        if choix_combat_temple == "oui":
            print("Vous décidez de défier la créature du Temple des Souvenirs. Le combat est intense, chaque attaque déchaînant des éclairs de mémoire.")
            print("À mesure que vous triomphez, la créature s'incline, reconnaissant votre force et votre volonté de percer les secrets du temple.")
            print("En vainquant la créature, vous gagnez l'accès aux parties les plus profondes du temple, où les véritables énigmes vous attendent.")
            TempleDesSouvenirs = True
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
        else:
            print("Vous choisissez de ne pas combattre la créature du Temple des Souvenirs, optant plutôt pour une approche pacifique.")
            print("En utilisant votre sagesse, vous parvenez à apaiser la créature, montrant que votre quête est guidée par la recherche de connaissance.")
            print("La créature, impressionnée par votre respect, vous guide vers les archives les plus profondes du temple, révélant des vérités enfouies.")
            print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
    elif case == "Temple des Souvenirs" and TempleDesSouvenirs:
        print("Rebonjour dans le Temple des Souvenirs ! Les colonnes majestueuses, les arches élégantes et les souvenirs de l'affrontement avec la créature ancienne reviennent à votre esprit.")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

# -----------------------------------------------------------------------------------------------------------------#

# -----------------------------------------------------------------------------------------------------------------#
    elif case == "Porte des Étoiles" and not PorteDesEtoiles:
        print(Fore.MAGENTA + Style.BRIGHT +"La Porte des Étoiles trône au cœur d'une clairière ensorcelante, son cadre ancien illuminé par des symboles célestes.")
        print("Des éclats de lumière stellaire scintillent autour d'elle, créant une ambiance empreinte de magie.")
        input("L'atmosphère de cet endroit transcende la réalité, invitant chacun à contempler le mystère des étoiles.\n...")

        print("\nLes murmures doux du vent résonnent entre les arbres environnants, ajoutant une touche de sérénité à ce lieu sacré.")
        input("Lorsque vous vous tenez devant la Porte des Étoiles, vous ressentez une connexion avec l'infini cosmique, une sensation de transcendance qui va au-delà des limites du tangible.\n...")

        print("\nC'est un endroit où le temps semble suspendu, où les étoiles offrent leur lumière bienveillante.")
        print("Vous avez également la possibilité de vous reposer à la belle étoile, allongé sur l'herbe douce de la clairière.")
        input("Que ce soit pour méditer, contempler les constellations ou simplement vous ressourcer dans la quiétude, la Porte des Étoiles vous invite à une expérience immersive au cœur de la magie céleste.\n..."+Fore.RESET + Style.RESET_ALL)
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
    
    elif case == "Porte des Étoiles" and PorteDesEtoiles:
        print("Vous vous tenez une fois de plus devant la Porte des Étoiles, la clairière mystique et les symboles célestes vous rappelant votre précédent passage.")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

# -----------------------------------------------------------------------------------------------------------------#

# -----------------------------------------------------------------------------------------------------------------#
    elif case == "Collines d'Azur" and not CollinesDazur:
        print("Les Collines d'Azur s'étendent à perte de vue, leurs pentes douces et verdoyantes baignées par la lumière douce du soleil.")
        print("Des fleurs sauvages égayent le paysage d'une palette de couleurs vives, créant une symphonie visuelle.")
        print("Des rivières cristallines serpentent entre les collines, apportant avec elles une mélodie apaisante.")
        print("L'air est empreint du parfum sucré des herbes sauvages, faisant de cet endroit un havre de paix au sein de la nature.")

        print("\nLes Collines d'Azur sont réputées pour leur beauté sereine et leurs secrets cachés.")
        print("Alors que vous explorez ces vastes étendues, un murmure mystique dans le vent éveille votre curiosité.")
        print("Les anciennes légendes racontent que ces collines renferment des énergies magiques, un pouvoir en harmonie avec la nature elle-même.")

        print("\nÀ mesure que vous gravissez les collines, une présence douce se fait sentir.")
        print("Un esprit bienveillant de la nature, un Gardien d'Azur, apparaît devant vous.")
        print("Il vous salue avec une aura apaisante, révélant que les collines sont un sanctuaire protégé.")
        print("Le Gardien d'Azur offre son savoir aux âmes respectueuses de la nature.")

        print("\nSoudain, votre intuition vous guide vers une clairière isolée.")
        print("Au creux d'un vieux chêne, vous découvrez un coffre secret.")
        print("Son bois est orné de symboles mystiques, et une énergie magique émane de son contenu.")
        print("Vous vous demandez quels trésors et secrets il pourrait renfermer.")

        # Découverte de la potion de défense
        print("À l'intérieur du coffre, vous trouvez une potion scintillante aux reflets azur.")
        print("Cette potion de défense semble dégager une aura protectrice.")
        print("Elle pourrait s'avérer utile dans les épreuves à venir. Que choisirez-vous de faire avec cette précieuse trouvaille?")
        joueur.add_item(defpotion)
        print(Fore.WHITE + Style.DIM + "Vous avez obtenu une potion de défence" + Fore.RESET + Style.RESET_ALL)

        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)
    
    elif case == "Collines d'Azur" and CollinesDazur:
        print("Vous vous retrouvez une fois de plus parmi les Collines d'Azur,")
        print(Fore.WHITE + Style.BRIGHT + "Votre aventure se poursuit. Dans quelle direction souhaitez-vous vous diriger?" + Fore.RESET + Style.RESET_ALL)

# -----------------------------------------------------------------------------------------------------------------#

# -----------------------------------------------------------------------------------------------------------------#
    
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


                    
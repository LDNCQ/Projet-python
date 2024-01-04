run = True
menu = True
play = False
rules = False

HP = 50
ATK = 3


def save():
    list = [
        name,
        str(HP),
        str(ATK)
    ]

    f = open("load.txt", "w")
    
    for item in list:
        f.write(item + "\n")
    f.close()

while run:
    while menu:
        print("1, Nouvelle Partie")
        print("2, Sauvegarder la partie")
        print("3, Règles")
        print("4, Quitter")
        
        if rules:
            print("Je suis le développeur du jeu et voici les règles")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")
        
        if choice == "1":
            name = input("# Quelle est votre prénom ? ")
            menu = False
            play = True
        elif choice == "2":
            f = open("load.txt", "r")
            load_list = f.readlines
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()



while play:
    save()
    
    
    dest = input('# ')
    
    if dest == "0":
        play = False
        menu = True       
        save()
        
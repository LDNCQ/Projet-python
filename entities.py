from items import *
import random

"""   
    name, max_hp, hp, atk, defense, xp, xp_until_lvlup, level
    p1.max_hp, p1.hp, p1.atk, p1.defense, p1.xp, p1.xp_until_lvlup, p1.level p1.inventory


    Pour créer une classe joueur
    p1 = Player("Joueur")
"""

    
class Entity:
    def __init__(self, name : str):
        self.name = name
        self.max_hp = 10
        self.hp = 10  # Commence avec la santé maximale
        self.atk = 5
        self.defense = 5

    def show_stats(self):
        print(f"Stats de {self.name}")
        print("------------")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Attaque: {self.atk}")
        print(f"Defense: {self.defense}")
        print(f"Niveau: {self.level}")
                
    def attack(self, target):
        crit_rate = 0.15
        if random.random() < crit_rate:
            damage = self.atk * 2.2
            print("Coup critique !")
        damage = max(0, self.atk - target.defense//3)
        print(damage)   #debugger damage == 0 
        target.hp -= damage
        
    def is_defeated(self):
        return self.hp <= 0
    
    
    def take_turn(self, target):
        pass
        
        
        
        
        
    #UTILISATION EXCEPTIONNELLE

    def change_maxhp(self, hp_amount):
        self.max_hp += hp_amount
        
        #Ajuster les hp si les hp max sont inférieurs aux hp
        if self.max_hp < self.hp:
            self.hp = self.max_hp
            
        if self.max_hp <= 0:
            self.max_hp = 1
            print("HP minimum atteint (1)")
        
    def change_hp(self, hp_amount):
        self.hp += hp_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        
        #A AJUSTER EN IMPLEMENTANT LE GAMEOVER
        if self.hp <= 0:
            game_over()
    
    
    def change_atk(self, atk_amount):
        self.atk += atk_amount
        if self.atk <= 0:
            self.afk = 1
            print("Attaque minimale atteinte (1)")
                
    def change_def(self, def_amount):
        self.defense += def_amount
        if self.defense <= 0:
            self.defense = 1
            print("Defense minimale atteinte (1)")



    
            
class Player(Entity):
    def __init__(self, name : str):
        super().__init__(name=name)
        self.level = 1
        self.xp = 0
        self.xp_until_lvlup = 20  # Valeur à ajuster selon votre logique de jeu
        self.inventory = []
        
    def level_up(self):
        self.max_hp += 6
        self.hp = self.max_hp
        self.atk += 4
        self.defense += 3
        self.xp_until_lvlup *= 1.6
        self.level += 1
        print(f"{self.name} a monté de niveau !")
        
    def show_stats(self):
        super().show_stats()
        print(f"XP: {self.xp}/{self.xp_until_lvlup}")
        self.show_inv()     
             
    def show_inv(self): 
        print("Inventaire :")
        for i in self.inventory:
            print(i.name) 

    
    def show_ennemy_stats(self, monster):
        print(f"Stats de {monster.name}")
        print("-----------")
        print(f"HP: Entre {monster.hp-random.randint(1,10)} et {monster.hp + random.randint(1, 14)}")
        print(f"Attaque : Entre {monster.atk-random.randint(1,5)} et {monster.atk + random.randint(1, 6)}")
        print(f"Défense : Entre {monster.defense-random.randint(1,5)} et {monster.defense + random.randint(1, 6)}")
        
         
    def add_item(self, item):
        self.inventory.append(item)
             
    """
    Potion de défense = defpotion
    Potion d'attaque = atkpotion
    Potion de heal = healpotion
    """
    
    def use_item(self, item):
        if isinstance(item, Items):
            if item in self.inventory:
                item.use(self)
                self.inventory.remove(item)
            else:
                print(f"{self.name} ne possède pas {item.name} dans son inventaire.")
        else:
            print("Cet objet ne peut pas être utilisé")
                
            

    def xp_gain(self, xp_gained):
        self.xp += xp_gained
        while self.xp >= self.xp_until_lvlup:
            self.level_up()
                    
            
            
            
            
            
    def start_combat(self, target):
        print(f"Vous entrez en combat contre {target.name}")
        #Boucle tour par tour
        while not target.is_defeated() and not self.is_defeated():
            self.take_turn(target)
            if not target.is_defeated():
                target.take_turn(self)
               
                
    def combat_use_item(self):
        if len(self.inventory) == 0:
            print("Vous ne possedez aucun objet")
        else:
            while True:
                try:
                    for i, item in enumerate(self.inventory):
                        print(f"{i}. {item.name}")
                    choice = int(input("Quel objet souhaitez vous utiliser ? "))
                    if 0 <= choice < len(self.inventory):
                        self.use_item(self.inventory[choice])
                        break
                    else:
                        print("Choix invalide. Veuillez entrer un numéro d'objet valide.")
                except ValueError:
                    print("Ce n'est pas un objet utilisable")
            
                
            
            
                
    def take_turn(self, target):
        
        while True:
            print("1. Attaque simple")
            print("2. Attaque spéciale (nom a modifier)")
            print("3. Utiliser un objet")
            print("4. Afficher ses statistiques")
            print("5. Afficher les statistiques de l'ennemi")
            print("6. Fuir le combat")
            
            try:
                action = int(input())
                
                if action == 1:
                    self.attack(target)
                    break
                    
                elif action == 2:
                    self.special_attack(target)
                    break
                    
                elif action == 3:
                    self.combat_use_item()
                    break
                    
                elif action == 4:
                    self.show_stats()
                    break
                
                elif action == 5:
                    self.show_ennemy_stats(target)
                    break
                
                
                elif action == 6:
                    print("Vous avez fui le combat.")
                    break
                    
                else:
                    print("Action invalide. Veuillez choisir une action valide.")
                    
                    
            except ValueError:                    
                print("Action invalide. Veuillez choisir une action valide.")
                
                
        
        
        
        
class Monster(Entity):
    def __init__(self, name:str):
        self.name = name
        self.level = joueur.level+(random.randint(0,5))
        self.atk = 5+self.level
        self.defense = 6+self.level
        self.max_hp = 15+self.level
        self.hp = self.max_hp
        
    def take_turn(self, target):
        self.attack(target)
        

joueur = Player("à changer au lancement du jeu")
            
    #def monster(self, name : str)
    #FAIRE FONCTION MONSTRE
        

        

    
    
    
         
    
    
    
    
    
    
    
    
    

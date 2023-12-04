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
            self.hp = 1
    
    
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
        print("Objets disponibles :")
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
                print(f"{self.name} a utilisé {item.name}")
            else:
                print(f"{self.name} ne possède pas {item.name} dans son inventaire.")
        else:
            print("Cet objet ne peut pas être utilisé")
                
    def xp_gain(self, xp_gained):
        self.xp += xp_gained
        while self.xp >= self.xp_until_lvlup:
            self.level_up()
                    
        
        
        
        
        
class Monster(Entity):
    def __init__(self, name:str):
        self.name = name
        self.level = 2
        self.atk = 5+self.level*1.8
        self.defense = 6+self.level*2
        self.max_hp = 15+self.level*6
        self.hp = self.max_hp
        
            
            
    #def monster(self, name : str)
    #FAIRE FONCTION MONSTRE
        

        

    
    
    
         
    
    
    
    
    
    
    
    
    

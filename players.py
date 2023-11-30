from items import *
class Entity:
    
    
    """   
    name, max_hp, hp, atk, defense, xp, xp_until_lvlup, level
    p1.max_hp, p1.hp, p1.atk, p1.defense, p1.xp, p1.xp_until_lvlup, p1.level
    """
    
    """
    Pour créer une classe joueur
    p1 = Entity
    p1.player(p1, "Joueur 1")
    """

    
    def player(self, name : str):
        self.name = name
        self.max_hp = 10
        self.hp = 10
        self.atk = 5
        self.defense = 5
        self.xp = 0
        self.xp_until_lvlup = 10
        self.level = 1
        self.inventory = []
        while self.xp >= self.xp_until_lvlup:
            self.level_up()
            
            
            
            
    #def monster(self, name : str, max_hp, hp, atk, defense)
    #FAIRE FONCTION MONSTRE
        

        
    def show_stats(self):
        print("Stats")
        print("------------")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Attaque: {self.atk}")
        print(f"Defense: {self.defense}")
        print(f"XP: {self.xp}/{self.xp_until_lvlup}")
        print(f"Level: {self.level}")
        print("Objets disponibles :")
        for i in self.inventory:
            print(i.name)

        
    def level_up(self):
        self.max_hp += 4
        self.hp = self.max_hp
        self.atk += 3
        self.defense += 3
        self.xp = 0
        self.xp_until_lvlup += 6
        self.level += 1
        print(f"{self.name} a gagné un niveau !")
        
    
    
    def xp_gain(self, xp_gained):
        self.xp += xp_gained
        while self.xp >= self.xp_until_lvlup:
            self.level_up()
         
    def add_item(self, item):
        self.inventory.append(item)
        
        
    """
    Potion de défense = defpotion
    Potion d'attaque = atkpotion
    Potion de heal = healpotion
    """  
    
    
    def use_item(self, item):
        if item in self.inventory:
            item.use(self)
            self.inventory.remove(item)
        else:
            print(f"{self.name} ne possède pas {item.name} dans son inventaire.")
            
    #test
            
    
    
    
    
    
    
    
    
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

    
    
            
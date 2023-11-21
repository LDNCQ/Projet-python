from items import *
class Entity:
    
    #name, max_hp, hp, atk, defense, xp, xp_until_lvlup, level
    #p1.max_hp, p1.hp, p1.atk, p1.defense, p1.xp, p1.xp_until_lvlup, p1.level
    
    def player(self, name : str, max_hp, hp, atk, defense, xp, xp_until_lvlup, level):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.xp = xp
        self.xp_until_lvlup = xp_until_lvlup
        self.level = level
        self.inventory = []
        while self.xp >= self.xp_until_lvlup:
            self.level_up()
            
    
    """def monster(self, name : str, max_hp, hp, atk, defense)"""
        

        
    def show_stats(self):
        print("Stats")
        print("------------")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Attaque: {self.atk}")
        print(f"Defense: {self.defense}")
        print(f"XP: {self.xp}/{self.xp_until_lvlup}")
        print(f"Level: {self.level}")
        print("Objets disponibles :")
        for i in range(len(self.inventory)):
            print(self.inventory[i].name)

        
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
        
        
    def use_item(self, item):
        if item in self.inventory:
            item.use(self)
            self.inventory.remove(item)
        else:
            print(f"{self.name} ne possède pas {item.name} dans son inventaire.")
            
    #test
            
    
    
    
    
    
    
    
    
    #UTILISATION EXCEPTIONNELLE

    def change_maxhp(self, hp_amount):
        self.max_hp -= hp_amount
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
            print("Defense minimale atteint (1)")

    
    
            
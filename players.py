class Player:
    #name, max_hp, hp, atk, defense, xp, xp_until_lvlup, level
    #p1.max_hp, p1.hp, p1.atk, p1.defense, p1.xp, p1.xp_until_lvlup, p1.level
    
    def __init__(self, name : str, max_hp, hp, atk, defense, xp, xp_until_lvlup, level):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.xp = xp
        self.xp_until_lvlup = xp_until_lvlup
        self.level = level
        
    def show_stats(self, max_hp, hp, atk, defense, xp, xp_until_lvlup, level):
        print("Stats")
        print("------------")
        print(f"HP : {hp}/{max_hp}")
        print(f"Attack : {atk}")
        print(f"Defense : {defense}")
        print(f"XP : {xp}/{xp_until_lvlup}")
        print(f"Level : {level}")

        
    def level_up(self, max_hp, hp, atk, defense, xp, xp_until_lvlup, level):
        self.max_hp += 4
        self.hp = self.max_hp
        self.atk += 3
        self.defense += 3
        self.xp = 0
        self.xp_until_lvlup += 6
        self.level += 1
        print("You leveled up !")
        
    
    
    def xp_gain(self, max_hp, hp, atk, defense, xp, xp_until_lvlup, level, xp_gained):
        self.xp += xp_gained
        if self.xp > self.xp_until_lvlup:
            self.xp = self.xp_until_lvlup
            self.level_up(max_hp, hp, atk, defense, xp, xp_until_lvlup, level)
            
    
    
    
    
    
    
    
    
    #UTILISATION EXCEPTIONNELLE
    def increase_maxhp(self, max_hp, hp_gained):
        self.max_hp += hp_gained
    
    def decrease_maxhp(self, max_hp, hp_lost):
        self.max_hp -= hp_lost
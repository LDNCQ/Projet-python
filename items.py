from players import *
      

class Items:
    def HealingPotion(self):
        self.stat_type = "hp"
        self.name = "Potion de Soin"
        self.stat_boost = 10
    
    def AttackPotion(self):
        self.stat_type = "atk"
        self.stat_name = "Attaque"
        self.name = "Potion d'Attaque"
        self.stat_boost = 5  # Augmentation d'attaque
        
    def DefensePotion(self):
        self.stat_type = "defense"
        self.stat_name = "Défense"
        self.name = "Potion de Défense"
        self.stat_boost = 4  # Augmentation de défense
        
    def use(self, player):
        self.player.stat_type += self.boost
        if player.hp > player.max_hp:
            player.hp = player.max_hp
        if self.stat_type == "hp":
            print(f"{player.name} a utilisé une {self.name} et a récupéré {self.stat_boost} points de vie.")
        else:
            print(f"{player.name} a utilisé une {self.name} et a gagné {self.stat_boost} points d'{self.stat_name}.")
            
            
    



  
healpotion = Items
healpotion.HealingPotion(healpotion)

atkpotion = Items
atkpotion.AttackPotion(atkpotion)

defpotion = Items
defpotion.DefensePotion(defpotion)







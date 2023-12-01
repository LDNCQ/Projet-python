from players import *
      
"""
class Items:
    def HealingPotion(self):
        self.stat_type = "hp"
        self.name = "Potion de Soin"
        self.stat_boost = 10 # Soin
    
    def AttackPotion(self):
        self.stat_type = "atk"
        self.name = "Potion d'Attaque"
        self.stat_boost = 5  # Augmentation d'attaque
        
    def DefensePotion(self):
        self.stat_type = "defense"
        self.name = "Potion de Défense"
        self.stat_boost = 4  # Augmentation de défense
        
    def use(player, item):
        value = getattr(player, item.stat_type)
        new_value = value + item.stat_boost
        setattr(player, item.stat_type, new_value)     
        if player.hp > player.max_hp:
            player.hp = player.max_hp
        if item.stat_type == "hp":
            print(f"{player.name} a utilisé une {item.name} et a récupéré {item.stat_boost} points de vie.")
        else:
            print(f"{player.name} a utilisé une {item.name} et a gagné {item.stat_boost} points d'{item.stat_name}.")
"""         



class Items:
    def use(self, player):
        pass  # Méthode générale pour l'utilisation des objets, à définir dans chaque sous-classe

class HealingPotion(Items):
    def __init__(self):
        self.name = "Potion de soin"
        self.stat_type = "hp"
        self.stat_boost = 10

    def use(self, player):
        value = getattr(player, self.stat_type)
        new_value = value + self.stat_boost
        setattr(player, self.stat_type, new_value)
        if player.hp > player.max_hp:
            player.hp = player.max_hp
        print(f"{player.name} a utilisé une {self.name} et a récupéré {self.stat_boost} points de vie.")
        
class AttackPotion(Items):
    def __init__(self):
        self.name = "Potion d'attaque"
        self.stat_type = "atk"
        self.stat_boost = 5

    def use(self, player):
        value = getattr(player, self.stat_type)
        new_value = value + self.stat_boost
        setattr(player, self.stat_type, new_value)
        print(f"{player.name} a utilisé une {self.name} et a gagné {self.stat_boost} points de d'attaque.")


class DefensePotion(Items):
    def __init__(self):
        self.name = "Potion de défense"
        self.stat_type = "defense"
        self.stat_boost = 4

    def use(self, player):
        value = getattr(player, self.stat_type)
        new_value = value + self.stat_boost
        setattr(player, self.stat_type, new_value)
        print(f"{player.name} a utilisé une {self.name} et a gagné {self.stat_boost} points de défense.")


healpotion = HealingPotion()

atkpotion = AttackPotion()

defpotion = DefensePotion()

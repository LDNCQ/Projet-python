from players import *

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

from players import *

class HealingPotion:
    def __init__(self):
        self.name = "Potion de Soin"
        self.healing_amount = 10  # Montant de guérison

    def use(self, player):
        player.hp += self.healing_amount
        if player.hp > player.max_hp:
            player.hp = player.max_hp
        print(f"{player.name} a utilisé une {self.name} et a récupéré {self.healing_amount} points de vie.")


class AttackPotion:
    def __init__(self):
        self.name = "Potion d'Attaque"
        self.attack_boost = 5  # Augmentation d'attaque

    def use(self, player):
        player.atk += self.attack_boost
        print(f"{player.name} a utilisé une {self.name} et a augmenté son attaque de {self.attack_boost} points.")


class DefensePotion:
    def __init__(self):
        self.name = "Potion de Défense"
        self.defense_boost = 4  # Augmentation de défense

    def use(self, player):
        player.defense += self.defense_boost
        print(f"{player.name} a utilisé une {self.name} et a augmenté sa défense de {self.defense_boost} points.")


healing_potion = HealingPotion()
attack_potion = AttackPotion()
defense_potion = DefensePotion()
        
    
    
    
    
    

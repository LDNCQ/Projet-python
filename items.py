from players import *

class Heal_potion:
    def __init__(self, heal):
        self.heal = 5
        
        
        
    def on_use(self, heal):  
        heal(hp, hp_healed)
        print("You used a healing potion !")
        



class Attack_boost_potion:
    def __init__(self):
      self.atk_boost = 4
        
    def on_use(self):
        increase_atk(atk, atk_gained)
        print("You used an attack potion !")
        
        
        
class Defense_boost_potion:
    def __init__(self, def_boost):
        self.def_boost = 4
    
    def on_use(self, def_boost):
        increase_def(defense, def_gained)
        print("You used a defense potion !")
        
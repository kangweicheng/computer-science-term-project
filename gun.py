import turtle,config
class gun:
    def __init__(self,name):
        self.item=turtle.Turtle()
        self.name=name
    def __str__(self):
        return self.name
    def attack(self,pos,dir,attack_ratio, owner_name):
        b = None
        if self.name=='Poor Gun':
            b=config.poor_gun(attack_ratio, pos, dir, owner_name)
        elif self.name=='Bomber':
            b=config.bomber(attack_ratio, pos, dir, owner_name)
        elif self.name=='Musket':
            b=config.musket(attack_ratio, pos, dir, owner_name)
        elif self.name=='Three Muskets':
            b=config.three_muskets(attack_ratio, pos, dir, owner_name)
        elif self.name=='Dart Goblin':
            b=config.dart_goblin(attack_ratio, pos, dir, owner_name)
        elif self.name=='Electro Wizard':
            b=config.electro_wizard(attack_ratio, pos, dir, owner_name)
        elif self.name=='Sparky':
            b=config.sparky(attack_ratio, pos, dir, owner_name)
        elif self.name=='Hunter':
            b=config.hunter(attack_ratio, pos, dir, owner_name)
        elif self.name=='Wizard':
            b=config.wizard(attack_ratio, pos, dir, owner_name)
        elif self.name=='Ice Wizard':
            b=config.ice_wizard(attack_ratio, pos, dir, owner_name)
        return b
    def __del__(self):
        return

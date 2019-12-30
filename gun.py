import turtle,config
class gun:
    def __init__(self,name):
        self.item=turtle.Turtle()
        self.name=name
    def __str__(self):
        return self.name
    def attack(self,pos,dir,attack_ratio):
        b = None
        if self.name=='Poor Gun':
            b=config.poor_gun(attack_ratio, pos, dir)
        if self.name=='Bomber':
            b=config.bomber(attack_ratio, pos, dir)
        if self.name=='Musket':
            b=config.musket(attack_ratio, pos, dir)
        if self.name=='Three Muskets':
            b=config.three_muskets(attack_ratio, pos, dir)
        if self.name=='Dart Goblin':
            b=config.dart_goblin(attack_ratio, pos, dir)
        if self.name=='Electro Wizard':
            b=config.electro_wizard(attack_ratio, pos, dir)
        if self.name=='Sparky':
            b=config.sparky(attack_ratio, pos, dir)
        if self.name=='Hunter':
            b=config.hunter(attack_ratio, pos, dir)
        if self.name=='Wizard':
            b=config.wizard(attack_ratio, pos, dir)
        if self.name=='Ice Wizard':
            b=config.ice_wizard(attack_ratio, pos, dir)
        return b
#    def hit_gun(self,player_pos):
#        gun_width=20
#        player_width=10
#        xr=(self.item.xcor-gun_width/2,self.item.xcor+gun_width/2)
#        yr=(self.item.ycor-gun_width/2,self.item.ycor+gun_width/2)
#        if player_pos[0]+player_width>=xr[0] or player_pos[0]-player_width<=xr[1] or player_pos[1]+player_width>=yr[0] or player_pos[1]-player_width<=yr[1]:
#            return True
#    def hit_bullet(self,player_pos):
#        bullet_width=20
#        player_width=10
#        xr=(self.item.xcor-bullet_width/2,self.item.xcor+bullet_width/2)
#        yr=(self.item.ycor-bullet_width/2,self.item.ycor+bullet_width/2)
#        if player_pos[0]+player_width>=xr[0] or player_pos[0]-player_width<=xr[1] or player_pos[1]+player_width>=yr[0] or player_pos[1]-player_width<=yr[1]:
#            return True
    def __del__(self):
        return
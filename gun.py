import turtle,config
class gun:
    def __init__(self,name):
        self.item=turtle.Turtle()
        self.name=name
    def __str__(self):
        return self.name
    def attack(self,pos,dir):
        if self.name=='Poor Gun':
            b=config.bpoor_gun
        if self.name=='Bomber':
            b=config.bbomber
        if self.name=='Musket':
            b=config.bmusket
        if self.name=='Three Muskets':
            b=config.bthree_muskets
        if self.name=='Dart Goblin':
            b=config.bdart_goblin
        if self.name=='Electro Wizard':
            b=config.belectro_wizard
        if self.name=='Sparky':
            b=config.bsparky
        if self.name=='Hunter':
            b=config.bhunter
        if self.name=='Wizard':
            b=config.bwizard
        if self.name=='Ice Wizard':
            b=config.bice_wizard
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
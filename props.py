import turtle,random
class props:
    def __init__(self,):#props_gif
        self.item=turtle.Turtle()
        self.item.penup()
        self.item.setposition(random.randint(-250,250),random.randint(-250,250))
        prob=random.randint(1,3)
        if prob==1:
            self.type='defense'
        elif prob==2:
            self.type='attack'
        else:
            self.type='heal'
        prob=random.randint(1,6)
        if prob==1:
            self.ratio=2000 if self.type=='HEAL' else 0.2
        elif prob==2 or prob==3:
            self.ratio=1500 if self.type=='HEAL' else 0.15
        else:
            self.ratio=1000 if self.type=='HEAL' else 0.1
    def hit_prop(self,player_pos):#center to front
        props_width=20 #undetermined
        player_width=10
        xr=(self.item.xcor-props_width/2,self.item.xcor+props_width/2)
        yr=(self.item.ycor-props_width/2,self.item.ycor+props_width/2)
        if player_pos[0]+player_width>=xr[0] or player_pos[0]-player_width<=xr[1] or player_pos[1]+player_width>=yr[0] or player_pos[1]-player_width<=yr[1]:
            return True #I can't del self here, please do it in __main__.
    def __str__(self):
        return self.type
    def __del__(self):
        return

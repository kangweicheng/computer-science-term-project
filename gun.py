import turtle
class gun:
    '''
    name
    cd:countdown time
    nop:number of projectiles
    dop:damage of one projectile
    rop:radius of projectiles
    rod:radius of damage
    ang:spreading angle
    eff:special effects('Electrify':stuck for 1s,'Panic':keyboard go out of order for 2s,'Freeze':slowed down 50% for 5s)
    gun_gif:image of the gun
    bul_gif:image of bullets
    traj_col:color of trajectories
    ----------------------------------------------
    gun('Poor Gun',1.5,1,600,120,20,0,None,'dark grey')
    gun('Bomber',3,1,400,140,20,0,'Panic','orange')
    gun('Musket',1.1,1,1600,140,20,0,None,'plum')
    gun('Three Muskets',3,3,1600,140,20,30,None,'plum')
    gun('Dart Goblin',0,3,1000,180,20,0,None,'lawn green')
    gun('Electro Wizard',2.2,1,300,110,20,0,'Electrify','light sky blue')
    gun('Sparky',6,1,2500,90,20,0,None,'yellow')
    gun('Hunter',2.2,7,850,110,20,90,None,'slate grey')
    gun('Wizard',1.6,1,1000,140,50,0,None,'salmon')
    gun('Ice Wizard',2.2,1,400,110,20,0,'Freeze','azure')
    '''
    def __init__(self,name,cd,nop,dop,rop,rod,ang,eff,traj_col):#gun_gif,bul_gif
        self.item=turtle.Turtle()
        self.name=name
        self.cd=cd
        self.nop=nop
        self.dop=dop
        self.rop=rop
        self.rod=rod
        self.ang=ang
        self.eff=eff
        self.traj_col=traj_col
    def __str__(self):
        return self.name
    def attack(self,pos,dir):
        if self.nop==1:
            b=turtle.Turtle()
            b.penup()
            b.setposition(pos)
            b.pendown()
            if self.eff=='Electrify':
                b.speed(0)
                b.setheading(dir-10)
                b.pensize(self.rod*0.2)
                b.shape()
                b.pencolor(self.traj_col)
                while b.distance(before)<self.rop:
                    b.lt(30)
                    b.forward(10)
                    if b.distance(before)>=self.rop:
                        break
                    b.rt(30)
                    b.forward(10)
            else:
                b.setheading(dir)
                b.pensize(self.rod*0.5)
                if self.eff=='Freeze':
                    b.shape()
                    b.pencolor(self.traj_col)
                elif self.eff=='Panic':
                    b.shape('fireball.gif')
                    b.pencolor(self.traj_col)
                else:
                    if self.name=='Sparky':
                        b.speed(0)
                    b.shape()
                    b.pencolor(self.traj_col)
                while b.distance(pos)<self.rop:
                    b.forward(1)
            b.clear()
            b.hideturtle()
            del b
        else:
            middle=(self.nop-1)/2
            step_ang=self.ang/(self.nop-1)
            for i in range(self.nop):
                b=turtle.Turtle()
                b.penup()
                b.setposition(pos)
                b.pendown()
                b.setheading(dir+(middle-i)*step_ang)
                b.pensize(self.rod*0.5)
                b.shape()
                b.pencolor(self.traj_col)
                while b.distance(pos)<self.rop:
                    b.forward(1)
                b.clear()
                b.hideturtle()
                del b
    def hit_gun(self,player_pos):
        gun_width=20
        player_width=10
        xr=(self.item.xcor-gun_width/2,self.item.xcor+gun_width/2)
        yr=(self.item.ycor-gun_width/2,self.item.ycor+gun_width/2)
        if player_pos[0]+player_width>=xr[0] or player_pos[0]-player_width<=xr[1] or player_pos[1]+player_width>=yr[0] or player_pos[1]-player_width<=yr[1]:
            return True
    def hit_bullet(self,player_pos):
        bullet_width=20
        player_width=10
        xr=(self.item.xcor-bullet_width/2,self.item.xcor+bullet_width/2)
        yr=(self.item.ycor-bullet_width/2,self.item.ycor+bullet_width/2)
        if player_pos[0]+player_width>=xr[0] or player_pos[0]-player_width<=xr[1] or player_pos[1]+player_width>=yr[0] or player_pos[1]-player_width<=yr[1]:
            return True
    def __del__(self):
        return
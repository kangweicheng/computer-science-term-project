import turtle
class bullet:
    '''
    name
    cd:countdown time
    nop:number of projectiles
    damage:damage of one projectile
    rop:radius of projectiles
    rod:radius of damage
    ang:spreading angle
    '''
    def __init__(self,name,cd,nop,damage,rop,rod,ang,bul_gif,attack_ratio, pos, dir, affect_time, kill_self_callback=None, owner=None):
        self.affect_time=affect_time
        self.over = False
        self.isDeleted = False
        self.screen = turtle.getscreen()
        self.screen.tracer(0)
        self.owner = owner
        if nop==1:
            self.items=[turtle.Turtle()]
            self.items[0].speed(0)
            if name=='Electro Wizard':
                self.items[0].shape(bul_gif)
                self.items[0].color('gold')
#                self.items[0].turtlesize(1,1,1)
            else:
                self.items[0].shape(f'{bul_gif}-{str(dir)}.gif')
        else:
            if name=='Three Muskets':
                middle=1
            else:
                middle=3
            self.items=[turtle.Turtle() for i in range(nop)]
            for i,t in enumerate(self.items):
                if i%2==1:
                    i=-(i+1)
                angle=int((dir+15*(i/2))%360)
                t.speed(0)
                t.shape(f'{bul_gif}-{str(angle)}.gif')
        self.name=name
        self.cd=cd
        self.nop=nop
        self.damage=damage
        self.rop=rop*nop
        self.rod=rod
        self.ang=ang
        
        self.ratio = 10
        self.attack=attack_ratio
        self.pos = pos
        if name=='Electro Wizard':
            self.dir = dir-35
        else:
            self.dir=dir
        self.move_distance = 0

        if name=='Sparky':
            self.speed=300
        elif name=='Electro Wizard':
            self.speed=350
        else:
            self.speed = 150
        self.step_time = 50 # milliseconds
        self.step=self.speed*self.step_time/1000

        self.delete_callback = None

        self.initBulletAngle()
        self.screen.update()
        self.screen.tracer(1)
        self.routinely_move()
    # this function is to initialized angle of each bullet
    def initBulletAngle(self):
        if self.nop == 1:
            step_ang = 0
            middle = 0
        else:
            middle=(self.nop-1)/2
            step_ang=self.ang/(self.nop-1)
        for i,t in enumerate(self.items):
            if i%2==1:
                i=-(i+1)
            t.penup()
            t.setposition(self.pos)
            t.setheading(int((self.dir+15*(i/2))%360))
    # this method is responsible for move the bullets routinely
    def routinely_move(self):
        if not self.over:
            self.move()
            if self.move_distance < self.rop:
                self.screen.ontimer(self.routinely_move, self.step_time)
            else:
                self.deleteBullet()
                self.delete_callback(self)
    def move(self):
        if self.name=='Electro Wizard':
            print(self.items)
            self.items[0].pendown()
            self.items[0].pensize(self.rod*0.5)
            self.items[0].pencolor('gold')
        if not (self.over or self.isDeleted):
            if self.nop == 1:
                if self.name=='Electro Wizard':
                    self.items[0].lt(70)
                    self.items[0].fd(self.step/2)
                    self.items[0].rt(70)
                    self.items[0].fd(self.step/2)
                    self.move_distance += self.step
                elif self.name=='Sparky':
                    if self.move_distance<=self.step:
                        self.items[0].fd(self.step*0.5)
                        self.move_distance += self.step*0.5
                        if self.move_distance==self.step:
                            self.items[0].hideturtle()
                    else:
                        self.items[0].fd(self.step)
                        self.move_distance += self.step
                else:
                    self.items[0].fd(self.step)
                    self.move_distance += self.step
            else:
                for t in self.items:
                    t.fd(self.step*3)
                    self.move_distance += self.step*3
    def setDeleteCallback(self, callback):
        self.delete_callback = callback
    # remove all bullets objects
    def deleteBullet(self):
        self.isDeleted = True
        for t in self.items:
            #print('instance')
            #print(t)
            t.clear()
            t.hideturtle()
            del t
    # remove one object
    def deleteItem(self, item):
        #print(self.items)
        
        #print(index)
        try:
            index = self.items.index(item)
            self.items[index].clear()
            self.items[index].hideturtle()
            del self.items[index]
        except:
            print('except')



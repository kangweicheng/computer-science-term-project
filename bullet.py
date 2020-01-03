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
            elif name=='Bomber':
                self.items[0].shape(bul_gif)
                self.items[0].color('black')
            else:
                self.items[0].shape(f'{bul_gif}-{str(dir)}.gif')
        else:
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
        self.step_time = 20 # milliseconds
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
            for t in self.items:
                t.pendown()
                t.pensize(self.rod*0.5)
                t.pencolor('gold')
        if not (self.over or self.isDeleted):
            for t in self.items:
                if self.nop == 1:
                    if self.name=='Electro Wizard':
                        t.lt(70)
                        t.fd(self.step/2)
                        t.rt(70)
                        t.fd(self.step/2)
                        self.move_distance += self.step
                    elif self.name=='Sparky':
                        if self.move_distance<=self.step:
                            t.fd(self.step*0.5)
                            self.move_distance += self.step*0.5
                            if self.move_distance==self.step:
                                t.hideturtle()
                        else:
                            t.fd(self.step)
                            self.move_distance += self.step
                    else:
                        t.fd(self.step)
                        self.move_distance += self.step
                else:
                    t.fd(self.step*3)
                    self.move_distance += self.step*3
    def setDeleteCallback(self, callback):
        self.delete_callback = callback
    # remove all bullets objects
    def deleteBullet(self):
        print(self.items)
        self.isDeleted = True
        for t in self.items:
            if self.name=='Bomber':
                for i in range(24):
                    t.shape(f'{i}.gif')
            elif self.name=='Sparky':
                t.showturtle()
            #print('instance')
            #print(t)
            t.clear()
            t.hideturtle()
            del t
    # remove one object
    def deleteItem(self, item):
        try:
            for t in self.items:
                if self.name=='Bomber':
                    self.step=0
                    for i in range(24):
                        t.shape(f'{i}.gif')
                elif self.name=='Sparky':
                    t.showturtle()
            index = self.items.index(item)
            self.items[index].clear()
            self.items[index].hideturtle()
            del self.items[index]
        except:
            print('except')



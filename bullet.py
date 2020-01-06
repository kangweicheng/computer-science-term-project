import turtle, time
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
    def __init__(self,name,cd,nop,damage,rop,rod,ang,bul_gif,attack_ratio, pos, dir, affect_time, kill_self_callback=None, owner=None, map=None):
        self.affect_time=affect_time
        self.over = False
        self.isDeleted = False
        self.screen = turtle.getscreen()
        self.screen.tracer(0)
        self.owner = owner
        self.item_len=None
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
            self.item_len = 1
        else:
            self.item_len = nop
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
        
        self.map = map
        self.ratio = 10
        self.attack=attack_ratio
        self.pos = pos
        if name=='Electro Wizard':
            self.dir = dir-35
        else:
            self.dir=dir
        self.move_distance = 0

        if name=='Sparky':
            self.speed=600
        elif name=='Electro Wizard':
            self.speed=1000
        else:
            self.speed = 200
        self.step_time = 10 # milliseconds
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
            if self.move_distance < self.rop and (not self.isDeleted):
                self.screen.ontimer(self.routinely_move, self.step_time)
            else:
                self.deleteBullet()
                if self.delete_callback:
                    self.delete_callback(self)
    def addMap(self, map):
        self.map = map
    def move(self):
        # self.screen.tracer(0)
        # print('step', self.step)
        if self.name=='Electro Wizard':
            for t in self.items:
                if t:
                    t.pendown()
                    t.pensize(self.rod*0.4)
                    t.pencolor('gold')
        if not (self.over or self.isDeleted):
            for t in self.items:
                if t:
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
        # if self.map:
        #     self.map.updateBullets()
        #     self.map.bulletHitPlayers()
        # self.screen.update()
        # self.screen.tracer(1)
            # print('final')
    def setDeleteCallback(self, callback):
        self.delete_callback = callback
    # remove all bullets objects
    def deleteBullet(self):
        self.isDeleted = True
        for t in range(len(self.items)):
            if self.items[t]:
                if self.name=='Bomber':
                    self.step = 0
                    for i in range(24):
                        self.items[t].shape(f'{i}.gif')
                elif self.name=='Sparky':
                    self.step = 0
                    self.items[t].showturtle()
                    for i in range(24,54):
                            self.items[t].shape(f'{i}.gif')
                self.deleteItem(self.items[t])

    # remove one object
    def deleteItem(self, item):
        print('delete')
        if item:
            for t in self.items:
                if t:
                    if self.name=='Electro Wizard':
                        self.step = 0
                        t.pencolor('white')
                    elif self.name=='Bomber':
                        self.step = 0
                        for i in range(24):
                            t.shape(f'{i}.gif')
                    elif self.name=='Sparky':
                        self.step = 0
                        t.showturtle()
                        for i in range(24,54):
                            t.shape(f'{i}.gif')

            index = self.items.index(item)
            self.removeTurtleFromScreen(item)
            item.hideturtle()
            item.clear()
            self.items[index]=None
            self.item_len -= 1
            if self.item_len == 0:
                self.isDeleted = True
                if self.delete_callback:
                    self.delete_callback(self)
        # except:
        #     print('except')
    def removeTurtleFromScreen(self, turtle):
        # try:
            index = self.screen.turtles().index(turtle)
            del self.screen.turtles()[index]
        # except:
        #     print('except when removeTurtleFromScreen in bullet.py')



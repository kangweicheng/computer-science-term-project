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
    eff:special effects('Electrify':stuck,'Panic':keyboard out of order,'Freeze':slowed down)
    '''
    def __init__(self,name,cd,nop,damage,rop,rod,ang,eff,traj_col,bul_gif,attack_ratio, pos, dir, affect_time, kill_self_callback=None, owner=None):
        self.affect_time=affect_time
        self.over = False
        self.screen = turtle.getscreen()
        self.screen.tracer(0)
        self.owner = owner
        if nop==1:
            self.items=[turtle.Turtle()]
            self.items[0].speed(0)
            self.items[0].shape(f'{bul_gif}-{str(dir)}.gif')
        else:
            if name=='Three Muskets':
                middle=1
            else:
                middle=3
            self.items=[turtle.Turtle() for i in range(nop)]
            for i,t in enumerate(self.items):
                if dir==0 and i>middle:
                    angle=360-15*(i-middle)
                else:
                    angle=dir-15*(i-middle)
                t.speed(0)
                t.shape(f'{bul_gif}-{str(angle)}.gif')
        self.name=name
        self.cd=cd
        self.nop=nop
        self.damage=damage
        self.rop=rop
        self.rod=rod
        self.ang=ang
        
        self.ratio = 10
        self.attack=attack_ratio
        self.pos = pos
        self.dir = dir
        self.move_distance = 0

        self.speed = 100
        self.step_time = 100 # milliseconds
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
            t.penup()
            t.setposition(self.pos)
            t.setheading(self.dir+(middle-i)*step_ang)
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
        if self.nop == 1:
            if self.name=='Electro Wizard':
                self.items[0].lt(10)
                self.items[0].fd(self.step/2)
                self.items[0].rt(10)
                self.items[0].fd(self.step/2)
                self.move_distance += self.step
            else:
                for t in self.items:
                    t.fd(self.step)
                    self.move_distance += self.step
        else:
            for t in self.items:
                t.fd(self.step)
                self.move_distance += self.step
    def setDeleteCallback(self, callback):
        self.delete_callback = callback
    # remove all bullets objects
    def deleteBullet(self):
        for t in self.items:
            print('instance')
            print(t)
            t.clear()
            t.hideturtle()
            del t
    # remove one object
    def deleteItem(self, item):
        print(self.items)
        index = self.items.index(item)
        print(index)
        try:
            self.items[index].clear()
            self.items[index].hideturtle()
            del self.items[index]
        except:
            print('except')



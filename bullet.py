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
    eff:special effects('Electrify':stuck,'Panic':keyboard out of order,'Freeze':slowed down 50%)
    bul_gif:image of bullets
    traj_col:color of trajectories
    ----------------------------------------------
    bpoor_gun=bullet.bullet('Poor Gun',1.5,1,600,120,20,0,None,'dark grey','poor_gun.gif')
    bbomber=bullet.bullet('Bomber',3,1,400,140,20,0,'Panic','orange','fireball.gif')
    bmusket=bullet.bullet('Musket',1.1,1,1600,140,20,0,None,'plum','poor_gun.gif')
    bthree_muskets=bullet.bullet('Three Muskets',3,3,1600,140,20,30,None,'plum','poor_gun.gif')
    bdart_goblin=bullet.bullet('Dart Goblin',0,3,1000,180,2,0,None,'lawn green','poor_gun.gif')
    belectro_wizard=bullet.bullet('Electro Wizard',2.2,1,300,110,20,0,'Electrify','light sky blue','electrify.gif')
    bsparky=bullet.bullet('Sparky',6,1,2500,90,20,0,None,'yellow','electrify.gif')
    bhunter=bullet.bullet('Hunter',2.2,7,850,110,20,90,None,'slate grey','poor_gun.gif')
    bwizard=bullet.bullet('Wizard',2.2,1,1000,140,50,0,None,'salmon','wizard.gif')
    bice_wizard=bullet.bullet('Ice Wizard',2.2,1,400,110,20,0,'Freeze','azure','snowball.gif')
    '''
    def __init__(self,name,cd,nop,damage,rop,rod,ang,eff,traj_col,bul_gif,attack_ratio, pos, dir, affect_time, kill_self_callback=None, owner=None):
        self.affect_time=affect_time
        self.over = False
        self.screen = turtle.getscreen()
        self.screen.tracer(0)
        self.owner = owner
        if nop==1:

            self.items=[turtle.Turtle()]
            if name=='Electro Wizard' or name=='Sparky':
                self.items[0].speed(0)
            else:
                self.items[0].speed(8)
            self.items[0].pensize(rod*0.2)
            if bul_gif=='snowball.gif' or bul_gif=='electrify.gif' or bul_gif=='fireball.gif' or bul_gif=='poor_gun.gif':
                self.items[0].shape(bul_gif[:-4]+'-'+str(dir)+'.gif')
            else:
                self.items[0].shape(bul_gif)
            # self.items.hideturtle()
            # self.items.penup()
        else:
            self.items=[turtle.Turtle() for i in range(nop)]
            for t in self.items:
                t.pensize(rod*0.2)
                t.shape(bul_gif)
        self.name=name
        self.cd=cd
        self.nop=nop
        self.damage=damage
        self.rop=rop
        self.rod=rod
        self.ang=ang
        self.eff=eff
        self.traj_col=traj_col
        #################################
        # new attr
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
                self.items.lt(10)
                self.fd(self.step/2)
                self.items.rt(10)
                self.fd(self.step/2)
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



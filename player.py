import turtle,config,gun,math,bullet
class player(turtle.Turtle):
    def __init__(self,pos,name,dir,gif_head,bar_on_left_or_right, blood_empty_callback = None):
        self.over = False
        self.effect=None
        self.original_image=gif_head
        super().__init__()
        self.dir=dir
        self.image=gif_head
        self.penup()
        self.setposition(pos)
        self.penup()
        self.setheading(dir)
        self.original_pos=pos
        self.blood_empty_callback = blood_empty_callback
        # self.pos=list(pos)
        self.name=name
        self.attack=1
        self.hp=config.hpmax
        self.defense=1
        self.gun=config.POOR_GUN()
        self.bar=turtle.Turtle()
        self.bar.width(5)
        self.bar.pencolor('black')
        self.bar.hideturtle()
        self.trueblood=turtle.Turtle()
        self.trueblood.color('black','red')
        self.trueblood.width(5)
        self.trueblood.hideturtle()
        self.bar_on_left_or_right=bar_on_left_or_right
        self.bar.penup()
        self.trueblood.penup()
        if bar_on_left_or_right=='left':
            self.bar.setposition(-config.MAP_SIZE[0]/2-50,config.MAP_SIZE[1]/2+config.bar_height+50)
            self.trueblood.setposition(-config.MAP_SIZE[0]/2-50,config.MAP_SIZE[1]/2+config.bar_height+50)
            self.bar.write(self.name,False,'left',font=("Arial", 25, "normal"))
        else:
            self.bar.setposition(config.MAP_SIZE[0]/2+50,config.MAP_SIZE[1]/2+config.bar_height+50)
            self.trueblood.setposition(config.MAP_SIZE[0]/2+50,config.MAP_SIZE[1]/2+config.bar_height+50)
            self.bar.write(self.name,False,'right',font=("Arial", 25, "normal"))
            self.bar.back(config.bar_width)
        self.screen = turtle.getscreen()

        self.display_bar()
        self.bar.pendown()
        self.trueblood.pendown()
        self.bar.fd(config.bar_width)
        self.bar.rt(90)
        self.bar.fd(config.bar_height)
        self.bar.rt(90)
        self.bar.fd(config.bar_width)
        self.bar.rt(90)
        self.bar.fd(config.bar_height)
    def display_bar(self):
        if not self.over:
            self.screen.tracer(0)
            self.trueblood.clear()
            self.screen.update()
            self.trueblood.begin_fill()
            self.trueblood.speed(0)
            if self.bar_on_left_or_right=='left':
                self.trueblood.penup()
                self.trueblood.setposition(-config.MAP_SIZE[0]/2-50,config.MAP_SIZE[1]/2+config.bar_height+50)
                self.trueblood.setheading(0)
                self.trueblood.pendown()
                self.trueblood.write(f'槍名: {str(self.gun)}',False,'right',("Arial", 14, "normal"))
                self.trueblood.fd(self.hp*config.bar_width/config.hpmax)
                self.trueblood.rt(90)
                self.trueblood.fd(config.bar_height)
                self.trueblood.rt(90)
                self.trueblood.fd(self.hp*config.bar_width/config.hpmax)
                self.trueblood.write(f'血量: {self.hp}',False,'right',font=("Arial", 14, "normal"))
                self.trueblood.rt(90)
                self.trueblood.fd(config.bar_height)
                self.trueblood.penup()
                self.trueblood.setheading(270)
                self.trueblood.fd(55)
                self.trueblood.write(f'攻擊加成: {(self.attack-1)*100}%',False,'right',("Arial", 14, "normal"))
                self.trueblood.fd(25)
                self.trueblood.write(f'減低傷害: {(1-self.defense)*100}%',False,'right',("Arial", 14, "normal"))
                self.trueblood.rt(180)
                self.trueblood.fd(80)
                self.trueblood.rt(90)
                self.trueblood.pendown()
            else:
                self.trueblood.penup()
                self.trueblood.setposition(config.MAP_SIZE[0]/2+50,config.MAP_SIZE[1]/2+config.bar_height+50)
                self.trueblood.pendown()
                self.trueblood.write(f'槍名: {str(self.gun)}',False,'left',("Arial", 14, "normal"))
                self.trueblood.setheading(180)
                self.trueblood.fd(self.hp*config.bar_width/config.hpmax)
                self.trueblood.lt(90)
                self.trueblood.fd(config.bar_height)
                self.trueblood.lt(90)
                self.trueblood.fd(self.hp*config.bar_width/config.hpmax)
                self.trueblood.write(f'血量: {self.hp}',False,'left',font=("Arial", 14, "normal"))
                self.trueblood.lt(90)
                self.trueblood.fd(config.bar_height)
                self.trueblood.penup()
                self.trueblood.setheading(270)
                self.trueblood.fd(55)
                self.trueblood.write(f'攻擊加成: {(self.attack-1)*100}%',False,'left',("Arial", 14, "normal"))
                self.trueblood.fd(25)
                self.trueblood.write(f'減低傷害: {(1-self.defense)*100}%',False,'left',("Arial", 14, "normal"))
                self.trueblood.rt(180)
                self.trueblood.fd(80)
                self.trueblood.pendown()
            self.trueblood.end_fill()
            self.screen.update()
            self.screen.tracer(1)
            self.screen.ontimer(self.display_bar, 2000)
    def setheading(self,ang):
        if self.effect=='burnt':
            ang+=180
            ang%=360
        self.seth(ang)
        self.shape(self.image+f'-{ang}.gif')
        self.dir=ang
    def fd(self,dis):
        self.original_pos=self.position()
        self.forward(dis)
    def get_prop(self,other):
        if isinstance(other,gun.gun):
            self.gun=other
        elif str(other)=='defense':
            self.defense-=other.ratio
        elif str(other)=='heal':
            self.hp+=other.ratio
        else:
            self.attack+=other.ratio
    def hit(self,other):
        if isinstance(other,bullet.bullet):
            self.hp -= other.damage*other.attack*self.defense
            if other.name=='Bomber':
                self.image=self.original_image+'_burnt'
                self.shape(self.image+f'-{self.dir}.gif')
                self.effect='burnt'
                self.screen.ontimer(self.change_to_original_image,other.affect_time*1000)
            if other.name=='Ice Wizard':
                self.image=self.original_image+'_frozen'
                self.shape(self.image+f'-{self.dir}.gif')
                self.effect='frozen'
                self.screen.ontimer(self.change_to_original_image,other.affect_time*1000)
            if other.name=='Electro Wizard':
                self.image=self.original_image[:-1]+'_electrified'
                self.shape(self.image+f'-{self.dir}.gif')
                self.effect='electrified'
                self.screen.ontimer(self.change_to_original_image,other.affect_time*1000)
        elif type(other) == int:
            self.hp -= other
        else:
            self.hp -= other.damage*self.defense
        if self.hp <= 0:
            self.blood_empty_callback(self)
        return None

    def shoot(self):
        print(self.dir)
        return self.gun.attack(self.pos(),self.dir,self.attack, self.name)

    def change_to_original_image(self):
        self.image=self.original_image
        self.effect=None

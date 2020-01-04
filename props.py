import turtle,random,config
import datetime
class props(turtle.Turtle):
    def __init__(self,pos):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(pos)
        self.vanishTime = datetime.datetime.now() + datetime.timedelta(seconds = 15)
        if random.randint(1,3)==1:
            option=[('defense','DEF+'),('attack','ATK+'),('heal','HEAL')]
            t,s=random.choice(option)
            self.type=t
            option=[(2000,0.15,'30'),(1500,0.1,'25'),(1000,0.05,'20')]
            ch=random.choices(option,[1,2,3])[0]
            self.shape(s+ch[2]+'.gif')
            self.ratio=ch[0] if self.type=='heal' else ch[1]
        else:
            g=random.choice(config.GUN_LIST)()
            self.type='gun'
            self.object = g
            print(g)
            self.shape(f'{str(self.object)}.gif')
        self.showturtle()
    def deleteSelf(self):
        self.clear()
        self.hideturtle()
    def __str__(self):
        return self.type
    def __del__(self):
        return
if __name__=='__main__':
    turtle.addshape('ATK+.gif')
    turtle.addshape('DEF+.gif')
    turtle.addshape('HEAL.gif')
    p=props((0,0))
    print(p)

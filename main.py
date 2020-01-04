import turtle
from datetime import timedelta, datetime
import random
import time
import gun


def initScreen():
	screen = turtle.Screen()
	screen.register_shape("rect", ((-5, -5), (5, -5), (5,5), (-5, 5)))
	screen.screensize(1000, 1000)
	screen.setworldcoordinates(-300,-300,300,300)
	return screen


screen = initScreen()
for i in range(24):
	screen.addshape(f'poor_gun-{15*i}.gif')
	screen.addshape(f'{i}.gif')
for i in range(4):
        screen.addshape(f'dart-{90*i}.gif')
        screen.addshape(f'fireball-{90*i}.gif')
        screen.addshape(f'snowball-{90*i}.gif')
        screen.addshape(f'electrify-{90*i}.gif')
        screen.addshape(f'player1-{90*i}.gif')
        screen.addshape(f'player2-{90*i}.gif')
        screen.addshape(f'player1_burnt-{90*i}.gif')
        screen.addshape(f'player2_burnt-{90*i}.gif')
        screen.addshape(f'player1_hurt-{90*i}.gif')
        screen.addshape(f'player2_hurt-{90*i}.gif')
        screen.addshape(f'player1_frozen-{90*i}.gif')
        screen.addshape(f'player2_frozen-{90*i}.gif')
        screen.addshape(f'player_electrified-{90*i}.gif')
screen.addshape('ATK+.gif')
screen.addshape('DEF+.gif')
screen.addshape('HEAL.gif')
screen.addshape('Poor Gun.gif')
screen.addshape('Bomber.gif')
screen.addshape('Musket.gif')
screen.addshape('Three Muskets.gif')
screen.addshape('Dart Goblin.gif')
screen.addshape('Sparky.gif')
screen.addshape('Electro Wizard.gif')
screen.addshape('Hunter.gif')
screen.addshape('Wizard.gif')
screen.addshape('Ice Wizard.gif')
screen.addshape('th1.gif')

import player
from map import Map
from props import props

from PlayerKeyPressHandler import playerKeyPressHandler

import config

map_size = config.MAP_SIZE
fog_step = 2


gameMap = Map(map_size, fog_step, screen)

p1 = player.player((0, 10),'玩家1',90,'player1','left', blood_empty_callback = gameMap.playerDie)
p1.gun = config.BOMBER()
p2 = player.player((20, 20),'玩家2',270,'player2','right', blood_empty_callback = gameMap.playerDie)


def icon():
	screen.tracer(0)
	c_list=[turtle.Turtle() for i in range(13)]
	for i,c in enumerate(c_list):
		c.penup()
		c.setposition(-570,280-50*i)
		c.pendown()
	for i,c in enumerate(zip(c_list,config.GUN_LIST+config.PROPS_LIST)):
		c,g=c[0],c[1]
		if isinstance(g,str):
			c.shape(f'{g}.gif')
		else:
			g=g()
			c.shape(f'{str(g)}.gif')
		c.write(f'    {config.description[i]}',False,'left',("Arial", 14, "normal"))
	screen.tracer(1)

def decorating():
	screen.tracer(0)
	t=turtle.Turtle()
	t.penup()
	t.hideturtle()
	t.setposition(450,-80)
	t.showturtle()
	t.shape('th1.gif')
	screen.tracer(1)

icon()
decorating()


gameMap.registerPlayer(p1)
gameMap.registerPlayer(p2)

def update():
	gameMap.update()
	screen.ontimer(update, 10)

def playerForward(player):
	if player.effect!='electrified':
		if player.effect=='frozen':
			player.fd(1)
		else:
			player.fd(3)
		if screen:
			screen.update()
		time.sleep(0.07)
		if player.effect=='frozen':
			player.fd(1)
		else:
			player.fd(3)
		if screen:
			screen.update()
		time.sleep(0.07)
		if player.effect=='frozen':
			player.fd(1)
		else:
			player.fd(3)
		if screen:
			screen.update()
def funcUp_p1(screen = None , player = None):
	if player.effect!='electrified':
		player.setheading(90)
	playerForward(player)
def funcDown_p1(screen = None , player = None):
	if player.effect!='electrified':
	    player.setheading(270)
	playerForward(player)
def funcLeft_p1(screen = None , player = None):
	if player.effect!='electrified':
	    player.setheading(180)
	playerForward(player)
def funcRight_p1(screen = None , player = None):
	if player.effect!='electrified':
	    player.setheading(0)
	playerForward(player)
def funcAtt_p1(screen = None, player = None):
	bullet = player.shoot()
	if bullet:
		bullet.setDeleteCallback(gameMap.removeBullet)
		gameMap.registerBullet(bullet)


def funcUp_p2(screen = None , player = None):
	if player.effect!='electrified':
	    player.setheading(90)
	playerForward(player)
def funcDown_p2(screen = None , player = None):
	if player.effect!='electrified':
	    player.setheading(270)
	playerForward(player)
def funcLeft_p2(screen = None , player = None):
	if player.effect!='electrified':
	    player.setheading(180)
	playerForward(player)
def funcRight_p2(screen = None , player = None):
	if player.effect!='electrified':
	    player.setheading(0)
	playerForward(player)
def funcAtt_p2(screen = None, player = None):
	bullet = player.shoot()
	if bullet:
		bullet.setDeleteCallback(gameMap.removeBullet)
		gameMap.registerBullet(bullet)

def upCallback():
	None
def downCallback():
	None
def leftCallback():
	None
def rightCallback():
	None
def attackCallback():
	None

pressHandle = playerKeyPressHandler(
			screen = screen, shortest_event_interval = config.keyPressCoolTime, player = p1,
			upHandler = funcUp_p1, downHandler = funcDown_p1, 
			leftHandler = funcLeft_p1, rightHandler = funcRight_p1, 
			attackHandler = funcAtt_p1,
			upKey = "Up", downKey = "Down",
			leftKey = "Left", rightKey = "Right",
			attackKey = "Return",
			whenUpCallback = upCallback, whenDownCallback = downCallback, 
			whenLeftCallback = leftCallback, whenRightCallback = rightCallback,
			whenAttackCallback = attackCallback)

pressHandle = playerKeyPressHandler(
			screen = screen, shortest_event_interval = config.keyPressCoolTime, player = p2,
			upHandler = funcUp_p2, downHandler = funcDown_p2, 
			leftHandler = funcLeft_p2, rightHandler = funcRight_p2, 
			attackHandler = funcAtt_p2,
			upKey = "w", downKey = "s",
			leftKey = "a", rightKey = "d",
			attackKey = "j",
			whenUpCallback = upCallback, whenDownCallback = downCallback, 
			whenLeftCallback = leftCallback, whenRightCallback = rightCallback,
			whenAttackCallback = attackCallback)


screen.listen()
proplist = []
def createProps():
	if not gameMap.over:
		x = (random.random() - 0.5)* 500
		y = (random.random() - 0.5)* 500
		while not gameMap.validPos((x, y)):
			x = (random.random() - 0.5)* 500
			y = (random.random() - 0.5)* 500
		prop = props((x, y))
		gameMap.registerProps(prop)
		screen.ontimer(createProps, 3000)



createProps()


# screen.ontimer(t.shoot(),15000)
turtle.mainloop()

import turtle
from datetime import timedelta, datetime
import random
import time



def initScreen():
	screen = turtle.Screen()
	screen.register_shape("rect", ((-5, -5), (5, -5), (5,5), (-5, 5)))
	screen.screensize(1000, 1000)
	screen.setworldcoordinates(-300,-300,300,300)
	return screen


screen = initScreen()
for i in range(24):
	screen.addshape(f'poor_gun-{15*i}.gif')
for i in range(4):
	screen.addshape(f'fireball-{90*i}.gif')
	screen.addshape(f'snowball-{90*i}.gif')
	screen.addshape(f'electrify-{90*i}.gif')
	screen.addshape(f'player1-{90*i}.gif')
	screen.addshape(f'player2-{90*i}.gif')
	screen.addshape(f'player1_burnt-{90*i}.gif')
	screen.addshape(f'player2_burnt-{90*i}.gif')
	screen.addshape(f'player1_frozen-{90*i}.gif')
	screen.addshape(f'player2_frozen-{90*i}.gif')
	screen.addshape(f'player_electrified-{90*i}.gif')



import player
from map import Map
from props import props

from PlayerKeyPressHandler import playerKeyPressHandler

import config

map_size = config.MAP_SIZE
fog_step = 2


gameMap = Map(map_size, fog_step, screen)

p1 = player.player((200, 100),'玩家1',90,'player1','left', blood_empty_callback = gameMap.playerDie)
p1.get_prop(config.ICE_WIZARD())
p1.display_bar()


p2 = player.player((200, 200),'玩家2',270,'player2','right', blood_empty_callback = gameMap.playerDie)
p2.get_prop(config.BOMBER())
p2.display_bar()

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
	prop = props()
	gameMap.registerProps(prop)
	screen.ontimer(createProps, 5000)



createProps()


# screen.ontimer(t.shoot(),15000)
turtle.mainloop()

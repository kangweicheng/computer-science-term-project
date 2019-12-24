import turtle
from datetime import timedelta, datetime
import random
import config
import player
from PlayerKeyPressHandler import playerKeyPressHandler
from map import Map

def initScreen():
	screen = turtle.Screen()
	screen.register_shape("rect", ((-5, -5), (5, -5), (5,5), (-5, 5)))
	screen.setworldcoordinates(-300,-300,300,300)
	return screen

map_size = config.MAP_SIZE

fog_step = 2
screen = initScreen()
screen.addshape('player1.gif')
gameMap = Map(map_size, fog_step, screen)
t = player.player((-200, -200),'哈哈哈','player1.gif','right')
t.display_bar()
t.turtlesize(0.1)
gameMap.registerPlayer(t)
def update():
	gameMap.update()
	screen.ontimer(update, 10)


def funcUp(screen = None , player = None):
	player.setheading(90)
	player.fd(9)
	if screen:
		screen.update()
def funcDown(screen = None , player = None):
	player.setheading(270)
	player.fd(9)
	# update()
	if screen:
		screen.update()
def funcLeft(screen = None , player = None):
	player.setheading(180)
	player.fd(9)
	if screen:
		screen.update()
def funcRight(screen = None , player = None):
	player.setheading(0)
	player.fd(9)
	if screen:
		screen.update()
def funcAtt(screen = None, player = None):
	None


# def keyPressCallback():
# 	for i in gameMap.player:
# 		print(i.position())
# 		collide, backPos = gameMap.hit_wall(i)
# 		# print(valid)
# 		if collide:
# 			i.setpos(backPos)
# 			return
# 		collide, backPos = gameMap.hit_boundary(i)
# 		# print(valid)
# 		if collide:
# 			i.setpos(backPos)
# 			# i.hit(config.TOUCH_FOG_DAMAGE)
			# return

def upCallback():
	gameMap.updatePlayers()
def downCallback():
	gameMap.updatePlayers()
def leftCallback():
	gameMap.updatePlayers()
def rightCallback():
	gameMap.updatePlayers()
def attackCallback():
	gameMap.updatePlayers()
pressHandle = playerKeyPressHandler(
			screen = screen, shortest_event_interval = config.keyPressCoolTime, player = t,
			upHandler = funcUp, downHandler = funcDown, 
			leftHandler = funcLeft, rightHandler = funcRight, 
			attackHandler = funcAtt,
			upKey = "Up", downKey = "Down",
			leftKey = "Left", rightKey = "Right",
			attackKey = "space",
			whenUpCallback = upCallback, whenDownCallback = downCallback, 
			whenLeftCallback = leftCallback, whenRightCallback = rightCallback,
			whenAttackCallback = attackCallback)


screen.listen()



# screen.ontimer(t.shoot(),15000)
turtle.mainloop()
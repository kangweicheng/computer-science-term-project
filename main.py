# import turtle
# from datetime import timedelta, datetime
# import random
# import config
# import player
# from PlayerKeyPressHandler import playerKeyPressHandler
# from map import Map
# from props import props

# def initScreen():
# 	screen = turtle.Screen()
# 	screen.register_shape("rect", ((-5, -5), (5, -5), (5,5), (-5, 5)))
# 	screen.setworldcoordinates(-300,-300,300,300)
# 	return screen




# def update():
# 	gameMap.update()
# 	screen.ontimer(update, 10)


# def funcUp(screen = None , player = None):
# 	player.setheading(90,'player1-90.gif')
# 	player.fd(9)
# 	if screen:
# 		screen.update()
# def funcDown(screen = None , player = None):
# 	player.setheading(270,'player1-270.gif')
# 	player.fd(9)
# 	# update()
# 	if screen:
# 		screen.update()
# def funcLeft(screen = None , player = None):
# 	player.setheading(180,'player1-180.gif')
# 	player.fd(9)
# 	if screen:
# 		screen.update()
# def funcRight(screen = None , player = None):
# 	player.setheading(0,'player1-0.gif')
# 	player.fd(9)
# 	if screen:
# 		screen.update()
# def funcAtt(screen = None, player = None):
# 	None


# # def keyPressCallback():
# # 	for i in gameMap.player:
# # 		print(i.position())
# # 		collide, backPos = gameMap.hit_wall(i)
# # 		# print(valid)
# # 		if collide:
# # 			i.setpos(backPos)
# # 			return
# # 		collide, backPos = gameMap.hit_boundary(i)
# # 		# print(valid)
# # 		if collide:
# # 			i.setpos(backPos)
# # 			# i.hit(config.TOUCH_FOG_DAMAGE)
# 			# return

# def upCallback():
# 	gameMap.updatePlayers()
# def downCallback():
# 	gameMap.updatePlayers()
# def leftCallback():
# 	gameMap.updatePlayers()
# def rightCallback():
# 	gameMap.updatePlayers()
# def attackCallback():
# 	gameMap.updatePlayers()

# map_size = config.MAP_SIZE

# fog_step = 2
# screen = initScreen()
# screen.addshape('player1-0.gif')
# screen.addshape('player1-90.gif')
# screen.addshape('player1-180.gif')
# screen.addshape('player1-270.gif')
# screen.addshape('player2-0.gif')
# screen.addshape('player2-90.gif')
# screen.addshape('player2-180.gif')
# screen.addshape('player2-270.gif')
# gameMap = Map(map_size, fog_step, screen)
# t = player.player((-200, -200),'哈哈哈',0 ,'player1-0.gif','right')
# t.display_bar()
# t.turtlesize(0.1)
# gameMap.registerPlayer(t)

# pressHandle = playerKeyPressHandler(
# 			screen = screen, shortest_event_interval = config.keyPressCoolTime, player = t,
# 			upHandler = funcUp, downHandler = funcDown, 
# 			leftHandler = funcLeft, rightHandler = funcRight, 
# 			attackHandler = funcAtt,
# 			upKey = "Up", downKey = "Down",
# 			leftKey = "Left", rightKey = "Right",
# 			attackKey = "space",
# 			whenUpCallback = upCallback, whenDownCallback = downCallback, 
# 			whenLeftCallback = leftCallback, whenRightCallback = rightCallback,
# 			whenAttackCallback = attackCallback)


# screen.listen()


# class bullet:
# 	def __init__(self):
# 		self.damage = 1000


# # routinely hit
# def self_hit():
# 	print('hit')
# 	screen.tracer(0)
# 	t.shoot()
# 	t.hit(bullet())
# 	t.display_bar()
# 	screen.update()
# 	screen.tracer(1)
# 	screen.ontimer(self_hit, 1000)

# screen.ontimer(self_hit, 1000)
# # routinely create props
# # proplist = []
# # def createProps():
# # 	print('createProps')
# # 	proplist.append(props())
# # 	screen.ontimer(createProps, 1000)

# # screen.ontimer(createProps, 1000)


# # screen.ontimer(t.shoot(),15000)
# turtle.mainloop()

import turtle
from datetime import timedelta, datetime
import random
import config
import player
from PlayerKeyPressHandler import playerKeyPressHandler
from map import Map
from props import props

def initScreen():
	screen = turtle.Screen()
	screen.register_shape("rect", ((-5, -5), (5, -5), (5,5), (-5, 5)))
	screen.setworldcoordinates(-300,-300,300,300)
	return screen

map_size = config.MAP_SIZE

fog_step = 2
screen = initScreen()
screen.addshape('player1-0.gif')
screen.addshape('player1-90.gif')
screen.addshape('player1-180.gif')
screen.addshape('player1-270.gif')
gameMap = Map(map_size, fog_step, screen)
t = player.player((-200, -200),'哈哈哈',0,'player1-0.gif','left')
t.display_bar()
t.turtlesize(0.1)
gameMap.registerPlayer(t)
def update():
	gameMap.update()
	screen.ontimer(update, 10)


def funcUp(screen = None , player = None):
	player.setheading(90,'player1-90.gif')
	player.fd(9)
	if screen:
		screen.update()
def funcDown(screen = None , player = None):
	player.setheading(270,'player1-270.gif')
	player.fd(9)
	# update()
	if screen:
		screen.update()
def funcLeft(screen = None , player = None):
	player.setheading(180,'player1-180.gif')
	player.fd(9)
	if screen:
		screen.update()
def funcRight(screen = None , player = None):
	player.setheading(0,'player1-0.gif')
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
proplist = []
def createProps():
	proplist.append(props())
	screen.ontimer(createProps, 1000)
screen.ontimer(createProps, 1000)


# screen.ontimer(t.shoot(),15000)
turtle.mainloop()
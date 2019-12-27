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

screen.addshape('player2-0.gif')
screen.addshape('player2-90.gif')
screen.addshape('player2-180.gif')
screen.addshape('player2-270.gif')

gameMap = Map(map_size, fog_step, screen)

p1 = player.player((-200, -200),'哈哈哈',0,'player1-0.gif','left')
p1.display_bar()


p2 = player.player((200, 200),'哈哈哈',0,'player2-0.gif','right')
p2.display_bar()

gameMap.registerPlayer(p1)
gameMap.registerPlayer(p2)

def update():
	gameMap.update()
	screen.ontimer(update, 10)


def funcUp_p1(screen = None , player = None):
	player.setheading(90,'player1-90.gif')
	player.fd(9)
	if screen:
		screen.update()
def funcDown_p1(screen = None , player = None):
	player.setheading(270,'player1-270.gif')
	player.fd(9)
	# update()
	if screen:
		screen.update()
def funcLeft_p1(screen = None , player = None):
	player.setheading(180,'player1-180.gif')
	player.fd(9)
	if screen:
		screen.update()
def funcRight_p1(screen = None , player = None):
	player.setheading(0,'player1-0.gif')
	player.fd(9)
	if screen:
		screen.update()
def funcAtt_p1(screen = None, player = None):
	player.shoot()


def funcUp_p2(screen = None , player = None):
	player.setheading(90,'player2-90.gif')
	player.fd(9)
	if screen:
		screen.update()
def funcDown_p2(screen = None , player = None):
	player.setheading(270,'player2-270.gif')
	player.fd(9)
	# update()
	if screen:
		screen.update()
def funcLeft_p2(screen = None , player = None):
	player.setheading(180,'player2-180.gif')
	player.fd(9)
	if screen:
		screen.update()
def funcRight_p2(screen = None , player = None):
	player.setheading(0,'player2-0.gif')
	player.fd(9)
	if screen:
		screen.update()
def funcAtt_p2(screen = None, player = None):
	player.shoot()

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
			screen = screen, shortest_event_interval = config.keyPressCoolTime, player = p1,
			upHandler = funcUp_p1, downHandler = funcDown_p1, 
			leftHandler = funcLeft_p1, rightHandler = funcRight_p1, 
			attackHandler = funcAtt_p1,
			upKey = "Up", downKey = "Down",
			leftKey = "Left", rightKey = "Right",
			attackKey = "space",
			whenUpCallback = upCallback, whenDownCallback = downCallback, 
			whenLeftCallback = leftCallback, whenRightCallback = rightCallback,
			whenAttackCallback = attackCallback)

pressHandle = playerKeyPressHandler(
			screen = screen, shortest_event_interval = config.keyPressCoolTime, player = p2,
			upHandler = funcUp_p2, downHandler = funcDown_p2, 
			leftHandler = funcLeft_p2, rightHandler = funcRight_p2, 
			attackHandler = funcAtt_p2,
			upKey = "W", downKey = "S",
			leftKey = "A", rightKey = "D",
			attackKey = "O",
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
import turtle
from datetime import timedelta, datetime
import random
import config
import player
from PlayerKeyPressHandler import playerKeyPressHandler
class Map:
	def penup_set_pos(self, Turtle, pos):
		Turtle.penup()
		Turtle.setpos((pos[0], pos[1]))
		# Turtle.setx()
		# Turtle.sety(pos[1])
		Turtle.pendown()
	def pendown_set_pos(self, Turtle, pos):
		Turtle.setpos((pos[0], pos[1]))
		# Turtle.setx(pos[0])
		# Turtle.sety(pos[1])
	def draw_wall(self, Turtle, pos, size):

		Turtle.penup()
		Turtle.shape('square')
		Turtle.turtlesize(size / 20, size / 20)
		Turtle.setpos(pos[0], pos[1])
		stamp_id = Turtle.stamp()
		return stamp_id
		# t = turtle.Turtle()


	def initWallpos(self, num):
		self.wall_pos = []
		while len(self.wall_pos) < num:
			x1 = (random.random() - 0.5) * self.map_size[0]
			y1 = (random.random() - 0.5) * self.map_size[1]
			self.wall_pos.append((x1, y1))
	def initWall(self):
		self.screen.tracer(0)
		self.wall = []
		for i in self.wall_pos:
			t = turtle.Turtle()
			t.hideturtle()
			t.width(3)

			stamp_id = self.draw_wall(t, i, self.wall_size)
			# print(stamp_id)
			self.wall.append(stamp_id)
		self.screen.update()
		self.screen.tracer(1)
	def __init__(self, map_size, fog_step, screen, fogUpdateInterval = config.FOG_UPDATE_INTERVAL):
		self.screen = screen
		self.wall_vertex = []
		self.wall = []
		self.player = []
		self.fog_position = map_size[0]/ 2
		self.fog_step = fog_step
		self.map_size = map_size
		self.wall_size = 40
		self.fogUpdateInterval = fogUpdateInterval * 1000

		self.initWallpos(10)
		self.initWall()

		self.fog = turtle.Turtle()
		self.fog.color('green')
		self.fog.hideturtle()
		self.fog.width(fog_step)
		self.penup_set_pos(self.fog, ( -1 * map_size[0] /2 , -1 * map_size[1] / 2 - self.fog_step))# - self.fog_step))
		self.fogMove()
		self.screen.ontimer(self.update, self.fogUpdateInterval)
	def fogMove(self):
		self.screen.tracer(0)
		self.fog.forward(self.fog_step)
		self.fog.lt(90)
		self.fog.forward(self.fog_step)
		self.fog.forward(self.map_size[0])
		self.fog.rt(90)
		self.fog.forward(self.map_size[1])
		self.fog.rt(90)
		self.fog.forward(self.map_size[0])
		self.fog.rt(90)
		self.fog.forward(self.map_size[1])
		self.fog.rt(180)
		self.map_size = (self.map_size[0] - self.fog_step * 2, self.map_size[1]  - self.fog_step * 2)
		self.screen.update()
		self.screen.tracer(1)
		self.updatePlayers()

	def update(self):
		self.fogMove()
		self.screen.ontimer(self.update, self.fogUpdateInterval)
	def in_square(self, original_pos, pos, square_pos, square_size):
		xgt = square_pos[0] + square_size / 2 > pos[0]
		xlt = square_pos[0] - square_size / 2 < pos[0]
		ygt = square_pos[1] + square_size / 2 > pos[1]
		ylt = square_pos[1] - square_size / 2 < pos[1]
		if xgt and xlt and ygt and ylt:
			xgt = square_pos[0] + square_size / 2 <= original_pos[0]
			xlt = square_pos[0] - square_size / 2 >= original_pos[0]
			ygt = square_pos[1] + square_size / 2 <= original_pos[1]
			ylt = square_pos[1] - square_size / 2 >= original_pos[1]
			if xgt:
				return True, (square_pos[0]  + square_size / 2 + 1, original_pos[1])
			if xlt:
				return True, (square_pos[0]  - square_size / 2 - 1, original_pos[1])
			if ygt:
				return True, (original_pos[0], square_pos[1] + square_size / 2 + 1)
			if ylt:
				return True, (original_pos[0], square_pos[1] - square_size / 2 - 1)

			# return True, (square_pos[0]  - square_size / 2, pos[1])
		else:
			return False, None

	def hit_wall(self, obj):
		print(obj.pos)
		for i in self.wall_pos:
			x, y = self.in_square(obj.original_pos, obj.pos, i, self.wall_size)
			if x:
				return True, y
		return False, None
				# self.penup_set_pos(obj, y)
				# obj.penup()

	def hit_boundary(self, obj):
		square_pos = (0, 0)
		square_size = self.map_size[0]
		pos = obj.pos
		xgt = square_pos[0] + square_size / 2 > pos[0]
		xlt = square_pos[0] - square_size / 2 < pos[0]
		ygt = square_pos[1] + square_size / 2 > pos[1]
		ylt = square_pos[1] - square_size / 2 < pos[1]
		if xgt and xlt and ygt and ylt:
			return False, None
		else:
			pos = [obj.pos[0], obj.pos[1]]
			if obj.pos[0] > self.map_size[0]/2:
				pos[0] = self.map_size[0]/2
			elif obj.pos[0] < -1 * self.map_size[0]/2:
				pos[0] = -1 * self.map_size[0]/2

			if obj.pos[1] > self.map_size[1]/2:
				pos[1] = self.map_size[1]/2
			elif obj.pos[1] < -1 * self.map_size[1]/2:
				pos[1] = -1 * self.map_size[1]/2
			return True, pos
			# self.penup_set_pos(obj, pos)
			# # obj.hit(config.TOUCH_FOG_DAMAGE)
			# obj.penup()
			# return True, tuple(pos)
	def updatePlayers(self):
		for i in self.player:
			collide, backPos = self.hit_wall(i)
			print(collide)
			if collide:
				i.back(9)
				# i.setpos(backPos)
				return
			collide, backPos = self.hit_boundary(i)

			if collide:
				i.setpos(backPos)
				return

	def registerPlayer(self, Player):
		self.player.append(Player)

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

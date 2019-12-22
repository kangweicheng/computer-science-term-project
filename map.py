import turtle
import datetime
import random
import config
random.seed(0)

class player:
	def __init__(self, pos):
		self.original_pos = pos   #等於之前的pos
		self.pos = pos
		self.turtle = turtle.Turtle()
		self.turtle.penup()
		self.turtle.setpos(pos)
	def penup(self):
		self.turtle.penup()
	def pendown(self):
		self.turtle.pendown()
	def forward(self, x):
		self.turtle.penup()
		self.turtle.forward(x)
		self.update_pos()
	def lt(self, x):
		self.turtle.lt(x)
	def rt(self, x):
		self.turtle.rt(x)
	def setheading(self, x):
		self.turtle.setheading(x)
	def update_pos(self):
		self.original_pos = self.pos
		self.pos = self.turtle.position()
	def setpos(self, new_pos):
		self.turtle.penup()
		self.turtle.setpos(new_pos)
		self.update_pos()


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
	def __init__(self, map_size, fog_step, screen):
		self.screen = screen
		self.wall_vertex = []
		self.wall = []
		self.fog_position = map_size[0]/ 2
		self.fog_step = fog_step
		self.map_size = map_size
		self.wall_size = 40

		self.initWallpos(10)
		self.initWall()

		self.fog = turtle.Turtle()
		self.fog.color('green')
		self.fog.hideturtle()
		self.fog.width(fog_step)
		self.penup_set_pos(self.fog, ( -1 * map_size[0] /2 , -1 * map_size[1] / 2 - self.fog_step))# - self.fog_step))
		self.next_updateTime = datetime.datetime.now()
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
		self.next_updateTime += datetime.timedelta(seconds = config.FOG_UPDATE_INTERVAL)
		self.screen.update()
		self.screen.tracer(1)

	def update(self):
		if datetime.datetime.now() > self.next_updateTime :
			self.fogMove()
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
		for i in self.wall_pos:
			x, y = self.in_square(obj.original_pos, obj.pos, i, self.wall_size)
			if x:
				self.penup_set_pos(obj, y)
				obj.penup()

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
			self.penup_set_pos(obj, pos)
			# obj.hit(config.TOUCH_FOG_DAMAGE)
			obj.penup()
			# return True, tuple(pos)

def initScreen():
	screen = turtle.Screen()
	screen.register_shape("rect", ((-5, -5), (5, -5), (5,5), (-5, 5)))
	screen.setworldcoordinates(-300,-300,300,300)
	return screen

map_size = config.MAP_SIZE

fog_step = 2
screen = initScreen()

gameMap = Map(map_size, fog_step, screen)
t = player((-200, -200))
t.penup()
def update():
	gameMap.update()
	gameMap.hit_boundary(t)
	gameMap.hit_wall(t)
	screen.ontimer(update, 10)
def funcUp():
	t.setheading(90)
	t.forward(9)
	# update()
def funcDown():
	t.setheading(270)
	t.forward(9)
	# update()
	screen.update()
def funcLeft():
	t.setheading(180)
	t.forward(9)
	# update()
	screen.update()
def funcRight():
	t.setheading(0)
	t.forward(9)
	
	# screen.update()
screen.onkey(funcUp, "Up")
screen.onkey(funcDown, "Down")
screen.onkey(funcLeft, "Left")
screen.onkey(funcRight, "Right")
screen.listen()

screen.ontimer(update, 10)


turtle.mainloop()

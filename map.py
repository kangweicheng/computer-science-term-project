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
		Turtle.pendown()
	def pendown_set_pos(self, Turtle, pos):
		Turtle.setpos((pos[0], pos[1]))
	def draw_wall(self, Turtle, pos, size):
		Turtle.penup()
		Turtle.shape('square')
		Turtle.turtlesize(size / 20, size / 20)
		Turtle.setpos(pos[0], pos[1])
		stamp_id = Turtle.stamp()
		return stamp_id


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

		self.players = []
		self.bullets = []

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
		self.updateBullets()
		self.updatePlayers()
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


	def update(self):
		self.fogMove()
		self.screen.ontimer(self.update, self.fogUpdateInterval)
	def in_square(self, original_pos, pos, square_pos, square_size):
		xgt = square_pos[0] + square_size / 2 > pos[0]
		xlt = square_pos[0] - square_size / 2 < pos[0]
		ygt = square_pos[1] + square_size / 2 > pos[1]
		ylt = square_pos[1] - square_size / 2 < pos[1]
		if xgt and xlt and ygt and ylt:
			if original_pos:
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

				return True, (original_pos[0], square_pos[1] - square_size / 2 - 1)
			else:
				return True, None
		else:
			return False, None

	def hit_wall(self, obj):
		for i in self.wall_pos:
			if hasattr(obj, 'original_pos'):
				x, y = self.in_square(obj.original_pos, obj.pos(), i, self.wall_size)
			else:
				x, y = self.in_square(None, obj.pos(), i, self.wall_size)
			if x:
				return True, y
		return False, None
				# self.penup_set_pos(obj, y)
				# obj.penup()

	def hit_boundary(self, obj):
		square_pos = (0, 0)
		square_size = self.map_size[0]
		pos = obj.pos()
		xgt = square_pos[0] + square_size / 2 > pos[0]
		xlt = square_pos[0] - square_size / 2 < pos[0]
		ygt = square_pos[1] + square_size / 2 > pos[1]
		ylt = square_pos[1] - square_size / 2 < pos[1]
		if xgt and xlt and ygt and ylt:
			return False, None
		else:
			pos = [pos[0], pos[1]]
			if pos[0] > self.map_size[0]/2:
				pos[0] = self.map_size[0]/2
			elif pos[0] < -1 * self.map_size[0]/2:
				pos[0] = -1 * self.map_size[0]/2

			if pos[1] > self.map_size[1]/2:
				pos[1] = self.map_size[1]/2
			elif pos[1] < -1 * self.map_size[1]/2:
				pos[1] = -1 * self.map_size[1]/2
			return True, pos
	def updatePlayers(self):
		for i in self.players:
			collide, backPos = self.hit_wall(i)
			if collide:
				i.back(9)

			collide, backPos = self.hit_boundary(i)
			if collide:
				i.setpos(backPos)
		self.screen.ontimer(self.updatePlayers, 100)
	def updateBullets(self):
		for bullet in self.bullets:
			print('bullet')
			for obj in bullet.items:
				print('obj')
				collide, backPos = self.hit_wall(obj)
				if collide:
					bullet.deleteItem(obj)

				collide, backPos = self.hit_boundary(obj)
				if collide:
					bullet.deleteItem(obj)
		self.screen.ontimer(self.updateBullets, 100)
	def registerPlayer(self, Player):
		self.updatePlayers()
		self.players.append(Player)
	def registerProps(self, Props):
		None
	def removeProps(self, Props):
		None
	def registerBullet(self, Bullet):
		self.bullets.append(Bullet)
	def removeBullet(self, Bullet):
		index = self.bullets.index(Bullet)
		del self.bullets[index]


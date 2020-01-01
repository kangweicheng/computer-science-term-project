import turtle
from datetime import timedelta, datetime
import time
import random
import config
import player
from PlayerKeyPressHandler import playerKeyPressHandler
from props import props
class Map:
	def __init__(self, map_size, fog_step, screen, fogUpdateInterval = config.FOG_UPDATE_INTERVAL):
		self.over = False
		self.screen = screen
		self.wall_vertex = []
		self.wall = []

		self.players = []
		self.bullets = []
		self.props = []

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

		# self.screen.ontimer(, self.fogUpdateInterval)
		self.updateFog()
		self.updateBullets()
		self.updatePlayers()
		self.bulletHitPlayers()
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
	def generateProps(self):
		self.props.append(props())
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


	def updateFog(self):
		if not self.over:
			self.fogMove()
			self.screen.ontimer(self.updateFog, self.fogUpdateInterval)
	def in_square(self, original_pos, pos, square_pos, square_size, buffer_region = 10):
		xgt = square_pos[0] + square_size / 2 > pos[0] - buffer_region
		xlt = square_pos[0] - square_size / 2 < pos[0] + buffer_region
		ygt = square_pos[1] + square_size / 2 > pos[1] - buffer_region
		ylt = square_pos[1] - square_size / 2 < pos[1] + buffer_region
		if xgt and xlt and ygt and ylt:
			print('hit wall')
			if original_pos:
				xgt = square_pos[0] + square_size / 2 <= original_pos[0] - buffer_region
				xlt = square_pos[0] - square_size / 2 >= original_pos[0] + buffer_region
				ygt = square_pos[1] + square_size / 2 <= original_pos[1] - buffer_region
				ylt = square_pos[1] - square_size / 2 >= original_pos[1] + buffer_region
				if xgt:
					return True, (square_pos[0]  + square_size / 2 + 1 + buffer_region, original_pos[1])
				elif xlt:
					return True, (square_pos[0]  - square_size / 2 - 1 - buffer_region, original_pos[1])
				elif ygt:
					return True, (original_pos[0], square_pos[1] + square_size / 2 + 1 + buffer_region)
				elif ylt:
					return True, (original_pos[0], square_pos[1] - square_size / 2 - 1 - buffer_region)

				return True, (original_pos[0], square_pos[1] - square_size / 2 - 1 - buffer_region)
			else:
				return True, None
		else:
			return False, None

	def hit_wall(self, obj, buffer_region = 10):
		for i in self.wall_pos:
			if hasattr(obj, 'original_pos'):
				x, y = self.in_square(obj.original_pos, obj.pos(), i, self.wall_size, buffer_region = buffer_region)
			else:
				x, y = self.in_square(None, obj.pos(), i, self.wall_size, buffer_region = buffer_region)
			if x:
				print('collide')
				print(y)
				return True, y
		return False, None
				# self.penup_set_pos(obj, y)
				# obj.penup()

	def hit_boundary(self, obj, buffer_region = 10):
		square_pos = (0, 0)
		square_size = self.map_size[0]
		pos = obj.pos()
		xgt = square_pos[0] + square_size / 2 > pos[0] + buffer_region
		xlt = square_pos[0] - square_size / 2 < pos[0] - buffer_region
		ygt = square_pos[1] + square_size / 2 > pos[1] + buffer_region
		ylt = square_pos[1] - square_size / 2 < pos[1] - buffer_region
		if xgt and xlt and ygt and ylt:
			return False, None
		else:
			pos = [pos[0], pos[1]]
			if pos[0] > self.map_size[0]/2 - buffer_region:
				pos[0] = self.map_size[0]/2 - buffer_region
			elif pos[0] < -1 * self.map_size[0]/2 + buffer_region:
				pos[0] = -1 * self.map_size[0]/2 + buffer_region

			if pos[1] > self.map_size[1]/2 - buffer_region:
				pos[1] = self.map_size[1]/2 - buffer_region
			elif pos[1] < -1 * self.map_size[1]/2 + buffer_region:
				pos[1] = -1 * self.map_size[1]/2 + buffer_region
			return True, pos

	def updatePlayers(self):
		if not self.over:
			for i in self.players:
				collide, backPos = self.hit_wall(i)
				if collide:
					i.back(9)

				collide, backPos = self.hit_boundary(i)
				if collide:
					i.setpos(backPos)
					i.hit(config.TOUCH_FOG_DAMAGE)
			self.screen.ontimer(self.updatePlayers, 100)

	def updateBullets(self):
		if not self.over:

			for bullet in self.bullets:

				for obj in bullet.items:
					collide, backPos = self.hit_wall(obj, buffer_region = 10)
					if collide:

						bullet.deleteItem(obj)

					collide, backPos = self.hit_boundary(obj, buffer_region = 20)
					if collide:
						bullet.deleteItem(obj)
				if len(bullet.items) == 0:
					bullet.deleteBullet()

					self.removeBullet(bullet)
			self.screen.ontimer(self.updateBullets, 30)

	def touchPlayers(self, player, obj, rod):
		buffer_dist = 0
		if (player.pos()[0] - obj.pos()[0]) ** 2 + (player.pos()[1] - obj.pos()[1]) ** 2 < (rod + buffer_dist) ** 2:
			return True
		else:
			return False
	def bulletHitPlayers(self):
		if not self.over:
			for player in self.players:
				for bullet in self.bullets:
					for obj in bullet.items:
						if self.touchPlayers(player, obj, bullet.rod) and bullet.owner != player.name:
							bullet.deleteItem(obj)
							if len(bullet.items) == 0:
								bullet.deleteBullet()
								self.removeBullet(bullet)
							player.hit(bullet)
			self.screen.ontimer(self.bulletHitPlayers, 100)


	def registerPlayer(self, Player):
		self.updatePlayers()
		self.players.append(Player)
	def validProps(self, Props):
		collide, backPos = self.hit_wall(Props, buffer_region = 10)
		if collide:

			return False

		collide, backPos = self.hit_boundary(Props, buffer_region = 20)
		if collide:
			return False
		return True
	def registerProps(self, Props):
		self.props.append(Props)
	def removeProps(self, Props):
		try:
			index = self.props.index(Props)
			del self.props[index]
		except:
			None
	def registerBullet(self, Bullet):
		self.bullets.append(Bullet)
	def removeBullet(self, Bullet):
		try:
			index = self.bullets.index(Bullet)
			del self.bullets[index]
		except:
			None
	def gameOver(self):
		self.screen.clearscreen()
		for i in self.bullets:
			i.over = True
		for i in self.players:
			i.over = True
		self.over = True
		print('Gameover')
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		t.setpos(-150,50)
		t.pendown()
		t.write('Winner is %s'%(self.players[0].name), font=("Arial", 32, "normal"))
	def playerDie(self, player):
		try:
			player.hideturtle()
			player.clear()
			player.over = True
			index = self.players.index(player)
			del self.players[index]
			if len(self.players) == 1:
				self.gameOver()
		except:
			None


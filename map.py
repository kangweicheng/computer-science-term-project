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
		self.fog.color('grey')
		self.fog.hideturtle()
		self.fog.width(fog_step * 2)
		self.penup_set_pos(self.fog, ( -1 * map_size[0] /2 , -1 * map_size[1] / 2 - self.fog_step))# - self.fog_step))
		self.fogMove()

		# self.screen.ontimer(, self.fogUpdateInterval)
		self.updateFog()
		self.updateBullets()
		self.bulletHitPlayers()
		self.updatePlayers()
		self.updateProps()
		
		self.propsHitPlayers()

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
		self.wall_pos = [(0,0)]
		while len(self.wall_pos) < num:
			x1 = (random.random() - 0.5) * (self.map_size[0] - 50)
			y1 = (random.random() - 0.5) * (self.map_size[1] - 50)
			self.wall_pos.append((x1, y1))
	def initWall(self):
		self.screen.tracer(0)
		self.wall = []
		for i in self.wall_pos:
			t = turtle.Turtle()
			t.hideturtle()
			t.width(3)

			stamp_id = self.draw_wall(t, i, self.wall_size)
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

	def hit_wall(self, obj = None, pos = None, buffer_region = 10):
		if obj:
			for i in self.wall_pos:
				if hasattr(obj, 'original_pos'):
					x, y = self.in_square(obj.original_pos, obj.pos(), i, self.wall_size, buffer_region = buffer_region)
				else:
					x, y = self.in_square(None, obj.pos(), i, self.wall_size, buffer_region = buffer_region)
				if x:
					return True, y
			return False, None
		else:
			for i in self.wall_pos:
				x, y = self.in_square(None, pos, i, self.wall_size, buffer_region = buffer_region)
				if x:
					return True, y
			return False, None
	def hit_boundary(self, obj = None, pos = None, buffer_region = 10):
		square_pos = (0, 0)
		square_size = self.map_size[0]
		if obj:
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
				collide, backPos = self.hit_wall(obj = i, buffer_region = 15)
				if collide:
					i.back(9)

				collide, backPos = self.hit_boundary(obj = i, buffer_region = 15)
				if collide:
					i.setpos(backPos)
					i.hit(config.TOUCH_FOG_DAMAGE)
			self.screen.ontimer(self.updatePlayers, 100)

	def updateBullets(self):
		# print(len(self.screen.turtles()))
		# print('self.bullets', self.bullets)
		if not self.over:
			for bullet in self.bullets:
				if bullet:
					for obj in bullet.items:
						# print(bullet.items)
						if obj:
							collide, backPos = self.hit_wall(obj = obj, buffer_region = 10)
							if collide:
								# print(f'delete: {obj}')
								# print(bullet.items, obj, 'collide wall')
								bullet.deleteItem(obj)
								
							collide, backPos = self.hit_boundary(obj = obj, buffer_region = 10)
							if collide:
								# print(bullet.items, obj, 'collide boundary')
								# print(f'delete: {obj}')
								bullet.deleteItem(obj)
					if bullet.item_len == 0:
						# print('empty bullet in updateBullets')
						# print(bullet)
						bullet.deleteBullet()
						self.removeBullet(bullet)
			self.bullets= list(filter(lambda x : x, self.bullets))

			self.screen.ontimer(self.updateBullets, 20)

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
					if bullet:
						for obj in bullet.items:
							if obj:
								if self.touchPlayers(player, obj, bullet.rod) and bullet.owner != player.name:
									# print('hit')
									bullet.deleteItem(obj)
									player.hit(bullet)
						if bullet.item_len == 0:
							# print('empty bullet in bulletHitPlayers')
							# print(bullet)
							bullet.deleteBullet()
							self.removeBullet(bullet)
			self.bullets= list(filter(lambda x : x, self.bullets))
			self.screen.ontimer(self.bulletHitPlayers, 30)
	def propsHitPlayers(self):
		if not self.over:
			for player in self.players:
				for props in self.props:
					if props:
						if self.touchPlayers(player, props, 30):
							props.deleteSelf()
							player.get_prop(props)
							self.removeProps(props)
			self.props = list(filter(lambda x : x, self.props))
			self.screen.ontimer(self.propsHitPlayers, 100)
	def updateProps(self):
		for props in self.props:
			if props:
				if datetime.now() > props.vanishTime:
					props.deleteSelf()
					self.removeProps(props)
		self.props = list(filter(lambda x : x, self.props))
		self.screen.update()
		self.screen.ontimer(self.updateProps, 5000)
	def registerPlayer(self, Player):
		self.updatePlayers()
		self.players.append(Player)
	def validPos(self, Pos):
		collide, backPos = self.hit_wall(pos = Pos, buffer_region = 40)
		if collide:

			return False

		collide, backPos = self.hit_boundary(pos = Pos, buffer_region = 40)
		
		if collide:
			return False
		return True
	def registerProps(self, Props):
		self.props.append(Props)
	def removeProps(self, Props):
		try:
			index = self.props.index(Props)
			self.removeTurtleFromScreen(Props)
			self.props[index] = None
			print('remove props success')
		except:
			print('except when remove Props')
	def registerBullet(self, Bullet):
		# Bullet.addMap(self)
		# print(Bullet.items)
		self.bullets.append(Bullet)
	def removeBullet(self, Bullet):
		# print(self.bullets, Bullet)
		# try:
		index = self.bullets.index(Bullet)
		self.bullets[index] = None
		# except:
		# 	print('error')
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
		p=turtle.Turtle()
		p.penup()
		p.setpos(0,-100)
		p.shape(f'player{self.players[0].name[-1]}-90.gif')
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
	def removeTurtleFromScreen(self, turtle):
		try:
			index = self.screen.turtles().index(turtle)
			del self.screen.turtles()[index]
		except:
			print('except when removeTurtleFromScreen in map.py')



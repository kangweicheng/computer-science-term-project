from datetime import timedelta, datetime
class playerKeyPressHandler:
	def __init__(self, screen = None, player = None, shortest_event_interval = 3,
			upHandler = None, downHandler = None,
			leftHandler = None, rightHandler = None,
			attackHandler = None,
			upKey = None, downKey = None,
			leftKey = None, rightKey = None,
			attackKey = None,
			whenUpCallback = None, whenDownCallback = None,
			whenRightCallback = None, whenLeftCallback = None,
			whenAttackCallback = None
			):
		self.upHandler = upHandler
		self.downHandler = downHandler
		self.leftHandler = leftHandler
		self.rightHandler = rightHandler
		self.attackHandler = attackHandler

		self.upKey = upKey
		self.downKey= downKey
		self.leftKey = leftKey
		self.rightKey = rightKey
		self.attackKey = attackKey

		self.whenUpCallback = whenUpCallback
		self.whenDownCallback = whenDownCallback
		self.whenRightCallback = whenRightCallback
		self.whenLeftCallback = whenLeftCallback
		self.whenAttackCallback = whenAttackCallback

		self.player = player
		self.last_keyPress = datetime.now() - timedelta(seconds = 10)
		self.shortest_event_interval = shortest_event_interval


		self.screen = screen
		if self.upHandler and self.upKey:
			self.screen.onkeypress(self.up, self.upKey)
		if self.downHandler and self.downKey:
			self.screen.onkeypress(self.down, self.downKey)
		if self.leftHandler and self.leftKey:
			self.screen.onkeypress(self.left, self.leftKey)
		if self.rightHandler and self.rightKey:
			self.screen.onkeypress(self.right, self.rightKey)
		if self.attackHandler and self.attackKey:
			self.screen.onkey(self.attack, self.attackKey)
	def up(self):
		if datetime.now() - self.last_keyPress > timedelta(seconds = self.shortest_event_interval):
			self.last_keyPress = datetime.now()
			self.upHandler(self.screen, self.player)
			if self.whenUpCallback:
				self.whenUpCallback()
	def down(self):
		if datetime.now() - self.last_keyPress > timedelta(seconds = self.shortest_event_interval):
			self.last_keyPress = datetime.now()
			self.downHandler(self.screen, self.player)
			if self.whenDownCallback:
				print('whenUpCallback')
				self.whenDownCallback()
	def left(self):
		if datetime.now() - self.last_keyPress > timedelta(seconds = self.shortest_event_interval):
			self.last_keyPress = datetime.now()
			self.leftHandler(self.screen, self.player)
			if self.whenLeftCallback:
				self.whenLeftCallback()
	def right(self):
		if datetime.now() - self.last_keyPress > timedelta(seconds = self.shortest_event_interval):
			self.last_keyPress = datetime.now()
			self.rightHandler(self.screen, self.player)
			if self.whenRightCallback:
				self.whenRightCallback()
	def attack(self):
		print(datetime.now())
		if datetime.now() - self.last_keyPress > timedelta(seconds = self.shortest_event_interval):
			self.last_keyPress = datetime.now()
			self.attackHandler(self.screen, self.player)
			if self.whenAttackCallback:
				self.whenAttackCallback()


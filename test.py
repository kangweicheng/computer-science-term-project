import msvcrt
# while True:
#     if msvcrt.kbhit():
#         key_stroke = msvcrt.getch()
#         print(key_stroke)   # will print which key is pressed
import turtle
img = r"rsz_th.gif"
turtle.addshape(img)

class player:
	def __init__(self):
		self.turtle = turtle.Turtle()

		self.turtle.shape(img)
		self.turtle.shapesize(5, 1)
		self.turtle.penup()

		self.dir = 'right'
t = player()
turtle.mainloop()

# screen = turtle.Screen()  
# screen.tracer(0)      # tell screen to not show automatically
# don = turtle.Turtle()
# don.speed(100)
# don.width(3)
# don.hideturtle()            # hide donatello, we only want to see the drawing
# def draw_square() :
#     # for side in range(4) :
#     don.forward(100)
#     don.lt(180)
#     don.forward(100)
#     don.lt(180)
# don.penup()
# # don.goto(-350, 0)
# don.pendown()
# while True :
# 	don.clear()
# 	draw_square()
# 	screen.update() # only now show the screen, as one of the frames
# 	don.forward(0.1)
# turtle.mainloop()
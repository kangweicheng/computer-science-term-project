import turtle

def gameover(screen = None, winner = None):
	screen.clearscreen()
	screen._delete('all')
	t = turtle.Turtle()
	t.hideturtle()
	t.write('Winner is %s'%(winner.name), font=("Arial", 32, "normal"))
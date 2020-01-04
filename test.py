import PIL.Image as image
im=image.open('player1-90.gif')
# a=int(im.size[0]*1.2),int(im.size[1]*1.5)
nim=im.resize((30,30),image.BILINEAR)
nim.save('player1.gif')
im=image.open('player2-90.gif')
# a=int(im.size[0]*1.2),int(im.size[1]*1.5)
nim=im.resize((30,30),image.BILINEAR)
nim.save('player2.gif')
# im.save('castle.gif')
# nim=im.transpose(image.ROTATE_90)
# nim.save('player2_hurt-90.gif')
# nim=im.transpose(image.ROTATE_180)
# nim.save('player2_hurt-180.gif')
# nim=im.transpose(image.ROTATE_270)
# nim.save('player2_hurt-270.gif')
#for i in range(2):
# nim=im.rotate(45,image.BILINEAR)
# nim.save('poor_gun-225.gif')

# import config,turtle
# screen=turtle.Screen()
# screen.addshape('ATK+.gif')
# screen.addshape('DEF+.gif')
# screen.addshape('HEAL.gif')
# screen.addshape('Poor Gun.gif')
# screen.addshape('Bomber.gif')
# screen.addshape('Musket.gif')
# screen.addshape('Three Muskets.gif')
# screen.addshape('Dart Goblin.gif')
# screen.addshape('Sparky.gif')
# screen.addshape('Electro Wizard.gif')
# screen.addshape('Hunter.gif')
# screen.addshape('Wizard.gif')
# screen.addshape('Ice Wizard.gif')
# def comment():
# 	# c_list=[turtle.Turtle() for i in range(13)]
# 	for i in range(13):
# 		c=turtle.Turtle()
# 		# c.hideturtle()
# 		# c.penup()
# 		c.setposition(-570,270-50*i)
# 		# c.pendown()
# 		c.shape('Sparky.gif')
# 	# for g in config.GUN_LIST:
# 	# 	g=g()
# 	# 	for c in c_list:
# 	# 		c.shape('Sparky.gif')
# 	# for c,g in zip(c_list,config.GUN_LIST):
# 	# 	g=g()
# 	# 	c.shape(f'{str(g)}.gif')
# comment()

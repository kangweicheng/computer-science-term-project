import PIL.Image as image
im=image.open('poor_gun-180.gif')
#nim=im.transpose(image.ROTATE_270)
#nim.save('poor_gun-270.gif')
#for i in range(2):
nim=im.rotate(45,image.BILINEAR)
nim.save('poor_gun-225.gif')
import PIL.Image as image
im=image.open('snowball.gif')
im.save('snowball-180.gif')
nim=im.transpose(image.ROTATE_90)
nim.save('snowball-270.gif')
nim=im.transpose(image.ROTATE_180)
nim.save('snowball-0.gif')
nim=im.transpose(image.ROTATE_270)
nim.save('snowball-90.gif')
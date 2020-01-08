import PIL.Image as image
for i in range(6):
    im=image.open(f'{i}.gif')
    w,h=im.size
    nim=im.crop((20,0,w-20,h))
    nim.save(f'{i}.gif')
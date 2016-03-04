import random
import pygame
pygame.init()

width=400
height=300
windowsize=[width,height]
screen=pygame.display.set_mode(windowsize)
clock=pygame.time.Clock()
sqrw=width/10
sqrh=height/10
done=False
while not done:
    red=random.randrange(0,256)
    green=random.randrange(0,256)
    blue=random.randrange(0,256)
    x=random.randrange(0,width,sqrw)
    y=random.randrange(0,width,sqrh)
    pygame.draw.rect(screen,(red,green,blue),(x,y,sqrw,sqrh))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    clock.tick(10)
pygame.quit()
    

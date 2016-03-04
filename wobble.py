import math
import pygame
pygame.init()


windowsize=[400,300]
screen=pygame.display.set_mode(windowsize)
clock=pygame.time.Clock()
width=200
height=200
x=windowsize[0]/2-width/2
y=windowsize[1]/2-height/2
colour=pygame.color.Color('#ff9696')
black=pygame.color.Color('#123980')

count=0
done=False
while not done:
    screen.fill(black)
    pygame.draw.ellipse(screen,colour,[x,y,width,height])
    width+=math.cos(count)*10
    x-=(math.cos(count)*10)/2
    height+=math.sin(count)*10
    y-=(math.sin(count)*10)/2
    count+=0.5
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    clock.tick(24)
pygame.quit()






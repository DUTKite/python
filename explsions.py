import pygame
pygame.init()
import random

def randomcolour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
    

windowsize=[400,300]
screen=pygame.display.set_mode(windowsize)
clock=pygame.time.Clock()
black=pygame.color.Color("#000000")
colour=randomcolour()

count=0
click=False
limit=30
pos=(0,0)


done=False
while not done:
    screen.fill(black)
    if click and count < limit:
        pygame.draw.circle(screen,colour,pos,count)
        count+=1
        if count>=limit:
            click=False
            


    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            click=True
            count=0
            colour=randomcolour()
        if event.type==pygame.QUIT:
            done=True
    pygame.display.flip()
    clock.tick(45)
pygame.quit()
print points


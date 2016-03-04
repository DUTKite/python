import math
import pygame
import random

pygame.init()
import random

def checkoffscreenx(x):
    if x>windowsize[0]:
        x=0
    elif x<0:
        x=windowsize[0]
    return x
def checkoffscreeny(y):
    if y>windowsize[1]:
        y=0
    elif y<0:
        y=windowsize[1]
    return y
def checktouching():
    """causes a mini explosion if the players are touching"""
    global x
    global ballx
    global y
    global bally

    #check if player and ball are touching
    if -10<y-bally<10 and -10<x-ballx<10:
        #draw an explosion
        pygame.draw.circle(screen,white,[x,y],15)

        xdiff=x-ballx
        ydiff=y-bally

        #check if ball is on edge of screen
        if ballx==0:
            xdiff-=5
        elif ballx==windowsize[0]:
            xdiff+=5
        if bally==0:
            ydiff-=5
        elif bally==windowsize[1]:
            ydiff+=5

        #move the ball and player
        x+=xdiff*3
        ballx-=xdiff*3
        y+=ydiff*3
        bally-=ydiff*3
        


#window setup
windowsize=[400,300]
screen=pygame.display.set_mode(windowsize)
clock=pygame.time.Clock()
#player position
x=windowsize[0]/2
y=windowsize[1]/2
#ball position
ballx=random.randrange(0,windowsize[0])
bally=random.randrange(0,windowsize[1])
#goal position
goalx=windowsize[0]/2-10
goaly=windowsize[1]/2-10
goalw=20
goalh=20

#points
points=0

#colours
red=pygame.color.Color('#FF8080')
blue=pygame.color.Color('#8080FF')
white=pygame.color.Color('#FFFFFF')
black=pygame.color.Color('#000000')
#game loop
points=0
done=False
#get current time
timestart=pygame.time.get_ticks()

while not done:
    screen.fill(black)
    #draw the goal
    pygame.draw.rect(screen,white,(goalx,goaly,goalw,goalh))
    #check ball is in goal
    if goalx<=ballx<=goalx+goalw and goaly<=bally<=goaly+goalh:
        points+=1
            
        ballx=random.randrange(0,windowsize[0])
        bally=random.randrange(0,windowsize[1])
    #draw points
    for point in range(points):
        pointx=0+point*5
        pygame.draw.rect(screen,white,(pointx,3,4,7))

    
    keys=pygame.key.get_pressed()
    #display a message when the w key is pressed
    #player movement
    if keys[pygame.K_w]:
        y-=1
    if keys[pygame.K_s]:
        y+=1
    if keys[pygame.K_a]:
        x-=1
    if keys[pygame.K_d]:
        x+=1
    #draw player
    x=checkoffscreenx(x)
    y=checkoffscreeny(y)
    ballx=checkoffscreenx(ballx)
    bally=checkoffscreeny(bally)
    pygame.draw.circle(screen,red,[x,y],6)
    #check if player is touching the ball
    checktouching()
    
    #draw player
    pygame.draw.circle(screen,blue,[ballx,bally],6)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        clock.tick(24)
        #check elapsed time
        timenow=pygame.time.get_ticks()
        if timenow-timestart>=60000:
            done=True
pygame.quit()
print"total points: "+str(points)



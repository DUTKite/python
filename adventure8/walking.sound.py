import pygame
pygame.init()
import random

def move(image1,image2):
    global count
    if count < 5:
        image = image1
    elif count >=5:
        image=image2
    if count >=10:
        count=0
    else:
        count+=1
    return image
windowsize=[400,300]
screen=pygame.display.set_mode(windowsize)
clock=pygame.time.Clock()

standing=pygame.image.load('standing.png')

down1=pygame.image.load('down1.png')
down2=pygame.image.load('down2.png')

up1=pygame.image.load('up1.png')
up2=pygame.image.load('up2.png')

left1=pygame.image.load('side1.png')
left2=pygame.image.load('side2.png')

right1=pygame.transform.flip(left1,True,False)
right2=pygame.transform.flip(left2,True,False)

teleport1=pygame.image.load('teleport1.png')
teleport2=pygame.image.load('teleport2.png')
teleport3=pygame.image.load('teleport3.png')


white=pygame.color.Color("#FFFFFF")
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(1)
teleportsound=pygame.mixer.Sound("teleport.wav")


count=0
x=0
y=0

locked=False

done=False
while not done:
    screen.fill(white)
    keys=pygame.key.get_pressed()

    if not locked:

        if keys[pygame.K_s] or keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_d]:
        
            if keys[pygame.K_s]:
                image=move(down1,down2)
                y+=1  
            if keys[pygame.K_w]:
                image=move(up1,up2)
                y-=1
            if keys[pygame.K_a]:
                image=move(left1,left2)
                x-=1
            if keys[pygame.K_d]:
                image=move(right1,right2)
                x+=1
        elif keys[pygame.K_SPACE]:
            locked=True
        
        else:
            image=standing
            count=0
    else:
        if count==0:
            teleportsound.play()
       
        if count<5:
            image=teleport1
        elif count<10:
            image=teleport2
        elif count<15:
            image=teleport3
        else:
            x=random.randrange(0,windowsize[0])
            y=random.randrange(0,windowsize[1])
            count=-1
            locked=False
        count+=1
        
    screen.blit(image,(x,y))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.display.flip()
    clock.tick(32)

pygame.quit()

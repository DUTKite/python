import pygame
pygame.init()

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

white=pygame.color.Color("#FFFFFF")

count=0
x=0
y=0

done=False
while not done:
    screen.fill(white)
    keys=pygame.key.get_pressed()

    if keys[pygame.K_s]:
        image=move(down1,down2)
        y+=1
    elif keys[pygame.K_w]:
        image=move(up1,up2)
        y-=1
    elif keys[pygame.K_a]:
        image=move(left1,left2)
        x-=1
    elif keys[pygame.K_d]:
        image=move(right1,right2)
        x+=1
    else:
        image=standing

    screen.blit(image,(x,y))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.display.flip()
    clock.tick(32)

pygame.quit()

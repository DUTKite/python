import pygame
pygame.init()
width=400
height=300

windowsize=[width,height]

screen=pygame.display.set_mode(windowsize)

pygame.display.set_caption("circles+rect")
colour=pygame.color.Color('#231974')
row=0
done=False
while not done:
    increment=255/100
    while row<=height:
        pygame.draw.rect(screen,colour,[0,row,width,increment])
        pygame.display.flip()
        if colour[1]+increment<255:
            colour[1]+=increment
        row+=increment
        
    for event in pygame.event.get():
    
        if event.type==pygame.QUIT:
            done=True
pygame.quit()

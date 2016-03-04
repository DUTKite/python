import random
import pygame
pygame.init()

def moveAnimation(image1,image2,count):
    if 10<count%20<=20:
        return image2
    else:
        return image1

def upClear(x,y):
    canMove=True

    if verticalDoorLeft<=x<=verticalDoorRight and y-1<topWall:
        canMove=True
    elif y-1<topWall:
        canMove=False
    elif (x<leftWall or x>rightWall) and y-1<middleDoorsTop:
        canMove=False

    if canMove:
        return 1
    else:
        return 0


def downClear(x,y):
    canMove=True

    if verticalDoorLeft<=x<=verticalDoorRight and bottomWall<y+1:
        canMove=True
    elif bottomWall<y+1:
        canMove=False
    elif (x<leftWall or x>rightWall) and y+1>middleDoorsBottom:
        canMove=False

    if canMove:
        return 1
    else:
        return 0

def leftClear(x,y):
    canMove=True

    if middleDoorsTop<=y<=middleDoorsBottom and x-1<leftWall:
        canMove=True
    elif x-1<leftWall:
        canMove=False
    elif (y>bottomWall or y<topWall) and x-1<verticalDoorLeft:
        canMove=False

    if canMove:
        return 1
    else:
        return 0

def rightClear(x,y):
    canMove=True

    if middleDoorsTop<=y<=middleDoorsBottom and x+1>rightWall:
        canMove=True
    elif x+1>rightWall:
        canMove=False
    elif (y>bottomWall or y<topWall) and x+1>verticalDoorRight:
        canMove=False

    if canMove:
        return 1
    else:
        return 0

def chechOffscreen(x,y):
    if x<-14:
        x=windowsize[0]-14
    elif x>windowsize[0]-14:
        x=-14

    if y<-20:
        y=windowsize[1]-20
    elif y>windowsize[1]-20:
        y=-20
    return x,y

def playersTouching():
    global pOnex,pOney,pTwox,pTwoy
    if -32<pOnex-pTwox<32 and -40<pOney-pTwoy<40:
        xDiff=pOnex-pTwox
        yDiff=pOney-pTwoy

        for dist in range(abs(xDiff)/2):
            pOneMove=leftClear(pOnex,pOney)+rightClear(pOnex,pOney)
            pTwoMove=leftClear(pTwox,pTwoy)+rightClear(pTwox,pTwoy)

            if xDiff>0:
                pOnex+=pOneMove/2*xDiff/xDiff
                pTwox+=pTwoMove/2*xDiff/xDiff
            else:
                pOnex-=pOneMove/2*xDiff/xDiff
                pTwox+=pTwoMove/2*xDiff/xDiff
                
        for dist in range(abs(yDiff)/2):
            pOneMove=upClear(pOnex,pOney)+downClear(pOnex,pOney)
            pTwoMove=upClear(pTwox,pTwoy)+downClear(pTwox,pTwoy)

            if yDiff>0:
                pOnex+=pOneMove/2*yDiff/yDiff
                pTwox+=pTwoMove/2*yDiff/yDiff
            else:
                pOnex-=pOneMove/2*yDiff/yDiff
                pTwox+=pTwoMove/2*yDiff/yDiff


def touchingCoin(x,y):
    return -32<x-coinPos[0]<20 and -40<y-coinPos[1]<20
def randomPosition():
    x=random.randrange(32,windowsize[0]-52)
    y=random.randrange(32,windowsize[1]-52)
    return x,y

windowsize=[640,384]
screen=pygame.display.set_mode(windowsize)
clock=pygame.time.Clock()


#font for points
pointFont=pygame.font.SysFont("Monospace",15)

#Variables for position etc.
pOnex=windowsize[0]/4
pOney=windowsize[1]/2
pTwox=windowsize[0]/4*3
pTwoy=windowsize[1]/2

coinPos=randomPosition()
pOnePoints=0
pTwoPoints=0

pOneCount=0
pTwoCount=0

pOneMoving=False
pTwoMoving=False

#variables for walls
leftWall=28
topWall=16
rightWall=windowsize[0]-60
bottomWall=312


middleDoorsTop=144
middleDoorsBottom=182
verticalDoorLeft=284
verticalDoorRight=verticalDoorLeft+40

#Load images
background=pygame.image.load("background.png")
background=pygame.transform.scale(background,windowsize)

light=pygame.image.load("light.png")
light=pygame.transform.scale(light,windowsize)

pOneMove1=pygame.image.load("sprite1_walking1.png")
pOneMove1=pygame.transform.scale2x(pOneMove1)

pOneMove2=pygame.image.load("sprite1_walking2.png")
pOneMove2=pygame.transform.scale2x(pOneMove2)

pOneStanding=pygame.image.load("sprite1_walking2.png")
pOneStanding=pygame.transform.scale2x(pOneStanding)


pTwoMove1=pygame.image.load("sprite2_walking1.png")
pTwoMove1=pygame.transform.scale2x(pTwoMove1)

pTwoMove2=pygame.image.load("sprite2_walking2.png")
pTwoMove2=pygame.transform.scale2x(pTwoMove2)

pTwoStanding=pygame.image.load("sprite2_walking2.png")
pTwoStanding=pygame.transform.scale2x(pTwoStanding)


coin=pygame.image.load("coin.png")
coin=pygame.transform.scale2x(coin)

#load music and sound

coinSound=pygame.mixer.Sound("coin.wav")
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

#game loop
done=False
while not done :
	#get movement
	#player 1 movement
	pOneMoving=False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_s]:
		pOney += downClear(pOnex,pOney)
		pOneMoving=True
	if keys[pygame.K_w]:
		pOney -= upClear(pOnex,pOney)
		pOneMoving=True
	if keys[pygame.K_a]:
		pOnex -= leftClear(pOnex,pOney)
		pOneMoving=True 
	if keys[pygame.K_d]:
		pOnex += rightClear(pOnex,pOney)
		pOneMoving=True

	pOnex,pOney=chechOffscreen(pOnex,pOney)

	#player 1 animation
	if pOneMoving:
		pOneCount +=1
		pOneImage=moveAnimation(pOneMove1,pOneMove2,pOneCount)
	else:
		pOneImage=pOneStanding
		
		

	#player 2 movement
	pTwoMoving=False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_DOWN]:
		pTwoy += downClear(pTwox,pTwoy)
		pTwoMoving=True
	if keys[pygame.K_UP]:
		pTwoy -= upClear(pTwox,pTwoy)
		pTwoMoving=True
	if keys[pygame.K_LEFT]:
		pTwox -= leftClear(pTwox,pTwoy)
		pTwoMoving=True 
	if keys[pygame.K_RIGHT]:
		pTwox += rightClear(pTwox,pTwoy)
		pTwoMoving=True

	pTwox,pTwoy=chechOffscreen(pTwox,pTwoy)

	#player 1 animation
	if pTwoMoving:
		pTwoCount +=1
		pTwoImage=moveAnimation(pTwoMove1,pTwoMove2,pTwoCount)
	else:
		pTwoImage=pTwoStanding
		
	#Check touching
	playersTouching()
	
	#check touching  coin
	if touchingCoin(pOnex,pOney):
		pOnePoints +=1
		coinSound.play()
	if touchingCoin(pTwox,pTwoy):
		pTwoPoints +=1
		coinSound.play()
		
	#move coin if touching 
	if touchingCoin(pOnex,pOney) or touchingCoin(pTwox,pTwoy):
		coinPos=randomPosition()
		
	#render points for display
	pOnePointLabel=pointFont.render(str(pOnePoints),1,(255,255,255))
	pTwoPointLabel=pointFont.render(str(pTwoPoints),1,(255,255,255))
	
	#update display
	screen.blit(background,(0,0))
	screen.blit(coin,coinPos)
	screen.blit(pOneImage,[pOnex,pOney])
	screen.blit(pTwoImage,[pTwox,pTwoy])
	screen.blit(pOnePointLabel,[pOnex-9,pOney-9])
	screen.blit(pTwoPointLabel,[pTwox-9,pTwoy-9])
	screen.blit(light,(0,0))
	
	pygame.display.flip()
	
	#exit
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
	clock.tick(60)
pygame.quit()

	
	


       
                
                
        
    









    

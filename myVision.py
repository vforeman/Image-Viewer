####################myVision.py
###

import sys, pygame

from pygame import * 



def main():

    # Initialise screen
    pygame.init()
    size = width, height = 600, 600
    # was 550,600

    screen = pygame.display.set_mode(size)

    screen.fill((255,255,255))
    # Makes whole screen white
    
    leftWall = pygame.Rect(0, 0, 60, 600)
    
    pygame.draw.rect(screen,(64,50,132), leftWall,0)
    # makes left wall

    rightWall = pygame.Rect(540, 0, 60, 600)

    pygame.draw.rect(screen,(60,3,26), rightWall,0)
    # makes right wall

    baseLayer = pygame.Rect(60, 480, 480, 120)

    # makes button button holder (rectangle)

    pygame.draw.rect(screen,(104,114,113), baseLayer,0)

    blueButton = pygame.Rect(100, 500, 90, 65 )

    # blueButton = pygame.Rect(100, 500, 90, 65 )
    pygame.draw.rect(screen, (0,100,0), blueButton)

    #makes blue square button

   # pygame.Rect(100, 500, 70, 45 )

    pygame.draw.circle(screen, (255,255,0), (300,530), 35)

    # yellow circle
    print "hey"
    redButton = pygame.Rect(135, 500, 70, 45 )


    pygame.draw.polygon(screen, (255,0,0), [ (440, 500), (490,550), (390,550) ])
    # [ (440, 500), (515,550), (365,550) ])

    
    
 
    
    while True :
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
if __name__ == '__main__': main()

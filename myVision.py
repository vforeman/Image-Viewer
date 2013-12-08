import sys, pygame

from pygame import time 


from pygame import * 






def swell(button, base):

    button = pygame.Rect(0, 0, 90, 65 )
    #button = pygame.Rect(100, 500, 90, 65 )

    # blueButton = pygame.Rect(100, 500, 90, 65 )
    pygame.draw.rect(base, (255,255,255), button)



    return button,
    
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



    #makes Green button
    redButton = pygame.Rect(100, 500, 90, 65 )
    pygame.draw.rect(screen, (100,0,0), redButton)

    #makes
    greenButton = pygame.Rect(250, 500, 90, 65 )
    pygame.draw.rect(screen, (0,100,0), greenButton)


    blueButton = pygame.Rect(400, 500, 90, 65 )
    pygame.draw.rect(screen, (0,0,100), blueButton)



   

    
    

    


    
    while True :
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
if __name__ == '__main__': main()

import sys, pygame

from pygame import time 


from pygame import * 






def swell(button, base):

    button = pygame.Rect(0, 0, 90, 65 )
    #button = pygame.Rect(100, 500, 90, 65 )

    # blueButton = pygame.Rect(100, 500, 90, 65 )
    pygame.draw.rect(base, (255,255,255), button)



    return button,



def swell(bl, pos):

    x,y = pos

    for b in bl:
        if b.collidepoint(x,y):
            b.inflate(30,30)

            


    




    

    
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



    #red button
    ButtonList=[]
    redButton = pygame.Rect(100, 500, 90, 65 )
    ButtonList.append(redButton)
    pygame.draw.rect(screen, (100,0,0), redButton)

    #green button
    greenButton = pygame.Rect(250, 500, 90, 65 )
    ButtonList.append(greenButton)
    pygame.draw.rect(screen, (0,100,0), greenButton)

    #blue button 
    blueButton = pygame.Rect(400, 500, 90, 65 )
    ButtonList.append(blueButton)
    pygame.draw.rect(screen, (0,0,100), blueButton)



    
    mousePos = pygame.mouse.get_pos()
    


            
            

    
    #xBound = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90)
    #yBound=()
    
        
    while True :
        pygame.display.update()
        swell(ButtonList,mousePos)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            
            


            

                print "hello"
















            
if __name__ == '__main__': main()

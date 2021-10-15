# import the pygame module, so you can use it
from typing import no_type_check
import pygame
import random
#Game Control 
screen_width = 1200
screen_height = 700
playerSpeed = 10
bulletSpeed = 2

class Zombie:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.isXForward = True
        self.isYForward = True

def moveZombieByKeyboard(zombie:Zombie):
    pass

def moveZombieAuto(zombie:Zombie):
    # modify X coordinate
    if zombie.x > screen_width - 100:
        zombie.isXForward = True

    if zombie.x < 0:
        zombie.x = screen_width + random.randint(0,100)

    if zombie.isXForward == True:
        zombie.x = zombie.x - zombie.speed
    else:
        zombie.x = zombie.x + zombie.speed
    
    # modify Y coordinate
    # if zombie.y > screen_height - 100:
    #     zombie.isYForward = False

    # if zombie.y < 100:
    #     zombie.isYForward = True

    # if zombie.isYForward == True:
    #     zombie.y = zombie.y + zombie.speed
    # else:
    #     zombie.y = zombie.y - zombie.speed

def printZombie(screen, img, imgFlipped, zombie):
    
    if zombie.isXForward == True:
        screen.blit(img, (zombie.x, zombie.y))
    else:    
        screen.blit(imgFlipped, (zombie.x, zombie.y)) 

    
# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    bg = pygame.image.load("bg.jpeg")
    bg = pygame.transform.scale(bg, (screen_width, screen_height))

    player1 = pygame.image.load("LVL1 Archer Shooting.gif")
    player1 = pygame.transform.scale(player1, (150, 80))
    player1Flipped = pygame.transform.flip(player1, True, False)
    bullet1 = pygame.image.load("ArrowLvl1.gif")
    bullet1 = pygame.transform.scale(bullet1, (20, 50))
    zombie1 = pygame.image.load("zombie1.gif")
    zombie1 = pygame.transform.scale(zombie1, (60, 60))
    zombie1Flipped = pygame.transform.flip(zombie1, True, False)


    #pygame.display.set_icon(logo) 
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((screen_width,screen_height))
     
    # define a variable to control the main loop
    running = True


    zombies = list()
    for i in range(0,2):
        zombie = Zombie(screen_width+random.randint(0,100), random.randint(50,screen_height-100), random.randint(1,1))
        zombies.append(zombie)


    player1X =0
    player1Y =0
    bullet1X =0
    bullet1Y =0
    bulletFlag = False

    # main loop
    while running:
        screen.blit(bg, (0,0))

        #move all the zombies automatically
        for zombie in zombies:
            moveZombieAuto(zombie)
            printZombie(screen, zombie1, zombie1Flipped, zombie)

        #move a player character by keyboard
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player1X = player1X - playerSpeed
        if keys[pygame.K_d]:
            player1X = player1X + playerSpeed
        if keys[pygame.K_w]:
            player1Y = player1Y - playerSpeed
        if keys[pygame.K_s]:
            player1Y = player1Y + playerSpeed
        if player1X < 0:
            player1X = 0
        if player1X > screen_width - 80:
            player1X = screen_width - 80
        if player1Y > screen_height - 80:
            player1Y = screen_height - 80
        if player1Y < 0:
            player1Y = 0
            #move bullet location.
        if keys[pygame.K_SPACE]:
            bulletFlag = True
            bullet1X = player1X    
            bullet1Y = player1Y
        if bulletFlag == True:
            bullet1X = bullet1X + bulletSpeed


        screen.blit(player1, (player1X, player1Y))
        screen.blit(bullet1, (bullet1X, bullet1Y))

        

        
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pygame.display.update()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()   
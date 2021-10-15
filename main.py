# import the pygame module, so you can use it
from typing import no_type_check
import pygame
import random
import math

from pygame.constants import KEYDOWN
#Game Control 
screen_width = 1200
screen_height = 700
playerSpeed = 10
bulletSpeed = 4
bulletDamage = 2
zombieHP = 8

class Zombie:
    def __init__(self, x, y, speed, hp):
        self.x = x
        self.y = y
        self.hp=hp
        self.speed = speed
        self.isXForward = True
        self.isYForward = True

class Bullet:
    def __init__(self, x,y, speed, damage):
        self.x = x
        self.y = y
        self.damage = damage
        self.speed = speed


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

def checkCollision(bullet:Bullet, zombies:list[Zombie]):

    for zombie in zombies:
        distance =  math.sqrt((bullet.x - zombie.x)*(bullet.x - zombie.x) + (bullet.y - zombie.y)*(bullet.y - zombie.y))
        if distance < 10:
            zombie.hp = zombie.hp - bullet.damage
            return True

    return False
    
        
    
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
    for i in range(0,4):
        zombie = Zombie(screen_width+random.randint(0,100), random.randint(50,screen_height-100), random.randint(1,1), zombieHP )
        zombies.append(zombie)


    player1X =0
    player1Y =0

    bulletList = []
    keypressed = False

    # main loop
    while running:

        keypressed = False

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.KEYDOWN:
                keypressed = True

        screen.blit(bg, (0,0))

        #move all the zombies automatically
        for zombie in zombies:
            if zombie.hp <= 0:
                zombies.remove(zombie)
            else:    
                moveZombieAuto(zombie)
                printZombie(screen, zombie1, zombie1Flipped, zombie)

        #move a player character by keyboard
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player1X = player1X - playerSpeed
        if keys[pygame.K_RIGHT]:
            player1X = player1X + playerSpeed
        if keys[pygame.K_UP]:
            player1Y = player1Y - playerSpeed
        if keys[pygame.K_DOWN]:
            player1Y = player1Y + playerSpeed
        if player1X < 0:
            player1X = 0
        if player1X > screen_width - 80:
            player1X = screen_width - 80
        if player1Y > screen_height - 80:
            player1Y = screen_height - 80
        if player1Y < 0:
            player1Y = 0


        screen.blit(player1, (player1X, player1Y))
        

        #move bullet location.
        if keys[pygame.K_SPACE] and keypressed:
            bulletList.append( Bullet(player1X, player1Y, bulletSpeed, bulletDamage) )

        for bullet in bulletList:

            if checkCollision(bullet, zombies) == True:
                bulletList.remove(bullet)
            else:
                screen.blit(bullet1, (bullet.x, bullet.y))
                bullet.x = bullet.x + bullet.speed
                if bullet.x > screen_width:
                    bulletList.remove(bullet)
        

        pygame.display.update()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()   
# import the pygame module, so you can use it
from typing import no_type_check
import pygame
import random
import math
from GIFImage import GIFImage

from pygame.constants import KEYDOWN
#Game Control 
screen_width = 1200
screen_height = 700
playerSpeed = 6
bulletSpeed = 5
bulletDamage = 3
zombieHP = 9
score= 0

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

def printZombie(screen, gifImg, zombie):

    if zombie.isXForward == True:
        gifImg.render(screen, (zombie.x, zombie.y))
    else:    
        gifImg.render(screen, (zombie.x, zombie.y))

def checkCollision(bullet:Bullet, zombies:list[Zombie]):

    for zombie in zombies:
        distance =  math.sqrt((bullet.x - zombie.x)*(bullet.x - zombie.x) + (bullet.y - zombie.y)*(bullet.y - zombie.y))
        if distance < 40:
            zombie.hp = zombie.hp - bullet.damage
            return True

    return False
    
        
    
# define a main function
def main():

    score =0

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    bg = pygame.image.load("bg.jpeg")
    bg = pygame.transform.scale(bg, (screen_width, screen_height))

    player1 = pygame.image.load("LVL1 Archer Shooting.gif")
    player1 = pygame.transform.scale(player1, (150, 80))
    player1Flipped = pygame.transform.flip(player1, True, False)
    bullet1 = pygame.image.load("ArrowLvl1.gif")
    bullet1 = pygame.transform.scale(bullet1, (40, 70))
    zombie1 = pygame.image.load("zombie1.gif")
    zombie1 = pygame.transform.scale(zombie1, (60, 60))
    zombie1Flipped = pygame.transform.flip(zombie1, True, False)

    zombie1Gif = GIFImage("zombie1.gif")
    zombie1Gif.set_scale(0.05)

    player1Gif = GIFImage("LVL1 Archer Shooting.gif")
    player1Gif.set_scale(0.15)

    pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    myfont = pygame.font.SysFont('Phosphate', 30)


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
    bulletFired = False
    bulletAnimationCount = 0

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
        if len(zombies) < 5:
            zombie = Zombie(screen_width+random.randint(0,100), random.randint(50,screen_height-100), random.randint(1,1), zombieHP )
            zombies.append(zombie)


        for zombie in zombies:
            if zombie.hp <= 0:
                zombies.remove(zombie)
                score = score + 1
            else:    
                moveZombieAuto(zombie)
                printZombie(screen, zombie1Gif, zombie)

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


        #move bullet location.
        #if space bar is pressed, print out gif image, otherwise print out static image
        if keys[pygame.K_SPACE] and keypressed:
            bulletList.append( Bullet(player1X, player1Y, bulletSpeed, bulletDamage) )
            bulletFired = True
            bulletAnimationCount = 0
            player1Gif.seek(0)
        

        if bulletFired == True:
            player1Gif.render(screen, (player1X, player1Y))
            bulletAnimationCount = bulletAnimationCount + 1

            if bulletAnimationCount > 105:
                bulletFired = False
        else:
            screen.blit(player1, (player1X, player1Y))

        for bullet in bulletList:

            if checkCollision(bullet, zombies) == True:
                bulletList.remove(bullet)
            else:
                screen.blit(bullet1, (bullet.x, bullet.y))
                bullet.x = bullet.x + bullet.speed
                if bullet.x > screen_width:
                    bulletList.remove(bullet)
        


        textsurface = myfont.render("score:"+str(score), False, (0, 0, 0))
        screen.blit(textsurface,(0,0))
        
        pygame.display.update()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()   
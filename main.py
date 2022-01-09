# import the pygame module, so you can use it
import sys
import pygame
import random
import math
from GIFImage import GIFImage
import Base
from Zombie import Zombie
from ZombieType import ZombieType
from Player import Player
import Bullet
import Gun
import Armour
import Heal
import Guide
from pygame.constants import KEYDOWN
#Game Control until we have the code to control bullet damage and reload/speed per gun and Gif. 
screen_width = 1200
screen_height = 700
playerSpeed = 6
bulletSpeed = 5
bulletDamage = 3

z1 = ZombieType("zombie1", 3, 6, 1, 1)
z2 = ZombieType("zombie2", 9, 4, 3, 2)
z3 = ZombieType("Type 3", 12, 5, 5, 3)
z4 = ZombieType("Type 4", 16, 7, 10, 4)
z5 = ZombieType("Type Boss 1", 30, 6, 20, 5)
z6 = ZombieType("Type Boss 2", 45, 6, 30, 6)
z7 = ZombieType("Type Boss 3", 60, 5, 45, 7)
z8 = ZombieType("Type Mega Boss 1", 100, 5, 80, 8)
z9 = ZombieType("Type Mega Boss 2", 150, 4, 130, 9)
z10 = ZombieType("Type Heavy Boss 1", 300, 4, 280, 10)
z11 = ZombieType("Type Extreme Heavy Boss", 800, 3, 780, 11)
z12 = ZombieType("Type Fast Boss", 100, 6, 80, 12)



class Bullet:
    def __init__(self, x, y, speed, damage):
        self.x = x
        self.y = y
        self.damage = damage
        self.speed = speed

def moveZombieByKeyboard(zombie:Zombie):
    pass

def moveZombieAuto(zombie:Zombie, player:Player):
    # modify X coordinate
    if zombie.x > screen_width - 100:
        zombie.isXForward = True

    if zombie.isXForward == True:
        zombie.x = zombie.x - zombie.speed
        if zombie.x < 5: 
            player.hp = player.hp - zombie.damage
            zombie.x = screen_width + random.randint(0,100)


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


def drawBackground(backgroundNo, screen):

    if backgroundNo == 0:
        bg = pygame.image.load("bg.jpeg").convert()
        bg = pygame.transform.scale(bg, (screen_width, screen_height))
    elif backgroundNo == 1:
        bg = pygame.image.load("bg2.png").convert()
        bg = pygame.transform.scale(bg, (screen_width, screen_height))
    else:
        bg = pygame.image.load("bg3.png").convert()
        bg = pygame.transform.scale(bg, (screen_width, screen_height))

    screen.blit(bg, (0,0))

    
# define a main function
def main():

    player = Player()

    # initialize the pygame module
    pygame.init()
    # load and set the logo

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
    zombie2Gif = GIFImage("zombie2.gif")
    zombie2Gif.set_scale(0.2)

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


    zombies = []
    for i in range(0,4):
    
        #def __init__(self, x, y, speed, hp):
        #  type, hp, speed, money):
        zombie = Zombie(z1, screen_width+random.randint(0,100), random.randint(50,screen_height-100))
        zombies.append(zombie)

    bulletList = []
    keypressed = False
    bulletFired = False
    bulletAnimationCount = 0

    backgroundNo = random.randint(0,2)
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

        drawBackground(backgroundNo, screen)
        
        #move all the zombies automatically
        if len(zombies) < 5:
            zombie = Zombie(z2, screen_width+random.randint(0,100), random.randint(50,screen_height-100) )
            zombies.append(zombie)


        for zombie in zombies:
            if zombie.hp <= 0:
                zombies.remove(zombie)
                player.score = player.score + 1
                player.coin= player.coin + zombie.coin
            else:    
                moveZombieAuto(zombie, player)
                if zombie.zombieImageName == "zombie1":
                    printZombie(screen, zombie1Gif, zombie)

                if zombie.zombieImageName == "zombie2":
                    printZombie(screen, zombie2Gif, zombie)

        #move a player character by keyboard
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x = player.x - playerSpeed
        if keys[pygame.K_RIGHT]:
            player.x = player.x + playerSpeed
        if keys[pygame.K_UP]:
            player.y = player.y - playerSpeed
        if keys[pygame.K_DOWN]:
            player.y = player.y + playerSpeed
        if player.x < 0:
            player.x = 0
        if player.x > screen_width - 80:
            player.x = screen_width - 80
        if player.y > screen_height - 80:
            player.y = screen_height - 80
        if player.y < 0:
            player.y = 0


        #move bullet location.
        #if space bar is pressed, print out gif image, otherwise print out static image
        if keys[pygame.K_SPACE] and keypressed:
            bulletList.append( Bullet(player.x, player.y, bulletSpeed, bulletDamage) )
            bulletFired = True
            bulletAnimationCount = 0
            player1Gif.seek(0)
        

        if bulletFired == True:
            player1Gif.render(screen, (player.x, player.y))
            bulletAnimationCount = bulletAnimationCount + 1

            if bulletAnimationCount > 105:
                bulletFired = False
        else:
            screen.blit(player1, (player.x, player.y))

        for bullet in bulletList:

            if checkCollision(bullet, zombies) == True:
                bulletList.remove(bullet)
            else:
                screen.blit(bullet1, (bullet.x, bullet.y))
                bullet.x = bullet.x + bullet.speed
                if bullet.x > screen_width:
                    bulletList.remove(bullet)
        
        
            

        textsurface = myfont.render("score:"+str(player.score) + " coin:" + str(player.coin) + "hp:" + str(player.hp), False, (0, 0, 0))
        screen.blit(textsurface,(0,0))

        
        pygame.display.update()

        
        if player.hp < 0:
            sys.exit()
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()   
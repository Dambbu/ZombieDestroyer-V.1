import pygame
import sys
import Beginner's_Guide md.
pygame.init()
myfont = pygame.font.SysFont("Times New Roman, 14")
keys=pygame.key.get_pressed()
while True:
    for event in pygame.event.get():
        if keys[pygame.K_K]:
            if keys[pygame.K_K] and keypressed:
                keypressed = label = myfont.render("Beginner'sGuide.md", 1, (255,255,0))
        screen.blit(label, (100, 100))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
 


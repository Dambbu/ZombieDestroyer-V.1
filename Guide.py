import pygame
import sys
from pygame.constants import KEYDOWN
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Phosphate', 30)


screen_width = 800
screen_height = 600
keys=pygame.key.get_pressed()
screen = pygame.display.set_mode((screen_width,screen_height))
label = myfont.render("Guide.md", 1, (255,255,0))
while True:
    for event in pygame.event.get():
        if keys[pygame.K_k]:
            if keys[pygame.K_k]:
                label = myfont.render("Guide.md", 1, (255,255,0))
        screen.blit(label, (100, 100))
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

 


import pygame
import sys
pygame.font.init()
myfont = pygame.font.SysFont('Phosphate', 30)


keys=pygame.key.get_pressed()
while True:
    for event in pygame.event.get():
        if keys[pygame.K_K]:
            if keys[pygame.K_K] and keypressed:
                keypressed = label = myfont.render("Guide.md", 1, (255,255,0))
        screen.blit(label, (100, 100))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
 


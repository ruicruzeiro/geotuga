import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((560,838))
pygame.display.set_caption("Geotuga")
clock = pygame.time.Clock()
title_font = pygame.font.Font("font/FFF_Tusj.ttf", 40)

map_surf = pygame.image.load("graphics/portugal_clr.png")
text_surf = title_font.render("GeoTuga", True, "bisque4")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(map_surf, (0, 0))
    screen.blit(text_surf, (20, 20))

    pygame.display.update()
    clock.tick(60)

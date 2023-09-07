
import pygame
from start import first, playtext, starttext
from text import name


def dialogue(a, screen, font, protagonist, npc_list):
    protagonist.player_image = protagonist.frame_0
    pygame.event.clear(pygame.MOUSEBUTTONDOWN)
    pygame.event.clear(pygame.KEYDOWN)
    run = True
    starttext(screen, a, font, protagonist, npc_list)
    pygame.event.clear()
    while run:
        k = 0
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.clear()
                k = playtext(screen, font, protagonist, npc_list)
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if k == 1:
                run = False
    return 1
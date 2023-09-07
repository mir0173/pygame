import pygame
from start import first, playtext, starttext
from text import name


def dialogue(a, screen, font, protagonist):
    protagonist.player_image = protagonist.frame_0
    pygame.event.clear(pygame.MOUSEBUTTONDOWN)
    pygame.event.clear(pygame.KEYDOWN)
    run = True
    starttext(screen, a, font, protagonist)
    pygame.event.clear()
    i = 1
    while run:
        clock = pygame.time.Clock()
        dt = clock.tick(60)
        k = 0
        for event in pygame.event.get():
            if i == 0 and (event.type == pygame.MOUSEBUTTONDOWN or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)):
                pygame.event.clear()
                k = playtext(screen, font, protagonist)
                i = 1
            if i != 0:
                i += 1
                if i == 5:
                    i = 0
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if k == 1:
                run = False
    pygame.event.clear()
    return 1

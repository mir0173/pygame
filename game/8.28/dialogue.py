# 실질적 실행파일입니다.

import pygame
from start import first, playtext, starttext
from text import name


def main(a, screen, fontObj, fontObj2, fontObj3, protagonist):
    protagonist.player_image = protagonist.frame_0
    pygame.event.clear(pygame.MOUSEBUTTONDOWN)
    pygame.event.clear(pygame.KEYDOWN)
    run = True
    starttext(screen, a, fontObj, fontObj2, fontObj3, protagonist)
    pygame.event.clear()
    while run:
        k = 0
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.clear()
                k = playtext(screen, fontObj, fontObj2, fontObj3, protagonist)
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if k == 1:
                run = False
    print('b')
    return 1

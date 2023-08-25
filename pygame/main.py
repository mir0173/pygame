#실질적 실행파일입니다.

import pygame
from start import first, playtext, starttext
from text import background, bgpos, name
a = 20

def main():
    global a
    #first()
    pygame.event.clear(pygame.MOUSEBUTTONDOWN)
    pygame.event.clear(pygame.KEYDOWN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.clear()
                playtext()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    starttext(a, background[a], bgpos[a])
                    pygame.event.clear()
                    a += 1



main()

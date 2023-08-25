#실질적 실행파일입니다.

import pygame
from start import  playtext, starttext
from text import background, bgpos


def main():
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
                    starttext(20, background[20], bgpos)
                    pygame.event.clear()



main()

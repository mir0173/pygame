import pygame

import B2
import B4
import B5
import B6
from system import restart, restartok
from start import first
from sprite import protagonist

pygame.init()
fontObj = pygame.font.SysFont("malgungothic", 32)
fontObj2 = pygame.font.SysFont("malgungothic", 46)
fontObj3 = pygame.font.Font("freesansbold.ttf", 40)
fontObj4 = pygame.font.Font("freesansbold.ttf", 128)
font = [fontObj, fontObj2, fontObj3, fontObj4]
key2 = 0

def main():
    global lista, key2
    screen = pygame.display.set_mode((1600, 900))
    character_right = pygame.image.load('./assets/protagonist_male.png').convert_alpha()
    character_left = pygame.image.load('./assets/protagonist_male2.png').convert_alpha()
    while True:
        pygame.mouse.set_visible(False)
        restartok()
        key = first(screen, font, protagonist)
        key2 = restart()
        if key2 != 1 and key > 5:
            a = B6.B6(screen, font)
            a.tutorial(character_left, character_right)
        key2 = restart()
        if key2 != 1 and key > 4:
            screen.blit(pygame.transform.scale(pygame.image.load('./assets/black.png'), (160 * 10, 90 * 10)), (0, 0))
            pygame.display.update()
            ladder = pygame.mixer.Sound('./assets/ladder sound.mp3')
            ladder.play()
            pygame.time.wait(4000)
            b = B5.B5(screen, font)
            b.story(character_left, character_right)
        key2 = restart()
        if key2 != 1 and key > 3:
            c = B4.B4(screen, font)
            c.story(character_left, character_right)
        key2 = restart()
        '''if key2 != 1 and key > 1:
            e = B2.B2(screen, font)
            e.story(character_left, character_right)
        key2 = restart()'''


main()

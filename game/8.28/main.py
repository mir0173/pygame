import pygame
import B6
import start

pygame.init()
fontObj = pygame.font.SysFont("malgungothic", 32)
fontObj2 = pygame.font.SysFont("malgungothic", 46)
fontObj3 = pygame.font.Font("freesansbold.ttf", 64)


def main():
    screen = pygame.display.set_mode((1600, 900))
    character_right = pygame.image.load('./assets/protagonist_male.png').convert_alpha()
    character_left = pygame.image.load('./assets/protagonist_male2.png').convert_alpha()
    start.first(screen)
    a = B6.B6(screen, fontObj, fontObj2, fontObj3)
    a.tutorial(character_left, character_right)


main()

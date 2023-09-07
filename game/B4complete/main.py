import pygame

import B2
import B4
import B5
import B6
import start

pygame.init()
fontObj = pygame.font.SysFont("malgungothic", 32)
fontObj2 = pygame.font.SysFont("malgungothic", 46)
fontObj3 = pygame.font.Font("freesansbold.ttf", 40)

font = [fontObj, fontObj2, fontObj3]


def main():
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((1600, 900))
    character_right = pygame.image.load('./assets/protagonist_male.png').convert_alpha()
    character_left = pygame.image.load('./assets/protagonist_male2.png').convert_alpha()
    # start.first(screen)
    a = B6.B6(screen, font)
    # a.tutorial(character_left, character_right)
    # screen.blit(pygame.transform.scale(pygame.image.load('./assets/black.png'), (160 * 10, 90 * 10)), (0, 0))
    # pygame.display.update()
    # ladder = pygame.mixer.Sound('./assets/ladder sound.mp3')
    # ladder.play()
    # pygame.time.wait(4000)
    b = B5.B5(screen, font)
    # b.story(character_left, character_right)
    # screen.blit(pygame.transform.scale(pygame.image.load('./assets/black.png'), (160 * 10, 90 * 10)), (0, 0))
    # pygame.display.update()

    c = B4.B4(screen, font)
    # c.story(character_left, character_right)

    e = B2.B2(screen, font)
    e.story(character_left, character_right)


main()

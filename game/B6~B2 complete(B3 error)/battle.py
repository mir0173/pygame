import pygame
from battle_sprite import Protagonist
from battle_sprite import Michael, Michael_final


def Battle_Phase_1():
    pygame.init()
    # pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((1600, 900))
    character_right = pygame.image.load('./assets/protagonist_male_attack.png').convert_alpha()
    character_left = pygame.image.load('./assets/protagonist_male_attack2.png').convert_alpha()
    michael_right = pygame.image.load('./assets/michael1.png').convert_alpha()
    michael_left = pygame.image.load('./assets/michael2.png').convert_alpha()
    protagonist = Protagonist(character_left, character_right, 0)
    michael = Michael(michael_left, michael_right, 0)

    run = True
    while run:

        clock = pygame.time.Clock()
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        mouse = pygame.mouse.get_pressed()[0]
        protagonist.move(screen, dt, 0.6)
        protagonist.update(screen)
        michael.move(screen, dt, 0.6)
        michael.update(screen, protagonist)
        protagonist.attack(screen, [michael], mouse)
        pygame.display.update()

        if protagonist.health <= 0:
            return 0
        if michael.health <= 0:
            return 1


def Battle_Phase_2():
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((1600, 900))
    character_right = pygame.image.load('./assets/protagonist_male_attack.png').convert_alpha()
    character_left = pygame.image.load('./assets/protagonist_male_attack2.png').convert_alpha()
    protagonist = Protagonist(character_left, character_right, 0)
    michael_final = Michael_final(0, protagonist)

    run = True
    while run:

        clock = pygame.time.Clock()
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        mouse = pygame.mouse.get_pressed()[0]
        protagonist.move(screen, dt, 0.6)
        protagonist.update(screen)
        michael_final.update(screen, protagonist)
        protagonist.attack(screen, (
        michael_final, michael_final.sword_gun_1, michael_final.sword_gun_2, michael_final.sword_gun_3), mouse)
        pygame.display.update()

        if protagonist.health <= 0:
            return 0
        if michael_final.health <= 0:
            return 1

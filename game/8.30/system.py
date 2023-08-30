import pygame
from background import background_list
from background import obstacle_list
from background import movable
from background import movable_image

pausepopup = pygame.image.load('./assets/pause.png')
pauseresume = pygame.image.load('./assets/pause_resume.png')
pausemain = pygame.image.load('./assets/pause_main.png')


def esc(floor, screen, font, protagonist):
    floor.pause = True
    for i in range(6):
        clock = pygame.time.Clock()
        dt = clock.tick(60)
        update(screen, font, protagonist)
        screen.blit(pausepopup, (500, 900 - 130 * i))
        pygame.display.update()


def resume(floor, screen, font, protagonist):
    update(screen, font, protagonist)
    pos = pygame.mouse.get_pos()
    if 600 <= pos[0] <= 700 and 500 <= pos[1] <= 600:
        screen.blit(pauseresume, (500, 250))
    elif 900 <= pos[0] <= 1000 and 500 <= pos[1] <= 600:
        screen.blit(pausemain, (500, 250))
    else:
        screen.blit(pausepopup, (500, 250))
    pygame.display.update()
    click = pygame.mouse.get_pressed()
    if 600 <= pos[0] <= 700 and 500 <= pos[1] <= 600 and click[0] == 1:
        for i in range(6):
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            update(screen, font, protagonist)
            screen.blit(pausepopup, (500, 250 + 130 * i))
            pygame.display.update()
        floor.pause = False
    if 900 <= pos[0] <= 1000 and 500 <= pos[1] <= 600 and click[0] == 1:
        floor.tostart = True


def update(screen, font, protagonist):
    protagonist.frame_0.set_alpha(protagonist.alpha)
    protagonist.frame_1.set_alpha(protagonist.alpha)
    protagonist.frame_2.set_alpha(protagonist.alpha)
    protagonist.frame_3.set_alpha(protagonist.alpha)
    protagonist.frame_4.set_alpha(protagonist.alpha)
    protagonist.frame_5.set_alpha(protagonist.alpha)
    protagonist.frame_6.set_alpha(protagonist.alpha)
    protagonist.frame_7.set_alpha(protagonist.alpha)
    protagonist.frame_8.set_alpha(protagonist.alpha)
    protagonist.frame_9.set_alpha(protagonist.alpha)
    protagonist.animation_list = [protagonist.frame_1, protagonist.frame_2, protagonist.frame_3, protagonist.frame_2]
    protagonist.animation_list2 = [protagonist.frame_8, protagonist.frame_7, protagonist.frame_6, protagonist.frame_7]
    protagonist.background = background_list[protagonist.screen_number]
    protagonist.obstacle = obstacle_list[protagonist.screen_number]
    protagonist.movable = movable[protagonist.screen_number]
    protagonist.movable_image = movable_image[protagonist.screen_number]
    screen.blit(protagonist.background, (0, 0))
    screen.blit(protagonist.player_image, protagonist.player)
    E = pygame.transform.scale(pygame.image.load('./assets/E.png'), (40, 40))
    for i in range(len(protagonist.interact)):
        screen.blit(E, (protagonist.interact[i].centerx + 20, protagonist.interact[i].centery + 20))
    protagonist.movable_obstacle(screen)

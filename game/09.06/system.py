import pygame
from background import background_list
from background import obstacle_list
from background import movable
from background import movable_image

index = [[6, 1, 0], [6, 1, 0], [6, 1, 0], [6, 2, 0], [6, 2, 0], [6, 3, 0], [6, 3, 0], [5, 1, 1], [5, 1, 1], [5, 2, 1],
         [5, 2, 1], [5, 2, 1], [5, 2, 1], [5, 3, 1], [5, 3, 1], [5, 3, 1], [5, 3, 1], [5, 4, 1], [5, 4, 1], [4, 1, 2],
         [4, 2, 2], [4, 3, 2], [4, 3, 2], [4, 3, 2], [4, 4, 2], [4, 5, 2]]

BLACK = pygame.Color(0, 0, 0)
pausepopup = pygame.image.load('./assets/pause.png')
pausepopup = pygame.transform.scale(pausepopup, (1600, 900))
pausepopup.set_colorkey(BLACK)
pauseresume = pygame.image.load('./assets/pause_resume.png')
pauseresume = pygame.transform.scale(pauseresume, (1600, 900))
pauseresume.set_colorkey(BLACK)
pauseexit = pygame.image.load('./assets/pause_exit.png')
pauseexit = pygame.transform.scale(pauseexit, (1600, 900))
pauseexit.set_colorkey(BLACK)
pausemain = pygame.image.load('./assets/pause_main.png')
pausemain = pygame.transform.scale(pausemain, (1600, 900))
pausemain.set_colorkey(BLACK)


def esc(floor, screen, font, protagonist):
    pygame.mouse.set_visible(True)
    floor.pause = True
    for i in range(6):
        clock = pygame.time.Clock()
        dt = clock.tick(60)
        update(screen, font, protagonist)
        screen.blit(pausepopup, (0, 900 - 150 * i))
        screen.blit(pausemain, (96 - 16 * i, -5))
        pygame.display.update()


def resume(floor, screen, font, protagonist):
    update(screen, font, protagonist)
    pos = pygame.mouse.get_pos()
    if 647 <= pos[0] <= 951 and 290 <= pos[1] <= 363:
        screen.blit(pauseresume, (0, 0))
        screen.blit(pausemain, (0, -5))
    elif 697 <= pos[0] <= 901 and 478 <= pos[1] <= 552:
        screen.blit(pauseexit, (0, 0))
        screen.blit(pausemain, (0, -5))
    else:
        screen.blit(pausepopup, (0, 0))
        screen.blit(pausemain, (0, -5))
    pygame.display.update()
    click = pygame.mouse.get_pressed()
    if 647 <= pos[0] <= 951 and 290 <= pos[1] <= 363 and click[0] == 1:
        for i in range(6):
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            update(screen, font, protagonist)
            screen.blit(pausepopup, (0, 0 + 150 * i))
            screen.blit(pausemain, (0 + 16 * i, -5))
            pygame.display.update()
        floor.pause = False
        pygame.mouse.set_visible(False)
    if 697 <= pos[0] <= 901 and 478 <= pos[1] <= 552 and click[0] == 1:
        floor.tostart = True
        pygame.mouse.set_visible(False)


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
        screen.blit(E, (protagonist.interact[i].centerx - 20, protagonist.interact[i].centery - 20))
    text = font[2].render(f"{index[protagonist.screen_number][0]} - {index[protagonist.screen_number][1]}", True,
                          (255, 255, 255))
    screen.blit(protagonist.uilist[index[protagonist.screen_number][2]], (0, 0))
    screen.blit(text, (320, 50, 0, 0))
    protagonist.movable_obstacle(screen)

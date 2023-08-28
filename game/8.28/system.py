import pygame

pausepopup = pygame.image.load('./assets/pause.png')
pauseresume = pygame.image.load('./assets/pause_resume.png')
pausemain = pygame.image.load('./assets/pause_main.png')


def esc(floor, screen, protagonist):
    floor.pause = True
    for i in range(6):
        clock = pygame.time.Clock()
        dt = clock.tick(60)
        protagonist.update(screen)
        screen.blit(pausepopup, (500, 900 - 130 * i))
        pygame.display.update()


def resume(floor, screen, protagonist):
    protagonist.update(screen)
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
            protagonist.update(screen)
            screen.blit(pausepopup, (500, 250 + 130 * i))
            pygame.display.update()
        floor.pause = False
    if 900 <= pos[0] <= 1000 and 500 <= pos[1] <= 600 and click[0] == 1:
        floor.tostart = True

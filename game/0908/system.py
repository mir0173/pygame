import pygame
from background import background_list
from background import obstacle_list
from background import movable
from background import movable_image

index = [[6, 1, 0], [6, 1, 0], [6, 1, 0], [6, 2, 0], [6, 2, 0], [6, 3, 0], [6, 3, 0], [5, 1, 1], [5, 1, 1], [5, 2, 1],
         [5, 2, 1], [5, 2, 1], [5, 2, 1], [5, 3, 1], [5, 3, 1], [5, 3, 1], [5, 3, 1], [5, 4, 1], [5, 4, 1], [4, 1, 2],
         [4, 2, 2], [4, 3, 2], [4, 3, 2], [4, 3, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2],
         [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2],
         [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2], [4, 4, 2],
         ]

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
pausesave = pygame.image.load('./assets/pause_save.png')
pausesave = pygame.transform.scale(pausesave, (1600, 900))
pausesave.set_colorkey(BLACK)
saveup = pygame.image.load('./assets/saveup.png')
saveup = pygame.transform.scale(saveup, (1600, 900))
saveup.set_colorkey(BLACK)
savedown = pygame.image.load('./assets/savedown.png')
savedown = pygame.transform.scale(savedown, (1600, 900))
savedown.set_colorkey(BLACK)
saving = pygame.image.load('./assets/saving.png')
saving = pygame.transform.scale(saving, (1600, 900))
saving.set_colorkey(BLACK)
savegame = pygame.image.load('./assets/save.png')
savegame = pygame.transform.scale(savegame, (1600, 900))
savegame.set_colorkey(BLACK)
save5 = pygame.image.load('./assets/save5.png')
save5 = pygame.transform.scale(save5, (1600, 900))
save5.set_colorkey(BLACK)
save51 = pygame.image.load('./assets/save51.png')
save51 = pygame.transform.scale(save51, (1600, 900))
save51.set_colorkey(BLACK)
save52 = pygame.image.load('./assets/save52.png')
save52 = pygame.transform.scale(save52, (1600, 900))
save52.set_colorkey(BLACK)
save53 = pygame.image.load('./assets/save53.png')
save53 = pygame.transform.scale(save53, (1600, 900))
save53.set_colorkey(BLACK)
key = 0
saveindex = 0
floornow = [0, 0, 0, 0, 0, 0]
isc = 0
indexc = 0

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

def esc1(screen, font, protagonist):
    for i in range(6):
        clock = pygame.time.Clock()
        dt = clock.tick(60)
        update(screen, font, protagonist)
        screen.blit(pausepopup, (0, 0 + 150 * i))
        screen.blit(pausemain, (0 + 16 * i, -5))
        pygame.display.update()

def save(screen, font, protagonist, number):
    global saveindex, floornow, indexc
    saveindex = 0
    X = True
    while X:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if 282 <= pos[0] <= 347 and 641 <= pos[1] <= 705:
                if saveindex == 4:
                    screen.blit(save51, (0, 0))
                else:
                    screen.blit(saveup, (0, 0))
            elif 352 <= pos[0] <= 421 and 641 <= pos[1] <= 705:
                if saveindex == 4:
                    screen.blit(save52, (0, 0))
                else:
                    screen.blit(savedown, (0, 0))
            elif 1144 <= pos[0] <= 1351 and 641 <= pos[1] <= 705:
                if saveindex == 4:
                    screen.blit(save53, (0, 0))
                else:
                    screen.blit(saving, (0, 0))
            else:
                if saveindex == 4:
                    screen.blit(save5, (0, 0))
                else:
                    screen.blit(savegame, (0, 0))
            if floornow[saveindex] != 0:
                textfloor1 = font[3].render(f"B{floornow[saveindex]}", True, (1, 1, 1))
                screen.blit(textfloor1, (299, 327, 0, 0))
            textindex1 = font[2].render(f"{saveindex + 1}", True, (1, 1, 1))
            screen.blit(textindex1, (1307, 327, 0, 0))
            if floornow[saveindex + 1] != 0 and saveindex != 4:
                textfloor2 = font[3].render(f"B{floornow[saveindex + 1]}", True, (1, 1, 1))
                screen.blit(textfloor2, (299, 497, 0, 0))
            if saveindex != 4:
                textindex2 = font[2].render(f"{saveindex + 2}", True, (1, 1, 1))
                screen.blit(textindex2, (1307, 497, 0, 0))
            pygame.display.update()
            click = pygame.mouse.get_pressed()
            if 282 <= pos[0] <= 347 and 641 <= pos[1] <= 705 and click[0] == 1 and saveindex > 0:
                saveindex -= 1
            if 352 <= pos[0] <= 421 and 641 <= pos[1] <= 705 and click[0] == 1 and saveindex < 4:
                saveindex += 1
            if 1144 <= pos[0] <= 1351 and 641 <= pos[1] <= 705 and click[0] == 1 and number == 1:
                if protagonist.screen_number >= 0 and protagonist.screen_number <= 6:
                    floornow[saveindex] = 6
                elif protagonist.screen_number >= 7 and protagonist.screen_number <= 18:
                    floornow[saveindex] = 5
                elif protagonist.screen_number >= 19 and protagonist.screen_number <= 25:
                    floornow[saveindex] = 4
                elif protagonist.screen_number >= 34 and protagonist.screen_number <= 41:
                    floornow[saveindex] = 2
                    if indexc == 0:
                        isc[saveindex] = 0
                    elif indexc == 1:
                        isc[saveindex] = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return (-1, 0)
                if event.key == pygame.K_RETURN:
                    if floornow[saveindex] != 0:
                        return (floornow[saveindex], indexc)
            if event.type == pygame.QUIT:
                pygame.quit()

def havec():
    global indexc
    indexc = 1

def nothavec():
    global indexc
    indexc = 0
def resume(floor, screen, font, protagonist):
    global key
    update(screen, font, protagonist)
    pos = pygame.mouse.get_pos()
    if 647 <= pos[0] <= 951 and 290 <= pos[1] <= 364:
        screen.blit(pauseresume, (0, 0))
        screen.blit(pausemain, (0, -5))
    elif 697 <= pos[0] <= 901 and 384 <= pos[1] <= 458:
        screen.blit(pausesave, (0, 0))
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
    if 697 <= pos[0] <= 901 and 384 <= pos[1] <= 458 and click[0] == 1:
        save(screen, font, protagonist, 1)
    if 697 <= pos[0] <= 901 and 478 <= pos[1] <= 552 and click[0] == 1:
        floor.tostart = True
        pygame.mouse.set_visible(False)
        key = 1


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


def restart():
    global key
    if key == 1:
        return 1
    else:
        return 0

def restartok():
    global key
    pygame.time.wait(20)
    key = 0
import pygame
import math
from diaryinteraction import diary
from system import update

gray = pygame.Rect(0, 0, 0, 0)
nonejournal = pygame.Rect(560, 200, 0, 0)
textx = pygame.Rect(660, 720, 0, 0)
texty = pygame.Rect(720, 720, 0, 0)
textjournal = pygame.Rect(625, 720, 0, 0)
diary1pos = pygame.Rect(370, 183, 0, 0)
diary2pos = pygame.Rect(760, 183, 0, 0)

def interaction(player, object):
    distance = math.sqrt((player.centerx - object.centerx) ** 2 + (player.centery - object.centery) ** 2)
    key_INPUT = pygame.key.get_pressed()
    a = 0
    if a == 0 and key_INPUT[pygame.K_e] and distance < 200:
        a = 1
    if a == 1 and key_INPUT[pygame.K_x]:
        a = 0
    if a == 0 and distance < 200:
        return 1
    elif a == 1 and distance < 200:
        return 2
    return 0

def diaryinter (player, wadpos, background, font, number, count, protagonist):
    WHITE = (255, 255, 255)
    textsurfaceObj1 = font[3].render("Interact with the E key.", True, WHITE)
    textclickx = font[3].render("Out with the X key", True, WHITE)
    textclicky = font[3].render("Press Right key to go to the next page", True, WHITE)
    image_gray = pygame.image.load('./assets/gray.png')
    Gray = pygame.transform.scale(image_gray, (1600, 900))
    Gray.set_alpha(175)
    havenote = 0
    a = True
    n = 0
    while a:

        tsObj = textsurfaceObj1
        havediary = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result1 = math.sqrt(math.pow(player.centerx - wadpos.centerx, 2) + math.pow(player.centery - wadpos.centery, 2))
        key_INPUT = pygame.key.get_pressed()
        print(1)
        print(result1)
        print(havenote)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if key_INPUT[pygame.K_e] and result1 < 100 and havenote == 0:
                k = 0
                havenote += 1
                while( count < n ):
                    havediary[number + n] = 1
                    n += 1

            if key_INPUT[pygame.K_x]:
                if havenote == 1 and k == count - 1:
                    havenote += 1
                    a = False
            if key_INPUT[pygame.K_z] and havenote != 1:
                diaryindex = 0
                if havenote == 0:
                    havenote = 3
                if havenote == 2:
                    havenote = 4
            if key_INPUT[pygame.K_x] and  havenote != 1 and k == count - 1:
                if havenote == 3:
                    havenote = 0
                if havenote == 4:
                    havenote = 2
            if key_INPUT[pygame.K_LEFT] and (havenote == 3 or  havenote == 4) and  havenote != 1 and diaryindex > 0:
                diaryindex -= 2
            if key_INPUT[pygame.K_RIGHT] and (havenote == 3 or havenote == 4) and  havenote != 1 and diaryindex < 14:
                diaryindex += 2
            if key_INPUT[pygame.K_RIGHT] and havenote == 1 and k < count - 1:
                k += 1

            if result1 < 100:
                if havenote == 0:
                    update(background, font, protagonist)
                    background.blit(tsObj, wadpos)
                if havenote == 1:
                    background.blit(Gray, gray)
                    background.blit(diary[number + k], nonejournal)
                    if k == count - 1:
                        update(background, font, protagonist)
                        background.blit(Gray, gray)
                        background.blit(diary[number + k], nonejournal)
                        background.blit(textclickx, texty)
                    else :
                        update(background, font, protagonist)
                        background.blit(Gray, gray)
                        background.blit(diary[number + k], nonejournal)
                        background.blit(textclicky, textx)
            pygame.display.update()
    return 5

    '''if (havenote == 3 or havenote == 4):
            background.blit(image_gray, gray)
            if (havediary[diaryindex] == 1):
                background.blit(diary[diaryindex], diary1pos)
            else:
                background.blit(diary[14], diary1pos)
            if (havediary[diaryindex + 1] == 1):
                background.blit(diary[diaryindex + 1], diary2pos)
            else:
                background.blit(diary[15], diary2pos)'''
    #이 주석은 인벤토리 기능인데 잠시 지워놨슴다 그이유는 위에거에 4시간을 박았기 때문이죠 지우지 말아주십시요ㅠㅠ
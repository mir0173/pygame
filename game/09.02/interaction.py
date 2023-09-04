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
havediary = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
owndiary = []
left = pygame.transform.scale(pygame.image.load('./assets/left.png'), (40, 40))
right = pygame.transform.scale(pygame.image.load('./assets/right.png'), (40, 40))


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


def diaryinter(screen, font, number, start, end, protagonist):
    image_gray = pygame.image.load('./assets/gray.png')
    Gray = pygame.transform.scale(image_gray, (1600, 900))
    Gray.set_alpha(175)
    update(screen, font, protagonist)
    screen.blit(Gray, gray)
    screen.blit(diary[number - 1], nonejournal)
    havediary[number - 1] = 1
    key_INPUT = pygame.key.get_pressed()
    if number > start:
        screen.blit(left, (500, 500))
    if number < end:
        screen.blit(right, (1100, 500))
    pygame.display.update()
    if key_INPUT[pygame.K_x]:
        if number == end:
            return -1
    if key_INPUT[pygame.K_RIGHT]:
        if number < end:
            return number + 1
    if key_INPUT[pygame.K_LEFT]:
        if number > start:
            return number - 1
    return number


'''if key_INPUT[pygame.K_z] and havenote != 1:
        diaryindex = 0
        if havenote == 0:
            havenote = 3
        if havenote == 2:
            havenote = 4
    if key_INPUT[pygame.K_x] and havenote != 1 and k == count - 1:
        if havenote == 3:
            havenote = 0
        if havenote == 4:
            havenote = 2
    if key_INPUT[pygame.K_LEFT] and (havenote == 3 or havenote == 4) and havenote != 1 and diaryindex > 0:
        diaryindex -= 2
    if key_INPUT[pygame.K_RIGHT] and (havenote == 3 or havenote == 4) and havenote != 1 and diaryindex < 14:
        diaryindex += 2
    if key_INPUT[pygame.K_RIGHT] and havenote == 1 and k < count - 1:
        k += 1

    if result1 < 100:
        if havenote == 0:
            update(screen, font, protagonist)
            screen.blit(tsObj, wadpos)
        if havenote == 1:
            screen.blit(Gray, gray)
            screen.blit(diary[number + k], nonejournal)
            if k == count - 1:
                update(screen, font, protagonist)
                screen.blit(Gray, gray)
                screen.blit(diary[number + k], nonejournal)
                screen.blit(textclickx, texty)
            else:
                update(screen, font, protagonist)
                screen.blit(Gray, gray)
                screen.blit(diary[number + k], nonejournal)
                screen.blit(textclicky, textx)
        pygame.display.update()'''

'''if (havenote == 3 or havenote == 4):
            screen.blit(image_gray, gray)
            if (havediary[diaryindex] == 1):
                screen.blit(diary[diaryindex], diary1pos)
            else:
                screen.blit(diary[14], diary1pos)
            if (havediary[diaryindex + 1] == 1):
                screen.blit(diary[diaryindex + 1], diary2pos)
            else:
                screen.blit(diary[15], diary2pos)'''


# 이 주석은 인벤토리 기능인데 잠시 지워놨슴다 그이유는 위에거에 4시간을 박았기 때문이죠 지우지 말아주십시요ㅠㅠ

def inventory():
    owndiary = []
    for i in range(len(havediary)):
        if havediary[i]:
            owndiary.append(i)
    key_INPUT = pygame.key.get_pressed()
    if key_INPUT[pygame.K_b]:
        return 1
    return 0

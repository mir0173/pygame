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
global owndiary
owndiary2 = []
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
    text = font[2].render("Press X to Close", True, (255, 255, 255))
    if number == end:
        screen.blit(text, (620, 750))
    if number > start:
        screen.blit(left, (500, 500))
    if number < end:
        screen.blit(right, (1100, 500))
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


def inventory():
    global owndiary
    owndiary = []
    for i in range(len(havediary)):
        if havediary[i] == 1:
            owndiary.append(i)
    owndiary2 = owndiary
    key_INPUT = pygame.key.get_pressed()
    if key_INPUT[pygame.K_b]:
        return 1
    return 0


def viewdiary(screen, font, number, protagonist):
    global owndiary
    if len(owndiary) != 0:
        image_gray = pygame.image.load('./assets/gray.png')
        Gray = pygame.transform.scale(image_gray, (1600, 900))
        Gray.set_alpha(175)
        end = ((int)((len(owndiary) - 1) / 2)) * 2 + 1
        update(screen, font, protagonist)
        screen.blit(Gray, gray)
        screen.blit(diary[owndiary[number - 1]], diary1pos)
        if number != end or (number == end and len(owndiary) % 2 == 0):
            screen.blit(diary[owndiary[number]], diary2pos)
        key_INPUT = pygame.key.get_pressed()
        text = font[2].render("Press X to Close", True, (255, 255, 255))
        screen.blit(text, (620, 750))
        if number > 1:
            screen.blit(left, (200, 500))
        if number < end:
            screen.blit(right, (1400, 500))
        owndiary2 = owndiary
        if key_INPUT[pygame.K_x]:
            return -1
        if key_INPUT[pygame.K_RIGHT]:
            if number < end:
                return number + 2
        if key_INPUT[pygame.K_LEFT]:
            if number > 1:
                return number - 2
        return number
    else:
        image_gray = pygame.image.load('./assets/gray.png')
        Gray = pygame.transform.scale(image_gray, (1600, 900))
        Gray.set_alpha(175)
        screen.blit(Gray, gray)
        key_INPUT = pygame.key.get_pressed()
        text = font[2].render("Press X to Close", True, (255, 255, 255))
        screen.blit(text, (620, 550))
        text2 = font[2].render("Empty", True, (255, 255, 255))
        screen.blit(text2, (620, 400))
        owndiary2 = owndiary
        if key_INPUT[pygame.K_x]:
            return -1
        return number

def cleardiary(number):
    global havediary
    if number == 5:
        for i in range(0, 14):
            havediary[i] = 0

    if number == 4:
        for i in range(3, 14):
            havediary[i] = 0
    if number == 3:
        for i in range(6, 14):
            havediary[i] = 0
    if number == 2:
        for i in range(9, 13):
            havediary[i] = 0
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
havediary = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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


def diaryinter(screen, font, number, start, end, protagonist, npc_list):
    image_gray = pygame.image.load('./assets/gray.png')
    Gray = pygame.transform.scale(image_gray, (1600, 900))
    Gray.set_alpha(175)
    update(screen, font, protagonist, npc_list)
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


class Inventory():
    def __init__(self, screen):
        self.owndiary = []
        self.keyboard_press = False

    def inventory(self):
        self.owndiary = []
        for i in range(len(havediary)):
            if havediary[i] == 1:
                self.owndiary.append(i)
        key_INPUT = pygame.key.get_pressed()
        if key_INPUT[pygame.K_b]:
            return 1
        return 0

    def viewdiary(self, screen, font, number, protagonist, npc_list):
        if len(self.owndiary) != 0:
            image_gray = pygame.image.load('./assets/gray.png')
            Gray = pygame.transform.scale(image_gray, (1600, 900))
            Gray.set_alpha(175)
            end = ((int)((len(self.owndiary) - 1) / 2)) * 2 + 1
            update(screen, font, protagonist, npc_list)
            screen.blit(Gray, gray)
            screen.blit(diary[self.owndiary[number - 1]], diary1pos)
            if number != end or (number == end and len(self.owndiary) % 2 == 0):
                screen.blit(diary[self.owndiary[number]], diary2pos)
            key_INPUT = pygame.key.get_pressed()
            text = font[2].render("Press X to Close", True, (255, 255, 255))
            screen.blit(text, (620, 750))
            if number > 1:
                screen.blit(left, (200, 500))
            if number < end:
                screen.blit(right, (1400, 500))
            if key_INPUT[pygame.K_x]:
                return -1
            if key_INPUT[pygame.K_RIGHT] and not self.keyboard_press:
                self.keyboard_press = True
                if number < end:
                    return number + 2
            if key_INPUT[pygame.K_LEFT] and not self.keyboard_press:
                self.keyboard_press = True
                if number > 1:
                    return number - 2
            if not key_INPUT[pygame.K_RIGHT] and not key_INPUT[pygame.K_LEFT]:
                self.keyboard_press = False
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
            if key_INPUT[pygame.K_x]:
                return -1
            return number

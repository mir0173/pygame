import pygame
import math


def interaction(screen, player, object, protagonist):
    distance = math.sqrt((player.centerx - object.centerx) ** 2 + (player.centery - object.centery) ** 2)
    key_INPUT = pygame.key.get_pressed()
    WHITE = (255, 255, 255)
    a = 0
    if a == 0 and key_INPUT[pygame.K_e] and distance < 300:
        a = 1
    if a == 1 and key_INPUT[pygame.K_x]:
        a = 0
    if a == 0 and distance < 300:
        return 1
    elif a == 1 and distance < 300:
        return 2
    return 0

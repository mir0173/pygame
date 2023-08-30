import pygame
from text import text, char, pos, name, namepos
from system import update

black = pygame.Rect(0, 0, 0, 0)
bgpos = (-200, 0)
textRectObj = pygame.Rect(768, 300, 0, 0)
textRectObj2 = pygame.Rect(720, 400, 0, 0)
textplayer = pygame.Rect(20, 770, 0, 0)
texthero = pygame.Rect(1410, 690, 0, 0)
gray = pygame.Rect(0, 0, 0, 0)
hero = pygame.Rect(-75, 550, 0, 0)
Hero = pygame.image.load('./assets/hero2.png')
image_gray = pygame.image.load('./assets/gray.png')
image_gray = pygame.transform.scale(image_gray, (1600, 900))
textroom = pygame.Rect(20, 20, 0, 0)
index = -1
WHITE = (255, 255, 255)
textenum = 0


def first(screen):
    image_bg = pygame.transform.scale(pygame.image.load('./assets/B5.jpg'), (160 * 10, 90 * 10))
    bgpos = (0, 0)
    global gray, touchtexting
    screen.blit(image_gray, gray)
    pygame.display.update()
    pygame.time.wait(2000)
    for n in range(1, 25):
        screen.blit(image_bg, bgpos)
        image_gray.set_alpha(175 - n * 7)
        screen.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(75)
    pygame.time.wait(200)
    screen.blit(image_bg, bgpos)
    screen.blit(image_gray, gray)
    pygame.display.update()
    pygame.time.wait(1000)
    for n in range(1, 35):
        screen.blit(image_bg, bgpos)
        image_gray.set_alpha(n * 10)
        screen.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(50)
    pygame.time.wait(350)
    for n in range(1, 25):
        screen.blit(image_bg, bgpos)
        image_gray.set_alpha(350 - n * 7)
        screen.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(25)
    pygame.time.wait(200)
    for n in range(1, 50):
        screen.blit(image_bg, bgpos)
        image_gray.set_alpha((int)(175 + n * 3.5))
        screen.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(25)
    pygame.time.wait(200)
    for n in range(1, 50):
        screen.blit(image_bg, bgpos)
        image_gray.set_alpha(350 - n * 7)
        screen.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(25)
    pygame.time.wait(200)
    gray = pygame.Rect(0, 760, 0, 0)


def playtext(screen, font, protagonist):
    global index, textenum
    if (index == -1):
        return 1
    index += 1

    if text[textenum][index] == 0 and index > 0:
        endtext(screen, font, textenum, protagonist)
        return 1

    textPlayer = font[0].render(text[textenum][index], True, WHITE)
    update(screen, font, protagonist)
    char[textenum][index].set_alpha(250)
    screen.blit(char[textenum][index], pos[textenum][index])
    image_gray.set_alpha(100)
    screen.blit(image_gray, gray)
    screen.blit(textPlayer, textplayer)
    screen.blit(font[1].render(name[textenum][index], True, WHITE), namepos[textenum][index])
    pygame.display.update()
    return 0


def starttext(screen, k, font, protagonist):
    global index, textenum
    if (index != -1):
        return
    index += 1
    for n in range(1, 50):
        update(screen, font, protagonist)
        image_gray.set_alpha(2 * n)
        char[k][index + 1].set_alpha(5 * n)
        screen.blit(char[k][index + 1], pos[k][index + 1])
        screen.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(5)
    textenum = k
    playtext(screen, font, protagonist)


def endtext(screen, font, k, protagonist):
    global index
    for n in range(1, 50):
        update(screen, font, protagonist)
        image_gray.set_alpha(100 - 2 * n)
        char[k][index - 1].set_alpha(250 - 5 * n)
        screen.blit(char[k][index - 1], pos[k][index - 1])
        screen.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(5)
    index = -1
    return

import pygame
from text import text, char, pos, name, namepos
from system import update, save

black = pygame.Rect(0, 0, 0, 0)
bgpos = (-200, 0)
textRectObj = pygame.Rect(768, 300, 0, 0)
textRectObj2 = pygame.Rect(720, 400, 0, 0)
textplayer = pygame.Rect(20, 770, 0, 0)
texthero = pygame.Rect(1410, 690, 0, 0)
gray = pygame.Rect(0, 0, 0, 0)
hero = pygame.Rect(-75, 550, 0, 0)
Hero = pygame.image.load('./assets/lucifer.png')
image_gray = pygame.image.load('./assets/gray.png')
image_gray = pygame.transform.scale(image_gray, (1600, 900))
textroom = pygame.Rect(20, 20, 0, 0)
index = -1
WHITE = (255, 255, 255)
textenum = 0
key = 0

def first(screen, font, protagonist):
    pygame.init()
    pygame.mouse.set_visible(True)
    start = pygame.transform.scale(pygame.image.load('./assets/start.png'), (160 * 10, 90 * 10))
    start1 = pygame.transform.scale(pygame.image.load('./assets/start1.png'), (160 * 10, 90 * 10))
    start2 = pygame.transform.scale(pygame.image.load('./assets/start2.png'), (160 * 10, 90 * 10))
    start3 = pygame.transform.scale(pygame.image.load('./assets/start3.png'), (160 * 10, 90 * 10))
    bgpos = (0, 0)
    image_gray.set_alpha(200)
    global gray, touchtexting, key
    for i in range(20):
        screen.blit(start, bgpos)
        image_gray.set_alpha(200 - i * 10)
        screen.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(50)
    screen.blit(start, bgpos)
    pygame.display.update()
    image_gray.set_alpha(0)
    X = True
    while X:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 570 <= pos[0] < 1015 and 563 <= pos[1] <= 646:
                if click[0] == 1:
                    pygame.mouse.set_visible(False)
                    image_gray.set_alpha(175)
                    screen.blit(image_gray, gray)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    image_gray.set_alpha(0)
                    return (7, 0)
                screen.blit(start1, (0, 0))
            elif 570 <= pos[0] <= 1015 and 676 <= pos[1] <= 750:
                if click[0] == 1:
                    key = save(screen, font, protagonist, 0)
                    if key != (-1, 0):
                        return key
                screen.blit(start2, (0, 0))
            elif 570 <= pos[0] <= 1015 and 779 <= pos[1] <= 864:
                if click[0] == 1:
                    pygame.quit()
                screen.blit(start3, (0, 0))
            else:
                screen.blit(start, (0, 0))
            pygame.display.update()
            if event.type == pygame.QUIT:
                X = False
                pygame.quit()

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
    dialogue = pygame.mixer.Sound('./assets/dialogue.mp3')
    dialogue.play()
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
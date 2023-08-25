# 시작층 화면연출 구현입니다. (지하6층)
import pygame
from text import text, char, pos, name, namepos

pygame.init()
background = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("6F")
black = pygame.Rect(0, 0, 0, 0)
bgpos = (-200, 0)
textRectObj = pygame.Rect(768, 300, 0, 0)
textRectObj2 = pygame.Rect(720, 400, 0, 0)
textplayer = pygame.Rect(20, 770, 0, 0)
texthero = pygame.Rect(1410, 690, 0, 0)
gray = pygame.Rect(0, 0, 0, 0)
hero = pygame.Rect(-75, 550, 0, 0)
Hero = pygame.image.load('./image/hero2.png')
image_gray = pygame.image.load('./image/gray.png')
image_gray = pygame.transform.scale(image_gray, (1600, 900))
textroom = pygame.Rect(20, 20, 0, 0)
index = -1
WHITE = (255, 255, 255)
fontObj = pygame.font.SysFont("malgungothic", 32)
fontObj2 = pygame.font.SysFont("malgungothic", 46)
fontObj3 = pygame.font.Font("freesansbold.ttf", 64)
textenum = 0;






def first():
    image_bg = pygame.image.load('./image/B6.jpg')
    bgpos = (-200, 0)
    global gray, touchtexting
    background.blit(image_gray, gray)
    pygame.display.update()
    pygame.time.wait(2000)
    for n in range(1, 25):
        background.blit(image_bg, bgpos)
        image_gray.set_alpha(175 - n * 7)
        background.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(75)
    pygame.time.wait(200)
    background.blit(image_bg, bgpos)
    background.blit(image_gray, gray)
    pygame.display.update()
    pygame.time.wait(1000)
    for n in range(1, 35):
        background.blit(image_bg, bgpos)
        image_gray.set_alpha(n * 10)
        background.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(50)
    pygame.time.wait(350)
    for n in range(1, 25):
        background.blit(image_bg, bgpos)
        image_gray.set_alpha(350 - n * 7)
        background.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(25)
    pygame.time.wait(200)
    for n in range(1, 50):
        background.blit(image_bg, bgpos)
        image_gray.set_alpha(175 + n * 3.5)
        background.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(25)
    pygame.time.wait(200)
    for n in range(1, 50):
        background.blit(image_bg, bgpos)
        image_gray.set_alpha(350 - n * 7)
        background.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(25)
    pygame.time.wait(200)
    gray = pygame.Rect(0, 760, 0, 0)

def playtext():
    global index, textenum
    if(index == -1):
        return
    index += 1
    print(index)


    if text[textenum][index] == 0 and index > 0:
        endtext(textenum)
        return


    textPlayer = fontObj.render(text[textenum][index], True, WHITE)
    background.blit(image_bg, bgpos)
    background.blit(char[textenum][index], pos[textenum][index])
    image_gray.set_alpha(100)
    background.blit(image_gray, gray)
    background.blit(textPlayer, textplayer)
    background.blit(fontObj2.render(name[textenum][index], True, WHITE), namepos[textenum][index])
    pygame.display.update()


def starttext(k, image_bg1, bgpos1):
    global index, textenum, image_bg, bgpos
    image_bg = image_bg1
    bgpos = bgpos1
    if(index != -1):
        return
    index += 1
    for n in range(1, 50):
        background.blit(image_bg, bgpos)
        image_gray.set_alpha(2 * n)
        char[k][index + 1].set_alpha(5 * n)
        background.blit(char[k][index + 1], pos[k][index + 1])
        background.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(10)
    textenum = k
    playtext()



def endtext(k):
    global index
    for n in range(1, 50):
        background.blit(image_bg, bgpos)
        image_gray.set_alpha(100 - 2 * n)
        char[k][index - 1].set_alpha(250 - 5 * n)
        background.blit(char[k][index - 1], pos[k][index - 1])
        background.blit(image_gray, gray)
        pygame.display.update()
        pygame.time.wait(10)
    index = -1;

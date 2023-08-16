# 물건 인터렉션 구현입니다 (예시는 지하4층과 빈 연구노트)
import pygame
import sys
import math

def main():
    pygame.init()
    background = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("NF")

    image_hero = pygame.image.load('./image/hero.png')
    image_wadpaper = pygame.image.load('./image/wadpaper.png')
    image_bg = pygame.image.load('./image/B4.jpg')
    image_journal1 = pygame.image.load('./image/journal1.png')
    image_gray = pygame.image.load('./image/gray.png')
    image_gray = pygame.transform.scale(image_gray, (1600, 900))
    image_gray.set_alpha(215)
    player = pygame.Rect(100, 450, 0, 0)
    wadpaper = pygame.Rect(1150, 710, 0, 0)
    textRectObj = pygame.Rect(1100, 675, 0, 0)
    textjournal = pygame.Rect(615, 720, 0, 0)
    gray = pygame.Rect(0, 0, 0, 0)
    journal1 = pygame.Rect(550, 150, 0, 0)
    clock = pygame.time.Clock()
    game_speed = 0.15
    gravity = 0
    a = 0
    dt = clock.tick(60)
    
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    
    fontObj = pygame.font.Font("freesansbold.ttf",16)
    fontObj2 = pygame.font.Font("freesansbold.ttf",32)
    textSurfaceObj = fontObj.render("Interact with the E key.",True,WHITE)
    textJournal = fontObj2.render("Close with the X key.",True,WHITE)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit;
                        
        key_INPUT = pygame.key.get_pressed()
        if key_INPUT[pygame.K_LEFT] and player.left >=0 and a == 0:
            player.left -= game_speed*dt
        if key_INPUT[pygame.K_RIGHT] and player.right <= 1400 and a == 0:
            player.right += game_speed*dt
        if key_INPUT[pygame.K_e]:
            a = 1
        if key_INPUT[pygame.K_x]:
            a = 0
            
        player.top += gravity
        gravity += 0.05

        if player.bottom >= 500:
            gravity = 0
            if key_INPUT[pygame.K_UP] and a == 0:
                gravity = -4
        
        background.blit(image_bg, (-400,0))
        result = math.sqrt( math.pow(player.centerx - wadpaper.centerx, 2) + math.pow(player.centery - wadpaper.centery, 2))
        background.blit(image_wadpaper, wadpaper)
        if(result <300 and a == 0):
            background.blit(textSurfaceObj,textRectObj)
        background.blit(image_hero, player)
        if(a == 1):
            background.blit(image_gray,gray)
            background.blit(image_journal1,journal1)
            background.blit(textJournal,textjournal)
        pygame.display.update()
   
main()

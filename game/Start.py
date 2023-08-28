# 시작층 화면연출 구현입니다. (지하6층)
import pygame
import sys

def main():
    pygame.init()
    background = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("6F")
    black = pygame.Rect(0, 0, 0, 0)
    textRectObj = pygame.Rect(768, 300, 0, 0)
    textRectObj2 = pygame.Rect(720, 400, 0, 0)
    gray = pygame.Rect(0, 0, 0, 0)
    player = pygame.Rect(100, 450, 0, 0)
    image_black = pygame.image.load('./image/black.jpg')
    image_hero = pygame.image.load('./image/hero.png')
    image_gray = pygame.image.load('./image/gray.png')
    image_gray = pygame.transform.scale(image_gray, (1600, 900))
    image_bg = pygame.image.load('./image/B6.jpg')
    image_black = pygame.transform.scale(image_black, (1600, 900))
    textroom = pygame.Rect(20, 20, 0, 0)

    clock = pygame.time.Clock()
    WHITE = (255,255,255)
    game_speed = 0.15
    gravity = 0
    floor = 6
    room = 1
    a = 0
    dt = clock.tick(60)
    fontObj = pygame.font.SysFont("malgungothic",64)
    textObj = fontObj.render("으윽",True,WHITE)
    textObj2 = fontObj.render("머리가",True,WHITE)
    fontObj3 = pygame.font.Font("freesansbold.ttf",64)
    textRoom = fontObj3.render(f"6 - {room:,}", True ,WHITE)
    
    pygame.time.wait(5000)
    for i in range(1, 25): 
        background.blit(image_bg, (-200,0))
        image_gray.set_alpha(175 - i * 7)
        background.blit(image_gray,gray)
        pygame.display.update()
        pygame.time.wait(75)
    pygame.time.wait(200)
    background.blit(image_bg, (-200,0))
    background.blit(image_gray,gray)
    pygame.display.update()
    pygame.time.wait(2000)
    for i in range(1, 35): 
        background.blit(image_bg, (-200,0))
        image_gray.set_alpha(i * 10)
        background.blit(image_gray,gray)
        pygame.display.update()
        pygame.time.wait(50)
    pygame.time.wait(350)
    for i in range(1, 25): 
        background.blit(image_bg, (-200,0))
        image_gray.set_alpha(350 - i * 7)
        background.blit(image_gray,gray)
        pygame.display.update()
        pygame.time.wait(25)
    pygame.time.wait(200)
    for i in range(1, 50): 
        background.blit(image_bg, (-200,0))
        image_gray.set_alpha(175 + i * 3.5)
        background.blit(image_gray,gray)
        pygame.display.update()
        pygame.time.wait(25)
    pygame.time.wait(200)
    for i in range(1, 50): 
        image_black.set_alpha(i * 7)
        background.blit(image_black,black)
        pygame.display.update()
        pygame.time.wait(25)
    
    
    image_black.set_alpha(350)
    background.blit(image_black,black)
    pygame.display.update()
    pygame.time.wait(1000)
    background.blit(image_black,black)
    background.blit(textObj,textRectObj)
    pygame.display.update()
    pygame.time.wait(200)
    background.blit(image_black,black)
    textObj = fontObj.render("으윽.",True,WHITE)
    textRectObj = pygame.Rect(752, 300, 0, 0)
    background.blit(textObj,textRectObj)
    pygame.display.update()
    pygame.time.wait(200)
    background.blit(image_black,black)
    textObj = fontObj.render("으윽..",True,WHITE)
    textRectObj = pygame.Rect(732, 300, 0, 0)
    background.blit(textObj,textRectObj)
    pygame.display.update()
    pygame.time.wait(200)
    background.blit(image_black,black)
    textObj = fontObj.render("으윽...",True,WHITE)
    textRectObj = pygame.Rect(700, 300, 0, 0)
    background.blit(textObj,textRectObj)
    pygame.display.update()
    pygame.time.wait(500)
    background.blit(image_black,black)
    textObj = fontObj.render("으윽... 여기가",True,WHITE)
    textRectObj = pygame.Rect(580, 300, 0, 0)
    background.blit(textObj,textRectObj)
    pygame.display.update()
    pygame.time.wait(500)
    background.blit(image_black,black)
    textObj = fontObj.render("으윽... 여기가 어디지?",True,WHITE)
    textRectObj = pygame.Rect(468, 300, 0, 0)
    background.blit(textObj,textRectObj)
    pygame.display.update()
    pygame.time.wait(2000)
    background.blit(image_black,black)
    background.blit(textObj,textRectObj)
    background.blit(textObj2,textRectObj2)
    pygame.display.update()
    pygame.time.wait(333)
    background.blit(image_black,black)
    textObj2 = fontObj.render("머리가 너무",True,WHITE)
    textRectObj2 = pygame.Rect(642, 400, 0, 0)
    background.blit(textObj,textRectObj)
    background.blit(textObj2,textRectObj2)
    pygame.display.update()
    pygame.time.wait(666)
    background.blit(image_black,black)
    textObj2 = fontObj.render("머리가 너무 어지러워...",True,WHITE)
    textRectObj2 = pygame.Rect(450, 400, 0, 0)
    background.blit(textObj,textRectObj)
    background.blit(textObj2,textRectObj2)
    pygame.display.update()
    for i in range(1, 50): 
        background.blit(image_black, black)
        background.blit(textObj,textRectObj)
        background.blit(textObj2,textRectObj2)
        image_gray.set_alpha(i * 7)
        background.blit(image_gray,gray)
        pygame.display.update()
        pygame.time.wait(25)
    pygame.time.wait(200)
    for i in range(1, 50): 
        background.blit(image_bg, (-200,0))
        background.blit(image_hero, player)
        image_gray.set_alpha(350 - i * 7)
        background.blit(image_gray,gray)
        pygame.display.update()
        pygame.time.wait(25)
    pygame.time.wait(200)
    background.blit(image_bg, (-200,0))
    background.blit(image_hero, player)
    pygame.display.update()    

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit;
        
        key_INPUT = pygame.key.get_pressed()
        if (key_INPUT[pygame.K_LEFT] and player.left >=-200 and a == 0 and room != 1) or (key_INPUT[pygame.K_LEFT] and player.left >= 0 and a == 0 and room == 1):
            player.left -= game_speed*dt
        if (key_INPUT[pygame.K_RIGHT] and player.right <= 1625 and a == 0 and room != 3) or (key_INPUT[pygame.K_RIGHT] and player.right <= 1425 and a == 0 and room == 3):
            player.right += game_speed*dt
        if key_INPUT[pygame.K_e]:
            a = 1
        if key_INPUT[pygame.K_x]:
            a = 0
        if(player.left >=-200 and player.left <= -100 and room > 1):
            room -= 1
            image_gray.set_alpha(500)
            player.x = 1325
            background.blit(image_gray,gray)
            pygame.display.update()
            pygame.time.wait(500)
            image_gray.set_alpha(215)
        if(player.left >=1525 and player.left <= 1625 and room < 3):
            room += 1
            image_gray.set_alpha(500)
            player.x = 100
            background.blit(image_gray,gray)
            pygame.display.update()
            pygame.time.wait(500)
            image_gray.set_alpha(215)
            
        player.top += gravity
        gravity += 0.05

        if player.bottom >= 500:
            gravity = 0
            if key_INPUT[pygame.K_UP] and a == 0:
                gravity = -4
        
        if(floor == 6):
            background.blit(image_bg, (-200,0))
            if(room == 1):
                background.blit(image_hero, player)
                textRoom = fontObj.render("???", True ,WHITE)
                background.blit(textRoom,textroom)
            if(room == 2):
                background.blit(image_hero, player)
                textRoom = fontObj3.render(f"6 - {room:,}", True ,WHITE)
                background.blit(textRoom,textroom)
            if(room == 3):
                background.blit(image_hero, player)
                textRoom = fontObj3.render(f"6 - {room:,}", True ,WHITE)
                background.blit(textRoom,textroom)
        pygame.display.update()
        
    
main()

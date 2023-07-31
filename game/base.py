import pygame
import sys
import time

def main():
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("3F")

    player = pygame.Rect((width-50)/2, height-50, 50, 50)
    player_img1 = pygame.image.load('c1.png')
    player_img1 = pygame.transform.scale(player_img1, (50, 50))
    player_img2 = pygame.image.load('c2.png')
    player_img2 = pygame.transform.scale(player_img2, (50, 50))
    player_img3 = pygame.image.load('c3.png')
    player_img3 = pygame.transform.scale(player_img3, (50, 50))

    clock = pygame.time.Clock()
    game_speed = 0.3

    gravity = 0

    while True:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key_INPUT = pygame.key.get_pressed()
        if key_INPUT[pygame.K_LEFT] and player.left >=0:
            player.left -= game_speed*dt
        if key_INPUT[pygame.K_RIGHT] and player.right <= width:
            player.right += game_speed*dt

        #중력 엔진
        player.top += gravity
        gravity +=1

        if player.bottom >= 500:
            gravity = 0
            if key_INPUT[pygame.K_UP]:
                gravity = -18

        screen.fill((255, 255, 255))
        screen.blit(player_img1, player)
        pygame.display.update()
main()

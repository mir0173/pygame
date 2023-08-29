import pygame
import sprite
from background import screen_change


def main():
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    character_right = pygame.image.load('./image/protagonist_male.png').convert_alpha()
    character_left = pygame.image.load('./image/protagonist_male2.png').convert_alpha()
    character_right_1 = pygame.image.load('./image/michael.png').convert_alpha()
    character_left_1 = pygame.image.load('./image/michael2.png').convert_alpha()
    gun_left = pygame.image.load('./image/gun2.png').convert_alpha()
    gun_right = pygame.image.load('./image/gun.png').convert_alpha()
    bullet_ = pygame.image.load('./image/bullet.png').convert_alpha()
    protagonist = sprite.protagonist(character_left, character_right, 0)
    height, width = protagonist.location()
    gun = sprite.Gun(width, height, gun_left, gun_right)
    gun_list = pygame.sprite.Group(gun)
    bullet_list = pygame.sprite.Group()
    michael = sprite.Michael(character_left_1, character_right_1, 0)

    screen_number = 0
    run = True
    mouse_clicked = True

    while run:
        clock = pygame.time.Clock()
        dt = clock.tick(60)
        pygame.draw.rect(screen, (255, 0, 0), (500, 500, 404, 34))
        height, width = protagonist.location()
        lr = protagonist.left_right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse_clicked:
                bullet = sprite.Bullet(width, height, bullet_, lr)
                bullet_list.add(bullet)
                mouse_clicked = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_clicked = True

        bullet_list.update(michael, lr)
        gun_list.update(width, height, lr)
        screen_number = screen_change(protagonist, screen_number)
        protagonist.update(screen)
        michael.update(screen)
        protagonist.move(screen, dt, 0.3)
        michael.move(screen, dt, 0.3)
        protagonist.move2(screen, michael)
        bullet_list.draw(screen)
        gun_list.draw(screen)
        michael.update(screen)
        pygame.display.update()
        print(michael.health)

    pygame.quit()

main()
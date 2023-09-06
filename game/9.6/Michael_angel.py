import pygame
import sp


def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((1600, 900))
    character_right = pygame.image.load('./image/protagonist_male_attack.png').convert_alpha()
    character_left = pygame.image.load('./image/protagonist_male_attack2.png').convert_alpha()
    protagonist = sp.protagonist(character_left, character_right, 0)
    michael_final = sp.Michael_final(0, protagonist)  
    run = True
    while run:
        clock = pygame.time.Clock()
        dt = clock.tick(60)         

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        mouse = pygame.mouse.get_pressed()[0]
        protagonist.move(screen, dt, 0.3)
        protagonist.update(screen)

        michael_final.update(screen, protagonist)

        protagonist.attack(screen, (michael_final, michael_final.sword_gun_1, michael_final.sword_gun_2, michael_final.sword_gun_3), mouse)
        pygame.display.update()
    pygame.quit()

main()
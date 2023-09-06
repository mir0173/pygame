import pygame
import sp

def main():
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((1600, 900))
    character_right = pygame.image.load('./image/protagonist_male_attack.png').convert_alpha()
    character_left = pygame.image.load('./image/protagonist_male_attack2.png').convert_alpha()
    michael_right = pygame.image.load('./image/michael.png').convert_alpha()
    michael_left = pygame.image.load('./image/michael2.png').convert_alpha()
    protagonist = sp.protagonist(character_left, character_right, 0)
    michael = sp.Michael(michael_left, michael_right, 0) 
    
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
        michael.move(screen, dt, 0.3)
        michael.update(screen)
        protagonist.attack(screen, [michael], mouse)
        michael.attack(screen, protagonist)
        pygame.display.update()
    pygame.quit()

main()
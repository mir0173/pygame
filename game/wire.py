import pygame
from circuit import Circuit
from circuit import first_puzzle, first_puzzle_answer
from circuit import second_puzzle, second_puzzle_answer
from circuit import third_puzzle, third_puzzle_answer
from circuit import answer_check

screen_width = 1600
screen_height = 900

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pygame Sprite")

clock = pygame.time.Clock()
FPS = 60

BACKGROUND_COLOR = pygame.Color('white')
success_background_4x4 = pygame.transform.scale(pygame.image.load('assets/fail_background_4x4.png'), (1600, 900))
success_background_6x6 = pygame.transform.scale(pygame.image.load('assets/fail_background_6x6.png'), (1600, 900))
fail_background_4x4 = pygame.transform.scale(pygame.image.load('assets/success_background_4x4.png'), (1600, 900))
fail_background_6x6 = pygame.transform.scale(pygame.image.load('assets/success_background_6x6.png'), (1600, 900))
size_4x4 = (159, 159)
size_6x6 = (106, 106)


def wire_gimmick():
    current_puzzle_level = 0

    first_circuit_list = []
    for i in first_puzzle:
        first_circuit_list.append(Circuit(i, size_4x4))
    second_circuit_list = []
    for i in second_puzzle:
        second_circuit_list.append(Circuit(i, size_4x4))
    third_circuit_list = []
    for i in third_puzzle:
        third_circuit_list.append(Circuit(i, size_6x6))

    first_puzzle_sprites = pygame.sprite.Group()
    for i in first_circuit_list:
        first_puzzle_sprites.add(i)
    second_puzzle_sprites = pygame.sprite.Group()
    for i in second_circuit_list:
        second_puzzle_sprites.add(i)
    third_puzzle_sprites = pygame.sprite.Group()
    for i in third_circuit_list:
        third_puzzle_sprites.add(i)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        answer_sheet = []
        if current_puzzle_level == 0:
            for i in first_circuit_list:
                answer_sheet.append(i.current_state())
            result = answer_check(answer_sheet, first_puzzle_answer)

            if not result:
                first_puzzle_sprites.update()
                screen.blit(success_background_4x4, (0, 0))
                first_puzzle_sprites.draw(screen)
                pygame.display.update()
            else:
                screen.blit(fail_background_4x4, (0, 0))
                first_puzzle_sprites.draw(screen)
                pygame.display.update()
                pygame.time.delay(1500)
                current_puzzle_level = 1
        elif current_puzzle_level == 1:
            for i in second_circuit_list:
                answer_sheet.append(i.current_state())
            result = answer_check(answer_sheet, second_puzzle_answer)

            if not result:
                second_puzzle_sprites.update()
                screen.blit(success_background_4x4, (0, 0))
                second_puzzle_sprites.draw(screen)
                pygame.display.update()
            else:
                screen.blit(fail_background_4x4, (0, 0))
                second_puzzle_sprites.draw(screen)
                pygame.display.update()
                pygame.time.delay(1500)
                current_puzzle_level = 2
        elif current_puzzle_level == 2:
            for i in third_circuit_list:
                answer_sheet.append(i.current_state())
            result = answer_check(answer_sheet, third_puzzle_answer)

            if not result:
                third_puzzle_sprites.update()
                screen.blit(success_background_6x6, (0, 0))
                third_puzzle_sprites.draw(screen)
                pygame.display.update()
            else:
                screen.blit(fail_background_6x6, (0, 0))
                third_puzzle_sprites.draw(screen)
                pygame.display.update()
                pygame.time.delay(1500)
                current_puzzle_level = 3
        elif current_puzzle_level == 3:
            pygame.display.update()
            return True

        clock.tick(FPS)

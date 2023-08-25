import pygame
from start import starttext


def main():

    pygame.event.clear()
    while True:
        for event in pygame.event.get():
            if event.key == pygame.K_e:
                starttext()


main()
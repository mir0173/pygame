import pygame
import sprite
from background import screen_change
from background import right_area
from system import esc
from system import resume
from dialogue import main
from background import bottom_area

pausepopup = pygame.image.load('./assets/pause.png')


class B6():
    def __init__(self, screen, fontObj, fontObj2, fontObj3):
        self.pause = False
        self.screen_number = 0
        self.tostart = False
        self.screen = screen
        self.fontObj = fontObj
        self.fontObj2 = fontObj2
        self.fontObj3 = fontObj3

    def tutorial(self, character_left, character_right):
        protagonist = sprite.protagonist(character_left, character_right, 0)
        run = True
        k = 0
        n = 0
        m = 0
        canmove = True
        main(0, self.screen, self.fontObj, self.fontObj2, self.fontObj3, protagonist)
        while run:
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            if not self.pause:
                if canmove:
                    protagonist.move(self.screen, dt, 0.6)
                self.screen_number = screen_change(protagonist, self.screen_number)
                protagonist.update(self.screen)
                pygame.display.update()
                key_INPUT = pygame.key.get_pressed()
                if key_INPUT[pygame.K_ESCAPE]:
                    esc(self, self.screen, protagonist)
                if self.screen_number == 1:
                    if protagonist.player.right - right_area >= 800:
                        protagonist.player.right = right_area + 799
                        canmove = False
                        protagonist.player.bottom = 775 + bottom_area
                        k = main(1, self.screen, self.fontObj, self.fontObj2, self.fontObj3, protagonist)
                    if k == 1:
                        protagonist.update(self.screen)
                        pygame.display.update()
                        pygame.time.wait(2000)
                        canmove = True
                        protagonist.screen_number += 1
                        self.screen_number += 1
                        k = 0
                        protagonist.update(self.screen)
                        pygame.display.update()
                if self.screen_number == 2:
                    if k == 0:
                        pygame.time.wait(1000)
                        canmove = False
                        k = main(2, self.screen, self.fontObj, self.fontObj2, self.fontObj3, protagonist)
                    if k == 1:
                        pygame.time.wait(1000)
                        protagonist.screen_number += 1
                        self.screen_number += 1
                if self.screen_number == 3:
                    protagonist.update(self.screen)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    protagonist.screen_number += 1
                    self.screen_number += 1
                    k = 0
                if self.screen_number == 4:
                    protagonist.update(self.screen)
                    pygame.display.update()
                    if k == 0:
                        k = main(3, self.screen, self.fontObj, self.fontObj2, self.fontObj3, protagonist)
                    if k == 1:
                        canmove = True
                if self.screen_number == 5:
                    canmove = False
                    if n == 0:
                        n = main(4, self.screen, self.fontObj, self.fontObj2, self.fontObj3, protagonist)
                    if n == 1:
                        canmove = True
                    if protagonist.player.right - right_area >= 300:
                        canmove = False
                        protagonist.screen_number += 1
                        self.screen_number += 1
                        protagonist.update(self.screen)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        if m == 0:
                            m = main(5, self.screen, self.fontObj, self.fontObj2, self.fontObj3, protagonist)
                        if m == 1:
                            canmove = True
                            protagonist.update(self.screen)
                            pygame.display.update()
                if self.screen_number == 6:
                    if protagonist.player.right - right_area >= 1450:
                        return
                if self.screen_number == 7:
                    run = False
            else:
                resume(self, self.screen, protagonist)
            if self.tostart == True:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

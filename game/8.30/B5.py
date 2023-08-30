import pygame
from system import resume, esc, update
import sprite
from dialogue import dialogue
from background import right_area, screen_change
from interaction import interaction

cutscene = pygame.transform.scale(pygame.image.load('./assets/cutscene1.png'), (1600, 900))
gray = pygame.transform.scale(pygame.image.load('./assets/gray.png'), (1600, 900))


class B5():
    def __init__(self, screen, font, ):
        self.screen_number = 7
        self.font = font
        self.screen = screen
        self.pause = False
        self.tostart = False

    def story(self, character_left, character_right):
        protagonist = sprite.protagonist(self.font, character_left, character_right, 7)
        protagonist.alpha = 125
        update(self.screen, self.font, protagonist)
        pygame.display.update()
        run = True
        canmove = False
        x = dialogue(6, self.screen, self.font, protagonist)
        k = 0
        m = 0
        if x == 1:
            canmove = True
        while run:
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            self.screen_number = screen_change(protagonist, self.screen_number)
            if not self.pause:
                if canmove:
                    protagonist.move(self.screen, dt, 0.6)
                    pygame.display.update()
                key_INPUT = pygame.key.get_pressed()
                if key_INPUT[pygame.K_ESCAPE]:
                    esc(self, self.screen, self.font, protagonist)
                if self.screen_number == 7:
                    if protagonist.player.right - right_area >= 800:
                        self.screen_number += 1
                        protagonist.screen_number += 1
                        protagonist.alpha = 255
                if self.screen_number == 9:
                    if protagonist.player.right - right_area >= 800:
                        self.screen_number += 1
                        protagonist.screen_number += 1
                if self.screen_number == 10:
                    canmove = False
                    computer = pygame.Rect(1100, 500, 200, 100)
                    if k == 0:
                        k = dialogue(7, self.screen, self.font, protagonist)
                    if k == 1:
                        canmove = True
                        inter = interaction(self.screen, protagonist.player, computer, protagonist)
                        if inter == 0:
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == computer:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(computer)
                        if inter == 1:
                            protagonist.move(self.screen, dt, 0.6)
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == computer:
                                    a = 1
                            if a == 0:
                                protagonist.interact.append(computer)
                            pygame.display.update()
                        if inter == 2:
                            canmove = False
                            self.screen_number += 1
                            protagonist.screen_number += 1
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == computer:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(computer)
                            update(self.screen, self.font, protagonist)
                            pygame.display.update()
                            pygame.time.wait(1000)
                            m = self.cutscene()
                            if m == 1:
                                self.screen_number += 1
                                protagonist.screen_number += 1
                if self.screen_number == 11:
                    return


            else:
                resume(self, self.screen, self.font, protagonist)
            if self.tostart == True:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

    def cutscene(self):
        for n in range(25):
            self.screen.blit(cutscene, (0, 0))
            gray.set_alpha(175 - 7 * n)
            self.screen.blit(gray, (0, 0))
            pygame.display.update()
            pygame.time.wait(5)

        while True:
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            self.screen.blit(cutscene, (0, 0))
            pygame.display.update()
            break
        return 1

import pygame
from system import resume, esc, update
import sprite
from dialogue import dialogue
from background import right_area, screen_change
from interaction import interaction, diaryinter, inventory, viewdiary
from diaryinteraction import diary


class B2():
    def __init__(self, screen, font):
        self.screen_number = 34
        self.screen = screen
        self.font = font
        self.pause = False
        self.tostart = False

    def story(self, character_left, character_right):
        pygame.mouse.set_visible(True)
        protagonist = sprite.protagonist(self.font, character_left, character_right, 34)
        update(self.screen, self.font, protagonist)
        image_gray = pygame.image.load('./assets/gray.png')
        Gray = pygame.transform.scale(image_gray, (1600, 900))
        Gray.set_alpha(175)
        run = True
        canmove = False
        x = dialogue(32, self.screen, self.font, protagonist)
        if x == 1:
            canmove = True
        inven = 0
        foinven = 0
        nonejournal = pygame.Rect(560, 200, 0, 0)
        n = 0
        k = 0
        m = 0
        i = 0
        inter = 0
        number = 12
        number2 = 1

        select = -1
        while run:
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            if self.screen_number != 34 and self.screen_number != 40:
                self.screen_number = screen_change(protagonist, self.screen_number)
            if not self.pause:
                foinven = inven
                if canmove:
                    protagonist.move(self.screen, dt, 0.6)

                if self.screen_number == 34:
                    diary_ps = pygame.Rect(1000, 550, 150, 50)
                    update(self.screen, self.font, protagonist)
                    inter = interaction(protagonist.player, diary_ps)
                    if inter == 0:
                        a = 0
                        for i in range(len(protagonist.interact)):
                            if protagonist.interact[i] == diary_ps:
                                a = 1
                        if a == 1:
                            protagonist.interact.remove(diary_ps)
                    if inter == 1:
                        protagonist.move(self.screen, dt, 0.6)
                        a = 0
                        for i in range(len(protagonist.interact)):
                            if protagonist.interact[i] == diary_ps:
                                a = 1
                        if a == 0:
                            protagonist.interact.append(diary_ps)

                    if inter == 2:
                        canmove = False
                        if k == 0:
                            canmove = False
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == diary_ps:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(diary_ps)
                            update(self.screen, self.font, protagonist)
                            pygame.display.update()
                            k = dialogue(16, self.screen, self.font, protagonist)
                        if k == 1:
                            n = 0
                            k = 0
                            self.screen_number += 1
                            protagonist.screen_number += 1
                if self.screen_number == 35:
                    before = number
                    if i == 0:
                        number = diaryinter(self.screen, self.font, number, 12, 14, protagonist)
                    if before != number:
                        i = 1
                    if i != 0:
                        update(self.screen, self.font, protagonist)
                        self.screen.blit(Gray, (0, 0))
                        self.screen.blit(diary[number - 1], nonejournal)
                        i += 1
                    if i == 5:
                        i = 0
                    if number == -1:
                        if n == 0:
                            n = dialogue(18, self.screen, self.font, protagonist)
                        elif n == 1:
                            self.screen_number += 1
                            protagonist.screen_number += 1
                            update(self.screen, self.font, protagonist)
                            canmove = True
                            n = 0
                if self.screen_number == 37:
                    inter = 0
                    if n == 0:
                        canmove = False
                        n = dialogue(19, self.screen, self.font, protagonist)
                    elif n == 1:
                        canmove = True
                        if protagonist.player.right - right_area >= 800:
                            canmove = False
                            k = dialogue(20, self.screen, self.font, protagonist)
                    if k == 1:
                        canmove = True
                        if m == 0:
                            m = dialogue(21, self.screen, self.font, protagonist)
                        elif m == 1:
                            self.screen_number += 1
                            protagonist.screen_number += 1
                            n = 0
                            k = 0
                            m = 0
                            update(self.screen, self.font, protagonist)

                if self.screen_number == 38:
                    if n == 0:
                        number = 15
                        n = dialogue(22, self.screen, self.font, protagonist)
                    elif n == 1:
                        diary_ps = pygame.Rect(1000, 550, 150, 50)
                        update(self.screen, self.font, protagonist)
                        inter = interaction(protagonist.player, diary_ps)
                        if inter == 0:
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == diary_ps:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(diary_ps)
                        if inter == 1:
                            protagonist.move(self.screen, dt, 0.6)
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == diary_ps:
                                    a = 1
                            if a == 0:
                                protagonist.interact.append(diary_ps)

                        if inter == 2:
                            canmove = False
                            if k == 0:
                                canmove = False
                                a = 0
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == diary_ps:
                                        a = 1
                                if a == 1:
                                    protagonist.interact.remove(diary_ps)
                                update(self.screen, self.font, protagonist)
                                pygame.display.update()
                                k = dialogue(16, self.screen, self.font, protagonist)
                            if k == 1:
                                n = 0
                                k = 0
                                self.screen_number += 1
                                protagonist.screen_number += 1
                if self.screen_number == 39:
                    before = number
                    if i == 0:
                        number = diaryinter(self.screen, self.font, number, 15, 16, protagonist)
                    if before != number:
                        i = 1
                    if i != 0:
                        update(self.screen, self.font, protagonist)
                        self.screen.blit(Gray, (0, 0))
                        self.screen.blit(diary[number - 1], nonejournal)
                        i += 1
                    if i == 5:
                        i = 0
                    if number == -1:
                        if n == 0:
                            n = dialogue(18, self.screen, self.font, protagonist)
                        elif n == 1:
                            self.screen_number += 1
                            protagonist.screen_number += 1
                            update(self.screen, self.font, protagonist)
                            canmove = True
                            n = 0
                if self.screen_number == 40:
                    print('b')
                if self.screen_number == 41:
                    print('c')

                if canmove and inven == 0:
                    inven = inventory()
                elif inven == 1:
                    canmove = False
                    update(self.screen, self.font, protagonist)
                    number2 = viewdiary(self.screen, self.font, number2, protagonist)
                    if number2 == -1:
                        inven = 0
                        number2 = 1

                if foinven == 1 and inven == 0:
                    canmove = True

                key_INPUT = pygame.key.get_pressed()
                if key_INPUT[pygame.K_ESCAPE] and canmove:
                    pygame.mouse.set_visible(True)
                    esc(self, self.screen, self.font, protagonist)

                pygame.display.update()

                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    print(pygame.mouse.get_pos())
            else:
                resume(self, self.screen, self.font, protagonist)
            if self.tostart == True:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
import pygame
from system import resume, esc, update
import sprite
from dialogue import dialogue
from background import right_area, screen_change
from interaction import interaction, diaryinter, inventory, viewdiary, owndiary2
from diaryinteraction import diary
from wire import wire_gimmick

gray = pygame.transform.scale(pygame.image.load('./assets/gray.png'), (1600, 900))
ivenui = pygame.transform.scale(pygame.image.load('./assets/ivenui.png'), (1600, 900))
Black = pygame.Color(0 ,0 ,0)
ivenui.set_colorkey(Black)


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
        image_gray = pygame.image.load('./assets/gray.png')
        Gray = pygame.transform.scale(image_gray, (1600, 900))
        Gray.set_alpha(175)
        run = True
        canmove = False
        x = dialogue(6, self.screen, self.font, protagonist)
        k = 0
        m = 0
        n = 0
        i = 0
        j = 0
        inven = 0
        foinven = 0
        nonejournal = pygame.Rect(560, 200, 0, 0)
        diary1pos = pygame.Rect(370, 183, 0, 0)
        diary2pos = pygame.Rect(760, 183, 0, 0)
        number = 1
        number2 = 1
        inter = 0
        togimic = False
        complete = False
        if x == 1:
            canmove = True
        while run:
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            if self.screen_number != 10 and (
                    n == 1 or self.screen_number != 12) and self.screen_number != 14 and self.screen_number != 18:
                self.screen_number = screen_change(protagonist, self.screen_number)
            if not self.pause:
                foinven = inven

                if canmove:
                    protagonist.move(self.screen, dt, 0.6)

                if self.screen_number == 7:
                    if protagonist.player.right - right_area >= 800:
                        self.screen_number += 1
                        protagonist.screen_number += 1
                        protagonist.alpha = 255
                if self.screen_number == 9:
                    protagonist.alpha = 125
                    if protagonist.player.right - right_area >= 800:
                        self.screen_number += 1
                        protagonist.screen_number += 1
                if self.screen_number == 10:
                    protagonist.alpha = 255
                    canmove = False
                    computer = pygame.Rect(1100, 550, 300, 100)
                    if k == 0:
                        k = dialogue(7, self.screen, self.font, protagonist)
                    if k == 1:
                        canmove = True
                        inter = interaction(protagonist.player, computer)
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
                            pygame.time.wait(500)
                            m = self.cutscene()
                            if m == 1:
                                k = 0
                                inter = 0
                                self.screen_number += 1
                                protagonist.screen_number += 1
                if self.screen_number == 12:
                    if k == 0:
                        k = dialogue(8, self.screen, self.font, protagonist)
                    elif k == 1:
                        body = pygame.Rect(800, 675, 200, 100)
                        update(self.screen, self.font, protagonist)

                        canmove = True
                        inter = interaction(protagonist.player, body)
                        if inter == 0:
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == body:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(body)
                        if inter == 1:
                            protagonist.move(self.screen, dt, 0.6)
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == body:
                                    a = 1
                            if a == 0:
                                protagonist.interact.append(body)

                        if inter == 2:
                            canmove = False
                            if n == 0:
                                a = 0
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == body:
                                        a = 1
                                if a == 1:
                                    protagonist.interact.remove(body)
                                update(self.screen, self.font, protagonist)
                                pygame.display.update()
                                n = dialogue(9, self.screen, self.font, protagonist)
                            elif n == 1:
                                canmove = True
                if self.screen_number == 13:
                    n = 0
                    if protagonist.player.left >= 600:
                        self.screen_number += 1
                        protagonist.screen_number += 1
                if self.screen_number == 14:
                    diary_ps = pygame.Rect(700, 550, 200, 50)
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
                        if n == 0:
                            canmove = False
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == diary_ps:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(diary_ps)
                            update(self.screen, self.font, protagonist)
                            pygame.display.update()
                            n = dialogue(10, self.screen, self.font, protagonist)
                    if n == 1:
                        n = 0
                        self.screen_number += 1
                        protagonist.screen_number += 1

                if self.screen_number == 15:
                    before = number
                    if i == 0:
                        number = diaryinter(self.screen, self.font, number, 1, 3, protagonist)
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
                            n = dialogue(11, self.screen, self.font, protagonist)
                        elif n == 1:
                            self.screen_number += 1
                            protagonist.screen_number += 1
                            update(self.screen, self.font, protagonist)

                if self.screen_number == 16:
                    n = 0
                    canmove = True
                    inter = 0
                    a = 0
                    diary_ps = pygame.Rect(700, 550, 200, 50)
                    for i in range(len(protagonist.interact)):
                        if protagonist.interact[i] == diary_ps:
                            a = 1
                    if a == 1:
                        protagonist.interact.remove(diary_ps)
                    update(self.screen, self.font, protagonist)
                if self.screen_number == 17:
                    if protagonist.player.left >= 400:
                        self.screen_number += 1
                        protagonist.screen_number += 1
                        update(self.screen, self.font, protagonist)
                if self.screen_number == 18:
                    if not complete and not togimic:
                        wire = pygame.Rect(850, 500, 200, 200)
                        update(self.screen, self.font, protagonist)
                        inter = interaction(protagonist.player, wire)
                        if inter == 0:
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == wire:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(wire)
                        if inter == 1:
                            protagonist.move(self.screen, dt, 0.6)
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == wire:
                                    a = 1
                            if a == 0:
                                protagonist.interact.append(wire)

                        if inter == 2:
                            canmove = False
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == wire:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(wire)
                            togimic = True
                    elif togimic and not complete:
                        inter = 0
                        if n == 0:
                            pygame.mouse.set_visible(True)
                            n = dialogue(12, self.screen, self.font, protagonist)
                        elif n == 1:
                            complete = wire_gimmick()
                            if complete:
                                n = 0
                                canmove = True
                    elif complete:
                        if n == 0:
                            n = dialogue(13, self.screen, self.font, protagonist)
                        if n == 1:
                            pygame.mouse.set_visible(False)
                            elevator = pygame.Rect(1140, 320, 320, 455)
                            update(self.screen, self.font, protagonist)
                            inter = interaction(protagonist.player, elevator)
                            if inter == 0:
                                a = 0
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == elevator:
                                        a = 1
                                if a == 1:
                                    protagonist.interact.remove(elevator)
                            if inter == 1:
                                protagonist.move(self.screen, dt, 0.6)
                                a = 0
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == elevator:
                                        a = 1
                                if a == 0:
                                    protagonist.interact.append(elevator)

                            if inter == 2:
                                canmove = False
                                a = 0
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == elevator:
                                        a = 1
                                if a == 1:
                                    protagonist.interact.remove(elevator)
                                run = False
                if canmove and inven == 0:
                    inven = inventory()
                elif inven == 1:
                    canmove = False
                    before2 = number2
                    update(self.screen, self.font, protagonist)
                    end = ((int)((len(owndiary2) - 1) / 2)) * 2 + 1
                    if j == 0:
                        number2 = viewdiary(self.screen, self.font, number2, protagonist)
                        self.screen.blit(ivenui, (0, 0))
                    if len(owndiary2)!=0:
                        if before2 != number2:
                            j = 1
                        if j != 0:
                            self.screen.blit(Gray, (0, 0))
                            self.screen.blit(diary[owndiary2[number - 1]], diary1pos)
                            if number != end or (number == end and len(owndiary2) % 2 == 0):
                                self.screen.blit(diary[owndiary2[number]], diary2pos)
                                j += 1
                        if j == 5:
                            j = 0
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

            else:
                resume(self, self.screen, self.font, protagonist)
            if self.tostart == True:
                return

            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                print(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

    def cutscene(self):
        cutscene1 = pygame.transform.scale(pygame.image.load('./assets/cutscene1.png'), (1600, 900))
        cutscene2 = pygame.transform.scale(pygame.image.load('./assets/cutscene2.png'), (1600, 900))
        cutscene3 = pygame.transform.scale(pygame.image.load('./assets/cutscene3.png'), (1600, 900))
        cutscene4 = pygame.transform.scale(pygame.image.load('./assets/cutscene4.png'), (1600, 900))
        cutscene5 = pygame.transform.scale(pygame.image.load('./assets/cutscene5.png'), (1600, 900))
        cutscene6 = pygame.transform.scale(pygame.image.load('./assets/cutscene6.png'), (1600, 900))
        cutscene7 = pygame.transform.scale(pygame.image.load('./assets/cutscene7.png'), (1600, 900))
        cutscene8 = pygame.transform.scale(pygame.image.load('./assets/cutscene8.png'), (1600, 900))
        cutscene9 = pygame.transform.scale(pygame.image.load('./assets/cutscene9.png'), (1600, 900))
        cutscene10 = pygame.transform.scale(pygame.image.load('./assets/cutscene10.png'), (1600, 900))
        cutscene11 = pygame.transform.scale(pygame.image.load('./assets/cutscene11.png'), (1600, 900))
        cutscene12 = pygame.transform.scale(pygame.image.load('./assets/cutscene12.png'), (1600, 900))
        cutscene13 = pygame.transform.scale(pygame.image.load('./assets/cutscene13.png'), (1600, 900))
        cutscene14 = pygame.transform.scale(pygame.image.load('./assets/cutscene14.png'), (1600, 900))
        cutscene15 = pygame.transform.scale(pygame.image.load('./assets/cutscene15.png'), (1600, 900))
        cutscene16 = pygame.transform.scale(pygame.image.load('./assets/cutscene16.png'), (1600, 900))
        cutscene17 = pygame.transform.scale(pygame.image.load('./assets/cutscene17.png'), (1600, 900))
        cutscene18 = pygame.transform.scale(pygame.image.load('./assets/cutscene18.png'), (1600, 900))
        cutscene19 = pygame.transform.scale(pygame.image.load('./assets/cutscene19.png'), (1600, 900))
        cutscene20 = pygame.transform.scale(pygame.image.load('./assets/cutscene20.png'), (1600, 900))
        cutscene21 = pygame.transform.scale(pygame.image.load('./assets/cutscene21.png'), (1600, 900))
        cutscene22 = pygame.transform.scale(pygame.image.load('./assets/cutscene22.png'), (1600, 900))
        cutscene23 = pygame.transform.scale(pygame.image.load('./assets/cutscene23.png'), (1600, 900))
        cutscene24 = pygame.transform.scale(pygame.image.load('./assets/cutscene24.png'), (1600, 900))
        cutscene25 = pygame.transform.scale(pygame.image.load('./assets/cutscene25.png'), (1600, 900))
        cutscene26 = pygame.transform.scale(pygame.image.load('./assets/cutscene26.png'), (1600, 900))
        cutscene27 = pygame.transform.scale(pygame.image.load('./assets/cutscene27.png'), (1600, 900))
        cutscene28 = pygame.transform.scale(pygame.image.load('./assets/cutscene28.png'), (1600, 900))
        cutscene29 = pygame.transform.scale(pygame.image.load('./assets/cutscene29.png'), (1600, 900))
        cutscene30 = pygame.transform.scale(pygame.image.load('./assets/cutscene30.png'), (1600, 900))
        cutscene31 = pygame.transform.scale(pygame.image.load('./assets/cutscene31.png'), (1600, 900))
        cutscene32 = pygame.transform.scale(pygame.image.load('./assets/heaven1.jpg'), (1600, 900))
        cutscene33 = pygame.transform.scale(pygame.image.load('./assets/heaven2.jpg'), (1600, 900))
        cutscene34 = pygame.transform.scale(pygame.image.load('./assets/heaven3.jpg'), (1600, 900))
        cutscene35 = pygame.transform.scale(pygame.image.load('./assets/heaven4.png'), (1600, 900))
        cutscene36 = pygame.transform.scale(pygame.image.load('./assets/heaven5.jpg'), (1600, 900))
        cutscene37 = pygame.transform.scale(pygame.image.load('./assets/angel-devil.png'), (1600, 900))
        cutscene38 = pygame.transform.scale(pygame.image.load('./assets/skull.png'), (1600, 900))
        cutscene39 = pygame.transform.scale(pygame.image.load('./assets/access_denied.jpg'), (1600, 900))
        cutscene = [cutscene1, cutscene2, cutscene3, cutscene4, cutscene5, cutscene6, cutscene7, cutscene8]
        cutscene2 = [cutscene10, cutscene11, cutscene12, cutscene13, cutscene14, cutscene15, cutscene16, cutscene17,
                     cutscene18, cutscene19, cutscene20]
        cutscene3 = [cutscene21, cutscene22, cutscene23, cutscene24, cutscene25, cutscene26, cutscene27, cutscene28,
                     cutscene29, cutscene30, cutscene31]
        cutscene4 = [cutscene32, cutscene33, cutscene34, cutscene35, cutscene36, cutscene37, cutscene38]

        run = True
        step = 0
        while run:
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            if step <= 25:
                self.screen.blit(cutscene1, (0, 0))
                gray.set_alpha(175 - 7 * step)
                self.screen.blit(gray, (0, 0))
                pygame.display.update()
            elif 25 < step < 105:
                self.screen.blit(cutscene[int((step - 25) / 10)], (0, 0))
                pygame.display.update()
            elif 105 <= step <= 190:
                self.screen.blit(cutscene9, (0, 0))
                gray.set_alpha(255 - 3 * (step - 105))
                self.screen.blit(gray, (0, 0))
                pygame.display.update()
            elif 191 <= step < 278:
                self.screen.blit(cutscene2[int((step - 190) / 8)], (0, 0))
                pygame.display.update()
            elif 278 <= step < 366:
                self.screen.blit(cutscene3[int((step - 278) / 8)], (0, 0))
                pygame.display.update()
            elif 366 <= step < 387:
                self.screen.blit(cutscene4[int((step - 366) / 3)], (0, 0))
                pygame.display.update()
            elif 387 <= step < 500:
                self.screen.blit(cutscene39, (0, 0))
                pygame.display.update()
            else:
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
            step += 1
            if 25 < step < 105:
                text = self.font[0].render("이 프로그램은 뭐지..", True, (255, 255, 255))
                self.screen.blit(text, (680, 700))
                pygame.display.update()
        return 1

import pygame
from system import resume, esc, update
import sprite
from dialogue import dialogue
from background import right_area, screen_change
from interaction import interaction, diaryinter, inventory, viewdiary, owndiary2
import moving
from diaryinteraction import diary

ivenui = pygame.transform.scale(pygame.image.load('./assets/ivenui.png'), (1600, 900))
Black = pygame.Color(0 ,0 ,0)
ivenui.set_colorkey(Black)
class B4():
    def __init__(self, screen, font):
        self.screen_number = 19
        self.screen = screen
        self.font = font
        self.pause = False
        self.tostart = False

    def story(self, character_left, character_right):
        pygame.mouse.set_visible(True)
        protagonist = sprite.protagonist(self.font, character_left, character_right, 19)
        update(self.screen, self.font, protagonist)
        image_gray = pygame.image.load('./assets/gray.png')
        Gray = pygame.transform.scale(image_gray, (1600, 900))
        Gray.set_alpha(175)
        run = True
        canmove = False
        x = dialogue(14, self.screen, self.font, protagonist)
        if x == 1:
            canmove = True
        inven = 0
        foinven = 0
        nonejournal = pygame.Rect(560, 200, 0, 0)
        n = 0
        k = 0
        i = 0
        j = 0
        inter = 0
        number = 4
        number2 = 1
        select = -1
        diary1pos = pygame.Rect(370, 183, 0, 0)
        diary2pos = pygame.Rect(760, 183, 0, 0)
        move1 = moving.moving(19, self.screen, self.font)
        move2 = moving.moving(20, self.screen, self.font)
        move3 = moving.moving(24, self.screen, self.font)
        while run:
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            if self.screen_number != 21 and self.screen_number != 25:
                self.screen_number = screen_change(protagonist, self.screen_number)
            if not self.pause:
                pygame.mouse.set_visible(True)
                foinven = inven
                if canmove:
                    protagonist.move(self.screen, dt, 0.6)

                if self.screen_number == 19:
                    foselect = select
                    select = move1.moving_obstacle(self.screen, 0.3, dt, protagonist)
                    if select != -1:
                        canmove = False
                    if foselect != select and select == -1:
                        canmove = True
                if self.screen_number == 20:
                    if n == 0:
                        canmove = False
                        n = dialogue(15, self.screen, self.font, protagonist)
                    elif n == 1:
                        canmove = True
                        foselect = select
                        select = move2.moving_obstacle(self.screen, 0.3, dt, protagonist)
                        if select != -1:
                            canmove = False
                        if foselect != select and select == -1:
                            canmove = True
                if self.screen_number == 21:
                    # pygame.mouse.set_visible(False)
                    diary_ps = pygame.Rect(1350, 550, 150, 50)
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
                if self.screen_number == 22:
                    before = number
                    if i == 0:
                        number = diaryinter(self.screen, self.font, number, 4, 6, protagonist)
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
                            n = dialogue(17, self.screen, self.font, protagonist)
                        elif n == 1:
                            self.screen_number += 1
                            protagonist.screen_number += 1
                            update(self.screen, self.font, protagonist)
                            canmove = True
                            n = 0
                if self.screen_number == 24:
                    inter = 0
                    if n == 0:
                        canmove = False
                        n = dialogue(18, self.screen, self.font, protagonist)
                    elif n == 1:
                        canmove = True
                        foselect = select
                        select = move3.moving_obstacle(self.screen, 0.3, dt, protagonist)
                        if select != -1:
                            canmove = False
                        if foselect != select and select == -1:
                            canmove = True
                if self.screen_number == 25:
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
                    if len(owndiary2) != 0:
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

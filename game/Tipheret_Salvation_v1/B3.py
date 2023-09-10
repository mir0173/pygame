import pygame
from system import resume, esc, update
import sprite
import animal_sprite
from dialogue import dialogue
from background import screen_change, bird_screen_change
from interaction import interaction, diaryinter, Inventory, cleardiary
from diaryinteraction import diary

gray = pygame.transform.scale(pygame.image.load('./assets/gray.png'), (1600, 900))
bird_image = pygame.transform.scale(pygame.image.load('./assets/bird_image.png'), (160, 160))
mole_image = pygame.transform.scale(pygame.image.load('./assets/mole.png'), (160, 160))
bird_right = pygame.image.load('./assets/bird.png')
bird_left = pygame.image.load('./assets/bird2.png')

class B3():
    def __init__(self, screen, font):
        self.screen_number = 26
        self.font = font
        self.screen = screen
        self.pause = False
        self.tostart = False

    def story(self, character_left, character_right):
        cleardiary(3)
        protagonist = sprite.protagonist(self.font, character_left, character_right, 26)
        uriel_left = pygame.image.load('./assets/oriel2.png')
        uriel_right = pygame.image.load('./assets/oriel.png')
        uriel = sprite.NPC(self.font, uriel_left, uriel_right, 0, 1600)
        npc_list = [uriel]
        npc_list[0].visible = True
        invent = Inventory(self.screen)
        protagonist.alpha = 125
        update(self.screen, self.font, protagonist, npc_list)
        image_gray = pygame.image.load('./assets/gray.png')
        Gray = pygame.transform.scale(image_gray, (1600, 900))
        Gray.set_alpha(175)
        run = True
        canmove = False
        d1 = dialogue(19, self.screen, self.font, protagonist, npc_list)
        if d1 == 1:
            canmove = True
        d2 = 0
        d4 = 0
        d5 = 0
        d6 = 0
        d7 = 0
        d8 = 0
        d9 = 0
        d10 = 0
        d11 = 0
        d12 = 0
        d13 = 0
        k = 0
        m = 0
        n = 0
        i = 0
        j = 0
        p = 0
        l = 0
        z = 0
        f = 0
        e = 0
        y = 0
        inven = 0
        foinven = 0
        nonejournal = pygame.Rect(560, 200, 0, 0)
        diary1pos = pygame.Rect(370, 183, 0, 0)
        diary2pos = pygame.Rect(760, 183, 0, 0)
        number = 7
        inter = 0

        while run:
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            if self.screen_number != 27 and (self.screen_number != 28 or d6 == 1):
                self.screen_number = screen_change(protagonist, self.screen_number)
            if not self.pause:
                foinven = inven
                if canmove:
                    protagonist.alpha = 255
                    protagonist.move(self.screen, dt, 0.6, npc_list)

                if self.screen_number == 26:
                    canmove = False
                    npc_list[0].visible = True
                    if k == 0:
                        k = npc_list[0].force_move(self.screen, dt, 0.6, protagonist.player.right + 100, 0)
                        update(self.screen, self.font, protagonist, npc_list)
                    if k == 1:
                        if d2 == 0:
                            d2 = dialogue(20, self.screen, self.font, protagonist, npc_list)
                        if d2 == 1:
                            canmove = True
                            body = pygame.Rect(600, 650, 300, 100)
                            inter = interaction(protagonist.player, body)
                            if inter == 0:
                                a = 0
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == body:
                                        a = 1
                                if a == 1:
                                    protagonist.interact.remove(body)
                            if inter == 1:
                                a = 0
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == body:
                                        a = 1
                                if a == 0:
                                    protagonist.interact.append(body)

                            if inter == 2:
                                canmove = False
                                d3 = dialogue(21, self.screen, self.font, protagonist, npc_list)
                                a = 0
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == body:
                                        a = 1
                                if a == 1:
                                    protagonist.interact.remove(body)

                                update(self.screen, self.font, protagonist, npc_list)
                                pygame.display.update()
                                pygame.time.wait(500)

                if self.screen_number == 27:
                    if m == 0:
                        npc_list[0].visible = False
                        m = npc_list[0].force_move(self.screen, dt, 0.6, 0, 0)
                        update(self.screen, self.font, protagonist, npc_list)
                    if m == 1:
                        canmove = False
                        npc_list[0].visible = True
                        if j == 0:
                            j = npc_list[0].force_move(self.screen, dt, 0.6, protagonist.player.right + 150, 0)
                            update(self.screen, self.font, protagonist, npc_list)
                        if j == 1:
                            if d4 == 0:
                                d4 = dialogue(22, self.screen, self.font, protagonist, npc_list)
                            if d4 == 1:
                                canmove = True
                                computer = pygame.Rect(300, 650, 300, 100)
                                inter = interaction(protagonist.player, computer)
                                if inter == 0:
                                    a = 0
                                    for i in range(len(protagonist.interact)):
                                        if protagonist.interact[i] == computer:
                                            a = 1
                                    if a == 1:
                                        protagonist.interact.remove(computer)
                                if inter == 1:
                                    a = 0
                                    for i in range(len(protagonist.interact)):
                                        if protagonist.interact[i] == computer:
                                            a = 1
                                    if a == 0:
                                        protagonist.interact.append(computer)

                                if inter == 2:
                                    a = 0
                                    for i in range(len(protagonist.interact)):
                                        if protagonist.interact[i] == computer:
                                            a = 1
                                    if a == 1:
                                        protagonist.interact.remove(computer)
                                        self.screen_number += 1
                                        protagonist.screen_number += 1
                                        canmove = False
                                        npc_list[0].visible = False
                                        update(self.screen, self.font, protagonist, npc_list)
                                        pygame.display.update()
                                        pygame.time.wait(500)

                if self.screen_number == 28:
                    if d5 == 0:
                        d5 = dialogue(23, self.screen, self.font, protagonist, npc_list)
                    if d5 == 1:
                        canmove = True
                        update(self.screen, self.font, protagonist, npc_list)
                        pygame.display.update()
                        bird_im = pygame.Rect(1200, 650, 300, 100)
                        inter = interaction(protagonist.player, bird_im)
                        if inter == 0:
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == bird_im:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(bird_im)
                        if inter == 1 and i == 0:
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == bird_im:
                                    a = 1
                            if a == 0:
                                protagonist.interact.append(bird_im)

                        if inter == 2:
                            canmove = False
                            d6 = dialogue(24, self.screen, self.font, protagonist, npc_list)
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == bird_im:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(bird_im)
                                i = 1

                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                            pygame.time.wait(500)

                if self.screen_number == 29:
                    if n == 0:
                        bird = pygame.Rect(50, 650, 300, 100)
                        self.screen.blit(bird_image, bird)
                        pygame.display.update()
                    canmove = False
                    if d7 == 0:
                        d7 = dialogue(25, self.screen, self.font, protagonist, npc_list)
                    if d7 == 1:
                        if n == 0:
                            canmove = True
                            inter = interaction(protagonist.player, bird)
                            if inter == 0:
                                a = 0
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == bird:
                                        a = 1
                                if a == 1:
                                    protagonist.interact.remove(bird)
                            if inter == 1:
                                a = 0
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == bird:
                                        a = 1
                                if a == 0:
                                    protagonist.interact.append(bird)

                            if inter == 2:
                                a = 0
                                n = 1
                                canmove = False
                                protagonist.alpha = 0
                                update(self.screen, self.font, protagonist, npc_list)
                                pygame.display.update()
                                protagonist_bird = animal_sprite.Bird(self.font, self.screen_number)
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == bird:
                                        a = 1
                                if a == 1:
                                    protagonist.interact.remove(bird)

                                pygame.time.wait(500)
                        if n == 1:
                            protagonist_bird.move(self.screen, dt, 0.6)
                            protagonist_bird.update(self.screen)
                            pygame.display.update()
                            self.screen_number = bird_screen_change(protagonist_bird, protagonist, self.screen_number)

                if self.screen_number == 30:
                    if p == 0:
                        mole = pygame.Rect(50, 650, 300, 100)
                        self.screen.blit(mole_image, mole) 
                        pygame.display.update()
                        canmove = True
                        inter = interaction(protagonist.player, mole)
                        if inter == 0:
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == mole:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(mole)
                        if inter == 1:
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == mole:
                                    a = 1
                            if a == 0:
                                protagonist.interact.append(mole)

                        if inter == 2:
                            a = 0
                            p = 1
                            canmove = False
                            protagonist.alpha = 0
                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                            protagonist_mole = animal_sprite.Mole(self.font, self.screen_number)
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == mole:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(mole)

                            pygame.time.wait(500)
                    if p == 1:
                        l = protagonist_mole.move()
                        protagonist_mole.update(self.screen)
                        pygame.display.update()
                        if l:
                            self.screen_number += 1
                            protagonist.screen_number += 1

                if self.screen_number == 31:
                    canmove = False
                    protagonist.alpha = 255
                    if d8 == 0:
                        d8 = dialogue(26, self.screen, self.font, protagonist, npc_list)
                    if d8 == 1:
                        canmove = True
                        diary_ps = pygame.Rect(1350, 750, 150, 50)
                        update(self.screen, self.font, protagonist, npc_list)
                        inter = interaction(protagonist.player, diary_ps)
                        if inter == 0:
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == diary_ps:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(diary_ps)
                        if inter == 1:
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == diary_ps:
                                    a = 1
                            if a == 0:
                                protagonist.interact.append(diary_ps)

                        if inter == 2:
                            canmove = False
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == diary_ps:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(diary_ps)
                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                            self.screen_number += 1
                            protagonist.screen_number += 1

                if self.screen_number == 32:
                    before = number
                    if y == 0:
                        number = diaryinter(self.screen, self.font, number, 7, 9, protagonist, npc_list)
                    if before != number:
                        y = 1
                    if y != 0:
                        update(self.screen, self.font, protagonist, npc_list)
                        self.screen.blit(Gray, (0, 0))
                        self.screen.blit(diary[number - 1], nonejournal)
                        y += 1
                    if y == 5:
                        y = 0
                    if number == -1:
                        if d9 == 0:
                            d9 = dialogue(27, self.screen, self.font, protagonist, npc_list)
                        if d9 == 1:
                            self.screen_number += 1
                            protagonist.screen_number += 1
                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                            pygame.time.wait(500)
                            canmove = True

                if self.screen_number == 33:
                    update(self.screen, self.font, protagonist, npc_list)
                    npc_list[0].visible = True
                    if d10 == 0:
                        canmove = False
                        protagonist.player = pygame.Rect(50, 790 - 320 * 0.5, 320 * 0.5, 320 * 0.5)
                        d10 = dialogue(28, self.screen, self.font, protagonist, npc_list)
                    if d10 == 1:
                        canmove = True

                if self.screen_number == 34:
                    if d11 == 0:
                        canmove = False
                        d11 = dialogue(29, self.screen, self.font, protagonist, npc_list)
                    if d11 == 1:
                        if d12 == 0:
                            if z == 0:
                                z = npc_list[0].force_move(self.screen, dt, 0.6, 1140, 1)
                                update(self.screen, self.font, protagonist, npc_list)
                            if z == 1:
                                d12 = dialogue(30, self.screen, self.font, protagonist, npc_list)
                        if d12 == 1:
                            if d13 == 0:
                                if e == 0:
                                    e = npc_list[0].force_move(self.screen, dt, 0.6, 940, 1)
                                    update(self.screen, self.font, protagonist, npc_list)
                                if e == 1:
                                    if f == 0:
                                        f = protagonist.force_move(self.screen, dt, 0.6, 1140, 1)
                                        update(self.screen, self.font, protagonist, npc_list)
                                    if f == 1:
                                        d13 = dialogue(31, self.screen, self.font, protagonist, npc_list)
                            if d13 == 1:
                                canmove = True
                                elevator = pygame.Rect(1140, 320, 320, 455)
                                inter = interaction(protagonist.player, elevator)
                                if inter == 0:
                                    a = 0
                                    for i in range(len(protagonist.interact)):
                                        if protagonist.interact[i] == elevator:
                                            a = 1
                                    if a == 1:
                                        protagonist.interact.remove(elevator)
                                if inter == 1:
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
                    inven = invent.inventory()
                elif inven == 1:
                    canmove = False
                    update(self.screen, self.font, protagonist, npc_list)
                    end = ((int)((len(invent.owndiary) - 1) / 2)) * 2 + 1
                    number2 = invent.viewdiary(self.screen, self.font, number2, protagonist, npc_list)
                    if len(invent.owndiary) != 0:
                        self.screen.blit(diary[invent.owndiary[number2 - 1]], diary1pos)
                        if number2 != end or (number2 == end and len(invent.owndiary) % 2 == 0):
                            self.screen.blit(diary[invent.owndiary[number2]], diary2pos)
                    if number2 == -1:
                        inven = 0
                        number2 = 1

                if foinven == 1 and inven == 0:
                    canmove = True

                key_INPUT = pygame.key.get_pressed()

                if key_INPUT[pygame.K_ESCAPE] and canmove:
                    pygame.mouse.set_visible(True)
                    esc(self, self.screen, self.font, protagonist, npc_list)

                pygame.display.update()

            else:
                resume(self, self.screen, self.font, protagonist, npc_list)
            if self.tostart == True:
                return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

import pygame
from system import resume, esc, update, nothavec, havec
import sprite
from dialogue import dialogue
from background import bottom_area, screen_change
from interaction import interaction, diaryinter, Inventory, cleardiary
from diaryinteraction import diary


class B2():
    def __init__(self, screen, font):
        self.screen_number = 36
        self.screen = screen
        self.font = font
        self.pause = False
        self.tostart = False

    def story(self, character_left, character_right):
        cleardiary(2)
        nothavec()
        pygame.mouse.set_visible(False)
        protagonist = sprite.protagonist(self.font, character_left, character_right, 36)
        uriel = sprite.NPC(self.font, pygame.image.load('./assets/uriel_left.png'),
                           pygame.image.load('./assets/uriel_right.png'), 1, 10)
        silB = sprite.NPC(self.font, pygame.transform.scale(pygame.image.load('./assets/silB_left.png'), (1600, 320)),
                          pygame.transform.scale(pygame.image.load('./assets/silB_right.png'), (1600, 320)), 0, 900)
        bul1 = sprite.NPC(self.font, pygame.transform.scale(pygame.image.load('./assets/Bul1.png'), (1600, 320)),
                          pygame.transform.scale(pygame.image.load('./assets/Bul1.png'), (1600, 320)), 0, 500)
        bul2 = sprite.NPC(self.font, pygame.transform.scale(pygame.image.load('./assets/Bul2.png'), (1600, 320)),
                          pygame.transform.scale(pygame.image.load('./assets/Bul2.png'), (1600, 320)), 0, 750)
        bul3 = sprite.NPC(self.font, pygame.transform.scale(pygame.image.load('./assets/Bul3.png'), (1600, 320)),
                          pygame.transform.scale(pygame.image.load('./assets/Bul3.png'), (1600, 320)), 0, 1000)
        bul4 = sprite.NPC(self.font, pygame.transform.scale(pygame.image.load('./assets/Bul4.png'), (1600, 320)),
                          pygame.transform.scale(pygame.image.load('./assets/Bul4.png'), (1600, 320)), 0, 1250)
        silC = sprite.NPC(self.font, pygame.transform.scale(pygame.image.load('./assets/silC_left.png'), (1600, 320)),
                          pygame.transform.scale(pygame.image.load('./assets/silC_right.png'), (1600, 320)), 1, 1200)
        npc_list = [uriel, silB, bul1, bul2, bul3, bul4, silC]
        npc_list[0].visible = True
        npc_list[1].visible = False
        npc_list[2].visible = False
        npc_list[3].visible = False
        npc_list[4].visible = False
        npc_list[5].visible = False
        npc_list[6].visible = False
        invent = Inventory(self.screen)
        update(self.screen, self.font, protagonist, npc_list)
        image_gray = pygame.image.load('./assets/gray.png')
        Gray = pygame.transform.scale(image_gray, (1600, 900))
        Gray.set_alpha(175)
        run = True
        canmove = False
        x = dialogue(32, self.screen, self.font, protagonist, npc_list)
        if x == 1:
            canmove = True
        inven = 0
        foinven = 0
        nonejournal = pygame.Rect(560, 200, 0, 0)
        diary1pos = pygame.Rect(330, 183, 0, 0)
        diary2pos = pygame.Rect(800, 183, 0, 0)
        ifCroute = False
        n = 0
        k = 0
        m = 0
        p = 0
        q = 0
        r = 0
        s = 0
        i = 0
        inter = 0
        intera = [0, 0, 0, 0]
        number = 10
        number2 = 1
        select = -1
        while run:
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            if self.screen_number != 36 and self.screen_number != 41 and self.screen_number != 42 and self.screen_number != 43 and self.screen_number != 44 and self.screen_number != 46:
                self.screen_number = screen_change(protagonist, self.screen_number)
            if not self.pause:
                foinven = inven
                if canmove:
                    protagonist.move(self.screen, dt, 0.6, npc_list)

                if self.screen_number == 36:
                    diary_ps = pygame.Rect(550, 725, 150, 50)
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
                        if k == 0:
                            canmove = False
                            a = 0
                            for i in range(len(protagonist.interact)):
                                if protagonist.interact[i] == diary_ps:
                                    a = 1
                            if a == 1:
                                protagonist.interact.remove(diary_ps)
                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                            k = dialogue(33, self.screen, self.font, protagonist, npc_list)
                        if k == 1:
                            n = 0
                            k = 0
                            self.screen_number += 1
                            protagonist.screen_number += 1
                if self.screen_number == 37:
                    before = number
                    if i == 0:
                        number = diaryinter(self.screen, self.font, number, 10, 12, protagonist, npc_list)
                    if before != number:
                        i = 1
                    if i != 0:
                        update(self.screen, self.font, protagonist, npc_list)
                        self.screen.blit(Gray, (0, 0))
                        self.screen.blit(diary[number - 1], nonejournal)
                        i += 1
                    if i == 5:
                        i = 0
                    if number == -1:
                        self.screen_number += 1
                        protagonist.screen_number += 1
                        update(self.screen, self.font, protagonist, npc_list)
                        canmove = True
                if self.screen_number == 39:
                    inter = 0
                    if n == 0:
                        canmove = False
                        n = dialogue(34, self.screen, self.font, protagonist, npc_list)
                    elif n == 1:
                        canmove = False
                        if k == 0:
                            k = protagonist.force_move(self.screen, dt, 0.4, 900, 1)
                            update(self.screen, self.font, protagonist, npc_list)
                        elif k == 1:
                            if m == 0:
                                m = dialogue(35, self.screen, self.font, protagonist, npc_list)
                            elif m == 1:
                                self.screen_number += 1
                                protagonist.screen_number += 1
                                update(self.screen, self.font, protagonist, npc_list)
                if self.screen_number == 40:
                    if p == 0:
                        npc_list[1].visible = True
                        p = npc_list[1].force_move(self.screen, dt, 0.6, 1500, 0)
                        update(self.screen, self.font, protagonist, npc_list)
                    elif p == 1:
                        if q == 0:
                            q = npc_list[0].force_move(self.screen, dt, 0.6, 800, 1)
                            update(self.screen, self.font, protagonist, npc_list)
                        elif q == 1:
                            if r == 0:
                                r = dialogue(36, self.screen, self.font, protagonist, npc_list)
                            elif r == 1:
                                if s == 0:
                                    s = protagonist.force_move(self.screen, dt, 0.4, 300, 1)
                                    update(self.screen, self.font, protagonist, npc_list)
                                elif s == 1:
                                    n = 0
                                    k = 0
                                    m = 0
                                    p = 0
                                    q = 0
                                    pygame.time.delay(1000)
                                    self.screen_number += 1
                                    protagonist.screen_number += 1
                                    npc_list[0].visible = False
                                    npc_list[1].visible = False
                                    protagonist.player.left = 50
                                    update(self.screen, self.font, protagonist, npc_list)
                                    canmove = True

                if self.screen_number == 41:
                    if n == 0:
                        number = 13
                        n = dialogue(37, self.screen, self.font, protagonist, npc_list)
                    elif n == 1:
                        diary_ps = pygame.Rect(1490, 700, 30, 25)
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
                            protagonist.move(self.screen, dt, 0.6, npc_list)
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
                                update(self.screen, self.font, protagonist, npc_list)
                                pygame.display.update()
                                k = dialogue(38, self.screen, self.font, protagonist, npc_list)
                            if k == 1:
                                n = 0
                                k = 0
                                self.screen_number += 1
                                protagonist.screen_number += 1
                if self.screen_number == 42:
                    before = number
                    if i == 0:
                        number = diaryinter(self.screen, self.font, number, 13, 14, protagonist, npc_list)
                    if before != number:
                        i = 1
                    if i != 0:
                        update(self.screen, self.font, protagonist, npc_list)
                        self.screen.blit(Gray, (0, 0))
                        self.screen.blit(diary[number - 1], nonejournal)
                        i += 1
                    if i == 5:
                        i = 0
                    if number == -1:
                        n = 0
                        self.screen_number += 1
                        protagonist.screen_number += 1
                        update(self.screen, self.font, protagonist, npc_list)
                        canmove = True
                if self.screen_number == 43:
                    if p == 0:
                        p = dialogue(43, self.screen, self.font, protagonist, npc_list)
                    elif p == 1:
                        pygame.mouse.set_visible(True)
                        npc_list[2].visible = True
                        npc_list[2].npc.top = 600
                        npc_list[3].visible = True
                        npc_list[3].npc.top = 600
                        npc_list[4].visible = True
                        npc_list[4].npc.top = 590
                        npc_list[5].visible = True
                        npc_list[5].npc.top = 590
                        bul = [npc_list[2].npc, npc_list[3].npc, npc_list[4].npc, npc_list[5].npc]
                        intera[0] = interaction(protagonist.player, bul[0])
                        intera[1] = interaction(protagonist.player, bul[1])
                        intera[2] = interaction(protagonist.player, bul[2])
                        intera[3] = interaction(protagonist.player, bul[3])
                        c = 0
                        for b in range(4):
                            if intera[b] == 0:
                                a = 0
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == bul[b]:
                                        a = 1
                                if a == 1:
                                    protagonist.interact.remove(bul[b])
                            if intera[b] == 1:
                                a = 0
                                for i in range(len(protagonist.interact)):
                                    if protagonist.interact[i] == bul[b]:
                                        a = 1
                                if a == 0:
                                    protagonist.interact.append(bul[b])

                            if intera[b] == 2 and c == 0:
                                c = 1
                                canmove = False
                                if k == 0:
                                    canmove = False
                                    a = 0
                                    for i in range(len(protagonist.interact)):
                                        if protagonist.interact[i] == bul[b]:
                                            a = 1
                                    if a == 1:
                                        protagonist.interact.remove(bul[b])
                                    update(self.screen, self.font, protagonist, npc_list)
                                    pygame.display.update()
                                    k = dialogue(39 + b, self.screen, self.font, protagonist, npc_list)
                                if k == 1:
                                    k = 0
                                    canmove = True

                        click = pygame.mouse.get_pressed()
                        pos = pygame.mouse.get_pos()
                        for b in range(4):
                            if bul[b].left <= pos[0] <= bul[b].right and bul[b].top <= pos[1] <= bul[b].bottom:
                                arrow = pygame.transform.scale(pygame.image.load('./assets/arrow.png'), (100, 100))
                                arrow.set_colorkey((255, 255, 255))
                                self.screen.blit(arrow, (bul[b].centerx - 50, 500))
                                if click[0] == 1:
                                    if b == 1:
                                        ifCroute = True
                                        havec()
                                    n = 1
                        if n == 1:
                            if q == 0:
                                canmove = False
                                q = dialogue(44, self.screen, self.font, protagonist, npc_list)
                            elif q == 1:
                                canmove = True
                                self.screen_number += 1
                                protagonist.screen_number += 1
                                n = 0
                                k = 0
                                p = 0
                                q = 0
                                for b in range(4):
                                    a = 0
                                    for i in range(len(protagonist.interact)):
                                        if protagonist.interact[i] == bul[b]:
                                            a = 1
                                    if a == 1:
                                        protagonist.interact.remove(bul[b])

                                protagonist.player = pygame.Rect(300, 775 - 320 * 0.5 + bottom_area, 320 * 0.5,
                                                                 320 * 0.5)
                                update(self.screen, self.font, protagonist, npc_list)
                                pygame.display.update()

                if self.screen_number == 44:
                    canmove = False
                    npc_list[2].visible = False
                    npc_list[3].visible = False
                    npc_list[4].visible = False
                    npc_list[5].visible = False
                    npc_list[0].visible = True
                    npc_list[1].visible = True
                    if ifCroute:
                        self.screen_number += 1
                        protagonist.screen_number += 1
                        update(self.screen, self.font, protagonist, npc_list)
                        pygame.display.update()
                    else:
                        if n == 0:
                            n = dialogue(46, self.screen, self.font, protagonist, npc_list)
                        elif n == 1:
                            canmove = True
                            if protagonist.player.right >= 1600:
                                if k == 0:
                                    a = npc_list[1].force_move(self.screen, dt, 0.6, 2000, 1)
                                    b = npc_list[0].force_move(self.screen, dt, 0.6, 1600, 1)
                                    k = a * b
                                if k == 1:
                                    protagonist.screen_number += 3
                                    self.screen_number += 3
                                    npc_list[0].npc = pygame.Rect(10, 775 - 320 * 0.5 + bottom_area, 320 * 0.5,
                                                                  320 * 0.5)
                                    protagonist.player = pygame.Rect(50, 775 - 320 * 0.5 + bottom_area, 320 * 0.5,
                                                                     320 * 0.5)
                                    n = 0
                                    k = 0
                                    npc_list[1].visible = False
                                    update(self.screen, self.font, protagonist, npc_list)
                                    pygame.display.update()
                if self.screen_number == 45:
                    update(self.screen, self.font, protagonist, npc_list)
                    pygame.display.update()
                    pygame.time.delay(1000)
                    self.screen_number += 1
                    protagonist.screen_number += 1
                if self.screen_number == 46:
                    update(self.screen, self.font, protagonist, npc_list)
                    pygame.display.update()
                    npc_list[6].visible = True
                    if n == 0:
                        n = dialogue(45, self.screen, self.font, protagonist, npc_list)
                    elif n == 1:
                        canmove = True
                        if protagonist.player.right >= 1600:
                            if k == 0:
                                k = npc_list[0].force_move(self.screen, dt, 0.6, 1600, 1)
                            if k == 1:
                                if p == 0:
                                    a = npc_list[1].force_move(self.screen, dt, 0.6, 1600, 1)
                                    b = npc_list[6].force_move(self.screen, dt, 0.6, 1600, 1)
                                    p = a * b
                                elif p == 1:
                                    protagonist.screen_number += 1
                                    self.screen_number += 1
                                    npc_list[1].visible = False
                                    npc_list[6].visible = False
                                    npc_list[0].npc = pygame.Rect(10, 775 - 320 * 0.5 + bottom_area, 320 * 0.5,
                                                                  320 * 0.5)
                                    protagonist.player = pygame.Rect(50, 775 - 320 * 0.5 + bottom_area, 320 * 0.5,
                                                                     320 * 0.5)

                                    n = 0
                                    k = 0
                                    update(self.screen, self.font, protagonist, npc_list)
                                    pygame.display.update()
                if self.screen_number == 47:
                    if n == 0:
                        n = npc_list[0].force_move(self.screen, dt, 0.6, 300, 0)
                    elif n == 1:
                        if k == 0:
                            npc_list[1].npc = pygame.Rect(350, 775 - 320 * 0.5 + bottom_area, 320 * 0.5, 320 * 0.5)
                            npc_list[1].left_right = 1
                            npc_list[6].npc = pygame.Rect(500, 775 - 320 * 0.5 + bottom_area + 5, 320 * 0.5, 320 * 0.5)
                            canmove = False
                            if ifCroute:
                                npc_list[1].visible = True
                                npc_list[6].visible = True
                            k = dialogue(47, self.screen, self.font, protagonist, npc_list)
                        elif k == 1:
                            canmove = True
                            pygame.mouse.set_visible(False)
                            elevator = pygame.Rect(1140, 320, 320, 455)
                            update(self.screen, self.font, protagonist, npc_list)
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

                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    print(pygame.mouse.get_pos())
            else:
                resume(self, self.screen, self.font, protagonist, npc_list)
            if self.tostart == True:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
        return

import pygame
from system import resume, esc, update, nothavec, havec
import sprite
from dialogue import dialogue
from background import bottom_area, screen_change
from interaction import interaction, diaryinter, Inventory, cleardiary
from diaryinteraction import diary
from battle import Battle_Phase_1, Battle_Phase_2


class B1:
    def __init__(self, screen, font, ifC):
        self.screen_number = 48
        self.screen = screen
        self.font = font
        self.pause = False
        self.tostart = False
        self.ifC = ifC

    def story(self, character_left, character_right, ):
        cleardiary(1)
        pygame.mouse.set_visible(False)
        protagonist = sprite.protagonist(self.font, character_left, character_right, 48)
        protagonist.player.left = 400
        uriel = sprite.NPC(self.font, pygame.image.load('./assets/uriel_left.png'),
                           pygame.image.load('./assets/uriel_right.png'), 1, 300)
        silB = sprite.NPC(self.font, pygame.transform.scale(pygame.image.load('./assets/silB_left.png'), (1600, 320)),
                          pygame.transform.scale(pygame.image.load('./assets/silB_right.png'), (1600, 320)), 1, 200)
        silC = sprite.NPC(self.font, pygame.transform.scale(pygame.image.load('./assets/silC_left.png'), (1600, 320)),
                          pygame.transform.scale(pygame.image.load('./assets/silC_right.png'), (1600, 320)), 1, 100)
        Rapha = sprite.NPC(self.font, pygame.image.load('./assets/raphael_left.png'),
                           pygame.image.load('./assets/raphael_right.png'), 0, 1400)
        guard1 = sprite.NPC(self.font, pygame.image.load('./assets/guard_left.png'),
                            pygame.image.load('./assets/guard_left.png'), 0, 1100)
        guard2 = sprite.NPC(self.font, pygame.image.load('./assets/guard_left.png'),
                            pygame.image.load('./assets/guard_left.png'), 0, 1150)
        guard3 = sprite.NPC(self.font, pygame.image.load('./assets/guard_left.png'),
                            pygame.image.load('./assets/guard_left.png'), 0, 1200)
        silA = sprite.NPC(self.font, pygame.image.load('./assets/silA_right.png'),
                          pygame.image.load('./assets/silA_right.png'), 1, 400)
        michael = sprite.NPC(self.font, pygame.image.load('./assets/michael2.png'),
                             pygame.image.load('./assets/michael1.png'), 0, 1200)
        robot = sprite.NPC(self.font, pygame.image.load('./assets/robot_left.png'),
                           pygame.image.load('./assets/robot_left.png'), 0, 900)
        bullet = sprite.NPC(self.font, pygame.image.load('./assets/bullets.png'),
                            pygame.image.load('./assets/bullets.png'), 1, 200)
        npc_list = [uriel, silB, silC, Rapha, guard1, guard2, guard3, silA, michael, robot, bullet]
        invent = Inventory(self.screen)
        image_gray = pygame.image.load('./assets/gray.png')
        Gray = pygame.transform.scale(image_gray, (1600, 900))
        Gray.set_alpha(175)
        run = True
        canmove = False
        number2 = 1
        npc_list[0].visible = True
        if self.ifC == 1:
            npc_list[1].visible = True
            npc_list[2].visible = True

        update(self.screen, self.font, protagonist, npc_list)
        pygame.display.update()
        x = dialogue(48, self.screen, self.font, protagonist, npc_list)
        if x == 1:
            canmove = True
        inven = 0
        foinven = 0
        diary1pos = pygame.Rect(330, 183, 0, 0)
        diary2pos = pygame.Rect(800, 183, 0, 0)
        n = 0
        k = 0
        m = 0
        p = 0
        q = 0
        r = 0
        s = 0
        win1 = -1
        win2 = -1
        i = 0
        shoot = pygame.mixer.Sound('./assets/shooting.mp3')
        while run:
            clock = pygame.time.Clock()
            dt = clock.tick(60)

            if not self.pause:
                foinven = inven
                if canmove:
                    protagonist.move(self.screen, dt, 0.6, npc_list)

                if self.screen_number == 48:
                    update(self.screen, self.font, protagonist, npc_list)
                    pygame.display.update()
                    if self.ifC == 1:
                        npc_list[2].visible = True
                    canmove = True
                    if protagonist.player.right >= 1600:
                        canmove = False
                        if k == 0:
                            k = npc_list[0].force_move(self.screen, dt, 1, 1600, 1)
                        if k == 1:
                            if p == 0:
                                a = npc_list[1].force_move(self.screen, dt, 1, 1600, 1)
                                b = npc_list[2].force_move(self.screen, dt, 1, 1600, 1)
                                p = a * b
                            elif p == 1:
                                protagonist.screen_number += 1
                                self.screen_number += 1
                                k = 0
                                p = 0
                                npc_list[1].visible = False
                                npc_list[2].visible = False
                                npc_list[0].npc = pygame.Rect(200, 775 - 320 * 0.5 + bottom_area, 320 * 0.5,
                                                              320 * 0.5)
                                npc_list[1].npc = pygame.Rect(60, 775 - 320 * 0.5 + bottom_area, 320 * 0.5,
                                                              320 * 0.5)
                                npc_list[2].npc = pygame.Rect(30, 775 - 320 * 0.5 + bottom_area + 12, 320 * 0.5,
                                                              320 * 0.5)
                                protagonist.player = pygame.Rect(100, 775 - 320 * 0.5 + bottom_area, 320 * 0.5,
                                                                 320 * 0.5)
                if self.screen_number == 49:
                    canmove = False
                    if n == 0:
                        npc_list[0].visible = True
                        npc_list[3].visible = True
                        npc_list[4].visible = True
                        npc_list[5].visible = True
                        npc_list[6].visible = True
                        npc_list[7].visible = True
                        if self.ifC == 1:
                            npc_list[1].visible = True
                            npc_list[2].visible = True
                        n = dialogue(49, self.screen, self.font, protagonist, npc_list)
                    if n == 1:
                        if s == 0:
                            npc_list[0] = sprite.NPC(self.font, pygame.image.load('./assets/uriel_gun.png'),
                                                     pygame.image.load('./assets/uriel_gun.png'), 1, 200)
                            npc_list[0].visible = True
                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                            pygame.time.wait(100)
                        s += 1
                        if s >= 1:
                            if k == 0:
                                k = dialogue(50, self.screen, self.font, protagonist, npc_list)
                            if k == 1:
                                if p == 0:
                                    shoot.play()
                                    npc_list[10].visible = True
                                    npc_list[10].force_move(self.screen, dt, 5, 2000, 1)
                                p += 1
                                if 0 <= p <= 100:
                                    npc_list[10].visible = True
                                    npc_list[10].force_move(self.screen, dt, 5, 2000, 1)
                                    update(self.screen, self.font, protagonist, npc_list)
                                    pygame.display.update()
                                if p == 10:
                                    npc_list[4].visible = False
                                if p == 100:
                                    shoot.play()
                                    npc_list[10].npc.left = 200
                                    update(self.screen, self.font, protagonist, npc_list)
                                    pygame.display.update()
                                if p == 110:
                                    npc_list[5].visible = False
                                if 100 <= p <= 200:
                                    npc_list[10].visible = True
                                    npc_list[10].force_move(self.screen, dt, 5, 2000, 1)
                                    update(self.screen, self.font, protagonist, npc_list)
                                    pygame.display.update()
                                if p >= 200:
                                    npc_list[10].visible = False
                                    if q == 0:
                                        npc_list[0] = sprite.NPC(self.font,
                                                                 pygame.image.load('./assets/uriel_left.png'),
                                                                 pygame.image.load('./assets/uriel_right.png'), 1, 200)
                                        npc_list[0].visible = True
                                        update(self.screen, self.font, protagonist, npc_list)
                                        pygame.display.update()
                                        q = dialogue(51, self.screen, self.font, protagonist, npc_list)
                                    if q == 1:
                                        if m == 0:
                                            a = npc_list[0].force_move(self.screen, dt, 0.6, 2000, 1)
                                            b = npc_list[1].force_move(self.screen, dt, 0.6, 2000, 1)
                                            c = npc_list[2].force_move(self.screen, dt, 0.6, 2000, 1)
                                            d = protagonist.force_move(self.screen, dt, 0.6, 2000, 1)
                                            m = a * b * c * d
                                            update(self.screen, self.font, protagonist, npc_list)
                                            pygame.display.update()
                                        if m == 1:
                                            if r == 0:
                                                r = dialogue(52, self.screen, self.font, protagonist, npc_list)
                                            if r == 1:
                                                self.screen_number += 1
                                                protagonist.screen_number += 1
                                                n = 0
                                                k = 0
                                                p = 0
                                                q = 0
                                                m = 0
                                                r = 0
                                                update(self.screen, self.font, protagonist, npc_list)
                                                pygame.display.update()
                if self.screen_number == 50:
                    npc_list[0].npc = pygame.Rect(200, 775 - 320 * 0.5 + bottom_area, 320 * 0.5,
                                                  320 * 0.5)
                    npc_list[1].npc = pygame.Rect(60, 775 - 320 * 0.5 + bottom_area, 320 * 0.5,
                                                  320 * 0.5)
                    npc_list[2].npc = pygame.Rect(30, 775 - 320 * 0.5 + bottom_area, 320 * 0.5,
                                                  320 * 0.5)
                    protagonist.player = pygame.Rect(100, 775 - 320 * 0.5 + bottom_area, 320 * 0.5,
                                                     320 * 0.5)
                    if n == 0:
                        npc_list[0].visible = True
                        npc_list[3].visible = False
                        npc_list[4].visible = False
                        npc_list[5].visible = False
                        npc_list[6].visible = False
                        npc_list[7].visible = False
                        npc_list[8].visible = True
                        if self.ifC == 1:
                            npc_list[1].visible = True
                            npc_list[2].visible = True
                        n = dialogue(53, self.screen, self.font, protagonist, npc_list)
                    if n == 1:
                        if m == 0:
                            npc_list[0] = sprite.NPC(self.font, pygame.image.load('./assets/uriel_gun.png'),
                                                     pygame.image.load('./assets/uriel_gun.png'), 1, 200)
                            npc_list[0].visible = True
                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                            shoot.play()
                            npc_list[10].npc.left = 200
                        m += 1
                        if 0 <= m <= 50:
                            npc_list[10].visible = True
                            npc_list[9].visible = True
                            if (npc_list[10].force_move(self.screen, dt, 5, 900, 1) == 1):
                                npc_list[10].visible = False
                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                        if m == 50:
                            npc_list[10].visible = True
                            npc_list[10].npc.left = 900
                            npc_list[0] = sprite.NPC(self.font, pygame.image.load('./assets/uriel_left.png'),
                                                     pygame.image.load('./assets/uriel_right.png'), 1, 200)
                            npc_list[0].visible = True
                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                            shoot.play()
                        if 50 <= m <= 80:
                            npc_list[10].force_move(self.screen, dt, 5, 0, 0)
                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                        if m == 80:
                            npc_list[0] = sprite.NPC(self.font, pygame.image.load('./assets/uriel_hit.png'),
                                                     pygame.image.load('./assets/uriel_hit.png'), 1, 200)
                            npc_list[0].visible = True
                            npc_list[10].visible = False
                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                            pygame.time.wait(1000)
                            npc_list[0].visible = False
                            m = 101
                        if m >= 101:
                            if p == 0:
                                s = 0
                                m = 101
                                p = dialogue(54, self.screen, self.font, protagonist, npc_list)
                            if p == 1:
                                if s == 0:
                                    shoot.play()
                                    npc_list[9].visible = False
                                    npc_list[10].npc.left = 100
                                s += 1
                                if 0 <= s <= 20:
                                    npc_list[10].visible = True
                                    npc_list[10].force_move(self.screen, dt, 10, 2000, 1)
                                    update(self.screen, self.font, protagonist, npc_list)
                                    pygame.display.update()
                                print(s)
                                if s >= 20:
                                    if q == 0:
                                        npc_list[8] = sprite.NPC(self.font,
                                                                 pygame.image.load('./assets/michael_hit.png'),
                                                                 pygame.image.load('./assets/michael_hit.png'), 0, 1200)
                                        npc_list[8].visible = True
                                        q = dialogue(55, self.screen, self.font, protagonist, npc_list)
                                    if q == 1:
                                        npc_list[8] = sprite.NPC(self.font,
                                                                 pygame.image.load('./assets/michael2.png'),
                                                                 pygame.image.load('./assets/michael1.png'), 0, 1200)
                                        npc_list[8].visible = True
                                        self.screen_number += 1
                                        protagonist.screen_number += 1
                                        n = 0
                                        m = 0
                                        p = 0
                                        s = 0
                                        q = 0

                if self.screen_number == 51:
                    npc_list[1].visible = False
                    npc_list[2].visible = False
                    npc_list[9].visible = False
                    update(self.screen, self.font, protagonist, npc_list)
                    if n == 0:
                        n = dialogue(56, self.screen, self.font, protagonist, npc_list)
                    if n == 1:
                        if win1 == -1:
                            win1 = Battle_Phase_1()
                        if win1 == 1:
                            n = 0
                            self.screen_number += 1
                            protagonist.screen_number += 1
                        if win1 == 0:
                            if m == 0:
                                m = dialogue(57, self.screen, self.font, protagonist, npc_list)
                            if m == 1:
                                protagonist.player.left = - 500
                                npc_list[8].visible = False
                                self.screen.blit(pygame.transform.scale(pygame.image.load('./assets/firstend.png'),
                                                                        (1600, 900)), (0, 0))
                                pygame.display.update()
                                pygame.time.wait(5000)
                                return
                if self.screen_number == 52:
                    if n == 0:
                        n = dialogue(58, self.screen, self.font, protagonist, npc_list)
                    if n == 1:
                        npc_list[8].visible = False
                        update(self.screen, self.font, protagonist, npc_list)
                        self.screen.blit(
                            pygame.transform.scale(pygame.image.load('./assets/meta1.png'), (500, 500)),
                            (900, 265))
                        pygame.display.update()
                        pygame.time.delay(500)
                        self.screen.blit(
                            pygame.transform.scale(pygame.image.load('./assets/meta2.png'), (500, 500)),
                            (900, 265))
                        pygame.display.update()
                        pygame.time.delay(500)
                        self.screen.blit(
                            pygame.transform.scale(pygame.image.load('./assets/meta3.png'), (500, 500)),
                            (900, 265))
                        pygame.display.update()
                        pygame.time.delay(500)
                        self.screen.blit(
                            pygame.transform.scale(pygame.image.load('./assets/meta4.png'), (500, 500)),
                            (900, 265))
                        pygame.display.update()
                        pygame.time.delay(500)
                        self.screen.blit(
                            pygame.transform.scale(pygame.image.load('./assets/meta5.png'), (500, 500)),
                            (900, 265))
                        pygame.display.update()
                        pygame.time.delay(500)
                        self.screen.blit(
                            pygame.transform.scale(pygame.image.load('./assets/meta6.png'), (500, 500)),
                            (900, 265))
                        pygame.display.update()
                        pygame.time.delay(500)
                        self.screen.blit(
                            pygame.transform.scale(pygame.image.load('./assets/meta7.png'), (500, 500)),
                            (900, 265))
                        pygame.display.update()
                        pygame.time.delay(500)
                        self.screen.blit(
                            pygame.transform.scale(pygame.image.load('./assets/meta8.png'), (500, 500)),
                            (900, 265))
                        pygame.display.update()
                        pygame.time.delay(500)
                        pygame.display.update()
                        if m == 0:
                            m = dialogue(59, self.screen, self.font, protagonist, npc_list)
                        if m == 1:
                            if win2 == -1:
                                win2 = Battle_Phase_2()
                            if win2 == 0:
                                if self.ifC == 1:
                                    self.screen.blit(
                                        pygame.transform.scale(pygame.image.load('./assets/crack1.png'), (1600, 900)),
                                        (0, 0))
                                    pygame.display.update()
                                    pygame.time.delay(1000)
                                    if q == 0:
                                        q = dialogue(61, self.screen, self.font, protagonist, npc_list)
                                    if q == 1:
                                        protagonist.player.left = - 500
                                        npc_list[8].visible = False

                                        self.screen_number += 1
                                        protagonist.screen_number += 1
                                        n = 0
                                        k = 0
                                        m = 0
                                        q = 0
                                        update(self.screen, self.font, protagonist, npc_list)
                                        pygame.display.update()

                                if self.ifC == 0:
                                    if p == 0:
                                        p = dialogue(67, self.screen, self.font, protagonist, npc_list)
                                    if p == 1:
                                        self.screen.blit(
                                            pygame.transform.scale(pygame.image.load('./assets/secondend.png'),
                                                                   (1600, 900)), (0, 0))
                                        pygame.display.update()
                                        pygame.time.wait(5000)
                                        return
                            if win2 == 1:
                                if p == 0:
                                    p = dialogue(68, self.screen, self.font, protagonist, npc_list)

                                if p == 1:
                                    dialogue(69, self.screen, self.font, protagonist, npc_list)
                                    protagonist.player.left = - 500
                                    npc_list[8].visible = False
                                    self.screen_number = 56
                                    protagonist.screen_number = 56
                                    return
                if self.screen_number == 53:
                    npc_list[2].visible = True
                    npc_list[3].visible = True
                    npc_list[4].visible = True
                    npc_list[5].visible = True
                    npc_list[6].visible = True
                    if n == 0:
                        n = dialogue(63, self.screen, self.font, protagonist, npc_list)
                    if n == 1:
                        if q == 0:
                            q = npc_list[2].force_move(self.screen, dt, 0.6, 800, 1)
                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                        if q == 1:
                            if p == 0:
                                p = dialogue(64, self.screen, self.font, protagonist, npc_list)
                            if p == 1:
                                self.screen_number += 1
                                protagonist.screen_number += 1
                                npc_list[2].visible = False
                                npc_list[3].visible = False
                                npc_list[4].visible = False
                                npc_list[5].visible = False
                                npc_list[6].visible = False
                                update(self.screen, self.font, protagonist, npc_list)
                                pygame.display.update()

                if self.screen_number == 54:
                    protagonist.player.left = 100
                    npc_list[8].visible = True
                    update(self.screen, self.font, protagonist, npc_list)
                    self.screen.blit(
                        pygame.transform.scale(pygame.image.load('./assets/crack1.png'), (1600, 900)),
                        (0, 0))
                    pygame.display.update()
                    pygame.time.delay(500)
                    self.screen.blit(
                        pygame.transform.scale(pygame.image.load('./assets/crack2.png'), (1600, 900)),
                        (0, 0))
                    pygame.display.update()
                    pygame.time.delay(500)
                    self.screen.blit(
                        pygame.transform.scale(pygame.image.load('./assets/crack3.png'), (1600, 900)),
                        (0, 0))
                    pygame.display.update()
                    pygame.time.delay(500)
                    self.screen.blit(
                        pygame.transform.scale(pygame.image.load('./assets/crack4.png'), (1600, 900)),
                        (0, 0))
                    pygame.display.update()
                    pygame.time.delay(500)
                    self.screen.blit(
                        pygame.transform.scale(pygame.image.load('./assets/crack5.png'), (1600, 900)),
                        (0, 0))
                    pygame.display.update()
                    pygame.time.delay(500)
                    self.screen_number += 1
                    protagonist.screen_number += 1

                if self.screen_number == 55:
                    if k == 0:
                        k = dialogue(65, self.screen, self.font, protagonist, npc_list)
                    if k == 1:
                        self.screen_number += 1
                        protagonist.screen_number += 1

                if self.screen_number == 56:
                    protagonist.player.left = 500
                    npc_list[3].visible = True
                    npc_list[8].visible = False
                    if i == 0:
                        i = dialogue(71, self.screen, self.font, protagonist, npc_list)
                    if i == 1:
                        if win2 == 0:
                            self.screen.blit(
                                pygame.transform.scale(pygame.image.load('./assets/thirdend.png'),
                                                       (1600, 900)), (0, 0))
                            pygame.display.update()
                            pygame.time.wait(5000)
                            return
                        else:
                            self.screen.blit(
                                pygame.transform.scale(pygame.image.load('./assets/thirdend.png'),
                                                       (1600, 900)), (0, 0))
                            pygame.display.update()
                            pygame.time.wait(5000)
                            return

                pygame.display.update()

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
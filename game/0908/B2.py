import pygame
from system import resume, esc, update, havec, nothavec
import sprite
from dialogue import dialogue
from background import right_area, screen_change
from interaction import interaction, diaryinter, inventory, cleardiary
from diaryinteraction import diary
from text import text, namepos, name, pos, char


class B2():
    def __init__(self, screen, font):
        self.screen_number = 36
        self.screen = screen
        self.font = font
        self.pause = False
        self.tostart = False

    def story(self, character_left, character_right):
        nothavec()
        cleardiary(2)
        pygame.mouse.set_visible(True)
        protagonist = sprite.protagonist(self.font, character_left, character_right, 36)
        invent = inventory(self.screen)
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
        diary1pos = pygame.Rect(370, 183, 0, 0)
        diary2pos = pygame.Rect(760, 183, 0, 0)
        n = 0
        k = 0
        m = 0
        p = 0
        q = 0
        i = 0
        inter = 0
        intera = [0, 0, 0, 0]
        number = 12
        number2 = 1

        print(text[40])
        print(name[40])
        print(char[40])
        print(pos[40])

        select = -1
        while run:
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            if self.screen_number != 36 and self.screen_number != 42:
                self.screen_number = screen_change(protagonist, self.screen_number)
            if not self.pause:
                foinven = inven
                if canmove:
                    protagonist.move(self.screen, dt, 0.6)

                if self.screen_number == 36:
                    diary_ps = pygame.Rect(550, 725, 150, 50)
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
                            k = dialogue(33, self.screen, self.font, protagonist)
                        if k == 1:
                            n = 0
                            k = 0
                            self.screen_number += 1
                            protagonist.screen_number += 1
                if self.screen_number == 37:
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
                        self.screen_number += 1
                        protagonist.screen_number += 1
                        update(self.screen, self.font, protagonist)
                        canmove = True
                if self.screen_number == 39:
                    inter = 0
                    if n == 0:
                        canmove = False
                        n = dialogue(34, self.screen, self.font, protagonist)
                    elif n == 1:
                        canmove = True
                        if k == 0:
                            k = protagonist.forced_move(self.screen, dt, 0.6, 800)
                            k = 1
                        elif k == 1:
                            if m == 0:
                                m = dialogue(35, self.screen, self.font, protagonist)
                            elif m == 1:
                                if p == 0:
                                    # p = npcmove
                                    print('d')
                                    p = 1
                                elif p == 1:
                                    if q == 0:
                                        q = dialogue(36, self.screen, self.font, protagonist)
                                    elif q == 1:
                                        n = 0
                                        k = 0
                                        m = 0
                                        p = 0
                                        q = 0
                                        self.screen_number += 1
                                        protagonist.screen_number += 1
                                        update(self.screen, self.font, protagonist)
                                        canmove = True

                if self.screen_number == 40:
                    if n == 0:
                        number = 15
                        n = dialogue(37, self.screen, self.font, protagonist)
                    elif n == 1:
                        diary_ps = pygame.Rect(500, 550, 150, 50)
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
                                k = dialogue(38, self.screen, self.font, protagonist)
                            if k == 1:
                                n = 0
                                k = 0
                                self.screen_number += 1
                                protagonist.screen_number += 1
                if self.screen_number == 41:
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
                        self.screen_number += 1
                        protagonist.screen_number += 1
                        update(self.screen, self.font, protagonist)
                        canmove = True
                if self.screen_number == 42:
                    bul = [pygame.Rect(500, 550, 150, 50), pygame.Rect(750, 550, 150, 50),
                           pygame.Rect(1000, 550, 150, 50), pygame.Rect(1250, 550, 150, 50)]
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
                                update(self.screen, self.font, protagonist)
                                pygame.display.update()
                                k = dialogue(39 + b, self.screen, self.font, protagonist)
                            if k == 1:
                                n = 0
                                k = 0
                                canmove = True
                if self.screen_number == 43:
                    print('c')
                    # havec()  이거 그 c를 만약 데려가면 그 부분에서 이거 써줘야한다
                if canmove and inven == 0:
                    inven = invent.inventory()
                elif inven == 1:
                    canmove = False
                    update(self.screen, self.font, protagonist)
                    end = ((int)((len(invent.owndiary) - 1) / 2)) * 2 + 1
                    number2 = invent.viewdiary(self.screen, self.font, number2, protagonist)
                    if len(invent.owndiary) != 0:
                        self.screen.blit(Gray, (0, 0))
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
import pygame
import sprite
from background import screen_change
from background import right_area
from system import esc
from system import resume
from system import update
from dialogue import dialogue
from background import bottom_area
from interaction import interaction

pausepopup = pygame.image.load('./assets/pause.png')


class B6:
    def __init__(self, screen, font):
        self.pause = False
        self.screen_number = 0
        self.tostart = False
        self.screen = screen
        self.font = font

    def tutorial(self, character_left, character_right):
        door_close = pygame.mixer.Sound('./assets/door_close.mp3')
        door_open = pygame.mixer.Sound('./assets/door_open.mp3')
        protagonist = sprite.protagonist(self.font, character_left, character_right, 0)
        run = True
        k = 0
        n = 0
        m = 0
        inter = 0
        temp = 0
        canmove = True
        npc = sprite.NPC(self.font, character_left, character_right, 0, 1200)
        npc2 = sprite.NPC(self.font, character_left, character_right, 0, 700)
        npc_list = [npc, npc2]
        npc.visible = npc2.visible = False

        dialogue(0, self.screen, self.font, protagonist, npc_list)
        while run:
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            if not self.pause:
                if canmove:
                    if inter != 1:
                        protagonist.move(self.screen, dt, 0.6, npc_list)
                        pygame.display.update()
                if self.screen_number != 6:
                    self.screen_number = screen_change(protagonist, self.screen_number)
                key_INPUT = pygame.key.get_pressed()
                if key_INPUT[pygame.K_ESCAPE]:
                    esc(self, self.screen, self.font, protagonist, npc_list)
                if self.screen_number == 1:
                    npc.visible = True
                    if temp == 0:
                        temp = protagonist.force_move(self.screen, dt, 0.6, 700, 0)
                        canmove = False
                    else:
                        canmove = True
                    npc.force_move(self.screen, dt, 0.6, 300, 1)
                    protagonist.alpha = 255
                    update(self.screen, self.font, protagonist, npc_list)
                    pygame.display.update()
                    if protagonist.player.right - right_area >= 800:
                        protagonist.player.right = right_area + 799
                        canmove = False
                        protagonist.player.bottom = 775 + bottom_area
                        k = dialogue(1, self.screen, self.font, protagonist, npc_list)
                    if k == 1:
                        update(self.screen, self.font, protagonist, npc_list)
                        pygame.display.update()
                        pygame.time.wait(2000)
                        canmove = True
                        protagonist.screen_number += 1
                        self.screen_number += 1
                        k = 0
                        update(self.screen, self.font, protagonist, npc_list)
                        pygame.display.update()
                if self.screen_number == 2:
                    npc.visible = False
                    door_open.play()
                    if k == 0:
                        pygame.time.wait(1000)
                        canmove = False
                        k = dialogue(2, self.screen, self.font, protagonist, npc_list)
                    if k == 1:
                        pygame.time.wait(1000)
                        protagonist.screen_number += 1
                        self.screen_number += 1
                if self.screen_number == 3:
                    door_close.play()
                    update(self.screen, self.font, protagonist, npc_list)
                    pygame.display.update()
                    pygame.time.wait(1000)
                    protagonist.screen_number += 1
                    self.screen_number += 1
                    k = 0
                if self.screen_number == 4:
                    npc2.visible = True
                    npc2.force_move(self.screen, dt, 0.6, 300, 1)
                    update(self.screen, self.font, protagonist, npc_list)
                    pygame.display.update()
                    if k == 0:
                        door_open.play()
                        k = dialogue(3, self.screen, self.font, protagonist, npc_list)
                    if k == 1:
                        canmove = True
                if self.screen_number == 5:
                    npc2.visible = False
                    protagonist.alpha = 125
                    canmove = False
                    if n == 0:
                        n = dialogue(4, self.screen, self.font, protagonist, npc_list)
                    if n == 1:
                        canmove = True
                    if protagonist.player.right - right_area >= 300:
                        canmove = False
                        protagonist.alpha = 255
                        protagonist.screen_number += 1
                        self.screen_number += 1
                        update(self.screen, self.font, protagonist, npc_list)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        if m == 0:
                            m = dialogue(5, self.screen, self.font, protagonist, npc_list)
                        if m == 1:
                            canmove = True
                            update(self.screen, self.font, protagonist, npc_list)
                            pygame.display.update()
                if self.screen_number == 6:
                    ladder = pygame.Rect(1300, 575, 200, 200)
                    inter = interaction(protagonist.player, ladder)
                    if inter == 0:
                        a = 0
                        for i in range(len(protagonist.interact)):
                            if protagonist.interact[i] == ladder:
                                a = 1
                        if a == 1:
                            protagonist.interact.remove(ladder)
                    if inter == 1:
                        protagonist.move(self.screen, dt, 0.6, npc_list)
                        a = 0
                        for i in range(len(protagonist.interact)):
                            if protagonist.interact[i] == ladder:
                                a = 1
                        if a == 0:
                            protagonist.interact.append(ladder)
                        pygame.display.update()
                    if inter == 2:
                        self.screen_number += 1
                        protagonist.screen_number += 1
                if self.screen_number == 7:
                    run = False
            else:
                resume(self, self.screen, self.font, protagonist, npc_list)
            if self.tostart == True:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
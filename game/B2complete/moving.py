import pygame
from background import obstacle_list, movable, movable_image, ifcrash ,right_area
from system import update


class moving():
    def __init__(self, screen_number, screen, font):
        self.obstacle = obstacle_list[screen_number]
        self.movable = movable[screen_number]
        self.movable_image = movable_image[screen_number]
        self.selected = -1
        self.selob = pygame.Rect(0, 0, 0, 0)
        self.foselob = pygame.Rect(0, 0, 0, 0)
        self.screen = screen
        self.font = font
        self.activate = 0

    def moving_obstacle(self, screen, game_speed, dt, protagonist):

        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        npc_list = []
        self.foselob.right = self.selob.right
        self.foselob.left = self.selob.left
        self.foselob.top = self.selob.top
        self.foselob.bottom = self.selob.bottom
        if self.selected == -1:
            if self.activate == 0:
                if click[0] == 1 and protagonist.player.right-right_area < 400:
                    for x in range(len(self.movable)):
                        if self.obstacle[self.movable[x]].left <= pos[0] <= self.obstacle[self.movable[x]].right and \
                                self.obstacle[self.movable[x]].top <= pos[1] <= self.obstacle[self.movable[x]].bottom:
                            self.selected = x
                            self.selob = self.obstacle[self.movable[x]]
                            self.movable_image[self.selected] = pygame.transform.scale(
                                pygame.image.load('./assets/move2.png'), (125, 125))
                elif click[0] == 1:
                    self.activate = 1

            elif self.activate < 60:
                text = pygame.image.load('./assets/tutorial8.png')
                text.set_colorkey((0, 0, 0))
                screen.blit(text, (500, 200))
                self.activate += 1
            elif self.activate == 60:
                self.activate = 0
        else:
            key_INPUT = pygame.key.get_pressed()
            if key_INPUT[pygame.K_LEFT] and self.selob.left >= 401:
                self.selob.left -= game_speed * dt
                for i in range(len(self.obstacle)):
                    if i == self.movable[self.selected]:
                        continue
                    if ifcrash(self.selob.left, self.selob.right, self.obstacle[i].left,
                               self.obstacle[i].right) and ifcrash(self.selob.top, self.selob.bottom,
                                                                   self.obstacle[i].top, self.obstacle[i].bottom):
                        self.selob.right = self.foselob.right
                        self.selob.left = self.foselob.left
                        self.selob.top = self.foselob.top
                        self.selob.bottom = self.foselob.bottom
            if key_INPUT[pygame.K_RIGHT] and self.selob.right <= 1600:
                self.selob.left += game_speed * dt
                for i in range(len(self.obstacle)):
                    if i == self.movable[self.selected]:
                        continue
                    if ifcrash(self.selob.left, self.selob.right, self.obstacle[i].left,
                               self.obstacle[i].right) and ifcrash(self.selob.top, self.selob.bottom,
                                                                   self.obstacle[i].top, self.obstacle[i].bottom):
                        self.selob.right = self.foselob.right
                        self.selob.left = self.foselob.left
                        self.selob.top = self.foselob.top
                        self.selob.bottom = self.foselob.bottom
            if key_INPUT[pygame.K_UP]:
                self.selob.top -= game_speed * dt
                for i in range(len(self.obstacle)):
                    if i == self.movable[self.selected]:
                        continue
                    if ifcrash(self.selob.left, self.selob.right, self.obstacle[i].left,
                               self.obstacle[i].right) and ifcrash(self.selob.top, self.selob.bottom,
                                                                   self.obstacle[i].top, self.obstacle[i].bottom):
                        self.selob.right = self.foselob.right
                        self.selob.left = self.foselob.left
                        self.selob.top = self.foselob.top
                        self.selob.bottom = self.foselob.bottom

            if key_INPUT[pygame.K_DOWN]:
                self.selob.top += game_speed * dt
                for i in range(len(self.obstacle)):
                    if i == self.movable[self.selected]:
                        continue
                    if ifcrash(self.selob.left, self.selob.right, self.obstacle[i].left,
                               self.obstacle[i].right) and ifcrash(self.selob.top, self.selob.bottom,
                                                                   self.obstacle[i].top, self.obstacle[i].bottom):
                        self.selob.right = self.foselob.right
                        self.selob.left = self.foselob.left
                        self.selob.top = self.foselob.top
                        self.selob.bottom = self.foselob.bottom

            update(self.screen, self.font, protagonist, npc_list)

            self.obstacle[self.movable[self.selected]] = self.selob

            if click[2] == 1:
                self.movable_image[self.selected] = pygame.transform.scale(pygame.image.load('./assets/move.png'),
                                                                           (125, 125))
                self.selected = -1

        protagonist.obstacle = self.obstacle
        protagonist.movable_image = self.movable_image
        return self.selected

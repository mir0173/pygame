import pygame
from background import bird_crash
from background import bird_left_area
from background import bird_right_area
from background import bird_bottom_area
from background import bird_top_area
from background import background_list
from background import obstacle_list
from background import movable
from background import movable_image
from background import ifcrash
from system import index

floor = 775
gravitation = 0.6
jumping = 6


class Bird(pygame.sprite.Sprite):
    def __init__(self, font, i):
        super().__init__()
        self.sheet1 = pygame.image.load('./assets/bird.png').convert_alpha()
        self.sheet2 = pygame.image.load('./assets/bird2.png').convert_alpha()
        self.screen_number = i
        self.background = background_list[self.screen_number]
        self.obstacle = obstacle_list[self.screen_number]
        self.movable = movable[self.screen_number]
        self.movable_image = movable_image[self.screen_number]
        self.frame_0 = self.get_image(0, 0.5, (0, 0, 0), 1)
        self.frame_1 = self.get_image(1, 0.5, (0, 0, 0), 1)
        self.frame_2 = self.get_image(2, 0.5, (0, 0, 0), 1)
        self.frame_3 = self.get_image(0, 0.5, (0, 0, 0), 0)
        self.frame_4 = self.get_image(1, 0.5, (0, 0, 0), 0)
        self.frame_5 = self.get_image(2, 0.5, (0, 0, 0), 0)
        self.animation_list_1 = [self.frame_0, self.frame_1, self.frame_2]
        self.animation_list_2 = [self.frame_3, self.frame_4, self.frame_5]
        self.last_update = pygame.time.get_ticks()
        self.font = font
        self.frame = 0
        self.gravity = 0
        self.player = pygame.Rect(0, 775 - 200 + bird_bottom_area, 160, 160)
        self.player_image = self.frame_0
        self.left_right = 1
        self.forplayer = pygame.Rect(0, 775 - 200 + bird_bottom_area, 160, 160)
        self.ui = pygame.image.load('./assets/ui7.png')
        self.ui = pygame.transform.scale(self.ui, (1600, 900))
        self.ui.set_colorkey((255, 255, 254))

    def get_image(self, frame, scale, color, mod):
        if mod == 0:
            image = pygame.Surface((320, 320)).convert_alpha()
            image.blit(self.sheet1, (0, 0), (frame * 320, 0, 320, 320))
            image = pygame.transform.scale(image, (320 * scale, 320 * scale))
            image.set_colorkey(color)
            return image
        if mod == 1:
            image = pygame.Surface((320, 320)).convert_alpha()
            image.blit(self.sheet2, (0, 0), (frame * 320, 0, 320, 320))
            image = pygame.transform.scale(image, (320 * scale, 320 * scale))
            image.set_colorkey(color)
            return image

    def move(self, screen, dt, game_speed):
        self.forplayer.right = self.player.right
        self.forplayer.left = self.player.left
        self.forplayer.top = self.player.top
        self.forplayer.bottom = self.player.bottom
        screen.blit(self.background, (0, 0))
        self.movable_obstacle(screen)

        if self.left_right == 0:
            screen.blit(self.frame_3, self.player)
        else:
            screen.blit(self.frame_0, self.player)

        key_INPUT = pygame.key.get_pressed()
        if key_INPUT[pygame.K_a] and self.player.left >= 0:
            self.left_right = 0
            self.player.left -= game_speed * dt
            for i in range(len(self.obstacle)):
                if bird_crash(self.obstacle[i], self.player, self.left_right):
                    self.player.right = self.forplayer.right
                    self.player.left = self.forplayer.left
                    self.player.top = self.forplayer.top
                    self.player.bottom = self.forplayer.bottom

        if key_INPUT[pygame.K_d] and self.player.right <= 1600:
            self.left_right = 1
            self.player.right += game_speed * dt
            for i in range(len(self.obstacle)):
                if bird_crash(self.obstacle[i], self.player, self.left_right):
                    self.player.right = self.forplayer.right
                    self.player.left = self.forplayer.left
                    self.player.top = self.forplayer.top
                    self.player.bottom = self.forplayer.bottom

        if key_INPUT[pygame.K_SPACE]:
            self.gravity = -jumping
        self.player.top += self.gravity
        self.gravity += gravitation

        b = 1

        for i in range(len(self.obstacle)):
            if self.left_right == 1:
                if self.player.top + bird_top_area < self.obstacle[
                    i].top < self.player.bottom - bird_bottom_area and ifcrash(
                        self.player.left + bird_left_area, self.player.right - bird_right_area, self.obstacle[i].left,
                        self.obstacle[i].right):
                    b = 0
            if self.left_right == 0:
                if self.player.top + bird_top_area < self.obstacle[
                    i].top < self.player.bottom - bird_bottom_area and ifcrash(
                        self.player.left + bird_right_area, self.player.right - bird_left_area, self.obstacle[i].left,
                        self.obstacle[i].right):
                    b = 0
        if b == 0:
            self.player.top = self.forplayer.top
            self.player.bottom = self.forplayer.bottom
            self.gravity = 0

        b = 1

        for i in range(len(self.obstacle)):
            if self.left_right == 1:
                if self.player.top + bird_top_area < self.obstacle[
                    i].bottom < self.player.bottom - bird_bottom_area and ifcrash(
                        self.player.left + bird_left_area, self.player.right - bird_right_area, self.obstacle[i].left,
                        self.obstacle[i].right):
                    b = 0
            if self.left_right == 0:
                if self.player.top + bird_top_area < self.obstacle[
                    i].bottom < self.player.bottom - bird_bottom_area and ifcrash(
                        self.player.left + bird_right_area, self.player.right - bird_left_area, self.obstacle[i].left,
                        self.obstacle[i].right):
                    b = 0
        if b == 0:
            self.player.top = self.forplayer.top
            self.player.bottom = self.forplayer.bottom
            self.gravity = 0

    def update(self, screen):
        if self.left_right == 0:
            self.player_image = self.animation_list_1[self.frame]
            self.frame += 1
            self.frame = self.frame % 3
        if self.left_right == 1:
            self.player_image = self.animation_list_2[self.frame]
            self.frame += 1
            self.frame = self.frame % 3
        self.background = background_list[self.screen_number]
        screen.blit(self.background, (0, 0))
        screen.blit(self.player_image, self.player)
        self.movable_obstacle(screen)
        text = self.font[2].render(f"{index[self.screen_number][0]} - {index[self.screen_number][1]}", True,
                                   (255, 255, 255))
        screen.blit(self.ui, (0, 0))
        screen.blit(text, (320, 50, 0, 0))
        pygame.display.update()

    def movable_obstacle(self, screen):
        for x in range(len(self.movable)):
            screen.blit(self.movable_image[x], self.obstacle[self.movable[x]])


class Mole(pygame.sprite.Sprite):
    def __init__(self, font, i):
        super().__init__()
        self.font = font
        self.screen_number = i
        self.moving = False
        self.position = (150, 600)
        self.size = (160, 160)
        self.rect = pygame.Rect(self.position, self.size)
        self.image_index = 0
        images = [pygame.image.load('assets/mole.png')]
        self.images = [pygame.transform.scale(image, self.size) for image in images]
        self.current_position = 1
        self.next_position = 1
        self.end_position = False
        self.image = self.images[self.image_index]
        self.move_list = {1: [0, 0, 0, 2],
                          2: [5, 1, 0, 3],
                          3: [5, 4, 2, 6],
                          4: [5, 1, 3, 7],
                          5: [6, 4, 2, 3],
                          6: [7, 5, 3, 8],
                          7: [6, 1, 4, 0],
                          8: [6, 1, 0, 9]}
        self.position_list = {1: (150, 600),
                              2: (590, 550),
                              3: (1110, 430),
                              4: (470, 250),
                              5: (880, 220),
                              6: (1210, 75),
                              7: (620, 45),
                              8: (1430, 580)}
        self.ui = pygame.image.load('./assets/ui7.png')  # 파란색 UI
        self.ui = pygame.transform.scale(self.ui, (1600, 900))
        self.ui.set_colorkey((255, 255, 254))

    def move(self):
        key = pygame.key.get_pressed()
        if self.end_position:
            return True
        elif key[pygame.K_UP] and not self.moving:
            self.moving = True
            self.next_position = self.move_list[self.current_position][0]
        elif key[pygame.K_LEFT] and not self.moving:
            self.moving = True
            self.next_position = self.move_list[self.current_position][1]
        elif key[pygame.K_DOWN] and not self.moving:
            self.moving = True
            self.next_position = self.move_list[self.current_position][2]
        elif key[pygame.K_RIGHT] and not self.moving:
            self.moving = True
            self.next_position = self.move_list[self.current_position][3]
        if not key[pygame.K_UP] and not key[pygame.K_LEFT] and not key[pygame.K_DOWN] and not key[pygame.K_RIGHT]:
            self.moving = False

    def update(self, screen):
        screen.blit(background_list[self.screen_number], (0, 0))
        screen.blit(self.image, self.position)
        text = self.font[2].render(f"{index[self.screen_number][0]} - {index[self.screen_number][1]}", True,
                                   (255, 255, 255))
        screen.blit(self.ui, (0, 0))
        screen.blit(text, (320, 50, 0, 0))
        if self.next_position == 0:
            self.next_position = self.current_position
        elif self.next_position == 9:
            self.end_position = True
        elif self.next_position == self.current_position:
            self.image = self.images[self.image_index]
        elif self.next_position != self.current_position:
            self.position = self.position_list[self.next_position]
            pygame.mixer.Sound('assets/mole_sound.mp3').play()
            self.current_position = self.next_position

        self.rect = pygame.Rect(self.position, self.size)
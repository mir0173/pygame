import pygame
from random import randint
from background import crash
from background import left_area
from background import right_area
from background import bottom_area
from background import top_area
from background import background_list
from background import obstacle_list
from background import movable
from background import movable_image
from background import ifcrash
from system import update

floor = 775
gravitation = 0.6
jumping = 12


class protagonist():
    def __init__(self, font, image1, image2, i):
        self.sheet1 = image1
        self.sheet2 = image2
        self.screen_number = i
        self.alpha = 255
        self.background = background_list[self.screen_number]
        self.obstacle = obstacle_list[self.screen_number]
        self.movable = movable[self.screen_number]
        self.movable_image = movable_image[self.screen_number]
        self.frame_0 = self.get_image(0, 0.5, (0, 0, 0), 1)
        self.frame_1 = self.get_image(1, 0.5, (0, 0, 0), 1)
        self.frame_2 = self.get_image(2, 0.5, (0, 0, 0), 1)
        self.frame_3 = self.get_image(3, 0.5, (0, 0, 0), 1)
        self.frame_4 = self.get_image(4, 0.5, (0, 0, 0), 1)
        self.frame_5 = self.get_image(0, 0.5, (0, 0, 0), 0)
        self.frame_6 = self.get_image(1, 0.5, (0, 0, 0), 0)
        self.frame_7 = self.get_image(2, 0.5, (0, 0, 0), 0)
        self.frame_8 = self.get_image(3, 0.5, (0, 0, 0), 0)
        self.frame_9 = self.get_image(4, 0.5, (0, 0, 0), 0)
        self.animation_list = [self.frame_1, self.frame_2, self.frame_3, self.frame_2]
        self.animation_list2 = [self.frame_8, self.frame_7, self.frame_6, self.frame_7]
        self.last_update = pygame.time.get_ticks()
        self.frame = 0
        self.run = True
        self.gravity = 0
        self.player = pygame.Rect(50, 775 - 320 * 0.5 + bottom_area, 320 * 0.5, 320 * 0.5)
        self.left_right = 1
        self.player_image = self.frame_0
        walking1 = pygame.mixer.Sound('./assets/walking1.mp3')
        walking2 = pygame.mixer.Sound('./assets/walking2.mp3')
        walking3 = pygame.mixer.Sound('./assets/walking3.mp3')
        walking4 = pygame.mixer.Sound('./assets/walking4.mp3')
        walking5 = pygame.mixer.Sound('./assets/walking5.mp3')
        self.landing = pygame.mixer.Sound('./assets/landing.mp3')
        self.walking = [walking1, walking2, walking3, walking4, walking5]
        self.jump = 0
        self.sound = 0
        self.forplayer = pygame.Rect(50, 775 - 320 * 0.5 + bottom_area, 320 * 0.5, 320 * 0.5)
        self.interact = []
        self.font = font

    def get_image(self, frame, scale, color, leftright):
        if leftright == 0:
            image = pygame.Surface((320, 320)).convert_alpha()
            image.blit(self.sheet1, (0, 0), (frame * 320, 0, 320, 320))
            image = pygame.transform.scale(image, (320 * scale, 320 * scale))
            image.set_colorkey(color)
            return image
        if leftright == 1:
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
        self.frame_0.set_alpha(self.alpha)
        self.frame_1.set_alpha(self.alpha)
        self.frame_2.set_alpha(self.alpha)
        self.frame_3.set_alpha(self.alpha)
        self.frame_4.set_alpha(self.alpha)
        self.frame_5.set_alpha(self.alpha)
        self.frame_6.set_alpha(self.alpha)
        self.frame_7.set_alpha(self.alpha)
        self.frame_8.set_alpha(self.alpha)
        self.frame_9.set_alpha(self.alpha)
        self.animation_list = [self.frame_1, self.frame_2, self.frame_3, self.frame_2]
        self.animation_list2 = [self.frame_8, self.frame_7, self.frame_6, self.frame_7]
        screen.blit(self.background, (0, 0))
        if self.jump == 0:
            if self.left_right == 0:
                screen.blit(self.frame_9, self.player)
                self.player_image = self.frame_9
            else:
                screen.blit(self.frame_0, self.player)
                self.player_image = self.frame_0
        else:
            if self.left_right == 0:
                screen.blit(self.frame_5, self.player)
                self.player_image = self.frame_5
            else:
                screen.blit(self.frame_4, self.player)
                self.player_image = self.frame_4
        self.movable_obstacle(screen)

        current_time = pygame.time.get_ticks()
        key_INPUT = pygame.key.get_pressed()
        if key_INPUT[pygame.K_a] and self.player.left >= 0:
            self.left_right = 0
            self.player.left -= game_speed * dt
            if current_time - self.last_update >= dt * 4:
                self.frame = (self.frame + 1) % 4
                self.last_update = current_time
            if self.jump == 0:
                screen.blit(self.background, (0, 0))
                screen.blit(self.animation_list2[self.frame], self.player)
                self.player_image = self.animation_list2[self.frame]
                self.movable_obstacle(screen)
                if self.sound == 0:
                    self.walking[randint(0, 4)].play()
            for i in range(len(self.obstacle)):
                if crash(self.obstacle[i], self.player, self.left_right):
                    self.player.right = self.forplayer.right
                    self.player.left = self.forplayer.left
                    self.player.top = self.forplayer.top
                    self.player.bottom = self.forplayer.bottom
        if key_INPUT[pygame.K_d] and self.player.right <= 1600:
            self.left_right = 1
            self.player.right += game_speed * dt
            if current_time - self.last_update >= dt * 4:
                self.frame = (self.frame + 1) % 4
                self.last_update = current_time
            if self.jump == 0:
                screen.blit(self.background, (0, 0))
                screen.blit(self.animation_list[self.frame], self.player)
                self.player_image = self.animation_list[self.frame]
                self.movable_obstacle(screen)
                if self.sound == 0:
                    self.walking[randint(0, 4)].play()
            for i in range(len(self.obstacle)):
                if crash(self.obstacle[i], self.player, self.left_right):
                    self.player.right = self.forplayer.right
                    self.player.left = self.forplayer.left
                    self.player.top = self.forplayer.top
                    self.player.bottom = self.forplayer.bottom

        self.player.top += self.gravity
        self.gravity += gravitation

        update(screen, self.font, self)

        b = 1
        for i in range(len(self.obstacle)):
            if self.left_right == 1:
                if self.player.top + top_area < self.obstacle[i].top < self.player.bottom - bottom_area and ifcrash(
                        self.player.left + left_area, self.player.right - right_area, self.obstacle[i].left,
                        self.obstacle[i].right):
                    b = 0
            if self.left_right == 0:
                if self.player.top + top_area < self.obstacle[i].top < self.player.bottom - bottom_area and ifcrash(
                        self.player.left + right_area, self.player.right - left_area, self.obstacle[i].left,
                        self.obstacle[i].right):
                    b = 0
        if b == 0:
            self.player.top = self.forplayer.top
            self.player.bottom = self.forplayer.bottom
            if self.jump == 1:
                self.landing.play()
            self.jump = 0
            self.gravity = 0
        elif self.gravity > 2:
            self.jump = 1
        if self.jump == 0:
            if key_INPUT[pygame.K_SPACE]:
                self.gravity = -jumping
                self.jump = 1

        c = 1
        for i in range(len(self.obstacle)):
            if self.left_right == 1:
                if self.player.top + top_area < self.obstacle[i].bottom < self.player.bottom - bottom_area and (not (
                        self.player.right - right_area <= self.obstacle[i].left) and not (
                        self.player.left + left_area >= self.obstacle[i].right)):
                    c = 0
            if self.left_right == 0:
                if self.player.top + top_area < self.obstacle[i].bottom < self.player.bottom - bottom_area and (not (
                        self.player.right - left_area <= self.obstacle[i].left) and not (
                        self.player.left + right_area >= self.obstacle[i].right)):
                    c = 0
        if c == 0:
            self.player.top = self.forplayer.top
            self.player.bottom = self.forplayer.bottom
            self.gravity = 0


        update(screen, self.font, self)
        if self.screen_number == 0:
            text = self.font[0].render("A, D키를 이용해 좌우로 이동할 수 있습니다", True, (0, 0, 0))
            screen.blit(text, (500, 300))
        if self.screen_number == 6:
            text = self.font[0].render("어떤 물체들은 가까이 갈 시 E키를 통해 상호작용할 수 있습니다", True, (0, 0, 0))
            screen.blit(text, (500, 300))
        if self.screen_number == 8:
            text = self.font[0].render("이제부터 루시퍼가 가까이 가면 전등이 자동으로 켜집니다.", True, (0, 0, 0))
            screen.blit(text, (500, 300))
        pygame.display.update()

        self.sound = (self.sound + 1) % 10

    def movable_obstacle(self, screen):
        for x in range(len(self.movable)):
            screen.blit(self.movable_image[x], self.obstacle[self.movable[x]])

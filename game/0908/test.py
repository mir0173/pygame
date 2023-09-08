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
from system import update, index


class NPC:
    def __init__(self, font, image1, image2, lr, initial_position):
        self.sheet1 = image1
        self.sheet2 = image2
        self.alpha = 255
        self.font = font
        self.npc = initial_position
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
        self.npc = pygame.Rect(50, 775 - 320 * 0.5 + bottom_area, 320 * 0.5, 320 * 0.5)
        self.left_right = lr
        self.npc_image = self.frame_0
        walking1 = pygame.mixer.Sound('./assets/walking1.mp3')
        walking2 = pygame.mixer.Sound('./assets/walking2.mp3')
        walking3 = pygame.mixer.Sound('./assets/walking3.mp3')
        walking4 = pygame.mixer.Sound('./assets/walking4.mp3')
        walking5 = pygame.mixer.Sound('./assets/walking5.mp3')
        self.walking = [walking1, walking2, walking3, walking4, walking5]
        self.sound = 0

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

    def npc_update(self, screen):
        self.frame_0.set_alpha(self.alpha)
        self.frame_9.set_alpha(self.alpha)
        if self.left_right == 0:
            screen.blit(self.frame_9, self.npc)
            self.npc_image = self.frame_9
        else:
            screen.blit(self.frame_0, self.npc)
            self.npc_image = self.frame_0

    def move(self, screen, dt, game_speed, destination):
        self.frame_1.set_alpha(self.alpha)
        self.frame_2.set_alpha(self.alpha)
        self.frame_3.set_alpha(self.alpha)
        self.frame_4.set_alpha(self.alpha)
        self.frame_5.set_alpha(self.alpha)
        self.frame_6.set_alpha(self.alpha)
        self.frame_7.set_alpha(self.alpha)
        self.frame_8.set_alpha(self.alpha)
        self.animation_list = [self.frame_1, self.frame_2, self.frame_3, self.frame_2]
        self.animation_list2 = [self.frame_8, self.frame_7, self.frame_6, self.frame_7]
        current_time = pygame.time.get_ticks()
        if destination < self.npc.centerx:
            self.left_right = 0
            self.npc.left -= game_speed * dt
            if current_time - self.last_update >= dt * 4:
                self.frame = (self.frame + 1) % 4
                self.last_update = current_time
                screen.blit(self.animation_list[self.frame], self.npc)
                self.npc_image = self.animation_list[self.frame]
                self.walking[randint(0, 4)].play()
        elif destination > self.npc.centerx:
            self.left_right = 1
            self.npc.right += game_speed * dt
            if current_time - self.last_update >= dt * 4:
                self.frame = (self.frame + 1) % 4
                self.last_update = current_time
                screen.blit(self.animation_list[self.frame], self.npc)
                self.npc_image = self.animation_list[self.frame]
                self.walking[randint(0, 4)].play()
        elif destination == self.npc.centerx:
            return 1
        return 0
import pygame
import math
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
import asyncio

floor = 775
gravitation = 0.6
jumping = 12

def health_bar(surface, health, x, y):
    ratio = health / 100
    pygame.draw.rect(surface, (0, 0, 0), (x-2, y-2, 404, 34))
    pygame.draw.rect(surface, (255, 0, 0), (x, y, 400, 30))
    pygame.draw.rect(surface, (255, 255, 0), (x, y, 400*ratio, 30))

class protagonist():
    def __init__(self, image1, image2, i):
        self.sheet1 = image1
        self.sheet2 = image2
        self.screen_number = i
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
        self.health = 100

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
            #pygame.display.update()
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
            #pygame.display.update()

        self.player.top += self.gravity
        self.gravity += gravitation

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

        #pygame.display.update()

        self.sound = (self.sound + 1) % 10

    def move2(self, surface, target):
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            self.attack(surface, target)

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.player.centerx, self.player.y, 0.8 * self.player.width, self.player.height)
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10

    def update(self, screen):
        self.background = background_list[self.screen_number]
        self.obstacle = obstacle_list[self.screen_number]
        self.movable = movable[self.screen_number]
        self.movable_image = movable_image[self.screen_number]
        screen.blit(self.background, (0, 0))
        screen.blit(self.player_image, self.player)
        self.movable_obstacle(screen)

    def movable_obstacle(self, screen):
        for x in range(len(self.movable)):
            screen.blit(self.movable_image[x], self.obstacle[self.movable[x]])

    def location(self):  #0일 때 왼쪽, 1일 때 오른쪽
        if self.left_right==0:
            return self.player.top+90, self.player.left+95
        else:
            return self.player.top+90, self.player.right-95
        
class Gun(pygame.sprite.Sprite):
    def __init__(self, width, height, image1, image2):
        super().__init__()
        self.width = width
        self.height = height
        self.image_left = pygame.transform.scale(image1, (160, 160))
        self.image_right = pygame.transform.scale(image2, (160, 160))
        self.angle = 0
         
    def update(self, width, height, lr):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        self.width = width
        self.height = height

        if lr==0:
            self.angle = math.pi/2 + math.atan2(mouse_x - self.width, mouse_y - self.height)
            self.image = pygame.transform.rotate(self.image_left, (int(math.degrees(self.angle))))
            self.rect = self.image.get_rect()
            self.rect.center = (self.width, self.height)
            if pygame.mouse.get_pressed()[0]:
                self.rect.centerx += 5
        else:
            self.angle = math.pi/2 - math.atan2(mouse_x - self.width, mouse_y - self.height)
            self.image = pygame.transform.rotate(self.image_right, -(int(math.degrees(self.angle))))
            self.rect = self.image.get_rect()
            self.rect.center = (self.width, self.height)
            if pygame.mouse.get_pressed()[0]:
                self.rect.centerx -= 5 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, width, height, image, lr):
        super().__init__()
        self.image_ = image
        self.speed = 10
        self.index = 0
        self.time = 0
        self.frame_1 = self.sprite_image(0)
        self.frame_2 = self.sprite_image(1)
        self.frame_3 = self.sprite_image(2)
        self.frame_4 = self.sprite_image(3)
        self.frame_5 = self.sprite_image(4)
        self.animation_list3 = [self.frame_2, self.frame_3, self.frame_4, self.frame_5]
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if lr==0:
            self.angle = math.pi - math.atan2(mouse_x - int(width), mouse_y - int(height))
            self.image = pygame.transform.rotate(self.frame_1, 270-(int(math.degrees(self.angle))))
            self.image.set_colorkey((0, 0, 0))
            alpha = math.atan(5/12)
            self.x = width + 45*math.sin(self.angle-alpha)
            self.y = height - 30*math.cos(self.angle-alpha)            
        else:
            self.angle = math.pi - math.atan2(mouse_x - int(width), mouse_y - int(height))
            self.image = pygame.transform.rotate(self.frame_1, 90-(int(math.degrees(self.angle))))
            self.image.set_colorkey((0, 0, 0))
            alpha = math.atan(5/12)
            self.x = width - 45*math.sin(-self.angle-alpha)
            self.y = height - 30*math.cos(-self.angle-alpha)
        
    def sprite_image(self, frame):
        image = pygame.Surface((320, 320)).convert_alpha()
        image.blit(self.image_, (0, 0), (frame * 320, 0, 320, 320))
        image = pygame.transform.scale(image, (160, 160))
        return image
         
    def update(self, target, lr):
        self.rect = self.image.get_rect()
        #self.rect = pygame.Rect(self.x+75, self.y+45, 5, 5)
        self.x += self.speed * math.sin(self.angle)
        self.y -= self.speed * math.cos(self.angle)
        self.rect.center = (self.x, self.y)
        #self.rect.center = (self.x+75, self.y+45)

        if self.rect.colliderect(target.heatbox):
            self.time += 1
            if self.time > 4:
                if lr==0:
                    self.image = pygame.transform.rotate(self.animation_list3[self.index], 90+(int(math.degrees(self.angle))))
                    self.image = pygame.transform.flip(self.image, True, False)
                else:
                    self.image = pygame.transform.rotate(self.animation_list3[self.index], 90-(int(math.degrees(self.angle))))                
                self.image.set_colorkey((0, 0, 0))

                self.index += 1
                if self.index == 1:
                    target.health -= 10
                if self.index == 4:
                    self.kill()


class Michael():
    def __init__(self, image1, image2, i):
        self.sheet1 = image1
        self.sheet2 = image2
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
        self.player = pygame.Rect(50, 775 - 450 + bottom_area, 160, 160)
        self.left_right = 1
        self.player_image = self.frame_0
        self.jump = 0
        self.forplayer = pygame.Rect(50, 775 - 450 + bottom_area, 160, 160)
        self.health = 100
        self.screen_number = i
        self.obstacle = obstacle_list[self.screen_number]
        self.heatbox = pygame.Rect(self.player.centerx-35, 15, 50, 100)

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
        self.action = randint(0, 6)
        self.provability = randint(0, 99)
        if self.provability < 95:
            self.j_action = 0
        else:
            self.j_action = 1

        self.forplayer.right = self.player.right
        self.forplayer.left = self.player.left
        self.forplayer.top = self.player.top
        self.forplayer.bottom = self.player.bottom
        if self.jump == 0:
            if self.left_right == 0:
                screen.blit(self.frame_9, self.player)
                pygame.draw.rect(screen, (255, 0, 0), self.heatbox)
                self.player_image = self.frame_9
            else:
                screen.blit(self.frame_0, self.player)
                pygame.draw.rect(screen, (255, 0, 0), self.heatbox)
                self.player_image = self.frame_0
        else:
            if self.left_right == 0:
                screen.blit(self.frame_5, self.player)
                pygame.draw.rect(screen, (255, 0, 0), self.heatbox)
                self.player_image = self.frame_5
            else:
                screen.blit(self.frame_4, self.player)
                pygame.draw.rect(screen, (255, 0, 0), self.heatbox)
                self.player_image = self.frame_4

        current_time = pygame.time.get_ticks()

        if self.action == 2 and self.player.left >= 0:
            self.left_right = 0
            self.player.left -= game_speed * dt
            if current_time - self.last_update >= dt * 4:
                self.frame = (self.frame + 1) % 4
                self.last_update = current_time
            if self.jump == 0:
                screen.blit(self.animation_list2[self.frame], self.player)
                pygame.draw.rect(screen, (255, 0, 0), self.heatbox)
                self.player_image = self.animation_list2[self.frame]
            for i in range(len(self.obstacle)):
                if crash(self.obstacle[i], self.player, self.left_right):
                    self.player.right = self.forplayer.right
                    self.player.left = self.forplayer.left
                    self.player.top = self.forplayer.top
                    self.player.bottom = self.forplayer.bottom
            #pygame.display.update()
        if self.action == 1 and self.player.right <= 1600:
            self.left_right = 1
            self.player.right += game_speed * dt
            if current_time - self.last_update >= dt * 4:
                self.frame = (self.frame + 1) % 4
                self.last_update = current_time
            if self.jump == 0:
                screen.blit(self.animation_list[self.frame], self.player)
                pygame.draw.rect(screen, (255, 0, 0), self.heatbox)
                self.player_image = self.animation_list[self.frame]
            for i in range(len(self.obstacle)):
                if crash(self.obstacle[i], self.player, self.left_right):
                    self.player.right = self.forplayer.right
                    self.player.left = self.forplayer.left
                    self.player.top = self.forplayer.top
                    self.player.bottom = self.forplayer.bottom
            #pygame.display.update()

        self.player.top += self.gravity
        self.gravity += gravitation

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
            self.jump = 0
            self.gravity = 0
        elif self.gravity > 2:
            self.jump = 1
        if self.jump == 0:
            if self.j_action == 1:
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

        self.heatbox.center = self.player.center

    def update(self, screen):
        screen.blit(self.player_image, self.player)
        pygame.draw.rect(screen, (255, 0, 0), self.heatbox)


STOP = 0
RIGHT = 1
LEFT = 2
ATTACK1 = 3
ATTACK2 = 4
ATTACK3 = 5
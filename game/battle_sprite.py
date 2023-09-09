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

floor = 775
gravitation = 0.6
jumping = 12

class Protagonist():
    def __init__(self, image1, image2, i):
        self.sheet1 = image1
        self.sheet2 = image2
        self.screen_number = i
        self.background = background_list[self.screen_number]
        self.obstacle = list(obstacle_list[self.screen_number])
        self.movable = list(movable[self.screen_number])
        self.movable_image = list(movable_image[self.screen_number])
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
        self.animation_list_1 = [self.frame_1, self.frame_2, self.frame_3, self.frame_2]
        self.animation_list_2 = [self.frame_8, self.frame_7, self.frame_6, self.frame_7]
        self.last_update = pygame.time.get_ticks()
        self.frame = 0
        self.run = True
        self.gravity = 0
        self.player = pygame.Rect(50, 775 - 320 * 0.5 + bottom_area, 320 * 0.5, 320 * 0.5)
        self.left_right = 1
        self.image = self.frame_0
        self.rect = self.image.get_rect()
        walking1 = pygame.mixer.Sound('./assets/walking1.mp3')
        walking2 = pygame.mixer.Sound('./assets/walking2.mp3')
        walking3 = pygame.mixer.Sound('./assets/walking3.mp3')
        walking4 = pygame.mixer.Sound('./assets/walking4.mp3')
        walking5 = pygame.mixer.Sound('./assets/walking5.mp3')
        self.landing = pygame.mixer.Sound('./assets/landing.mp3')
        self.changing = pygame.mixer.Sound('./assets/changing_attack.mp3')
        self.walking = [walking1, walking2, walking3, walking4, walking5]
        self.jump = 0
        self.sound = 0
        self.forplayer = pygame.Rect(50, 775 - 320 * 0.5 + bottom_area, 320 * 0.5, 320 * 0.5)
        self.interact = []

        self.sword_y, self.sword_x = self.sword_location()
        sword_left = pygame.image.load('./assets/left_sword.png').convert_alpha()
        sword_right = pygame.image.load('./assets/right_sword.png').convert_alpha()
        sword = Sword(sword_left, sword_right)
        self.sword_list = pygame.sprite.Group(sword)
        
        self.gun_y, self.gun_x = self.gun_location()
        gun_left = pygame.image.load('./assets/gun2.png').convert_alpha()
        gun_right = pygame.image.load('./assets/gun.png').convert_alpha()
        self.aim = pygame.transform.scale(pygame.image.load('./assets/aim.png').convert_alpha(), (80, 80))
        self.shooting = pygame.mixer.Sound('./assets/shooting.mp3')
        self.reloading = pygame.mixer.Sound('./assets/reloading.mp3')
        self.bullet_image = pygame.image.load('./assets/bullet.png').convert_alpha()
        self.gun = Gun(gun_left, gun_right)
        self.bullet_list = pygame.sprite.Group()
        self.gun_list = pygame.sprite.Group(self.gun)
        self.bullet_limit = 5

        self.hitbox = pygame.Rect(self.player.centerx-35, 15, 80, 120)
        self.attack_type = 0
        self.health = 100
        self.current_health = 100
        self.hurt_image = pygame.transform.scale(pygame.image.load('./assets/hurt.png').convert_alpha(), (1600, 900))
        self.time = 0
        self.key_pressed = True
        self.mouse_clicked = True
        self.mask = pygame.mask.from_surface(self.image)

        self.ui = pygame.image.load('./assets/ui8.png')
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
        if self.health > 0:
            self.forplayer.right = self.player.right
            self.forplayer.left = self.player.left
            self.forplayer.top = self.player.top
            self.forplayer.bottom = self.player.bottom
            screen.blit(self.background, (0, 0))
            if self.jump == 0:
                if self.left_right == 0:
                    screen.blit(self.frame_9, self.player)
                    self.image = self.frame_9
                else:
                    screen.blit(self.frame_0, self.player)
                    self.image = self.frame_0
            else:
                if self.left_right == 0:
                    screen.blit(self.frame_5, self.player)
                    self.image = self.frame_5
                else:
                    screen.blit(self.frame_4, self.player)
                    self.image = self.frame_4
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
                    screen.blit(self.animation_list_2[self.frame], self.player)
                    self.image = self.animation_list_2[self.frame]
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
                    screen.blit(self.animation_list_1[self.frame], self.player)
                    self.image = self.animation_list_1[self.frame]
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

            self.sound = (self.sound + 1) % 10
            self.hitbox.center = self.player.center
        

    def update(self, screen):
        self.rect = self.player
        self.background = background_list[self.screen_number]
        screen.blit(self.background, (0, 0))
        screen.blit(self.ui, (0, 0))
        screen.blit(self.image, self.player)
        self.movable_obstacle(screen)
        self.health_bar(screen)

    def movable_obstacle(self, screen):
        for x in range(len(self.movable)):
            screen.blit(self.movable_image[x], self.obstacle[self.movable[x]])

    def sword_location(self):  #0일 때 왼쪽, 1일 때 오른쪽
        if self.left_right==0:
            return self.player.top+95, self.player.left+95
        else:
            return self.player.top+95, self.player.right-95

    def gun_location(self):  #0일 때 왼쪽, 1일 때 오른쪽
        if self.left_right==0:
            return self.player.top+90, self.player.left+95
        else:
            return self.player.top+90, self.player.right-95

    def attack(self, screen, target_list, mouse):
        key = pygame.key.get_pressed()

        if key[pygame.K_f] and self.key_pressed:
            self.changing.play()
            self.key_pressed = False
            self.attack_type += 1
            if self.attack_type == 2:
                self.attack_type = 0
        elif not(key[pygame.K_f] or self.key_pressed):
            self.key_pressed = True
        else:
            pass

        if self.attack_type == 0:
            self.gun_attack(screen, target_list[0], mouse)
        else:
            self.sword_attack(screen, target_list, mouse)

    def sword_attack(self, screen, target_list, mouse):
        self.bullet_list.update(target_list[0], self.left_right)
        self.bullet_list.draw(screen)
        self.sword_y, self.sword_x = self.sword_location()
        self.sword_list.update(self.sword_x, self.sword_y, self.left_right, mouse, target_list)
        self.sword_list.draw(screen)

    def gun_attack(self, screen, target, mouse):
        self.gun_y, self.gun_x = self.gun_location()
        if mouse and self.mouse_clicked:
            if self.bullet_limit > 0:
                bullet = Bullet(self.gun_x, self.gun_y, self.bullet_image, self.left_right)
                self.bullet_list.add(bullet)
                self.mouse_clicked = False
                self.shooting.play()
                self.bullet_limit -= 1
        elif not (mouse or self.mouse_clicked):
            self.mouse_clicked = True
        else:
            pass

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        screen.blit(self.aim, (mouse_x-50, mouse_y-50))

        self.bullet_limit = self.gun.reload(self.bullet_limit)
        self.bullet_list.update(target, self.left_right)
        self.gun_list.update(self.gun_x, self.gun_y, self.left_right)
        self.bullet_list.draw(screen)
        self.gun_list.draw(screen)

    def health_bar(self, screen):
        ratio = self.health / 100
        pygame.draw.rect(screen, (255, 255, 0), (115, 54, 193*ratio, 21))
        if self.health != self.current_health or 0 < self.time < 60:
            if self.health != self.current_health:
                self.time = 0
            self.time += 1
            self.current_health = self.health
            screen.blit(self.hurt_image, (0, 0))
        else:
            self.time = 0


class Sword(pygame.sprite.Sprite):
    def __init__(self, image1, image2):
        super().__init__()
        self.sword_left = pygame.transform.scale(image1, (160, 160))
        self.sword_right = pygame.transform.scale(image2, (160, 160))
        self.up_frame_0, self.frame_0, self.frame_1, self.frame_2, self.frame_3, self.frame_4 = self.sprite_image(self.sword_left, 0)
        self.up_frame_1, self.frame_5, self.frame_6, self.frame_7, self.frame_8, self.frame_9 = self.sprite_image(self.sword_right, 1)
        self.animation_list_4 = [self.up_frame_0, self.frame_0, self.frame_1, self.frame_2, self.frame_3, self.frame_4]
        self.animation_list_5 = [self.up_frame_1, self.frame_5, self.frame_6, self.frame_7, self.frame_8, self.frame_9]
        self.animation_length = len(self.animation_list_4)
        self.swing = pygame.mixer.Sound('./assets/swing.wav')
        self.promouse = True
        self.index = -1
        self.attacking = False
        self.is_hit = [0]*10

    def sprite_image(self, sword_image, lr):
        if lr == 0:
            i_0 = pygame.transform.rotate(sword_image, -15)
            i_1 = pygame.transform.rotate(sword_image, 15)
            i_2 = pygame.transform.rotate(sword_image, 30)
            i_3 = pygame.transform.rotate(sword_image, 45)
            i_4 = pygame.transform.rotate(sword_image, 60)
            i_5 = pygame.transform.rotate(sword_image, 75)
        else:
            i_0 = pygame.transform.rotate(sword_image, 15)
            i_1 = pygame.transform.rotate(sword_image, -15) 
            i_2 = pygame.transform.rotate(sword_image, -30)
            i_3 = pygame.transform.rotate(sword_image, -45)
            i_4 = pygame.transform.rotate(sword_image, -60)
            i_5 = pygame.transform.rotate(sword_image, -75)
        
        return i_0, i_1, i_2, i_3, i_4, i_5

    def update(self, sword_x, sword_y, lr, mouse, target_list):
        self.sword_x = sword_x
        self.sword_y = sword_y
        if lr == 0:
            attacking_rect = pygame.Rect(self.sword_x-120, self.sword_y-60, 50, 110)
            if self.index == -1:
                self.is_hit = [0 for _ in range(len(target_list))]
                self.image = self.sword_left
                self.rect = self.image.get_rect()
                self.rect.center = (self.sword_x, self.sword_y)
                if self.promouse!=mouse==True:
                    self.swing.play()
                    self.attacking = True
                    for i, target in enumerate(target_list):
                        if attacking_rect.colliderect(target.hitbox) and not self.is_hit[i]:
                            target.health -= 10
                            self.is_hit[i] = 1
                    self.index = 0
            else:
                self.image = self.animation_list_4[self.index]
                self.rect = self.image.get_rect()
                self.rect.center = (self.sword_x, self.sword_y)
                for i, target in enumerate(target_list):
                    if attacking_rect.colliderect(target.hitbox) and not self.is_hit[i]:
                        target.health -= 10
                        self.is_hit[i] = 1
                if self.index == self.animation_length-1 or not self.attacking:
                    self.index -= 1
                    self.attacking = False
                    if self.index == 1:
                        self.index == -1
                else:
                    self.index += 1
                    self.attacking = True
        else:
            attacking_rect = pygame.Rect(self.sword_x+40, self.sword_y-60, 50, 110)
            if self.index == -1:
                self.is_hit = [0 for _ in range(len(target_list))]
                self.image = self.sword_right
                self.rect = self.image.get_rect()
                self.rect.center = (self.sword_x, self.sword_y)
                if self.promouse!=mouse==True:
                    self.swing.play()
                    self.attacking = True
                    for i, target in enumerate(target_list):
                        if attacking_rect.colliderect(target.hitbox) and not self.is_hit[i]:
                            target.health -= 10
                            self.is_hit[i] = 1
                    self.index = 0
            else:
                self.image = self.animation_list_5[self.index]
                self.rect = self.image.get_rect()
                self.rect.center = (self.sword_x, self.sword_y)
                for i, target in enumerate(target_list):
                    if attacking_rect.colliderect(target.hitbox) and not self.is_hit[i]:
                        target.health -= 10
                        self.is_hit[i] = True
                if self.index == self.animation_length-1 or not self.attacking:
                    self.index -= 1
                    self.attacking = False
                    if self.index == 1:
                        self.index == -1
                else:
                    self.index += 1
                    self.attacking = True

        self.promouse = mouse
            
class Gun(pygame.sprite.Sprite):
    def __init__(self, image1, image2):
        super().__init__()
        self.image_left = pygame.transform.scale(image1, (160, 160))
        self.image_right = pygame.transform.scale(image2, (160, 160))
        self.reloading = pygame.mixer.Sound('./assets/reloading.mp3')
        self.angle = 0
        self.reload_time = 0
        self.key_pressed = True
        self.key_r = False
         
    def update(self, gun_x, gun_y, lr):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if self.reload_time > 0:
            if lr == 0:
                self.image = pygame.transform.rotate(self.image_left, 70)
                self.rect = self.image.get_rect()
                self.rect.center = (gun_x, gun_y)
            else:
                self.image = pygame.transform.rotate(self.image_right, -70)
                self.rect = self.image.get_rect()
                self.rect.center = (gun_x, gun_y) 
        else:
            if lr == 0:
                self.angle = math.pi/2 + math.atan2(mouse_x - gun_x, mouse_y - gun_y)
                self.image = pygame.transform.rotate(self.image_left, (int(math.degrees(self.angle))))
                self.rect = self.image.get_rect()
                self.rect.center = (gun_x, gun_y)
                if pygame.mouse.get_pressed()[0]:
                    self.rect.centerx += 5
            else:
                self.angle = math.pi/2 - math.atan2(mouse_x - gun_x, mouse_y - gun_y)
                self.image = pygame.transform.rotate(self.image_right, -(int(math.degrees(self.angle))))
                self.rect = self.image.get_rect()
                self.rect.center = (gun_x, gun_y)
                if pygame.mouse.get_pressed()[0]:
                    self.rect.centerx -= 5                

    def reload(self, bullet_limit):
        if bullet_limit != 5:
            key = pygame.key.get_pressed()
            if key[pygame.K_r]  or self.key_r:
                self.key_r = True
                self.reload_time += 1
                if self.reload_time <= 120:
                    return bullet_limit
                else:
                    self.key_r = False
                    self.reload_time = 0
                    self.reloading.play()
                    return 5
            else:
                return bullet_limit
        else:
            return bullet_limit

class Bullet(pygame.sprite.Sprite):
    def __init__(self, gun_x, gun_y, image, lr):
        super().__init__()
        self.image_ = image
        self.is_hit = False
        self.speed = 20
        self.index = 0
        self.gun_x = gun_x
        self.gun_y = gun_y
        self.frame_1 = self.sprite_image((20, 10), (150, 90, 20, 10)) #이미지 사이즈
        self.frame_2 = self.sprite_image((20, 30), (480, 80, 20, 30))
        self.frame_3 = self.sprite_image((30, 50), (790, 70, 30, 50))
        self.frame_4 = self.sprite_image((30, 50), (1110, 70, 30, 50))
        self.animation_list_3 = [self.frame_2, self.frame_3, self.frame_4]
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if lr==0:
            self.angle = math.pi - math.atan2(mouse_x - self.gun_x, mouse_y - self.gun_y)
            self.image = pygame.transform.rotate(self.frame_1, 270-(int(math.degrees(self.angle))))
            self.image.set_colorkey((0, 0, 0))
            alpha = math.atan(5/12)
            self.x = self.gun_x + 50*math.sin(self.angle+alpha)
            self.y = self.gun_y - 50*math.cos(self.angle+alpha)            
        else:
            self.angle = math.pi - math.atan2(mouse_x - self.gun_x, mouse_y - self.gun_y)
            self.image = pygame.transform.rotate(self.frame_1, 90-(int(math.degrees(self.angle))))
            self.image.set_colorkey((0, 0, 0))
            alpha = math.atan(5/12)
            self.x = self.gun_x + 50*math.sin(self.angle-alpha)
            self.y = self.gun_y - 50*math.cos(self.angle-alpha)
        
    def sprite_image(self, size, frame):
        image = pygame.Surface(size).convert_alpha()
        image.blit(self.image_, (0, 0), frame)
        image = pygame.transform.scale(image, (size[0]/2, size[1]/2))
        return image
         
    def update(self, target, lr):
        if not self.is_hit:
            self.rect = self.image.get_rect()
            self.x += self.speed * math.sin(self.angle)
            self.y -= self.speed * math.cos(self.angle)
            self.rect.center = (self.x, self.y)
            if self.rect.colliderect(target.hitbox):
                self.is_hit = True
        else:
            if lr==0:
                self.image = pygame.transform.rotate(self.animation_list_3[self.index], 90+(int(math.degrees(self.angle))))
                self.image = pygame.transform.flip(self.image, True, False)
            else:
                self.image = pygame.transform.rotate(self.animation_list_3[self.index], 90-(int(math.degrees(self.angle))))                
            self.image.set_colorkey((0, 0, 0))

            self.index += 1
            if self.index == 1:
                target.health -= 5
            if self.index == 3:
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
        self.animation_list_1 = [self.frame_1, self.frame_2, self.frame_3, self.frame_2]
        self.animation_list_2 = [self.frame_8, self.frame_7, self.frame_6, self.frame_7]
        self.last_update = pygame.time.get_ticks()
        self.frame = 0
        self.run = True
        self.gravity = 0
        self.player = pygame.Rect(50, 775 - 450 + bottom_area, 160, 160)
        self.left_right = 1
        self.player_image = self.frame_0
        self.jump = 0
        self.forplayer = pygame.Rect(50, 775 - 450 + bottom_area, 160, 160)
        self.health = 300
        self.screen_number = i
        self.obstacle = list(obstacle_list[self.screen_number])
        self.hitbox = pygame.Rect(self.player.centerx-35, 15, 80, 120)
        self.time = 60
        self.attack_time = 0 
        self.attacking = False

        self.attack_type = 2
        self.magic_image = pygame.image.load('./assets/magic.png')
        self.magic_list = pygame.sprite.Group()

        self.cage_image = pygame.image.load('./assets/cage.png')
        self.drop_image = pygame.image.load('./assets/ioio.png')
        self.dropping = pygame.mixer.Sound('./assets/drop.mp3')
        self.cage_list = pygame.sprite.Group()
        self.drop_list = pygame.sprite.Group()

        self.explosion_image = pygame.image.load('./assets/explosion.png')
        explosion = Explosion(self.explosion_image, self.player.centerx, self.player.centery)
        self.explosion_list = pygame.sprite.Group()
        self.explosion_list.add(explosion)

        self.x = 0
        self.y = 0

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
        if self.health > 0:
            if self.time >= 60:
                self.action = randint(1, 2)
                self.provability = randint(0, 10)
                if self.provability < 7:
                    self.j_action = 0
                else:
                    self.j_action = 1
                self.time = 0

            self.time += 1
            self.forplayer.right = self.player.right
            self.forplayer.left = self.player.left
            self.forplayer.top = self.player.top
            self.forplayer.bottom = self.player.bottom
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

            current_time = pygame.time.get_ticks()

            if self.action == 2 and self.player.left >= 0:
                self.left_right = 0
                self.player.left -= game_speed * dt
                if current_time - self.last_update >= dt * 4:
                    self.frame = (self.frame + 1) % 4
                    self.last_update = current_time
                if self.jump == 0:
                    screen.blit(self.animation_list_2[self.frame], self.player)
                    self.player_image = self.animation_list_2[self.frame]
                for i in range(len(self.obstacle)):
                    if crash(self.obstacle[i], self.player, self.left_right):
                        self.player.right = self.forplayer.right
                        self.player.left = self.forplayer.left
                        self.player.top = self.forplayer.top
                        self.player.bottom = self.forplayer.bottom

            if self.action == 1 and self.player.right <= 1600:
                self.left_right = 1
                self.player.right += game_speed * dt
                if current_time - self.last_update >= dt * 4:
                    self.frame = (self.frame + 1) % 4
                    self.last_update = current_time
                if self.jump == 0:
                    screen.blit(self.animation_list_1[self.frame], self.player)
                    self.player_image = self.animation_list_1[self.frame]
                for i in range(len(self.obstacle)):
                    if crash(self.obstacle[i], self.player, self.left_right):
                        self.player.right = self.forplayer.right
                        self.player.left = self.forplayer.left
                        self.player.top = self.forplayer.top
                        self.player.bottom = self.forplayer.bottom

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

            self.hitbox.center = self.player.center

    def attack(self, screen, target):
        if not self.attacking:
            self.attack_type = randint(1, 3)
            self.attacking = True

        if self.attack_type == 1:
            if self.attack_time == 60:
                magic = Magic(self.magic_image, target)
                self.magic_list.add(magic)
            self.magic_list.update(target)
            self.magic_list.draw(screen)
            if self.attack_time > 120:
                self.attacking = False
                self.attack_time = 0
            
        if self.attack_type == 2:
            if self.attack_time == 60:
                self.x = target.rect.centerx
                self.y = target.rect.bottom
                open_cage = Cage(self.cage_image, self.x, self.y, 0)
                target.obstacle.append(open_cage.rect)
                target.movable.append(0)
                target.movable_image.append(self.cage_image)
                self.cage_list.add(open_cage)
                close_cage = Cage(self.cage_image, self.x, self.y, 1)
                target.obstacle.append(close_cage.rect)
                target.movable.append(1)
                target.movable_image.append(self.cage_image)
                self.cage_list.add(close_cage)
            if self.attack_time == 100:
                drop = Drop(self.drop_image, self.x)
                self.drop_list.add(drop)
                self.dropping.play()
            if self.attack_time == 150:
                for _ in range(2):
                    target.obstacle.pop()
                    target.movable.pop()
                    target.movable_image.pop()
                for sprite in self.cage_list:
                    sprite.kill()
                self.attacking = False
                self.attack_time = 0
            self.cage_list.update()
            self.cage_list.draw(screen)
            self.drop_list.update(target)
            self.drop_list.draw(screen)

        if self.attack_type == 3:
            if self.attack_time == 30:
                self.attacking = False
                self.attack_time = 0
            self.explosion_list.update(self.player.centerx, self.player.centery, target)
            self.explosion_list.draw(screen)
        self.attack_time += 1

    def update(self, screen, target):
        self.attack(screen, target)
        screen.blit(self.player_image, self.player)
        self.health_bar(screen)

    def health_bar(self, screen):
        ratio = self.health / 300
        pygame.draw.rect(screen, (255, 255, 0), (525, 193, 550*ratio, 19))

class Magic(pygame.sprite.Sprite):
    def __init__(self, image, target):
        super().__init__()
        self.image_ = image
        self.index = 0
        self.frame = 0
        self.frame_1 = self.sprite_image((30, 20), (150, 300, 30, 20)) #이미지 사이즈
        self.frame_2 = self.sprite_image((40, 60), (460, 260, 40, 60))
        self.frame_3 = self.sprite_image((60, 100), (760, 220, 60, 100))
        self.frame_4 = self.sprite_image((60, 130), (1080, 190, 60, 130))
        self.frame_5 = self.sprite_image((60, 170), (1400, 150, 60, 170))
        self.frame_6 = self.sprite_image((60, 170), (1720, 150, 60, 170))
        self.frame_7 = self.sprite_image((60, 180), (2040, 160, 60, 180))
        self.frame_8 = self.sprite_image((80, 10), (2350, 310, 80, 10))
        self.frame_9 = self.sprite_image((80, 10), (2670, 310, 80, 10))
        self.animation_list_3 = []
        for _ in range(16):
            self.animation_list_3.append(self.frame_8)
            self.animation_list_3.append(self.frame_9)           
        self.animation_list_3.append(self.frame_1)
        self.animation_list_3.append(self.frame_2)
        self.animation_list_3.append(self.frame_3)
        self.animation_list_3.append(self.frame_4)
        for _ in range(4):
            self.animation_list_3.append(self.frame_5)
            self.animation_list_3.append(self.frame_6)
            self.animation_list_3.append(self.frame_7)
        
        self.image = self.animation_list_3[0]
        self.rect = self.image.get_rect()
        self.x = target.hitbox.centerx
        self.y = 770
        self.rect.centerx = self.x
        self.rect.bottom = self.y        
        self.magic_sound = pygame.mixer.Sound('./assets/magic.mp3')
        self.attacking = True
        
    def sprite_image(self, size, frame):
        image = pygame.Surface(size).convert_alpha()
        image.blit(self.image_, (0, 0), frame)
        image = pygame.transform.scale(image, (size[0], size[1]))
        image.set_colorkey((0, 0, 0))
        return image
         
    def update(self, target):
        self.image = self.animation_list_3[self.frame]
        self.rect = self.image.get_rect()
        self.frame += 1
        self.rect.centerx = self.x
        self.rect.bottom = self.y
        if self.frame == 19:
            self.magic_sound.play()
        if self.frame > 31:
            if self.rect.colliderect(target.hitbox):
                target.health -= 2
        if self.frame == len(self.animation_list_3):
            self.attacking = False
            self.kill()

class Cage(pygame.sprite.Sprite):
    def __init__(self, image, x, y, oc):
        super().__init__()
        self.oc = oc
        self.image = image
        if self.oc == 0:
            self.image = self.sprite_image((80, 150), (120, 130, 80, 150))
            self.rect = self.image.get_rect()
            self.cage_x = x - 70
            self.cage_y = y + 10
            self.rect.centerx = self.cage_x
            self.rect.bottom = self.cage_y
        if self.oc == 1:
            self.image = self.sprite_image((80, 150), (120, 130, 80, 150))
            self.rect = self.image.get_rect()
            self.cage_x = x + 70
            self.cage_y = y
            self.rect.centerx = self.cage_x
            self.rect.bottom = self.cage_y

    def sprite_image(self, size, frame):
        image = pygame.Surface(size).convert_alpha()
        image.blit(self.image, (0, 0), frame)
        image = pygame.transform.scale(image, (size[0]/1.4, size[1]/1.4))
        image.set_colorkey((0, 0, 0))
        return image

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.centerx = self.cage_x
        self.rect.bottom = self.cage_y

class Drop(pygame.sprite.Sprite):
    def __init__(self, image, x):
        super().__init__()
        self.image = image
        self.frame = 0
        self.is_hit = False
        self.attacking_rect = self.sprite_image((80, 80), (120, 230, 80, 80)).get_rect()
        self.frame_0 = self.sprite_image((320, 320), (0, 0, 320, 320))
        self.frame_1 = self.sprite_image((320, 320), (320, 0, 320, 320))
        self.frame_2 = self.sprite_image((320, 320), (640, 0, 320, 320))
        self.frame_3 = self.sprite_image((320, 320), (960, 0, 320, 320))
        self.frame_4 = self.sprite_image((320, 320), (1080, 0, 320, 320))
        self.animation_list = [self.frame_0, self.frame_1, self.frame_2, self.frame_3, self.frame_4]
        self.image = self.animation_list[0]
        self.drop_x = x
        self.drop_y = 0
        self.rect = self.image.get_rect()

    def sprite_image(self, size, frame):
        image = pygame.Surface(size).convert_alpha()
        image.blit(self.image, (0, 0), frame)
        image = pygame.transform.scale(image, (size[0]/1.4, size[1]/1.4))
        image.set_colorkey((0, 0, 0))
        return image

    def update(self, target):
        if self.is_hit or self.rect.bottom > 775:
            self.frame += 1
            self.image = self.animation_list[self.frame]
            self.rect = self.image.get_rect()
            self.rect.centerx = self.drop_x
            self.rect.bottom = 0
            if self.frame == len(self.animation_list)-1:
                self.kill()
        else:
            self.rect.centerx = self.drop_x
            self.attacking_rect.centerx = self.drop_x
            self.drop_y += 15
            self.rect.bottom += self.drop_y
            self.attacking_rect.bottom += self.drop_y
            if self.rect.bottom > 775:
                self.rect.bottom = 775
                self.attacking_rect.bottom = 775
            if self.attacking_rect.colliderect(target.hitbox) and not self.is_hit:
                target.health -= 15
                self.is_hit = True
            if self.attacking_rect.bottom == 775 and not self.is_hit:
                self.is_hit = True

class Explosion(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.frame_index = 0
        self.is_hit = False

        self.frame = [0]*30
        for i in range(30):
            self.frame[i] = self.sprite_image((640, 640), (640*i, 0, 640, 640))
        self.image = self.frame[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.explosing = pygame.mixer.Sound('./assets/explosion.mp3')

    def sprite_image(self, size, frame):
        image = pygame.Surface(size).convert_alpha()
        image.blit(self.image, (0, 0), frame)
        image = pygame.transform.scale(image, (size[0]/1.5, size[1]/1.5))
        image.set_colorkey((0, 0, 0))
        return image

    def update(self, x, y, target):
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.frame_index += 1

        if self.frame_index > 22:
            if self.frame_index == 23:
                self.explosing.play()
            if self.rect.colliderect(target.hitbox) and not self.is_hit:
                target.health -= 20
                self.is_hit = True
        if self.frame_index == 30:
            self.is_hit = False
            self.frame_index = 0
    
class Michael_final():
    def __init__(self, i, target):
        self.screen_number = i
        self.frame = [0]*61

        for i in range(61):
            self.frame[i] = pygame.image.load('./assets/michael_final (%d).png' %(i+1)).convert_alpha() 
            self.frame[i] = pygame.transform.scale(self.frame[i], (540, 540)).convert_alpha() 

        left_image = self.frame[25]
        left_image.set_alpha(60) 

        self.animation_list_left_1 = self.frame[:26]
        self.animation_list_left_1.append(left_image)
        self.animation_list_left_1.append(self.frame[25])
        self.animation_list_left_2 = self.frame[26:59]
        self.animation_list_left_default = self.frame[59:]

        for i in range(61):
            self.frame[i] = pygame.transform.flip(self.frame[i], True, False)

        right_image = self.frame[25]
        right_image.set_alpha(60)

        self.animation_list_right_1 = self.frame[:26]
        self.animation_list_right_1.append(right_image)
        self.animation_list_right_1.append(self.frame[25])
        self.animation_list_right_2 = self.frame[26:59]
        self.animation_list_right_default = self.frame[59:]
            
        self.player_image = self.animation_list_left_default[0]
        self.player = pygame.Rect(800, 250 + bottom_area, 420, 420)

        self.time = 0
        self.attack_index = 0
        self.attacking = False
        self.default_index = 0
        self.death_index = 255

        self.health = 500
        self.is_hit = False
        self.hitbox = pygame.Rect(self.player.centerx+20, 490, 100, 300)

        self.sword_aura_image_left = pygame.transform.scale(pygame.image.load('./assets/aura.png').convert_alpha(), (420, 420)).convert_alpha()
        self.sword_aura_image_right = pygame.transform.flip(self.sword_aura_image_left, True, False)
        self.sword_gun_image_left = pygame.transform.scale(pygame.image.load('./assets/sword_gun.png').convert_alpha(), (420, 420)).convert_alpha()
        self.sword_gun_image_right = pygame.transform.flip(self.sword_gun_image_left, True, False)
        #self.sword_gun_shooting = pygame.mixer.Sound('./asstes/sword_shot.mp3')

        self.sword_aura_list = pygame.sprite.Group()
        self.sword_gun_list = pygame.sprite.Group()

        self.sword_gun_1 = Sword_gun(self.player.centerx+500, randint(100, 300), self.sword_gun_image_left, target, 0)
        self.sword_gun_2 = Sword_gun(self.player.centerx+500, randint(300, 500), self.sword_gun_image_left, target, 0)
        self.sword_gun_3 = Sword_gun(self.player.centerx+500, randint(500, 700), self.sword_gun_image_left, target, 0)
    

    def attack(self, screen, target):
        attacking_rect = pygame.Rect(self.player.centerx-180, self.player.centery-200, 500, 550)
        if attacking_rect.colliderect(target.hitbox) and not self.is_hit:
            self.is_hit = True
            target.health -= 30
        
        if not self.attacking:
            self.attack_type = randint(1, 3)
            self.front_behind = randint(0, 1)
            self.front_behind = 1
            self.attacking = True

        if self.lr == 0:
            if self.attack_type == 1:
                self.player_image = self.animation_list_left_1[self.attack_index]
                self.attack_index += 1
                if self.attack_index == len(self.animation_list_left_1)-2:
                    self.is_hit = True
                if self.attack_index == len(self.animation_list_left_1)-1:
                    self.player.x = target.rect.x + 100
                if self.attack_index == len(self.animation_list_left_1):
                    self.attack_index = 0
                    self.is_hit = False
                    self.attacking = False
                    self.time = 0
                    if target.rect.left - 150 > 0:
                        if self.front_behind == 0:
                            self.player.x = target.rect.x + 50
                        else:
                            self.player.x = target.rect.x -350
                    else:
                        self.player.x = target.rect.x + 50
            if self.attack_type == 2:
                self.player_image = self.animation_list_left_2[self.attack_index]
                self.attack_index += 1
                if self.attack_index == len(self.animation_list_left_2):
                    self.attack_index = 0 
                    self.is_hit = False
                    self.attacking = False
                    self.time = 0
                if self.attack_index == len(self.animation_list_left_2)-5:
                    sword_aura = Sword_aura(self.player.centerx+20, 490, self.sword_aura_image_left, target, self.lr)
                    self.sword_aura_list.add(sword_aura)
                self.sword_aura_list.update()
                self.sword_aura_list.draw(screen) 
            if self.attack_type == 3:
                self.player_image = self.animation_list_left_2[self.attack_index]
                self.attack_index += 1
                if self.attack_index == len(self.animation_list_left_2):
                    self.attack_index = 0 
                    self.is_hit = False
                    self.attacking = False
                    self.time = 0
                if self.attack_index == len(self.animation_list_left_2)-20:
                    self.sword_gun_1 = Sword_gun(self.player.centerx+400, randint(100, 300), self.sword_gun_image_left, target, 0)
                    self.sword_gun_2 = Sword_gun(self.player.centerx+400, randint(300, 500), self.sword_gun_image_left, target, 0)
                    self.sword_gun_3 = Sword_gun(self.player.centerx+400, randint(500, 700), self.sword_gun_image_left, target, 0)
                    self.sword_gun_list.add(self.sword_gun_1, self.sword_gun_2, self.sword_gun_3)
                self.sword_gun_list.update()
                self.sword_gun_list.draw(screen)
            screen.blit(self.player_image, self.player)
        else:
            if self.attack_type == 1:
                self.player_image = self.animation_list_right_1[self.attack_index]
                self.attack_index += 1
                if self.attack_index == len(self.animation_list_right_1)-2:
                    self.is_hit = True
                if self.attack_index == len(self.animation_list_right_1)-1:
                    self.player.x = target.rect.x - 500
                if self.attack_index == len(self.animation_list_right_1):
                    self.attack_index = 0
                    self.is_hit = False
                    self.attacking = False
                    self.time = 0
                    if target.rect.right + 400 < 1600:
                        if self.front_behind == 0:
                            self.player.x = target.rect.x - 350
                        else:
                            self.player.x = target.rect.x + 80
                    else:
                        self.player.x = target.rect.x - 350
            if self.attack_type == 2:  
                self.player_image = self.animation_list_right_2[self.attack_index]
                self.attack_index += 1
                if self.attack_index == len(self.animation_list_right_2):
                    self.attack_index = 0 
                    self.is_hit = False
                    self.attacking = False
                    self.time = 0
                if self.attack_index == len(self.animation_list_right_2)-5:
                    sword_aura = Sword_aura(self.player.centerx-20, 490, self.sword_aura_image_right, target, self.lr)
                    self.sword_aura_list.add(sword_aura)
                self.sword_aura_list.update()
                self.sword_aura_list.draw(screen) 
            if self.attack_type == 3:  
                self.player_image = self.animation_list_right_2[self.attack_index]
                self.attack_index += 1
                if self.attack_index == len(self.animation_list_right_2):
                    self.attack_index = 0 
                    self.is_hit = False
                    self.attacking = False
                    self.time = 0
                if self.attack_index == len(self.animation_list_right_2)-20:
                    self.sword_gun_1 = Sword_gun(self.player.centerx-400, randint(100, 700), self.sword_gun_image_right, target, 1)
                    self.sword_gun_2 = Sword_gun(self.player.centerx-400, randint(300, 500), self.sword_gun_image_right, target, 1)
                    self.sword_gun_3 = Sword_gun(self.player.centerx-400, randint(500, 700), self.sword_gun_image_right, target, 1)
                    self.sword_gun_list.add(self.sword_gun_1, self.sword_gun_2, self.sword_gun_3)

                self.sword_gun_list.update()
                self.sword_gun_list.draw(screen)
            screen.blit(self.player_image, self.player)

    def update(self, screen, target):
        if self.health > 0:
            if target.rect.x > self.player.x+70:
                self.lr = 1
            else:
                self.lr = 0

            self.time += 1

            if self.time > 150:
                self.attack(screen, target)
            else:
                if self.lr == 0:
                    self.hitbox.x = self.player.centerx + 20
                    if self.time % 15 == 0:
                        self.default_index += 1
                        if self.default_index == 2:
                            self.default_index = 0
                        self.player_image = self.animation_list_left_default[self.default_index]
                else:
                    self.hitbox.x = self.player.centerx
                    if self.time % 15 == 0:
                        self.default_index += 1
                        if self.default_index == 2:
                            self.default_index = 0
                        self.player_image = self.animation_list_right_default[self.default_index]

                screen.blit(self.player_image, self.player)
                self.sword_aura_list.update()
                self.sword_aura_list.draw(screen)
                self.sword_gun_list.update()
                self.sword_gun_list.draw(screen) 
            self.health_bar(screen)

    def health_bar(self, screen):
        ratio = self.health / 500
        pygame.draw.rect(screen, (255, 255, 0), (525, 193, 550*ratio, 19))


class Sword_aura(pygame.sprite.Sprite):
    def __init__(self, aura_x, aura_y, image, target, lr):
        super().__init__()
        self.pre_image = image
        self.is_hit = False
        self.speed = 15
        self.x = aura_x
        self.y = aura_y
        self.target = target
        if lr == 0:
            self.angle = math.atan2((aura_x - target.player.centerx), (target.player.centery - aura_y))
            self.image = pygame.transform.rotate(self.pre_image, 90-math.degrees(self.angle))
        else:
            self.angle = math.atan2((aura_x - target.player.centerx), (target.player.centery - aura_y))
            self.image = pygame.transform.rotate(self.pre_image, -90-math.degrees(self.angle))            
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        self.attacking_rect = pygame.Rect(0, 0, 200, 120)
        self.x -= self.speed*math.sin(self.angle)
        self.y += self.speed*math.cos(self.angle)
        self.rect.center = (self.x, self.y)
        if not self.is_hit:
            if pygame.sprite.collide_mask(self, self.target):
                self.is_hit = True
                self.target.health -= 10

class Sword_gun(pygame.sprite.Sprite):
    def __init__(self, sg_x, sg_y, image, target, lr):
        super().__init__()
        self.image = image
        self.is_hit = False
        self.speed = 30
        self.x = sg_x
        self.y = sg_y
        self.target = target
        self.rect = self.image.get_rect()
        self.health = 5
        self.attacking_rect = pygame.Rect(0, 0, 300, 5)
        self.hitbox = self.attacking_rect
        self.lr = lr

    def update(self):
        if self.health > 0:
            self.attacking_rect = pygame.Rect(0, 0, 300, 5)
            self.hitbox = self.attacking_rect
            if self.lr == 0:
                self.x -= self.speed
                self.rect.center = (self.x+20, self.y-50)
                self.attacking_rect.center = (self.x, self.y)
                if self.x < -500:
                    self.kill()
            else:
                self.x += self.speed
                self.rect.center = (self.x-20, self.y-50)
                self.attacking_rect.center = (self.x, self.y)
                if self.x > 2100:
                    self.kill()              
            if not self.is_hit:
                if self.attacking_rect.colliderect(self.target.hitbox):
                    self.is_hit = True
                    self.target.health -= 15
        else:
            self.kill()

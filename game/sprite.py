import pygame

class spritesheet():
    def __init__(self, image1, image2, background):
        self.sheet1 = image1
        self.sheet2 = image2
        self.background = background

    def get_image(self, frame, width, height, scale, color, leftright):
        if leftright == 0:
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(self.sheet1, (0, 0), (frame * width, 0, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image.set_colorkey(color)
            return image
        if leftright == 1:
            image = pygame.Surface((width, height)).convert_alpha()
            image.blit(self.sheet2, (0, 0), (frame * width, 0, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image.set_colorkey(color)
            return image

    def move(self, width, height, screen):
        frame_0 = self.get_image(0, width, height, 0.5, (0, 0, 0), 1)
        frame_1 = self.get_image(1, width, height, 0.5, (0, 0, 0), 1)
        frame_2 = self.get_image(2, width, height, 0.5, (0, 0, 0), 1)
        frame_3 = self.get_image(3, width, height, 0.5, (0, 0, 0), 1)
        frame_4 = self.get_image(4, width, height, 0.5, (0, 0, 0), 1)
        frame_5 = self.get_image(0, width, height, 0.5, (0, 0, 0), 0)
        frame_6 = self.get_image(1, width, height, 0.5, (0, 0, 0), 0)
        frame_7 = self.get_image(2, width, height, 0.5, (0, 0, 0), 0)
        frame_8 = self.get_image(3, width, height, 0.5, (0, 0, 0), 0)
        frame_9 = self.get_image(4, width, height, 0.5, (0, 0, 0), 0)
        animation_list = [frame_1, frame_2, frame_3, frame_2]
        animation_list2 = [frame_8, frame_7, frame_6, frame_7]
        clock = pygame.time.Clock()
        dt = clock.tick(60)
        player = pygame.Rect((width - 50) / 2, height - 50, 320 * 0.5, 320 * 0.5)
        game_speed = 0.1
        last_update = pygame.time.get_ticks()
        frame = 0
        run = True
        left_right = 1
        gravity = 0
        while run:
            screen.blit(self.background, (0, 0))
            if left_right == 0:
                screen.blit(frame_9, player)
            else:
                screen.blit(frame_0, player)

            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            key_INPUT = pygame.key.get_pressed()
            if key_INPUT[pygame.K_LEFT] and player.left >= 0:
                left_right = 0
                player.left -= game_speed * dt
                if current_time - last_update >= dt * 10:
                    frame = (frame + 1) % 4
                    last_update = current_time
                screen.blit(self.background, (0, 0))
                screen.blit(animation_list2[frame], player)
                pygame.display.update()
            if key_INPUT[pygame.K_RIGHT] and player.right <= 1600:
                left_right = 1
                player.right += game_speed * dt
                if current_time - last_update >= dt * 10:
                    frame = (frame + 1) % 4
                    last_update = current_time
                screen.blit(self.background, (0, 0))
                screen.blit(animation_list[frame], player)
                pygame.display.update()

            player.top += gravity
            gravity += 0.05

            if player.bottom >= 800:
                screen.blit(self.background, (0, 0))
                if left_right == 0:
                    screen.blit(frame_9, player)
                else:
                    screen.blit(frame_0, player)
                gravity = 0
                if key_INPUT[pygame.K_UP]:
                    gravity = -4
                    screen.blit(self.background, (0, 0))
                    if left_right == 0:
                        screen.blit(frame_5, player)
                    else:
                        screen.blit(frame_4, player)

            pygame.display.update()

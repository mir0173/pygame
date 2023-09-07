import pygame
import sprite
from background import screen_change, right_area, bottom_area
from system import esc, resume, update
from dialogue import dialogue
from interaction import interaction, diaryinter, inventory, viewdiary

pausepopup = pygame.image.load('./assets/pause.png')


class B3:
    def __init__(self, screen, font):
        self.screen_number = 7
        self.font = font
        self.screen = screen
        self.pause = False
        self.tostart = False

    def story(self, character_left, character_right):
        protagonist = sprite.protagonist(self.font, character_left, character_right, 7)
        protagonist.alpha = 125
        update(self.screen, self.font, protagonist)
        image_gray = pygame.image.load('./assets/gray.png')
        Gray = pygame.transform.scale(image_gray, (1600, 900))
        Gray.set_alpha(175)
        run = True
        canmove = False
        x = dialogue(6, self.screen, self.font, protagonist)
        k = 0
        m = 0
        n = 0
        i = 0
        inven = 0
        foinven = 0
        nonejournal = pygame.Rect(560, 200, 0, 0)
        number = 1
        number2 = 1
        inter = 0
        togimic = False
        complete = False
        if x == 1:
            canmove = True
        while run:
            clock = pygame.time.Clock()
            dt = clock.tick(60)
            if (n == 1) and self.screen_number != 30:
                self.screen_number = screen_change(protagonist, self.screen_number)
            if not self.pause:
                foinven = inven

                if canmove:
                    protagonist.move(self.screen, dt, 0.6)

                key_INPUT = pygame.key.get_pressed()

                if key_INPUT[pygame.K_ESCAPE] and inter != 2:
                    esc(self, self.screen, self.font, protagonist)
                if self.screen_number == 24:


                if canmove and inven == 0:
                    inven = inventory()
                elif inven == 1:
                    canmove = False
                    update(self.screen, self.font, protagonist)
                    number2 = viewdiary(self.screen, self.font, number2, protagonist)
                    if number2 == -1:
                        inven = 0
                        number2 = 1

                if foinven == 1 and inven == 0:
                    canmove = True

                pygame.display.update()

            else:
                resume(self, self.screen, self.font, protagonist)
            if self.tostart:
                return

            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                print(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

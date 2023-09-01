import pygame

background_list = []
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-1.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-2dark.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-2open.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-2dark.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-2open.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-3dark.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-3bright.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-1dark.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-1bright.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-2dark.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-2bright.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-2on.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-2bright.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-4dark.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-4bright.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-4nodiary.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))  # 3층
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))  # 2층
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))

left_area = 55
right_area = 55
bottom_area = 15
top_area = 20

obstacle_list = []
for i in range(len(background_list)):
    obstacle_list.append([pygame.Rect(-500, 775, 2600, 125), pygame.Rect(-500, -100, 2600, 100)])

obstacle_list[0] = [pygame.Rect(-500, 775, 2600, 125), pygame.Rect(-500, -100, 2600, 100),
                    pygame.Rect(945, 650, 125, 125)]

obstacle_list[7] = [pygame.Rect(-500, 775, 2600, 125), pygame.Rect(-500, -100, 2600, 100),
                    pygame.Rect(250, 650, 125, 125), pygame.Rect(1075, 650, 125, 125), pygame.Rect(1225, 650, 125, 125),
                    pygame.Rect(1175, 525, 125, 125)]

obstacle_list[8] = [pygame.Rect(-500, 775, 2600, 125), pygame.Rect(-500, -100, 2600, 100),
                    pygame.Rect(250, 650, 125, 125), pygame.Rect(1075, 650, 125, 125), pygame.Rect(1225, 650, 125, 125),
                    pygame.Rect(1175, 525, 125, 125)]


movable = []
for i in range(len(background_list)):
    movable.append([])

movable[0] = []

movable_image = []
for i in range(len(background_list)):
    movable_image.append([])

movable_image[0] = []


def crash(obstacle, player, left_right):
    if left_right == 1:
        if not ifcrash(player.left + left_area, player.right - right_area, obstacle.left, obstacle.right):
            return False
        else:
            if ifcrash(player.top + top_area, player.bottom - bottom_area, obstacle.top, obstacle.bottom):
                return True
            else:
                return False
    elif left_right == 0:
        if not ifcrash(player.left + right_area, player.right - left_area, obstacle.left, obstacle.right):
            return False
        else:
            if ifcrash(player.top + top_area, player.bottom - bottom_area, obstacle.top, obstacle.bottom):
                return True
            else:
                return False


def screen_change(protagonist, screen_number):
    if protagonist.player.right >= 1600 and screen_number + 1 < len(background_list):
        protagonist.screen_number += 1
        screen_number += 1
        protagonist.player = pygame.Rect(50, 775 - 320 * 0.5 + bottom_area, 320 * 0.5, 320 * 0.5)
    return screen_number


def ifcrash(playerleft, playerright, obstacleleft, obstacleright):
    if not playerright <= obstacleleft and not playerleft >= obstacleright:
        return True
    else:
        return False

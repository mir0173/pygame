# 배경에 관한 파일

import pygame

# 배경 이미지 불러오기
background_list = []
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-1.png'), (160 * 10, 90 * 10)))  # 6층(튜토리얼) : 7
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-2dark.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-2open.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-2dark.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-2open.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-3dark.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/6-3bright.png'), (160 * 10, 90 * 10)))

background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-1dark.png'), (160 * 10, 90 * 10)))   # 5층 : 12
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-1bright.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-2dark.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-2bright.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-2on.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-2bright.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-4dark.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-4bright.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-4nodiary.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-4nodiary.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-5dark.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/5-5bright.png'), (160 * 10, 90 * 10)))

background_list.append(pygame.transform.scale(pygame.image.load('./assets/4-1.png'), (160 * 10, 90 * 10)))  # 4층 : 7
background_list.append(pygame.transform.scale(pygame.image.load('./assets/4-2.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/4-3diary.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/4-3nodiary.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/4-3nodiary.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/4-4.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/4-5.png'), (160 * 10, 90 * 10)))

background_list.append(pygame.transform.scale(pygame.image.load('./assets/3-1.png'), (160 * 10, 90 * 10)))  # 3층 : 10
background_list.append(pygame.transform.scale(pygame.image.load('./assets/3-2.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/0-1.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/0-2.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/0-3.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/0-4diary.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/0-4nodiary.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/0-4nodiary.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/3-2.png'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/3-4.png'), (160 * 10, 90 * 10)))

background_list.append(pygame.transform.scale(pygame.image.load('./assets/na.png'), (160 * 10, 90 * 10)))  # 2층 : 4
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))
background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))

background_list.append(pygame.transform.scale(pygame.image.load('./assets/B6.jpg'), (160 * 10, 90 * 10)))

left_area = 55
right_area = 55
bottom_area = 15
top_area = 20

bird_left_area = 35
bird_right_area = 25
bird_bottom_area = 60
bird_top_area = 50

# 각 배경의 바닥과 천장을 장애물 취급
obstacle_list = []
for i in range(len(background_list)):
    obstacle_list.append([pygame.Rect(-500, 775, 2600, 125), pygame.Rect(-500, -100, 2600, 100)])

#각 배경의 장애물 설정
obstacle_list[0] = [pygame.Rect(-500, 775, 2600, 125), pygame.Rect(-500, -100, 2600, 100),
                    pygame.Rect(945, 650, 125, 125)]

obstacle_list[7] = [pygame.Rect(-500, 775, 2600, 125), pygame.Rect(-500, -100, 2600, 100),
                    pygame.Rect(250, 650, 125, 125), pygame.Rect(1075, 650, 125, 125), pygame.Rect(1225, 650, 125, 125),
                    pygame.Rect(1175, 525, 125, 125)]

obstacle_list[8] = [pygame.Rect(-500, 775, 2600, 125), pygame.Rect(-500, -100, 2600, 100),
                    pygame.Rect(250, 650, 125, 125), pygame.Rect(1075, 650, 125, 125), pygame.Rect(1225, 650, 125, 125),
                    pygame.Rect(1175, 525, 125, 125)]

obstacle_list[19] = [pygame.Rect(-500, 775, 2600, 125), pygame.Rect(-500, -100, 2600, 100),
                     pygame.Rect(900, 520, 125, 125), pygame.Rect(900, 650, 125, 125)]

obstacle_list[20] = [pygame.Rect(-500, 775, 2600, 125), pygame.Rect(-500, -100, 2600, 100),
                     pygame.Rect(400, 650, 125, 125), pygame.Rect(400, 275, 125, 250), pygame.Rect(525, 650, 125, 125),
                     pygame.Rect(1100, 525, 125, 250)]

obstacle_list[24] = [pygame.Rect(-500, 775, 2600, 125), pygame.Rect(-500, -100, 2600, 100),
                     pygame.Rect(400, 525, 125, 125), pygame.Rect(400, 650, 125, 125), pygame.Rect(525, 525, 125, 125),
                     pygame.Rect(525, 650, 125, 125), pygame.Rect(775, 525, 125, 375), pygame.Rect(1025, 275, 125, 500)]

obstacle_list[29] = [pygame.Rect(-500, 775, 2600, 125), pygame.Rect(-500, -100, 2600, 100), 
                     pygame.Rect(175, 0, 125, 300), pygame.Rect(175, 460, 125, 440), 
                     pygame.Rect(425, 0, 125, 405), pygame.Rect(425, 575, 125, 325),
                     pygame.Rect(675, 0, 125, 170), pygame.Rect(675, 320, 125, 580),
                     pygame.Rect(925, 0, 125, 20), pygame.Rect(925, 200, 125, 700), 
                     pygame.Rect(1175, 0, 125, 425), pygame.Rect(1175, 620, 125, 280),
                     pygame.Rect(1425, 0, 125, 170), pygame.Rect(1425, 385, 125, 515)]


# movable에는 장애물의 인덱스를 저장, movable_image에는 장애물의 이미지를 저장
movable = []
for i in range(len(background_list)):
    movable.append([])

movable[19] = [2]
movable[20] = [2]
movable[24] = [2, 3, 4, 5]

movable_image = []
for i in range(len(background_list)):
    movable_image.append([])

movable_image[19] = [pygame.transform.scale(pygame.image.load('./assets/move.png'), (125, 125))]
movable_image[20] = [pygame.transform.scale(pygame.image.load('./assets/move.png'), (125, 125))]
movable_image[24] = [pygame.transform.scale(pygame.image.load('./assets/move.png'), (125, 125)),
                     pygame.transform.scale(pygame.image.load('./assets/move.png'), (125, 125)),
                     pygame.transform.scale(pygame.image.load('./assets/move.png'), (125, 125)),
                     pygame.transform.scale(pygame.image.load('./assets/move.png'), (125, 125))]

# 장애물 피격 함수
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
            
def bird_crash(obstacle, player, left_right):
    if left_right == 1:
        if not ifcrash(player.left + bird_left_area, player.right - bird_right_area, obstacle.left, obstacle.right):
            return False
        else:
            if ifcrash(player.top + bird_top_area, player.bottom - bottom_area, obstacle.top, obstacle.bottom):
                return True
            else:
                return False
    elif left_right == 0:
        if not ifcrash(player.left + bird_right_area, player.right - bird_left_area, obstacle.left, obstacle.right):
            return False
        else:
            if ifcrash(player.top + bird_top_area, player.bottom - bottom_area, obstacle.top, obstacle.bottom):
                return True
            else:
                return False
            
# 장애물 피격 함수
def ifcrash(playerleft, playerright, obstacleleft, obstacleright):
    if not playerright <= obstacleleft and not playerleft >= obstacleright:
        return True
    else:
        return False

# 배경을 바꾸는 함수
def screen_change(protagonist, screen_number):
    if protagonist.player.right >= 1600 and screen_number + 1 < len(background_list):
        protagonist.screen_number += 1
        screen_number += 1
        protagonist.player = pygame.Rect(50, 775 - 320 * 0.5 + bottom_area, 320 * 0.5, 320 * 0.5)
    return screen_number

def bird_screen_change(bird, protagonist, screen_number):
    if bird.player.right >= 1600 and screen_number + 1 < len(background_list):
        protagonist.screen_number += 1
        screen_number += 1
        protagonist.alpha = 255
        protagonist.player = pygame.Rect(50, 775 - 320 * 0.5 + bottom_area, 320 * 0.5, 320 * 0.5)
    return screen_number

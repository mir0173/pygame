import pygame

first_puzzle = [[(480, 130), 0], [(640, 130), 1], [(800, 130), 2], [(960, 130), 1],
                [(480, 290), 0], [(640, 290), 2], [(800, 290), 0], [(960, 290), 3],
                [(480, 450), 2], [(640, 450), 4], [(800, 450), 1], [(960, 450), 2],
                [(480, 610), 0], [(640, 610), 1], [(800, 610), 0], [(960, 610), 0]]

first_puzzle_answer = [[0], [2], [1], [1],
                       [0], [0], [0], [0, 3],
                       [1], [0], [0, 1, 2, 3], [0, 1],
                       [0], [0, 1, 2, 3], [0], [0]]

second_puzzle = [[(480, 130), 2], [(640, 130), 2], [(800, 130), 3], [(960, 130), 2],
                 [(480, 290), 3], [(640, 290), 1], [(800, 290), 2], [(960, 290), 1],
                 [(480, 450), 1], [(640, 450), 4], [(800, 450), 1], [(960, 450), 3],
                 [(480, 610), 2], [(640, 610), 3], [(800, 610), 2], [(960, 610), 1]]

second_puzzle_answer = [[0, 1], [0, 1], [0, 1, 2, 3], [0, 1],
                        [2, 3], [1], [0, 1], [2],
                        [0], [0], [0, 1, 2, 3], [1, 3],
                        [0, 1], [0, 3], [1], [0]]

third_puzzle = [[(482, 132), 3], [(588, 132), 3], [(694, 132), 2], [(800, 132), 1], [(906, 132), 2], [(1012, 132), 2],
                [(482, 238), 2], [(588, 238), 1], [(694, 238), 1], [(800, 238), 4], [(906, 238), 1], [(1012, 238), 3],
                [(482, 344), 2], [(588, 344), 2], [(694, 344), 1], [(800, 344), 3], [(906, 344), 2], [(1012, 344), 0],
                [(482, 450), 3], [(588, 450), 1], [(694, 450), 3], [(800, 450), 0], [(906, 450), 1], [(1012, 450), 1],
                [(482, 556), 1], [(588, 556), 1], [(694, 556), 2], [(800, 556), 2], [(906, 556), 0], [(1012, 556), 3],
                [(482, 662), 4], [(588, 662), 1], [(694, 662), 1], [(800, 662), 3], [(906, 662), 2], [(1012, 662), 3]]

third_puzzle_answer = [[2, 3], [0, 2], [1], [1], [0, 1], [0, 1],
                       [0], [0, 1, 2, 3], [0, 1, 2, 3], [0], [2], [0, 2],
                       [0], [0, 1], [2], [0, 1], [0], [0],
                       [1, 3], [0, 1, 2, 3], [1, 3], [0], [3], [1],
                       [0], [0, 1, 2, 3], [0], [0, 1], [0], [1, 3],
                       [0], [0, 1, 2, 3], [3], [0, 2], [1], [0, 1]]


class Circuit(pygame.sprite.Sprite):
    def __init__(self, information, size):
        super().__init__()
        self.size = size
        position = information[0]
        circuit_number = information[1]
        self.position = position
        self.rect = pygame.Rect(position, self.size)
        empty_images = [pygame.image.load('image/empty_circuit.png')]
        right_angle_images = [pygame.image.load('image/right_angle_circuit1.png'),
                              pygame.image.load('image/right_angle_circuit2.png'),
                              pygame.image.load('image/right_angle_circuit3.png'),
                              pygame.image.load('image/right_angle_circuit4.png')]
        t_images = [pygame.image.load('image/t_circuit1.png'),
                    pygame.image.load('image/t_circuit2.png'),
                    pygame.image.load('image/t_circuit3.png'),
                    pygame.image.load('image/t_circuit4.png')]
        linear_images = [pygame.image.load('image/linear_circuit1.png'),
                         pygame.image.load('image/linear_circuit2.png')]
        cross_images = [pygame.image.load('image/cross_circuit.png')]
        if circuit_number == 0:
            images = empty_images
        elif circuit_number == 1:
            images = right_angle_images
        elif circuit_number == 2:
            images = linear_images
        elif circuit_number == 3:
            images = t_images
        else:
            images = cross_images
        self.images = [pygame.transform.scale(image, size) for image in images]
        self.index = 0
        self.index_max = len(images) - 1
        self.image = images[self.index]
        self.mouse_clicked = True

    def update(self):
        mouse_input = pygame.mouse.get_pressed()[0]
        mouse_position = pygame.mouse.get_pos()
        if self.position[0] <= mouse_position[0] <= self.position[0] + self.size[0] \
                and self.position[1] <= mouse_position[1] <= self.position[1] + self.size[0]:
            if mouse_input and self.mouse_clicked:
                self.mouse_clicked = False
                if self.index < self.index_max:
                    self.index += 1
                else:
                    self.index = 0
            elif not mouse_input:
                self.mouse_clicked = True

        self.image = self.images[self.index]

    def current_state(self):
        return self.index


def answer_check(answer_sheet: list, answer: list):
    count = 0
    for i in range(len(answer)):
        if answer_sheet[i] not in answer[i]:
            count += 1

    if count == 0:
        return True
    else:
        return False

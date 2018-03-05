import pygame
import os
import random
pygame.init()
size = (1400, 1000)
screen = pygame.display.set_mode(size)
backspace = 150
number_of_points = 0
ACCELERATION_CONSTANT = 300
SPEED_INCREASE_CONSTANT = 1
LEVEL_THRESHOLD_CONSTANT = 15
list_of_Name = ['']


def making_board(a, n):
    for i in range(a // n):
        for j in range(a // n):
            if (i + j) % 2 == 1:
                pygame.draw.rect(screen, (135, 206, 235), (i * a // n + backspace, j * a // n + backspace, a // n + 1, a // n + 1))
            else:
                pygame.draw.rect(screen, (100, 149, 237), (i * a // n + backspace, j * a // n + backspace, a // n + 1, a // n + 1))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        return image
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)


def making_random_apple():
    a = random.randint(150, 700)
    b = random.randint(150, 700)
    return (a, b)


def making_random_bonus():
    c = random.randint(1, 100)
    if c < 20:
        a = random.randint(150, 700)
        b = random.randint(150, 700)
        return (a, b)


def making_random_life():
    c = random.randint(1, 100)
    if c < 5:
        a = random.randint(150, 700)
        b = random.randint(150, 700)
        return (a, b)


def intersection_of_rectangles_function(first_coords, first_size, second_coords, second_size):
    k = True
    if (first_coords[0] + first_size) < second_coords[0]:
        k = False

    if (first_coords[1] + first_size) < second_coords[1]:
        k = False

    if first_coords[0] > (second_coords[0] + second_size[0]):
        k = False

    if first_coords[1] > (second_coords[1] + second_size[1]):
        k = False

    return  k


def counter_function(n, Lvl):
    font = pygame.font.Font(None, 40)
    text = font.render(str(n + (Lvl - 1) * 15), 1, (128, 0, 0))
    screen.blit(text, (500 - text.get_width() // 2 + 700, 30))


def Lvl_counter_function(n):
    font = pygame.font.Font(None, 40)
    text = font.render('Lvl' + ': ' +str(n), 1, (128, 0, 0))
    screen.blit(text, (500 - text.get_width() // 2 + 700, 100))


def acceleration_system_function(acceleration):
    pygame.draw.rect(screen, (139, 69, 19), (10, 10, ACCELERATION_CONSTANT, 20), 3)
    if abs(acceleration) > 5:
        pygame.draw.rect(screen, (128, 5, 128), (11, 10, acceleration, 18))


def health_system_fuction(health):
    k = 0
    for i in range(health):
        screen.blit(life_picture, (1000 + i * 40, 200 + k * 50))


def work_with_file(lvl, n):
    file = open('record.txt', 'a')
    file.write(' ' + str((lvl - 1) * 15 + n))
    file.close()


def making_random_killer():
    c = random.randint(1, 4)

    if c == 1:
        a = random.randint(150, 700)
        return [c, a, 0]

    if c == 2:
        a = random.randint(150, 700)
        return [c, 1000, a]

    if c == 3:
        a = random.randint(150, 700)
        return [c, a, 1000]

    if c == 4:
        a = random.randint(150, 700)
        return [c, 0, a]


def making_random_lazer():
    c = random.randint(1, 4)
    if c == 1:
        a = random.randint(145, 845)
        return (c, a, 75)
    if c == 2:
        a = random.randint(145, 845)
        return (c, 850, a)
    if c == 3:
        a = random.randint(110, 810)
        return (c, a, 850)
    if c == 4:
        a = random.randint(110, 810)
        return (c, 75, a)


class Lazer:
    def __init__(self):
        self.L_timer = 0
        self.shot = False
        self.spis_of_lazer = []
        self.death = False

    def render(self, Lvl, coords):
        self.death = False
        self.L_timer += v
        if self.L_timer > 600 and self.shot == False:
            self.shot = True
            self.L_timer = 0
            self.spis_of_laser = []
            for i in range(int(1.4 * Lvl + 6)):
                self.spis_of_laser.append(making_random_lazer())
        if self.shot == True:
            for el in self.spis_of_laser:
                if el[0] == 1:
                    screen.blit(lazer_pic1, (el[1], el[2]))
                if el[0] == 2:
                    screen.blit(lazer_pic2, (el[1], el[2]))
                if el[0] == 3:
                    screen.blit(lazer_pic3, (el[1], el[2]))
                if el[0] == 4:
                    screen.blit(lazer_pic4, (el[1], el[2]))

                if self.L_timer < 254 and self.shot:
                    if el[0] == 1:
                        pygame.draw.rect(screen, (int(self.L_timer), 20, 60), (el[1] + 10, el[2] + 60, 2, 1010))
                    if el[0] == 2:
                        pygame.draw.rect(screen, (int(self.L_timer), 20, 60), (el[1] - 1000, el[2] + 7, 1004, 2))
                    if el[0] == 3:
                        pygame.draw.rect(screen, (int(self.L_timer), 20, 60), (el[1] + 50, el[2] - 1000, 2, 1004))
                    if el[0] == 4:
                        pygame.draw.rect(screen, (int(self.L_timer), 20, 60), (el[1] + 55, el[2] + 50, 1010, 2))

                elif self.L_timer > 256 and self.shot:
                    if el[0] == 1:
                        pygame.draw.rect(screen, (255, 0, 0), (el[1] + 10, el[2] + 60, 7, 1010))
                        if intersection_of_rectangles_function(coords, size_pic, (el[1] + 10, el[2] + 60), (7, 1010)):
                            self.death = True

                    if el[0] == 2:
                        pygame.draw.rect(screen, (255, 0, 0), (el[1] - 1000, el[2] + 7, 1004, 7))
                        if intersection_of_rectangles_function(coords, size_pic, (el[1] - 1000, el[2] + 7), (1004, 7)):
                            self.death = True

                    if el[0] == 3:
                        pygame.draw.rect(screen, (255, 0, 0), (el[1] + 50, el[2] - 1000, 7, 1004))
                        if intersection_of_rectangles_function(coords, size_pic, (el[1] + 50, el[2] - 1000), (7, 1004)):
                            self.death = True

                    if el[0] == 4:
                        pygame.draw.rect(screen, (255, 0, 0), (el[1] + 55, el[2] + 50, 1010, 7))
                        if intersection_of_rectangles_function(coords, size_pic, (el[1] + 55, el[2] + 50), (1010, 7)):
                            self.death = True

                if self.L_timer > 600:
                    self.L_timer = 0
                    self.shot = False

    def character_states(self):
        return self.death


class Killer:
    def __init__(self):
        self.list_of_killer = []
        self.K_timmer = 0
        self.death = False

    def render(self, Lvl):
        self.K_timmer += v

        if self.K_timmer > 100 // 1.3 ** (Lvl - 1):
            self.K_timmer = 0
            self.list_of_killer.append(making_random_killer())

        for el in self.list_of_killer:
            if el[0] == 1:
                el[2] += v + SPEED_INCREASE_CONSTANT * (Lvl - 1)

            if el[0] == 2:
                el[1] -= v + SPEED_INCREASE_CONSTANT * (Lvl - 1)

            if el[0] == 3:
                el[2] -= v + SPEED_INCREASE_CONSTANT * (Lvl - 1)

            if el[0] == 4:
                el[1] += v + SPEED_INCREASE_CONSTANT * (Lvl - 1)

            screen.blit(killer_picture, (el[1], el[2]))

            if max(el) > 1000:
                self.list_of_killer.remove(el)

    def collision(self, coords):
        self.death = False
        for el in self.list_of_killer:
            if intersection_of_rectangles_function(coords, size_pic, (el[1], el[2]), (size_killer, size_killer)):
                self.list_of_killer.remove(el)
                self.death = True

    def character_states(self):
        return self.death



class Board:
    def __init__(self):
        self.A_timmer = 0
        self.K_timmer = 0
        self.N_timmer = 0
        self.list_of_apple = []
        self.list_of_bonus = []
        self.list_of_killer = []
        self.number_of_points = 0
        self.Lvl = 1
        self.acceleration = ACCELERATION_CONSTANT // 2
        self.vector = 2
        self.acceleration_bul = False
        self.coords = [300, 300]
        self.game_process = True
        self.health = 3
        self.pause = False
        self.laser = Lazer()
        self.killer = Killer()
        self.invulnerability = False

    def preparation_board_function(self):
        screen.fill((255, 255, 224))
        making_board(400, N)

        self.A_timmer += v
        self.K_timmer += v
        self.N_timmer += v

        if self.N_timmer > 300:
            self.invulnerability = False

        if self.A_timmer > 100:
            self.A_timmer = 0
            if len(self.list_of_apple) < 20:
                self.list_of_apple.append(making_random_apple())

            if len(self.list_of_bonus) < 15:
                a__ = making_random_bonus()
                if a__:
                    self.list_of_bonus.append([0, *a__])

                a__ = making_random_life()
                if a__:
                    self.list_of_bonus.append([1, *a__])


        for el in self.list_of_apple:
            screen.blit(apple, (el[0], el[1]))

        for el in self.list_of_bonus:
            if el[0] == 0:
                screen.blit(acceleration_picture, (el[1], el[2]))

            elif el[0] == 1:
                screen.blit(life_picture, (el[1], el[2]))


        for el in self.list_of_killer:
            screen.blit(killer_picture, (el[1], el[2]))

        self.laser.render(self.Lvl, self.coords)
        self.killer.render(self.Lvl)
        if self.laser.character_states() and not self.invulnerability:
            self.health = -100


        pygame.draw.rect(screen, (222, 184, 135),(1000, 0, 400, 1000))

    def event_check_function(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key ==  273:
                self.vector = 1
            elif event.key  == 274:
                self.vector = 3
            elif event.key  == 275:
                self.vector = 2
            elif event.key == 276 :
                self.vector = 4

            if event.key == 32 and self.acceleration > 0:
                self.acceleration_bul = True


        if event.type == pygame.KEYUP:
            if event.key == 32:
                self.acceleration_bul = False

    def motion_function(self):
        if self.vector == 1:

            if self.acceleration_bul == True and self.acceleration > 0:
                x = 2 * v
                self.acceleration -= v
            else:
                x = v
                if self.acceleration + v > ACCELERATION_CONSTANT:
                    self.acceleration = ACCELERATION_CONSTANT
                else:
                    self.acceleration += v / 3


            self.coords[1] -= x

        elif self.vector == 2:

            if self.acceleration_bul == True and self.acceleration > 0:
                x = 2 * v
                self.acceleration -= v
            else:
                x = v
                if self.acceleration + v > ACCELERATION_CONSTANT:
                    self.acceleration = ACCELERATION_CONSTANT
                else:
                    self.acceleration += v / 3


            self.coords[0] += x

        elif self.vector == 3:

            if self.acceleration_bul == True and self.acceleration > 0:
                x = 2 * v
                self.acceleration -= v
            else:
                x = v
                if self.acceleration + v > ACCELERATION_CONSTANT:
                    self.acceleration = ACCELERATION_CONSTANT
                else:
                    self.acceleration += v / 3


            self.coords[1] += x

        elif self.vector == 4:
            if self.acceleration_bul == True and self.acceleration > 0:
                x = 2 * v
                self.acceleration -= v
            else:
                x = v
                if self.acceleration + v > ACCELERATION_CONSTANT:
                    self.acceleration = ACCELERATION_CONSTANT
                else:
                    self.acceleration += v / 3


            self.coords[0] -= x

        self.coords[0] = self.coords[0] % size[0]
        self.coords[1] = self.coords[1] % size[0]
        if self.invulnerability:
            screen.blit(creature_fon, (self.coords[0], self.coords[1]))
        else:
            screen.blit(creature, (self.coords[0], self.coords[1]))

    def check_contact_function(self):
        for el in self.list_of_apple:
            if intersection_of_rectangles_function(self.coords, size_pic, el, (size_apple, size_apple)) and not self.invulnerability:
                self.list_of_apple.remove(el)
                self.number_of_points += 1

        for el in self.list_of_bonus:
            if intersection_of_rectangles_function(self.coords, size_pic, [el[1] , el[2]], (size_acceleration_picture, size_acceleration_picture)) and el[0] == 0 and not self.invulnerability:
                self.list_of_bonus.remove(el)
                self.number_of_points += 1
                if self.acceleration + 100 > ACCELERATION_CONSTANT:
                    self.acceleration = ACCELERATION_CONSTANT
                else:
                    self.acceleration += 100

            elif intersection_of_rectangles_function(self.coords, size_pic, [el[1] , el[2]], (size_acceleration_picture, size_acceleration_picture)) and el[0] == 1 and not self.invulnerability:
                self.health += 1
                self.list_of_bonus.remove(el)
                self.number_of_points += 1



        self.killer.collision(self.coords)
        if (self.killer.character_states() or  self.health < 1) and not self.invulnerability :
            if self.health < 2:
                self.game_process = False
                file = open('record.txt', 'a')
                file.write(' ' + str((self.Lvl - 1) * LEVEL_THRESHOLD_CONSTANT + self.number_of_points))
                file.close()
            else:
                self.health -= 1
                self.N_timmer = 0
                self.invulnerability = True

        if self.number_of_points == LEVEL_THRESHOLD_CONSTANT:
            self.Lvl += 1
            self.number_of_points = 0
        health_system_fuction(self.health)
        acceleration_system_function(self.acceleration)
        Lvl_counter_function(self.Lvl)
        counter_function(self.number_of_points, self.Lvl)

    def check_for_the_game(self):
        return self.game_process

    def draw_score(self):
        screen.fill((255, 255, 224))
        font = pygame.font.Font(None, 40)
        text = font.render('количество очков' + ': ' + str(self.number_of_points), 1, (128, 0, 0))
        screen.blit(text, (500 - text.get_width() // 2, 400))

        font = pygame.font.Font(None, 40)
        text = font.render('достугнутый уровень' + ': ' + str(self.Lvl), 1, (128, 0, 0))
        screen.blit(text, (500 - text.get_width() // 2, 450))


        k = 0
        file = open('record.txt', 'r')
        string = file.read().split()
        a = int(string[-1])
        file.close()
        for i in range(len(string)):
            string[i] = int(string[i])
            if int(string[i]) > a:
                k += 1
        font = pygame.font.Font(None, 35)
        text = font.render('итоговое число очков' + ' ' + str(a), 1, (128, 0, 0))
        screen.blit(text, (500 - text.get_width() // 2, 550))

        font = pygame.font.Font(None, 35)
        text = font.render('поздравляю вы обогнали' + ' ' + str(int((len(string) - k)/ len(string) * 100)) + '%', 1, (128, 0, 0))
        screen.blit(text, (500 - text.get_width() // 2, 600))

        font = pygame.font.Font(None, 35)
        text = font.render('текущий лучший результат' + ' ' +str(max(string)), 1, (128, 0, 0))
        screen.blit(text, (500 - text.get_width() // 2, 650))


        font = pygame.font.Font(None, 20)
        text = font.render('Для того что бы начать игру сначала нажмите "r" ', 1, (128, 0, 0))
        screen.blit(text, (500 - text.get_width() // 2, 950))

        pygame.draw.rect(screen, (222, 184, 135), (1000, 0, 400, 1000))

    def draw_pause(self):
        screen.fill((255, 255, 224))
        font = pygame.font.Font(None, 40)
        text = font.render('ну вот типо вам пауза', 1, (128, 0, 0))
        screen.blit(text, (500 - text.get_width() // 2, 400))


size_pic = 30
creature = load_image('creature.png', (255, 255, 255))
creature = pygame.transform.scale(creature, (size_pic, size_pic))
coords_pic = [100, 100]

creature_fon = load_image('creature_fon.png', (255, 255, 255))
creature_fon = pygame.transform.scale(creature_fon, (size_pic, size_pic))

size_apple = 30
apple = load_image('apple.png', (255, 255, 255))
apple = pygame.transform.scale(apple, (size_apple, size_apple))
list_of_apple = []

size_acceleration_picture = 30
acceleration_picture = load_image('acceleration_picture.png', (255, 255, 255))
acceleration_picture = pygame.transform.scale(acceleration_picture, (size_acceleration_picture, size_acceleration_picture))
list_of_bonus = []

size_life_picrure = 30
life_picture = load_image('life_pict.png', (255, 255, 255))
life_picture = pygame.transform.scale(life_picture, (size_life_picrure, size_life_picrure))

size_killer = 30
killer_picture = load_image('killer.jpg', (255, 255, 255))
killer_picture = pygame.transform.scale(killer_picture, (size_killer, size_killer))
list_of_killer = []

size_lazer = 60
lazer_pic1 = load_image('lazer1.png', (255, 255, 255))
lazer_pic1 = pygame.transform.scale(lazer_pic1, (size_lazer, size_lazer))

lazer_pic2 = load_image('lazer2.png', (255, 255, 255))
lazer_pic2 = pygame.transform.scale(lazer_pic2, (size_lazer, size_lazer))

lazer_pic3 = load_image('lazer3.png', (255, 255, 255))
lazer_pic3 = pygame.transform.scale(lazer_pic3, (size_lazer, size_lazer))

lazer_pic4 = load_image('lazer4.png', (255, 255, 255))
lazer_pic4 = pygame.transform.scale(lazer_pic4, (size_lazer, size_lazer))

x = 0
v = 5
fps = 30
clock = pygame.time.Clock()

N = 15
running = True
board = Board()
pause = False
while running:

    if board.check_for_the_game():
        board.preparation_board_function()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == 112:
                    pause = True
            board.event_check_function(event)
        board.motion_function()
        board.check_contact_function()
        clock.tick(fps)
        pygame.display.flip()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == 114:
                    board = Board()
        pygame.display.flip()
        board.draw_score()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pause = False
            if event.type == pygame.KEYDOWN:
                if event.key == 112:
                    pause = False
        board.draw_pause()
        pygame.display.flip()


pygame.quit()

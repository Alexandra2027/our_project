import pygame
import os
import sys
import sqlite3
from PIL import Image
import random


def show_text(screen, text, fontname, size, color, pos):  # функция для вывода текста
    font = pygame.font.SysFont(fontname, size)
    t = font.render(f"{text}", True, color)
    screen.blit(t, pos)


def load_image(name, colorkey=None):  # функция для загрузки изображений
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image()


class Xitori:
    def __init__(self, level_number):
        if level_number == 1:
            w = 3
            self.board = [[0] * w for _ in range(w)]
            self.board2 = [[0] * w for _ in range(w)]
            self.board2[0][1] = 2
            self.board2[2][0] = 2
            self.board2[2][2] = 2
            for i in range(w):
                for j in range(w):
                    if self.board2[i][j] == 0:
                        self.board2[i][j] = 1
        elif level_number == 2:
            w = 4
            self.board = [[0] * w for _ in range(w)]
            self.board2 = [[0] * w for _ in range(w)]
            self.board2[1][0] = 2
            self.board2[1][2] = 2
            self.board2[2][1] = 2
            self.board2[3][3] = 2
            for i in range(w):
                for j in range(w):
                    if self.board2[i][j] == 0:
                        self.board2[i][j] = 1
        else:
            w = 5
            self.board = [[0] * w for _ in range(w)]
            self.board2 = [[0] * w for _ in range(w)]
            self.board2[0][0] = 2
            self.board2[0][3] = 2
            self.board2[1][2] = 2
            self.board2[2][1] = 2
            self.board2[3][3] = 2
            self.board2[4][0] = 2
            self.board2[4][4] = 2
            for i in range(w):
                for j in range(w):
                    if self.board2[i][j] == 0:
                        self.board2[i][j] = 1
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.width = level_number + 2

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.width):
                if self.board[j][i] == 0:
                    screen.fill(pygame.Color(255, 255, 255), (
                    self.left + i * self.cell_size - 1, self.top + j * self.cell_size - 1, self.cell_size - 1,
                    self.cell_size - 1))
                elif self.board[j][i] == 1:
                    screen.fill(pygame.Color(241, 156, 187), (
                    self.left + i * self.cell_size - 1, self.top + j * self.cell_size - 1, self.cell_size - 1,
                    self.cell_size - 1))
                elif self.board[j][i] == 2:
                    screen.fill(pygame.Color(19, 0, 144), (
                    self.left + i * self.cell_size - 1, self.top + j * self.cell_size - 1, self.cell_size - 1,
                    self.cell_size - 1))

    def get_cell(self, mouse_pos):
        xm, ym = mouse_pos
        w = self.left + self.width * self.cell_size
        h = self.top + self.width * self.cell_size
        if self.left > xm or xm > w or self.top > ym or ym > h:
            return None
        else:
            i = (xm - self.left) // self.cell_size
            j = (ym - self.top) // self.cell_size
        return (i, j)

    def on_click(self, cell_coords):
        x, y = cell_coords
        if self.board[y][x] == 0:
            self.board[y][x] = 1
        elif self.board[y][x] == 1:
            self.board[y][x] = 2
        elif self.board[y][x] == 2:
            self.board[y][x] = 0
        if self.board == self.board2:
            print('win')

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.on_click(cell)


class KeyBord:  # Класс для клавиатуры
    def __init__(self, letter, coords, screen):
        self.letter = letter
        self.x = coords[0]
        self.y = coords[1]
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color((204, 204, 204)), (self.x, self.y, 45, 45))
        show_text(self.screen, self.letter, None, 40, (28, 28, 28), (self.x + 10, self.y + 10))
        pygame.display.flip()

    def click(self, pos):
        if pos[0] >= self.x and pos[0] <= self.x + 45 and pos[1] >= self.y and pos[1] <= self.y + 45:
            return self.letter
        else:
            return None


class MainWindow:
    def __init__(self, screen):
        self.screen = screen

    def drawing(self):
        self.screen.fill((53, 10, 26))
        draw_image(self.screen, (50, 270), 'data/main/keys.png', 480)
        show_text(self.screen, "Добро пожаловать в игру", 'comicsansms', 35, (255, 255, 255), (100, 50))
        show_text(self.screen, """ "Мир-Головоломок" """, 'comicsansms', 50, (233, 208, 178), (230, 120))
        # Кнопка Войти
        pygame.draw.rect(self.screen, (255, 255, 255), (450, 300, 230, 50))
        show_text(self.screen, "Войти", 'comicsansms', 30, (53, 10, 26), (515, 303))
        # Кнопка Зарегистирироваться
        pygame.draw.rect(self.screen, (255, 255, 255), (450, 400, 230, 50))
        show_text(self.screen, "Регистрация", 'comicsansms', 30, (53, 10, 26), (480, 403))
        pygame.display.flip()

    def get_click(self, mouse_pos):
        btn = self.is_button(mouse_pos)
        if btn == 1:  # если нажата кнопка Войти
            return 0.1
        elif btn == 2:  # если нажата кнопка Зарегистироваться
            return 0.2

    def is_button(self, mouse_pos):
        xm, ym = mouse_pos
        x = 450
        x1 = 670
        y = 300
        y1 = 350
        if x > xm or xm > x1:
            return None
        elif y <= ym and y1 >= ym:
            return 1
        elif y + 100 <= ym and y1 + 100 >= ym:
            return 2
        else:
            return None


class Regitration:
    def __init__(self, screen):
        self.screen = screen

    def drawing(self):
        self.screen.fill((53, 10, 26))
        # Кнопка Назад
        pygame.draw.rect(self.screen, (204, 204, 204), (50, 50, 100, 30))
        show_text(self.screen, "Назад", 'comicsansms', 20, (53, 10, 26), (75, 50))
        # регистриация
        show_text(self.screen, "Login", 'comicsansms', 30, (204, 204, 204), (310, 115))
        pygame.draw.line(self.screen, (205, 204, 204), (400, 150), (700, 150), width=2)
        show_text(self.screen, "Password", 'comicsansms', 30, (204, 204, 204), (310, 215))
        pygame.draw.line(self.screen, (205, 204, 204), (450, 250), (700, 250), width=2)
        # Кнопка Удвлить
        pygame.draw.rect(self.screen, (204, 204, 204), (50, 130, 100, 30))
        show_text(self.screen, "Удалить", 'comicsansms', 20, (53, 10, 26), (60, 130))
        # Кнопка Далее
        pygame.draw.rect(self.screen, (204, 204, 204), (160, 130, 100, 30))
        show_text(self.screen, "Далее", 'comicsansms', 20, (53, 10, 26), (170, 130))
        # Кнопка Удвлить 2
        pygame.draw.rect(self.screen, (204, 204, 204), (50, 220, 100, 30))
        show_text(self.screen, "Удалить", 'comicsansms', 20, (53, 10, 26), (60, 220))
        # Кнопка Далее 2
        pygame.draw.rect(self.screen, (204, 204, 204), (160, 220, 100, 30))
        show_text(self.screen, "Далее", 'comicsansms', 20, (53, 10, 26), (170, 220))
        pygame.display.flip()

    def is_button(self, mouse_pos):
        xm, ym = mouse_pos
        if 50 < xm and xm < 200 and 50 < ym and ym < 100:
            return 0
        elif 50 < xm and xm < 150 and 130 < ym and ym < 160:
            return 100
        elif 160 < xm and xm < 260 and 130 < ym and ym < 160:
            return 150
        elif 50 < xm and xm < 150 and 220 < ym and ym < 250:
            return 200
        elif 160 < xm and xm < 260 and 220 < ym and ym < 250:
            return 250
        else:
            return None


class level1:
    def __init__(self, screen):
        self.screen = screen

    def drawing(self):
        draw_image(self.screen, (0, 0,), 'data/level 1/fon.png', 800)
        draw_image(self.screen, (405, 200), 'data/level 1/panel.png', 200)
        pygame.display.flip()

    def get_click(self, mouse_pos):
        if mouse_pos[0] >= 410 and mouse_pos[0] <= 610 and mouse_pos[1] >= 200 and mouse_pos[1] <= 400:
            return 1
        else:
            return None


class Bomb(pygame.sprite.Sprite):
    fullname = os.path.join('data/level 1', "bomb.png")
    fullname1 = os.path.join('data/level 1', "boom.png")
    if not os.path.isfile(fullname) or not os.path.isfile(fullname1):
        print("Файл с изображением не найден")
        sys.exit()
    image = pygame.image.load(os.path.join('data/level 1', "bomb.png"))
    image_boom = pygame.image.load(os.path.join('data/level 1', "boom.png"))

    def __init__(self, group):
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        x = random.randrange(0, 7) * (width // 7)
        y = random.randrange(0, 7) * (height // 7)
        if not (x, y) in a:
            self.rect.x = x
            self.rect.y = y
            a.append((x, y))

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
           self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


def draw_image(screen, pos, img, size):
    img = Image.open(img)
    img.thumbnail((size, size))
    PIL_draw(screen, img, pos)


def PIL_draw(screen, img, pos):
    pygame_img = pygame.image.fromstring(img.tobytes(), img.size, "RGB")
    screen.blit(pygame_img, pos)


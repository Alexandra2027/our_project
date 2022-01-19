import os
import sys
import pygame
from mod import show_text  # холст, текст, шрифт, размер, цвет (кортедж), позиция (кортедж)
from mod import load_image  # путь, прозроачность
from mod import Xitori
https://github.com/Alexandra2027/our_project/blob/main/main.py
if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    running = True
    screen = pygame.display.set_mode(size)
    screen.fill((53, 10, 26))
    show_text(screen, "Добро пожаловать в игру", 'comicsansms', 35, (255, 255, 255), (100, 50))
    show_text(screen, """ "Название игры" """, 'comicsansms', 50, (233, 208, 178), (230, 120))
    pygame.draw.rect(screen, (255, 255, 255), (50, 250, 200, 300), width=2)  # Прямоугольник для картинки
    # Кнопка Войти
    pygame.draw.rect(screen, (255, 255, 255), (450, 300, 230, 50))
    show_text(screen, "Войти", 'comicsansms', 30, (53, 10, 26), (515, 303))
    # Кнопка Зарегистирироваться
    pygame.draw.rect(screen, (255, 255, 255), (450, 400, 230, 50))
    show_text(screen, "Регистрация", 'comicsansms', 30, (53, 10, 26), (480, 403))
    pygame.display.flip()
    level = 0  # номер уровня
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 450 and event.pos[0] <= 670 and event.pos[1] >= 300 and event.pos[1] <= 350 and \
                        level == 0:  # Нажата Кнопка Войти
                    screen1 = pygame.display.set_mode(size)
                    screen1.fill((255, 255, 255))
                    pygame.display.flip()
                    level = 0.1
                elif event.pos[0] >= 450 and event.pos[0] <= 670 and event.pos[1] >= 400 and event.pos[1] <= 450 and \
                        level == 0:  # Нажата Кнопка Зарегистироваться
                    screen1 = pygame.display.set_mode(size)
                    screen1.fill((0, 0, 0))
                    pygame.display.flip()
                    level = 0.2
                elif level == 0.1:
                    pass
    pygame.quit()


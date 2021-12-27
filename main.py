import os
import sys
import pygame
from mod import show_text  # холст, текаст, шрифт, размер, цвет (кортедж), позиция (кортедж)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    running = True
    screen = pygame.display.set_mode(size)
    screen.fill((53, 10, 26))
    show_text(screen, "Добро пожаловать в игру", 'comicsansms', 35, (255, 255, 255), (100, 50))
    show_text(screen, """ "Название игры" """, 'comicsansms', 50, (233, 208, 178), (230, 120))
    pygame.draw.rect(screen, (255, 255, 255), (50, 250, 200, 300), width=2)  # Прямоугольник для картинки
    # Кнопка Войти
    pygame.draw.rect(screen, (255, 255, 255), (450, 300, 230, 50))
    show_text(screen, "Войти", 'comicsansms', 30, (53, 10, 26), (515, 303))
    # Кнопки Регистрация
    pygame.draw.rect(screen, (255, 255, 255), (450, 400, 230, 50))
    show_text(screen, "Зарегистрироваться", 'comicsansms', 20, (53, 10, 26), (475, 410))
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 450 and event.pos[0] <= 670 and event.pos[1] >= 300 and event.pos[1] <= 350:
                    print('нажата кнопка Войти')
                if event.pos[0] >= 450 and event.pos[0] <= 670 and event.pos[1] >= 400 and event.pos[1] <= 450:
                    print('нажата кнопка Зарегистрироваться')
    pygame.quit()


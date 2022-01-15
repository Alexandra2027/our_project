import os
import sys
import pygame
from mod import show_text  # холст, текст, шрифт, размер, цвет (кортедж), позиция (кортедж)
from mod import load_image  # путь, прозроачность


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
    show_text(screen, "Играть", 'comicsansms', 30, (53, 10, 26), (515, 303))
    pygame.display.flip()
    level = 0  # номер уровня
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 450 and event.pos[0] <= 670 and event.pos[1] >= 300 and event.pos[1] <= 350 and \
                        level == 0:
                    print('нажата кнопка Играть')
                    screen1 = pygame.display.set_mode(size)
                    screen1.fill((255, 255, 255))
                    show_text(screen1, 'Здесь должен быть fon.png, ', None, 50, (13, 155, 66), (10, 10))
                    show_text(screen1, 'который находиться в папке data/level 1', None, 50, (13, 155, 66), (10, 60))
                    show_text(screen1, 'А на двери должан быть спрайт', None, 50, (13, 155, 66), (10, 110))
                    show_text(screen1, 'под назвнием "data/level 1/panel.png"', None, 50, (13, 155, 66), (10, 160))
                    show_text(screen1, 'и при нажатии на него открывается игра', None, 50, (13, 155, 66), (10, 210))
                    show_text(screen1, '"бомбочки-конопочки"', None, 50, (13, 155, 66), (10, 260))
                    pygame.display.flip()
                    level = 1
                if level == 1:
                    pass



    pygame.quit()



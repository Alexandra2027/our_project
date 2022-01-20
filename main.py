import os
import sys
import pygame
from mod import show_text  # холст, текст, шрифт, размер, цвет (кортедж), позиция (кортедж)
from mod import load_image  # путь, прозроачность
from mod import Xitori
from mod import KeyBord
from mod import MainWindow, Regitration

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    running = True
    screen = pygame.display.set_mode(size)
    window = MainWindow(screen)
    window.drawing()
    login_text = ''
    level = 0
    while running:
        if level == 0.1:
            screen.fill((30, 120, 240))
            pygame.display.flip()
        elif level == 0.2:
            window = Regitration(screen)
            window.drawing()
            Key_A = KeyBord('A', (100, 550), screen)
            Key_A.draw()
            Key_B = KeyBord('B', (150, 550), screen)
            Key_B.draw()
            Key_C = KeyBord('C', (200, 550), screen)
            Key_C.draw()
            Key_D = KeyBord('D', (250, 550), screen)
            Key_D.draw()
            Key_E = KeyBord('E', (300, 550), screen)
            Key_E.draw()
            Key_F = KeyBord('F', (350, 550), screen)
            Key_F.draw()
            Key_G = KeyBord('G', (400, 550), screen)
            Key_G.draw()
            Key_H = KeyBord('H', (450, 550), screen)
            Key_H.draw()
            Key_I = KeyBord('I', (500, 550), screen)
            Key_I.draw()
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level == 0 and window.get_click(event.pos) != None:
                    level = window.get_click(event.pos)
                elif level == 0.2:
                    if Key_A.click(event.pos) != None:
                        letter = Key_A.click(event.pos)
                        login_text += letter
                        print(login_text)
                    elif Key_B.click(event.pos) != None:
                        letter = Key_B.click(event.pos)
                        login_text += letter
                        print(login_text)
                    elif Key_C.click(event.pos) != None:
                        letter = Key_C.click(event.pos)
                        login_text += letter
                        print(login_text)
                    elif Key_D.click(event.pos) != None:
                        letter = Key_D.click(event.pos)
                        login_text += letter
                        print(login_text)
                    elif Key_E.click(event.pos) != None:
                        letter = Key_E.click(event.pos)
                        login_text += letter
                        print(login_text)
                    elif Key_F.click(event.pos) != None:
                        letter = Key_F.click(event.pos)
                        login_text += letter
                        print(login_text)
                    elif Key_G.click(event.pos) != None:
                        letter = Key_G.click(event.pos)
                        login_text += letter
                        print(login_text)
                    elif Key_H.click(event.pos) != None:
                        letter = Key_H.click(event.pos)
                        login_text += letter
                        print(login_text)
                    elif Key_I.click(event.pos) != None:
                        letter = Key_I.click(event.pos)
                        login_text += letter
                        print(login_text)
                    # Второй ряд

    pygame.quit()


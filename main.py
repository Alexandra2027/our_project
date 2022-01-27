import pygame
import sys
import time
import random
from pygame.locals import *
from moves import *
from mod import show_text  # холст, текст, шрифт, размер, цвет (кортедж), позиция (кортедж)
from mod import load_image  # путь, прозроачность
from mod import Xitori
from mod import KeyBord
from mod import MainWindow, Regitration, level1, level11, level2, level3, level4, level5
import sqlite3

pygame.init()
font1 = pygame.font.SysFont(None, 50)
WHITE = (255, 255, 255)
GREEN = (77, 204, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def buildText(board, i, j):
    if board[j][i] == "0":
        text = font1.render(" ", True, BLUE)
    else:
        text = font1.render(board[j][i], True, BLUE)
    textRect = text.get_rect()
    textRect.centerx = i * 100 + 75
    textRect.centery = j * 100 + 180
    return text, textRect


def showText(board):
    for i in range(4):
        for j in range(4):
            screen.blit(buildText(board, i, j)[0], buildText(board, i, j)[1])


def game_over():
    label = font1.render("GAME OVER", True, RED)
    screen.blit(label, (120, 70))
    event = pygame.event.wait()
    quitWindow(event)


def win():
    screen.fill(WHITE)
    label = font1.render("You WIN!!", True, RED)
    screen.blit(label, (120, 70))
    event = pygame.event.wait()
    quitWindow(event)


def quitWindow(event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    running = True
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Мир-головоломок')
    level = 0
    while running:
        if level == 0:
            window = MainWindow(screen)
            login_text = ''
            password = ''
            window.drawing()
        elif level == 0.1 and f:
            lp = True
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
            Key_J = KeyBord('J', (100, 600), screen)
            Key_J.draw()
            Key_K = KeyBord('K', (150, 600), screen)
            Key_K.draw()
            Key_L = KeyBord('L', (200, 600), screen)
            Key_L.draw()
            Key_M = KeyBord('M', (250, 600), screen)
            Key_M.draw()
            Key_N = KeyBord('N', (300, 600), screen)
            Key_N.draw()
            Key_O = KeyBord('O', (350, 600), screen)
            Key_O.draw()
            Key_P = KeyBord('P', (400, 600), screen)
            Key_P.draw()
            Key_Q = KeyBord('Q', (450, 600), screen)
            Key_Q.draw()
            Key_R = KeyBord('R', (500, 600), screen)
            Key_R.draw()
            Key_S = KeyBord('S', (125, 650), screen)
            Key_S.draw()
            Key_T = KeyBord('T', (175, 650), screen)
            Key_T.draw()
            Key_U = KeyBord('U', (225, 650), screen)
            Key_U.draw()
            Key_V = KeyBord('V', (275, 650), screen)
            Key_V.draw()
            Key_W = KeyBord('W', (325, 650), screen)
            Key_W.draw()
            Key_X = KeyBord('X', (375, 650), screen)
            Key_X.draw()
            Key_Y = KeyBord('Y', (425, 650), screen)
            Key_Y.draw()
            Key_Z = KeyBord('Z', (475, 650), screen)
            Key_Z.draw()
            pygame.display.flip()
            f = False
        elif level == 0.2 and f:
            lp = True
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
            Key_J = KeyBord('J', (100, 600), screen)
            Key_J.draw()
            Key_K = KeyBord('K', (150, 600), screen)
            Key_K.draw()
            Key_L = KeyBord('L', (200, 600), screen)
            Key_L.draw()
            Key_M = KeyBord('M', (250, 600), screen)
            Key_M.draw()
            Key_N = KeyBord('N', (300, 600), screen)
            Key_N.draw()
            Key_O = KeyBord('O', (350, 600), screen)
            Key_O.draw()
            Key_P = KeyBord('P', (400, 600), screen)
            Key_P.draw()
            Key_Q = KeyBord('Q', (450, 600), screen)
            Key_Q.draw()
            Key_R = KeyBord('R', (500, 600), screen)
            Key_R.draw()
            Key_S = KeyBord('S', (125, 650), screen)
            Key_S.draw()
            Key_T = KeyBord('T', (175, 650), screen)
            Key_T.draw()
            Key_U = KeyBord('U', (225, 650), screen)
            Key_U.draw()
            Key_V = KeyBord('V', (275, 650), screen)
            Key_V.draw()
            Key_W = KeyBord('W', (325, 650), screen)
            Key_W.draw()
            Key_X = KeyBord('X', (375, 650), screen)
            Key_X.draw()
            Key_Y = KeyBord('Y', (425, 650), screen)
            Key_Y.draw()
            Key_Z = KeyBord('Z', (475, 650), screen)
            Key_Z.draw()
            pygame.display.flip()
            f = False
        elif level == 1:
            window = level1(screen)
            window.drawing()
        elif level == 1.1 and f:
            all_sprites = pygame.sprite.Group()
            sprite = pygame.sprite.Sprite()
            window = level11(screen, all_sprites)
            window.drawing()
            f = False
        elif level == 2:
            cur.execute("UPDATE login SET level = ? WHERE login == ?", (level, login))
            con.commit()
            window = level2(screen)
            window.drawing()
        elif level == 2.1:
            blocks = []
            if f:
                board = init_board()
                f = False
            for i in range(4):
                for j in range(4):
                    blocks.append([pygame.Rect((i * 100) + 30, (j * 100) + 135, 90, 90), WHITE])
            screen.fill(WHITE)
            header = font1.render("2048", True, BLUE)
            screen.blit(header, (180, 30))
            pygame.draw.rect(screen, GREEN, pygame.Rect(20, 125, 410, 410))
            for block in blocks:
                pygame.draw.rect(screen, block[1], block[0])
            showText(board)
            if checkLose(board):
                game_over()
                time.sleep(3.5)
                f = True
            elif checkWin(board):
                win()
                time.sleep(3.5)
                level = 3
            pygame.display.update()
            time.sleep(0.2)
        elif level == 3:
            cur.execute("UPDATE login SET level = ? WHERE login == ?", (level, login))
            con.commit()
            window = level3(screen)
            window.drawing()
        elif level == 3.1:
            screen.fill((130, 255, 220))
            pygame.display.flip()
        elif level == 4:
            cur.execute("UPDATE login SET level = ? WHERE login == ?", (level, login))
            con.commit()
            window = level4(screen)
            window.drawing()
        elif level == 4.1 and f:
            screen.fill((0, 0, 0))
            board = Xitori(1)
            board.set_view(200, 200, 100)
            board.render(screen)
            pygame.display.flip()
            f = False
        elif level == 4.2 and f:
            screen.fill((0, 0, 0))
            board = Xitori(2)
            board.set_view(180, 180, 100)
            board.render(screen)
            pygame.display.flip()
            f = False
        elif level == 4.3 and f:
            screen.fill((0, 0, 0))
            board = Xitori(3)
            board.set_view(150, 150, 100)
            board.render(screen)
            pygame.display.flip()
            f = False
        elif level == 5:
            cur.execute("UPDATE login SET level = ? WHERE login == ?", (level, login))
            con.commit()
            window = level5(screen)
            window.drawing()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level == 0 and window.get_click(event.pos) != None:
                    level = window.get_click(event.pos)
                    f = True
                    a = True
                elif level == 0.2:
                    if len(login_text) <= 12 and lp or len(login_text) <= 8 and not lp and a:
                        pygame.draw.rect(screen, (53, 10, 26), (50, 450, 450, 75))
                        if Key_A.click(event.pos) != None:
                            letter = Key_A.click(event.pos)
                            login_text += letter
                        elif Key_B.click(event.pos) != None:
                            letter = Key_B.click(event.pos)
                            login_text += letter
                        elif Key_C.click(event.pos) != None:
                            letter = Key_C.click(event.pos)
                            login_text += letter
                        elif Key_D.click(event.pos) != None:
                            letter = Key_D.click(event.pos)
                            login_text += letter
                        elif Key_E.click(event.pos) != None:
                            letter = Key_E.click(event.pos)
                            login_text += letter
                        elif Key_F.click(event.pos) != None:
                            letter = Key_F.click(event.pos)
                            login_text += letter
                        elif Key_G.click(event.pos) != None:
                            letter = Key_G.click(event.pos)
                            login_text += letter
                        elif Key_H.click(event.pos) != None:
                            letter = Key_H.click(event.pos)
                            login_text += letter
                        elif Key_I.click(event.pos) != None:
                            letter = Key_I.click(event.pos)
                            login_text += letter
                        # Второй ряд
                        elif Key_J.click(event.pos) != None:
                            letter = Key_J.click(event.pos)
                            login_text += letter
                        elif Key_K.click(event.pos) != None:
                            letter = Key_K.click(event.pos)
                            login_text += letter
                        elif Key_L.click(event.pos) != None:
                            letter = Key_L.click(event.pos)
                            login_text += letter
                        elif Key_M.click(event.pos) != None:
                            letter = Key_M.click(event.pos)
                            login_text += letter
                        elif Key_N.click(event.pos) != None:
                            letter = Key_N.click(event.pos)
                            login_text += letter
                        elif Key_O.click(event.pos) != None:
                            letter = Key_O.click(event.pos)
                            login_text += letter
                        elif Key_P.click(event.pos) != None:
                            letter = Key_P.click(event.pos)
                            login_text += letter
                        elif Key_Q.click(event.pos) != None:
                            letter = Key_Q.click(event.pos)
                            login_text += letter
                        elif Key_R.click(event.pos) != None:
                            letter = Key_R.click(event.pos)
                            login_text += letter
                        # Третий ряд
                        elif Key_S.click(event.pos) != None:
                            letter = Key_S.click(event.pos)
                            login_text += letter
                        elif Key_T.click(event.pos) != None:
                            letter = Key_T.click(event.pos)
                            login_text += letter
                        elif Key_U.click(event.pos) != None:
                            letter = Key_U.click(event.pos)
                            login_text += letter
                        elif Key_V.click(event.pos) != None:
                            letter = Key_V.click(event.pos)
                            login_text += letter
                        elif Key_W.click(event.pos) != None:
                            letter = Key_W.click(event.pos)
                            login_text += letter
                        elif Key_X.click(event.pos) != None:
                            letter = Key_X.click(event.pos)
                            login_text += letter
                        elif Key_Y.click(event.pos) != None:
                            letter = Key_Y.click(event.pos)
                            login_text += letter
                        elif Key_Z.click(event.pos) != None:
                            letter = Key_Z.click(event.pos)
                            login_text += letter
                    if window.is_button(event.pos) == 0:
                        level = window.is_button(event.pos)
                    elif window.is_button(event.pos) == 100:
                        login_text = ''
                        lp = True
                        pygame.draw.rect(screen, (53, 10, 26), (400, 100, 300, 50))
                        pygame.draw.rect(screen, (53, 10, 26), (450, 200, 300, 50))
                        pygame.display.flip()
                    elif window.is_button(event.pos) == 150:
                        login = login_text
                        login_text = ''
                        pygame.display.flip()
                        lp = False
                    elif window.is_button(event.pos) == 200:
                        login_text = ''
                        pygame.draw.rect(screen, (53, 10, 26), (450, 200, 300, 50))
                        pygame.display.flip()
                    elif window.is_button(event.pos) == 250:
                        password = login_text
                        if password != '' and login != '' and len(password) >= 4:
                            con = sqlite3.connect("data/members.db")
                            cur = con.cursor()
                            result = cur.execute("""SELECT * FROM login
                                        WHERE login = ?""", (login,)).fetchall()
                            if not bool(result):
                                show_text(screen, 'Регистрация прошла успешно', 'comicsansms', 40, (204, 204, 204), (50, 450))
                                a = False
                                cur.execute('''INSERT INTO login VALUES (?, ?, ?)''', (login, password, 1))
                                con.commit()
                            else:
                                show_text(screen, 'Такой логин уже есть', 'comicsansms', 40, (204, 204, 204), (50, 450))
                                pygame.draw.rect(screen, (53, 10, 26), (400, 100, 300, 50))
                                pygame.draw.rect(screen, (53, 10, 26), (450, 200, 300, 50))
                                login_text = ''
                                lp = True
                        elif password == '' or len(password) < 3:
                            show_text(screen, 'Недопустимый пароль', 'comicsansms', 40, (204, 204, 204), (50, 450))
                            pygame.draw.rect(screen, (53, 10, 26), (400, 100, 300, 50))
                            pygame.draw.rect(screen, (53, 10, 26), (450, 200, 300, 50))
                            login_text = ''
                            lp = True
                        elif login == '' or bool(result):
                            show_text(screen, 'Недопустимый логин', 'comicsansms', 40, (204, 204, 204), (50, 450))
                            pygame.draw.rect(screen, (53, 10, 26), (400, 100, 300, 50))
                            pygame.draw.rect(screen, (53, 10, 26), (450, 200, 300, 50))
                            login_text = ''
                            lp = True
                        pygame.display.flip()
                    if lp:
                        show_text(screen, login_text, 'comicsansms', 30, (204, 204, 204), (400, 100))
                    else:
                        show_text(screen, login_text, 'comicsansms', 30, (204, 204, 204), (450, 200))
                    pygame.display.flip()
                elif level == 0.1:
                    if len(login_text) <= 12 and lp or len(login_text) <= 8 and not lp and a:
                        pygame.draw.rect(screen, (53, 10, 26), (50, 450, 500, 75))
                        if Key_A.click(event.pos) != None:
                            letter = Key_A.click(event.pos)
                            login_text += letter
                        elif Key_B.click(event.pos) != None:
                            letter = Key_B.click(event.pos)
                            login_text += letter
                        elif Key_C.click(event.pos) != None:
                            letter = Key_C.click(event.pos)
                            login_text += letter
                        elif Key_D.click(event.pos) != None:
                            letter = Key_D.click(event.pos)
                            login_text += letter
                        elif Key_E.click(event.pos) != None:
                            letter = Key_E.click(event.pos)
                            login_text += letter
                        elif Key_F.click(event.pos) != None:
                            letter = Key_F.click(event.pos)
                            login_text += letter
                        elif Key_G.click(event.pos) != None:
                            letter = Key_G.click(event.pos)
                            login_text += letter
                        elif Key_H.click(event.pos) != None:
                            letter = Key_H.click(event.pos)
                            login_text += letter
                        elif Key_I.click(event.pos) != None:
                            letter = Key_I.click(event.pos)
                            login_text += letter
                        # Второй ряд
                        elif Key_J.click(event.pos) != None:
                            letter = Key_J.click(event.pos)
                            login_text += letter
                        elif Key_K.click(event.pos) != None:
                            letter = Key_K.click(event.pos)
                            login_text += letter
                        elif Key_L.click(event.pos) != None:
                            letter = Key_L.click(event.pos)
                            login_text += letter
                        elif Key_M.click(event.pos) != None:
                            letter = Key_M.click(event.pos)
                            login_text += letter
                        elif Key_N.click(event.pos) != None:
                            letter = Key_N.click(event.pos)
                            login_text += letter
                        elif Key_O.click(event.pos) != None:
                            letter = Key_O.click(event.pos)
                            login_text += letter
                        elif Key_P.click(event.pos) != None:
                            letter = Key_P.click(event.pos)
                            login_text += letter
                        elif Key_Q.click(event.pos) != None:
                            letter = Key_Q.click(event.pos)
                            login_text += letter
                        elif Key_R.click(event.pos) != None:
                            letter = Key_R.click(event.pos)
                            login_text += letter
                        # Третий ряд
                        elif Key_S.click(event.pos) != None:
                            letter = Key_S.click(event.pos)
                            login_text += letter
                        elif Key_T.click(event.pos) != None:
                            letter = Key_T.click(event.pos)
                            login_text += letter
                        elif Key_U.click(event.pos) != None:
                            letter = Key_U.click(event.pos)
                            login_text += letter
                        elif Key_V.click(event.pos) != None:
                            letter = Key_V.click(event.pos)
                            login_text += letter
                        elif Key_W.click(event.pos) != None:
                            letter = Key_W.click(event.pos)
                            login_text += letter
                        elif Key_X.click(event.pos) != None:
                            letter = Key_X.click(event.pos)
                            login_text += letter
                        elif Key_Y.click(event.pos) != None:
                            letter = Key_Y.click(event.pos)
                            login_text += letter
                        elif Key_Z.click(event.pos) != None:
                            letter = Key_Z.click(event.pos)
                            login_text += letter
                    if window.is_button(event.pos) == 0:
                        level = window.is_button(event.pos)
                    elif window.is_button(event.pos) == 100:
                        login_text = ''
                        lp = True
                        pygame.draw.rect(screen, (53, 10, 26), (400, 100, 300, 50))
                        pygame.draw.rect(screen, (53, 10, 26), (450, 200, 300, 50))
                        pygame.display.flip()
                    elif window.is_button(event.pos) == 150:
                        login = login_text
                        login_text = ''
                        pygame.display.flip()
                        lp = False
                    elif window.is_button(event.pos) == 200:
                        login_text = ''
                        pygame.draw.rect(screen, (53, 10, 26), (450, 200, 300, 50))
                        pygame.display.flip()
                    elif window.is_button(event.pos) == 250:
                        password = login_text
                        if password != '' and login != '' and len(password) >= 4:
                            con = sqlite3.connect("data/members.db")
                            cur = con.cursor()
                            result = cur.execute("""SELECT * FROM login
                                        WHERE login = ?""", (login,)).fetchall()
                            if not bool(result):
                                show_text(screen, 'Такого логина не существует', 'comicsansms', 40, (204, 204, 204), (50, 450))
                                pygame.draw.rect(screen, (53, 10, 26), (400, 100, 300, 50))
                                pygame.draw.rect(screen, (53, 10, 26), (450, 200, 300, 50))
                                login_text = ''
                                lp = True
                            else:
                                if result[0][1] == password:
                                    level = result[0][2]
                                else:
                                    show_text(screen, 'Неправильный пароль', 'comicsansms', 40, (204, 204, 204), (50, 450))
                                    pygame.draw.rect(screen, (53, 10, 26), (400, 100, 300, 50))
                                    pygame.draw.rect(screen, (53, 10, 26), (450, 200, 300, 50))
                                    login_text = ''
                                    lp = True
                        elif password == '' or len(password) < 3:
                            show_text(screen, 'Недопустимый пароль', 'comicsansms', 40, (204, 204, 204), (50, 450))
                            pygame.draw.rect(screen, (53, 10, 26), (400, 100, 300, 50))
                            pygame.draw.rect(screen, (53, 10, 26), (450, 200, 300, 50))
                            login_text = ''
                            lp = True
                        elif login == '' or bool(result):
                            show_text(screen, 'Недопустимый логин', 'comicsansms', 40, (204, 204, 204), (50, 450))
                            pygame.draw.rect(screen, (53, 10, 26), (400, 100, 300, 50))
                            pygame.draw.rect(screen, (53, 10, 26), (450, 200, 300, 50))
                            login_text = ''
                            lp = True
                        pygame.display.flip()
                    if lp:
                        show_text(screen, login_text, 'comicsansms', 30, (204, 204, 204), (400, 100))
                    else:
                        show_text(screen, login_text, 'comicsansms', 30, (204, 204, 204), (450, 200))
                    pygame.display.flip()
                elif level == 1:
                    if window.get_click(event.pos) == 1:
                        level = 1.1
                        f = True
                elif level == 1.1:
                    all_sprites.update(event)
                    all_sprites.draw(screen)
                    pygame.display.flip()
                elif level == 2:
                    if window.get_click(event.pos) == 1:
                        level = 2.1
                        f = True
                elif level == 3:
                    if window.get_click(event.pos) == 1:
                        level = 3.1
                elif level == 4:
                    if window.get_click(event.pos) == 1:
                        level = 4.1
                        f = True
                elif level == 4.1:
                    board.get_click(event.pos)
                    board.render(screen)
                    if board.is_win() == 1:
                        level = 4.2
                        f = True
                    pygame.display.flip()
                elif level == 4.2:
                    board.get_click(event.pos)
                    board.render(screen)
                    if board.is_win() == 1:
                        level = 4.3
                        f = True
                    pygame.display.flip()
                elif level == 4.3:
                    board.get_click(event.pos)
                    board.render(screen)
                    if board.is_win() == 1:
                        level = 5
                        f = True
                    pygame.display.flip()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    board = main(board, "u")
                if event.key == K_DOWN:
                    board = main(board, "d")
                if event.key == K_LEFT:
                    board = main(board, "l")
                if event.key == K_RIGHT:
                    board = main(board, "r")
    pygame.quit()

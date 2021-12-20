import pygame
from mod import show_text  # холст, текаст, шрифт, размер, цвет (кортедж), позиция (кортедж)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    show_text(screen, "Hello, world", None, 50, (230, 116, 99), (100, 100))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

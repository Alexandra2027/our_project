import pygame


def show_text(screen, text, fontname, size, color, pos):  # функция для вывода текста
    font = pygame.font.SysFont(fontname, size)
    t = font.render(f"{text}", True, color)
    screen.blit(t, pos)

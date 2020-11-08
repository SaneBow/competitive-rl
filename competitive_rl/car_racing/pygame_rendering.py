import pygame


def pygame_draw(screen, color, path):
    pygame.draw.polygon(screen, color, path)


def vertical_ind(screen, x, y, width, height, value, color):
    pygame.draw.rect(screen, color, (x, y, width, height * value))


def horiz_ind(screen, x, y, width, height, value, color):
    pygame.draw.rect(screen, color, (x, y, width * value, height))


def draw_text(screen, text, x, y, scale=30, color=(255, 255, 255)):
    if scale not in _font_registry:
        myfont = pygame.font.SysFont('Comic Sans MS', scale)
        _font_registry[scale] = myfont
    else:
        myfont = _font_registry[scale]
    textsurface = myfont.render(text, False, color)
    screen.blit(textsurface, (x, y))


def draw_dot(screen, color, center, radius):
    pygame.draw.circle(screen, color, center, radius)


_font_registry = dict()

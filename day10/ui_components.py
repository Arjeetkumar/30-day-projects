# ui_components.py
import pygame
from constants import COLOR_BTN, COLOR_TEXT

pygame.font.init()
FONT = pygame.font.SysFont("Arial", 16)
BIG = pygame.font.SysFont("Arial", 20, bold=True)

class Button:
    def __init__(self, rect, text, color=COLOR_BTN, text_color=(0,0,0)):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color = color
        self.text_color = text_color

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, border_radius=8)
        txt = FONT.render(self.text, True, self.text_color)
        tw, th = txt.get_size()
        surf.blit(txt, (self.rect.centerx - tw//2, self.rect.centery - th//2))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

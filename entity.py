import pygame

class Dice:
    def __init__(self, surface):
        self.surface = surface
        self.rect = pygame.Rect(0, 0, 64, 64)

    def draw():
        pygame.draw.rect(self.surface, (255, 255, 255), self.rect)

class Entity:
    def __init__(self, surface, x, y, width, height):
        self.surface = surface
        self.rect = pygame.Rect(x, y, width, height)

    def draw():
        pygame.draw.rect(self.surface, (255, 0, 0), self.rect)

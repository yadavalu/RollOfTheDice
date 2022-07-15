import pygame

class Entity:
    def __init__(self, surface, x, y, width, height):
        self.surface = surface
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, colour=(255, 0, 0)):
        pygame.draw.rect(self.surface, colour, self.rect)

class Dice(Entity):
    def __init__(self, surface, x, y):
        super().__init__(surface, x, y, 64, 64)

    def draw(self):
        super().draw(colour=(255, 255, 255))
        
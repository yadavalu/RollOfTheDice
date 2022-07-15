import pygame
pygame.init()

from entity import Dice

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Roll of the Dice")

dice = Dice(screen, 0, 0)


while 1:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            pass

    dice.draw()

    pygame.display.update()

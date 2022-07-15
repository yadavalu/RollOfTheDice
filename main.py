import pygame
pygame.init()


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Roll of the Dice")


while 1:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            pass

    pygame.display.update()

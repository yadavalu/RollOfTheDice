import pygame
pygame.init()

from entity import Player, Dice

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Roll of the Dice")

player = Player(screen, 0, 0, "assets/viking/viking2.png", [[32, 32], [3, 3], [7, 6, 5, 9, 9, 9]])
dice = Dice(screen, 0, 0, "assets/red.png", "assets/symbols.png", [[22, 22], [3, 3]])

clock = pygame.time.Clock()

while 1:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()

    player.update(keys)
    player.draw()

    dice.update(keys)
    dice.draw()

    pygame.display.update()   
    

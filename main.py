import pygame
import settings as set
import algorithm

runGame = True
while runGame:
    for event in pygame.event.get():
        # Для закрытия программы
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        set.grid()
        set.points()
        #algorithm.rgb_lines()
        algorithm.labirinth()

        pygame.display.update()
pygame.quit()
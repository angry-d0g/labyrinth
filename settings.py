import pygame
#import algorithm

# Окно программы
pygame.init()
windowX = 300
windowY = 300
delay = 70
dis = pygame.display.set_mode((windowX, windowY))
pygame.display.set_caption('Лабиринт')



#сетка
    # Размеры одной клетки змейки
sizeX, sizeY = (20, 20)  # ТОЛЬКО ЧЕТНЫЕ ЧИСЛА!

countX = windowX // sizeX - 1
countY = windowY // sizeY - 1

gray = (50, 50, 50)
red = (100, 0, 0)
yellow = (100, 100, 0)
green = (0, 100, 0)

def grid():
    for i in range(0, windowX, sizeX):
        pygame.draw.aaline(dis, gray, [i, 0], [i, windowY])
    for j in range(0, windowY, sizeY):
        pygame.draw.aaline(dis, gray, [0, j], [windowX, j])

def points():
    for i in range(20, windowX, 20):
        for j in range(20, windowY, 20):
            pygame.draw.circle(dis, gray, [i, j], 4)


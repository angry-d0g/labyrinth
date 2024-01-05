#import numpy as np
import pygame
import settings as set
import random

# n = 4 * set.countY * set.countX
# arr = np.arange(n).reshape(set.countX * set.countY, 4)
# right_down = [[1,10]]*1000
# for i in range(set.countX * set.countY):
#     #for k in range(4):
#
#     arr[i][3] = right_down[i-1][0]
#
#     arr[i][0] = right_down[i - 14][1]
#
#     arr[i][1] = random.randint(1, 12)
#     arr[i][2] = random.randint(1, 12)
#     right_down[i][0],right_down[i][1] = arr[i][1], arr[i][2]
# print(arr)
arr = []
for i in range(set.countX * set.countY):
    if i <= 13:
        arr.append([random.randint(1, 12), i, i + 1])

    if i > 13 and i % 14 != 0:
        arr.append([random.randint(1, 12), i, i - 14])
        arr.append([random.randint(1, 12), i, i + 1])

#вывод массива
# for i in range(len(arr)):
#     print(arr[i], end=' ')
#     if i % 14 == 0 and i != 0:
#         print()
# print(len(arr))


def chek_color(c):
    if c <= 4:
        return set.green
    elif c <= 8:
        return set.yellow
    else:
        return set.red


# def rgb_lines():
#     y = 0
#     for i in range(len(arr)):
#
#         if i % 14 == 0:
#             y += 1
#         if i % 2 == 0 or i < 14:
#             pygame.draw.line(set.dis, chek_color(arr[i][0]), [(i + 1) * 20, y * 20], [(i + 1) * 20 + 20, y * 20], 3)
#         else:
#             pygame.draw.line(set.dis, chek_color(arr[i][0]), [(i + 1) * 20, y * 20], [(i + 1) * 20, y * 20 - 20], 3)
#             print(123)


# -------------------------------------------------
# Алгоритм Краскала поиска минимального остова графа
# -------------------------------------------------
def kruskal(R):
    # список ребер графа (длина, вершина 1, вершина 2)

    Rs = sorted(R, key=lambda x: x[0])
    U = []  # список соединенных вершин
    D = {}  # словарь списка изолированных групп вершин
    T = []  # список ребер остова

    for r in Rs:
        if r[1] not in U or r[2] not in U:  # проверка для исключения циклов в остове
            if r[1] not in U and r[2] not in U:  # если обе вершины не соединены, то
                D[r[1]] = [r[1], r[2]]  # формируем в словаре ключ с номерами вершин
                D[r[2]] = D[r[1]]  # и связываем их с одним и тем же списком вершин
            else:  # иначе
                if not D.get(r[1]):  # если в словаре нет первой вершины, то
                    D[r[2]].append(r[1])  # добавляем в список первую вершину
                    D[r[1]] = D[r[2]]  # и добавляем ключ с номером первой вершины
                else:
                    D[r[1]].append(r[2])  # иначе, все то же самое делаем со второй вершиной
                    D[r[2]] = D[r[1]]

            T.append(r)  # добавляем ребро в остов
            U.append(r[1])  # добавляем вершины в множество U
            U.append(r[2])

    for r in Rs:  # проходим по ребрам второй раз и объединяем разрозненные группы вершин
        if r[2] not in D[r[1]]:  # если вершины принадлежат разным группам, то объединяем
            T.append(r)  # добавляем ребро в остов

            # pygame.draw.line(set.dis, (0,0,0), [i, j], [i + 20, j], 4)

            gr1 = D[r[1]]
            D[r[1]] += D[r[2]]  # объединем списки двух групп вершин
            D[r[2]] += gr1
            return T #НЕ ДОБАВЛЯЕТ ОТДЕЛЬНЫЕ ГРУППЫ В ОСТОВ, НО ТОЖЕ КРАСИВО =)
    #return T #а вот это уже похоже на остов
#pygame.draw.line(set.dis, (255, 255, 255), [20,20], [40,20], 4)

def labirinth():
    lab = kruskal(arr)
    print(lab)
    r = 20
    c=20
    for i in range(len(lab)):
        if (lab[i][1]+1) % 14 != 0 or lab[i][1] ==0:
            pygame.draw.line(set.dis, chek_color(lab[i][0]), chek_coords(lab[i][1]), chek_coords(lab[i][2]), 10)
        # if i%14==0 and i !=0:
        #     r+=20
        #     c=0
        # c+=20

def chek_coords(n):
    x= n%14*20+20
    y=n//14*20 + 20
    return [x,y]
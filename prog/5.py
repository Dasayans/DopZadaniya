import pygame
from itertools import product
from time import sleep
import numpy as np

g = np.random.random_integers(1, 7)
print(g)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Гири")
font = pygame.font.SysFont(name='arial', size=20)
font2 = pygame.font.SysFont(name='arial', size=50)
r1 = pygame.Rect(450, 895, 100, 105)
girya = pygame.image.load('5219346(2).png')
BigGirya = pygame.image.load('5219346.png')
krest = pygame.image.load('free-png.ru-388.png')
nacl = 0
sum = sum(range(8))


def startpage():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, r1, 0)
    for i in range(50, 650, 90):
        screen.blit(girya, (30, i))
        screen.blit(girya, (1000 - 130, i))
        font_surf = font.render(str(int((i - 50) / 90) + 1), True, (0, 0, 0))
        screen.blit(font_surf, (75, i + 50))
        font_surf = font.render('?', True, (0, 0, 0))
        screen.blit(font_surf, (1000 - 85, i + 50))
    pygame.draw.polygon(screen, BLACK,
                        [[900, 900 + nacl], [900, 885 + nacl], [100, 885 - nacl], [100, 900 - nacl], ])


def makekrest(i):
    screen.blit(krest, (30, (i - 1) * 90 + 50))
    screen.blit(krest, (1000 - 130, 50))


def disprez(s):
    screen.blit(BigGirya, (250, 200))
    font_surf2 = font2.render(str(s), True, (0, 0, 0))
    screen.blit(font_surf2, (500, 500))
    pygame.display.flip()
    sleep(4)
    pygame.quit()


startpage()
pygame.display.flip()
sleep(5)
s = 4
if (sum - g < sum - s):
    nacl = -20
    s = 6
elif (sum - g > sum - s):
    nacl = 20
    s = 2
startpage()
makekrest(4)
pygame.display.flip()
sleep(4)
if (nacl == 0):
    disprez(s)
s1 = s
if (sum - g < sum - s):
    nacl = -20
    s = s + 1
elif (sum - g > sum - s):
    nacl = 20
    s = s - 1
else:
    nacl = 0
startpage()
makekrest(s1)
pygame.display.flip()
sleep(4)
disprez(s)
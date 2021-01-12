from typing import List

import pygame
import segment

from pygame.locals import *
import pygame.math as pm
import math


pygame.init()

WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
FPS = 60

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Kinematics Test")

clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Comic Sans MS', 16)
is_running = True

seg = segment.Segment(WIDTH//2, HEIGHT, 70, 0, 0)
arm: List[segment.Segment] = [seg]
for i in range(1, 6):
 temp_seg = arm[i-1]
 arm.append(temp_seg.generate_parent(temp_seg, 70, 0, i))



while is_running:
    screen.fill(pygame.Color("cornflowerblue"))
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            is_running = False

    for s in reversed(arm):
        if s.parent == None:
            mx, my = pygame.mouse.get_pos()
            s.follow(mx, my)

        else:
            s.follow(s.parent.a.x, s.parent.a.y)
        s.update()


    for i in range(len(arm)-1):
        s = arm[i]
        if i == 0:
            s.return_to_base()
        else:
            s.a = arm[i-1].b
        s.update()
        s.draw(screen)

    s = arm[len(arm)-1]
    print(s.b)
    print(pygame.mouse.get_pos())



    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

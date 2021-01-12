import pygame
import math
from pygame import math as pm


class Segment:
    def __init__(self, x: int, y: int, length: int, angle: float, id: int):

        self.myfont = pygame.font.SysFont('Comic Sans MS', 16)

        self.angle = angle
        self.length = length
        self.a = pm.Vector2(x, y)
        self.b = pm.Vector2(0, 0)
        self.calculateB()
        self.id = id
        self.parent = None
        if id == 0:
            self.base_x = x
            self.base_y = y
        else:
            self.base_x = None
            self.base_y = None

    def generate_parent(self, child_segment, length: int, angle: int, id: int):
        s = Segment(child_segment.b.x, child_segment.b.y, length, angle, id)
        child_segment.parent = s
        s.follow(child_segment.a.x, child_segment.a.y)

        return s

    def calculateB(self):
        dx = (self.a.x + math.cos(math.radians(self.angle)) * self.length)
        dy = (self.a.y + math.sin(math.radians(self.angle)) * self.length)
        #self.b = pm.Vector2(dx, dy)
        self.b.update(dx, dy)

    def follow(self, tx: int, ty: int):
        target = pm.Vector2(tx, ty)
        direction = target - self.a
        self.angle = pm.Vector2().angle_to(direction)
        direction.normalize_ip()
        pm.Vector2.scale_to_length(direction, self.length)
        direction *= -1

        self.a = target + direction

    def return_to_base(self):
        if self.base_x is not None and self.base_y is not None:
            self.a = pm.Vector2(self.base_x, self.base_y)


    def update(self):
        self.calculateB()

    def draw(self, surf: pygame.Surface):
        pygame.draw.line(surf, pygame.Color("white"), self.a, self.b, 5)
        pygame.draw.circle(surf, pygame.Color("white"), self.a, 7, 1)
        pygame.draw.circle(surf, pygame.Color("yellow"), self.b, 4)
        textsurface = self.myfont.render(str(self.b), False, (0, 255, 0))
        surf.blit(textsurface, self.b)
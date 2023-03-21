import itertools
import random

import pygame

pygame.init()
window = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Brain Network Visualizer')

class Circle:
    def __init__(self, x, y, color, radius):
        self.pos = (x, y)
        self.x_boundary = (x - radius, x + radius)
        self.y_boundary = (y - radius, y + radius)
        self.boundary_color = (127,121,173)
        self.main_color = (46,52,64)
        self.radius = radius
        self.selected = False

    def recalc_boundary(self):
        self.x_boundary = (
            self.pos[0] - self.radius, self.pos[0] + self.radius
        )
        self.y_boundary = (
            self.pos[1] - self.radius, self.pos[1] + self.radius
        )

    def draw(self, window): 
        pygame.draw.circle(
            window, self.boundary_color,
            self.pos,
            self.radius
        )

        pygame.draw.circle(
            window, self.main_color,
            self.pos,
            self.radius-(self.radius*0.3)
        )

within = lambda x, low, high: low <= x <= high

circles = [Circle(random.randint(10, 690), random.randint(10, 490), 
                  (199, 146, 234), 10) for _ in range(7)]


# boilerplate from stackoverflow
# https://stackoverflow.com/questions/53132386/why-can-i-not-click-and-drag-circles-on-python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                for circle in circles:
                    if (
                        within(pos[0], *circle.x_boundary)
                        and within(pos[1], *circle.y_boundary)
                    ):
                        circle.selected = True

        elif event.type == pygame.MOUSEBUTTONUP:
            for circle in circles:
                circle.selected = False

    for circle in circles:
        if circle.selected:
            circle.pos = pygame.mouse.get_pos()
            circle.recalc_boundary()

    window.fill((236,239,244))

    for circle in circles:
        circle.draw(window)

    for c1, c2 in itertools.permutations(circles, 2): 
        pygame.draw.line(window,(46,52,64), c1.pos, c2.pos, width=2)

    pygame.display.update()
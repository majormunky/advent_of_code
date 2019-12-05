import os
import sys
import common
from common import Point, Line, Path, PathManager
# import pygame
# from Engine.Engine import Engine
# from Engine.Config import set_screensize, get_screenrect
# from Engine.DataManager import set_data, get_data


class PathTest:
    def __init__(self):
        self.path_list = get_data("path_list")
        self.path_manager = PathManager(self.path_list[0], self.path_list[1])
        # print(self.path_manager.get_image_size())
        self.screenrect = get_screenrect()
        self.image = None
        self.collisions = []
        self.x_offset = self.screenrect.width // 2
        self.y_offset = self.screenrect.height // 2
        self.render_paths()
        self.generate_collisions()
        self.render_collisions()
        self.take_screenshot()
        sys.exit(0)

    def render_collisions(self):
        print(self.collisions)
        for c in self.collisions:
            cx = c[0] + self.x_offset
            cy = c[1] + self.y_offset
            print(cx, cy)
            pygame.draw.rect(self.image, (100, 100, 100), (cx, cy, 1, 1))

    def generate_collisions(self):
        self.collisions = []
        for line in self.path_manager.path1.lines:
            for line2 in self.path_manager.path2.lines:
                result = line.collide_with(line2)
                if result and result not in self.collisions:
                    self.collisions.append(result)
        if [0, 0] in self.collisions:
            self.collisions.remove([0, 0])
        print(self.collisions)

    def take_screenshot(self):
        pygame.image.save(self.image, "screenshot.png")

    def render_paths(self):
        self.image = pygame.Surface(
            (
                self.screenrect.width, 
                self.screenrect.height
            ),
            pygame.SRCALPHA,
        )
        self.image.fill((20, 20, 20))
        hx = self.x_offset
        hy = self.y_offset

        for line in self.path_list[0].lines:
            pygame.draw.line(
                self.image, 
                (255, 0, 255), 
                (line.start.x + hx, line.start.y + hy), 
                (line.end.x + hx, line.end.y + hy), 
                1
            )

        for line in self.path_list[1].lines:
            pygame.draw.line(
                self.image, 
                (255, 255, 0), 
                (line.start.x + hx, line.start.y + hy), 
                (line.end.x + hx, line.end.y + hy), 
                1
            )        
        

    def draw(self, canvas):
        canvas.blit(self.image, (50, 50))

    def update(self, dt):
        pass

    def handle_event(self, event):
        pass


def generate_collisions(path1, path2):
    collisions = []
    for line in path1.lines:
        for line2 in path2.lines:
            result = line.collide_with(line2)
            if result and result not in collisions:
                collisions.append(result)
    if [0, 0] in collisions:
        collisions.remove([0, 0])
    return collisions


def part1():
    path_manager = PathManager("day3_data.txt")
    min_distance = path_manager.get_min_distance()
    return min_distance


def part2():
    """
    For part 2 we need to:
    1: Walk through each line for each path
    2: Check if that line has a collision
    3: Calculate the distance from the start of the path to the collision

    After we do that, we then need to:
    1: for each collsion, get the distance to it
    2: check the other path for that collision and get the distance to it
    3: find the combination that leads to the shortest path
    """
    return "No idea?!"


def main():
    print("Answer for part 1: {}".format(part1()))
    print("Answer for part 2: {}".format(part2()))


if __name__ == '__main__':
    main()

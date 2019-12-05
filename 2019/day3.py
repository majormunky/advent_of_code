import os
import sys
import common
from common import Point, Line
# import pygame
# from Engine.Engine import Engine
# from Engine.Config import set_screensize, get_screenrect
# from Engine.DataManager import set_data, get_data
            

class PathManager(object):
    def __init__(self, filename):
        self.path1 = None
        self.path2 = None
        self.collisions = []

        fp = os.path.join("data", filename)
        stuff = common.get_file_lines(fp)
        wires = {
            0: [[0, 0],],
            1: [[0, 0],]
        }
        paths = []

        for index, line in enumerate(stuff):
            path = Path()
            for item in line.split(","):
                spos = wires[index][-1]
                a_line, end_pos = self.create_line(item, spos)
                path.add_line(a_line)
                wires[index].append(end_pos)
            paths.append(path)
        
        self.path1 = paths[0]
        self.path2 = paths[1]
        self.generate_collisions()

    def create_line(self, command, start_pos):
        parts = list(command)
        direction = parts.pop(0)
        amount = int("".join(parts))
        if direction == "U":
            end_pos = [
                start_pos[0],
                start_pos[1] - (amount)
            ]
        elif direction == "D":
            end_pos = [
                start_pos[0],
                start_pos[1] + amount
            ]            
        elif direction == "L":
            end_pos = [
                start_pos[0] - amount,
                start_pos[1]
            ]
        elif direction == "R":
            end_pos = [
                start_pos[0] + amount,
                start_pos[1]
            ]
            
        line = Line(
            start_pos[0], 
            start_pos[1], 
            end_pos[0], 
            end_pos[1],
            command
        )
        return (line, end_pos)

    def generate_collisions(self):
        self.collisions = []
        for line in self.path1.lines:
            for line2 in self.path2.lines:
                result = line.collide_with(line2)
                if result and result not in self.collisions:
                    self.collisions.append(result)
        if [0, 0] in self.collisions:
            self.collisions.remove([0, 0])

    def get_collisions(self):
        return self.collisions

    def manhattan(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def get_min_distance(self):
        distances = {}
        for c in self.collisions:
            distances[c] = self.manhattan(c, [0, 0])
        
        min_distance = sys.maxsize
        
        for k, v in distances.items():
            if v < min_distance:
                min_distance = v
        return min_distance

    def get_distance_to_next_collision(self, path_num, collision_index):
        distance = 0
        start = [0, 0]
        cur_path = None
        if path_num == 1:
            cur_path = self.path1
        else:
            cur_path = self.path2

        for line in cur_path.lines:
            has_collision = False
            # check to see if this line has any collisions
            for c in self.collisions:
                if line.direction == "Vertical":
                    # just check for x
                    if c[0] == line.start.x:
                        print("Found collision")
                        has_collision = True
                else:
                    # check for y
                    if c[1] == line.start.y:
                        print("Found collision")
                        has_collision = True
                if has_collision:
                    # calculate the distance from the start of the line
                    # to the collision
                    distance += line.get_distance(c)
                else:
                    # just add the entire length of the line to the distance
                    distance += line.get_distance()



class Path(object):
    def __init__(self):
        self.lines = []
        self.min_x = sys.maxsize
        self.max_x = 0
        self.min_y = sys.maxsize
        self.max_y = 0
    
    def add_line(self, line):
        self.lines.append(line)
        if line.start.x < self.min_x:
            self.min_x = line.start.x
        if line.start.y < self.min_y:
            self.min_y = line.start.y
        if line.end.x > self.max_x:
            self.max_x = line.end.x
        if line.end.y > self.max_y:
            self.max_y = line.end.y
    
    def print(self):
        for line in self.lines:
            print(line)


def create_line(item, start_pos):
    parts = list(item)
    direction = parts.pop(0)
    amount = int("".join(parts))
    if direction == "U":
        end_pos = [
            start_pos[0],
            start_pos[1] - (amount)
        ]
    elif direction == "D":
        end_pos = [
            start_pos[0],
            start_pos[1] + amount
        ]            
    elif direction == "L":
        end_pos = [
            start_pos[0] - amount,
            start_pos[1]
        ]
    elif direction == "R":
        end_pos = [
            start_pos[0] + amount,
            start_pos[1]
        ]
        
    line = Line(
        start_pos[0], 
        start_pos[1], 
        end_pos[0], 
        end_pos[1],
        item
    )
    return (line, end_pos)


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

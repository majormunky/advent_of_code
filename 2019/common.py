import os
import sys


DATA_DIR = os.path.join(".", "data")


def get_file_lines(filepath):
    lines = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "<{}, {}>".format(self.x, self.y)


class Line(object):
    def __init__(self, start_x, start_y, end_x, end_y, cmd):
        self.start = Point(start_x, start_y)
        self.end = Point(end_x, end_y)
        self.cmd = cmd
        self.direction = None
        if self.start.x == self.end.x:
            self.direction = "Vertical"
            if self.start.y > self.end.y:
                self.start, self.end = self.end, self.start
        elif self.start.y == self.end.y:
            self.direction = "Horizontal"
            if self.start.x > self.end.x:
                self.start, self.end = self.end, self.start
        else:  
            print("Detected diagonal line")
            self.direction = "BROKE"
    
    def __str__(self):
        return "{} Line ({}) - Start: {}, {} | End: {}, {}".format(
            self.direction,
            self.cmd,
            self.start.x,
            self.start.y,
            self.end.x,
            self.end.y
        )

    def get_length(self, point=None):
        """
        Returns the length of the line
        If point is passed in, we return the length of the line
        between the start of the line and the point
        """
        if self.direction == "Vertical":
            if point:
                return point[1] - self.start.y
            else:
                return self.end.y - self.start.y
        elif self.direction == "Horizontal":
            if point:
                return point[0] - self.start.x
            else:
                return self.end.x - self.start.x
    
    def collide_with(self, other):
        if self.direction == other.direction:
            return False

        # if the start of our line is to the left of the other line
        if self.start.x <= other.end.x:
            # and the end of our line is to the right of the other line
            if self.end.x >= other.start.x:
                # and the start of our line is above our other line
                if self.start.y <= other.end.y:
                    # and the end of our line is below the other line
                    if self.end.y >= other.start.y:
                        if self.direction == "Vertical":
                            return (self.start.x, other.start.y)
                        else:
                            return (other.start.x, self.start.y)
        return False


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


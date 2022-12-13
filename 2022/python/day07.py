from common import get_file_contents


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.directories = {}

    def add_file(self, file_obj):
        self.files.append(file_obj)

    def add_dir(self, dir_name):
        new_dir = Directory(dir_name, self)
        self.directories[dir_name] = new_dir

    def get_dir(self, dir_name):
        result = self.directories.get(dir_name, None)
        return result

    def get_parent_dir(self):
        return self.parent

    def get_size(self):
        size = 0

        for file in self.files:
            size += file.size

        for directory_name, directory in self.directories.items():
            size += directory.get_size()
        return size

    def print_file_listing(self, indent_level):
        output = []

        if indent_level == 0:
            dir_line = ""
        else:
            dir_line = " " * indent_level
        dir_line += " {}".format(self.name)
        output.append(dir_line)

        for file in self.files:
            new_line = " " * indent_level
            new_line += "{} ({}k)".format(file.name, file.size)
            output.append(new_line)

        for _, directory_obj in self.directories.items():
            output.extend(directory_obj.print_file_listing(indent_level + 1))
        return output

    def get_path(self):
        path_list = []

        path_list.insert(0, self.name)

        parent_dir = self.parent
        while parent_dir:
            if parent_dir.name != "/":
                path_list.insert(0, parent_dir.name)
                parent_dir = parent_dir.parent
            else:
                parent_dir = None

        path_string = "/".join(path_list)
        if path_string == "/":
            return "/"
        return "/{}".format(path_string)


class FileSystem:
    def __init__(self):
        self.data = Directory("/", None)
        self.current_dir = self.data

    def get_cwd(self):
        if self.current_dir:
            return self.current_dir.get_path()
        else:
            print("Current dir is empty!")
            print(self.current_dir)

    def add_file(self, file_obj):
        self.current_dir.add_file(file_obj)

    def add_dir(self, dir_name):
        self.current_dir.add_dir(dir_name)

    def change_dir(self, dir_name):
        if dir_name == "/":
            new_dir = self.data
        elif dir_name == "..":
            if self.current_dir.parent:
                new_dir = self.current_dir.get_parent_dir()
        elif dir_name.startswith("/"):
            parts = dir_name.split("/")
            self.change_dir("/")
            for part in parts:
                if part:
                    self.current_dir = self.current_dir.get_dir(part)
            new_dir = self.current_dir
        else:
            new_dir = self.current_dir.get_dir(dir_name)
        self.current_dir = new_dir

    def get_size(self):
        if self.current_dir:
            return self.current_dir.get_size()
        return 0

    def get_dir_names(self):
        result = []
        if self.current_dir:
            for directory_name, directory in self.current_dir.directories.items():
                result.append(directory.name)
        return result

    def print_file_listing(self):
        output = []

        indent_level = 0

        output.extend(self.data.print_file_listing(indent_level))

        for line in output:
            print(line)


def build_filesystem(command_list):
    fs = FileSystem()

    for command in command_list:
        if command.startswith("$"):
            # this is gonna do something
            command_parts = command.split(" ")
            # the real command is at the second position
            real_command = command_parts[1]
            if real_command == "cd":
                current_command = None
                fs.change_dir(command_parts[2])
            elif real_command == "ls":
                current_command = "ls"
        else:
            # this is probably a result of doing something
            if current_command == "ls":
                if command.startswith("dir"):
                    _, dir_name = command.split(" ")
                    fs.add_dir(dir_name)
                else:
                    size, name = command.split(" ")
                    new_file = File(name, size)
                    fs.add_file(new_file)
    return fs


def build_size_map(fs):
    fs.change_dir("/")
    dirs_to_check = set()
    result = {}
    next_dir = fs.get_cwd()

    while next_dir:
        fs.change_dir(next_dir)
        size_of_dir = fs.get_size()
        result[fs.get_cwd()] = size_of_dir
        for sub_dir in fs.get_dir_names():
            if next_dir == "/":
                full_dir = next_dir + sub_dir
            else:
                full_dir = next_dir + "/" + sub_dir
            dirs_to_check.add(full_dir)

        if len(dirs_to_check) > 0:
            next_dir = dirs_to_check.pop()
        else:
            next_dir = None
    return result


def p1():
    lines = get_file_contents("data/day07_input.txt")
    # print(len(lines))
    # lines = get_file_contents("data/day07_test.input")
    file_system = build_filesystem(lines)

    result = build_size_map(file_system)

    total = 0

    for k, v in result.items():
        if v <= 100_000:
            total += v
    print(total)


def p2():
    MAX_SIZE = 70_000_000
    REQUESTED_SIZE = 30_000_000
    # lines = get_file_contents("data/day07_test.input")
    lines = get_file_contents("data/day07_input.txt")
    file_system = build_filesystem(lines)
    result = build_size_map(file_system)

    free_space = MAX_SIZE - result["/"]
    space_needed = REQUESTED_SIZE - free_space
    print("Space Needed: ", space_needed)

    smallest = MAX_SIZE

    for k, v in result.items():
        if k == "/":
            continue
        if v > space_needed and v < smallest:
            smallest = v

    print(smallest)


    # print(result)


def main():
    p2()


if __name__ == "__main__":
    main()

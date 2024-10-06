const std = @import("std");
const utils = @import("utils.zig");

const Box = struct {
    length: i32 = 0,
    width: i32 = 0,
    height: i32 = 0,

    pub fn init(data: []const u8) !Box {
        var iter = std.mem.splitScalar(u8, data, 'x');
        return .{
            .length = try std.fmt.parseInt(i32, iter.next() orelse "0", 10),
            .width = try std.fmt.parseInt(i32, iter.next() orelse "0", 10),
            .height = try std.fmt.parseInt(i32, iter.next() orelse "0", 10),
        };
    }

    pub fn get_length(self: Box) i32 {
        return self.length * self.width;
    }

    pub fn get_width(self: Box) i32 {
        return self.width * self.height;
    }

    pub fn get_height(self: Box) i32 {
        return self.height * self.length;
    }

    pub fn get_length_perimeter(self: Box) i32 {
        return self.length + self.length + self.width + self.width;
    }

    pub fn get_width_perimeter(self: Box) i32 {
        return self.width + self.width + self.height + self.height;
    }

    pub fn get_height_perimeter(self: Box) i32 {
        return self.height + self.height + self.length + self.length;
    }

    pub fn get_size(self: Box) i32 {
        const length = self.get_length();
        const width = self.get_width();
        const height = self.get_height();

        var smallest = length;
        if (width < smallest) {
            smallest = width;
        }
        if (height < smallest) {
            smallest = height;
        }

        return (length * 2) + (width * 2) + (height * 2) + smallest;
    }

    pub fn get_ribbon_amount(self: Box) i32 {
        const length = self.get_length_perimeter();
        const width = self.get_width_perimeter();
        const height = self.get_height_perimeter();

        var smallest = length;
        if (width < smallest) {
            smallest = width;
        }
        if (height < smallest) {
            smallest = height;
        }

        return smallest + self.length * self.width * self.height;
    }
};

pub fn main() !void {
    try part01();
    try part02();
}

fn part01() !void {
    var allocator = std.heap.page_allocator;
    const contents = try utils.get_file_contents(allocator, "../data/day02_input.txt");
    defer allocator.free(contents);

    var answer: i64 = 0;

    var iter = std.mem.tokenizeSequence(u8, contents, "\n");
    while (iter.next()) |line| {
        var box = try Box.init(line);
        answer += box.get_size();
    }

    std.debug.print("Answer: {d}\n", .{answer});
}

fn part02() !void {
    var allocator = std.heap.page_allocator;
    const contents = try utils.get_file_contents(allocator, "../data/day02_input.txt");
    defer allocator.free(contents);

    var answer: i64 = 0;

    var iter = std.mem.tokenizeSequence(u8, contents, "\n");
    while (iter.next()) |line| {
        var box = try Box.init(line);
        answer += box.get_ribbon_amount();
    }

    std.debug.print("Answer: {d}\n", .{answer});
}

test "box calculates size correctly" {
    const testLine: []const u8 = "2x3x4";
    const box = try Box.init(testLine);
    const boxSize = box.get_size();
    try std.testing.expect(boxSize == 58);
}

test "box calculates ribbon amount correctly" {
    const testLine: []const u8 = "2x3x4";
    const box = try Box.init(testLine);
    const boxSize = box.get_ribbon_amount();
    try std.testing.expect(boxSize == 34);
}

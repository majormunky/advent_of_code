const std = @import("std");
const utils = @import("utils.zig");

pub fn main() !void {
    const answer_part01 = try part01();
    const answer_part02 = try part02();
    std.debug.print("Part 1: {d}\n", .{answer_part01});
    std.debug.print("Part 2: {d}\n", .{answer_part02});
}

fn part01() !i64 {
    var allocator = std.heap.page_allocator;
    const contents = try utils.get_file_contents(allocator, "../data/day01_input.txt");
    defer allocator.free(contents);

    var floor: i64 = 0;

    for (contents) |character| {
        if (character == ')') {
            floor -= 1;
        } else if (character == '(') {
            floor += 1;
        }
    }

    return floor;
}

fn part02() !usize {
    var allocator = std.heap.page_allocator;
    const contents = try utils.get_file_contents(allocator, "../data/day01_input.txt");
    defer allocator.free(contents);

    var floor: i64 = 0;
    var result: usize = 0;

    for (contents, 1..) |character, index| {
        if (character == ')') {
            floor -= 1;
        } else if (character == '(') {
            floor += 1;
        }
        if (floor < 0) {
            result = index;
            break;
        }
    }

    return result;
}

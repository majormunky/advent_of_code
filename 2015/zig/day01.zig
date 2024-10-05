const std = @import("std");

fn get_file_contents(allocator: std.mem.Allocator, path: []const u8) ![]u8 {
    // Open the file for reading
    const file = try std.fs.cwd().openFile(path, .{});

    // Read the contents of the file into a buffer
    const contents = try file.readToEndAlloc(allocator, 20000);
    defer file.close();
    return contents;
}

pub fn main() !void {
    const answer_day01 = try part01();
    std.debug.print("Day01: {d}\n", .{answer_day01});
}

fn part01() !i64 {
    var allocator = std.heap.page_allocator;
    const contents = try get_file_contents(allocator, "../data/day01_input.txt");
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

const std = @import("std");
const utils = @import("utils.zig");

pub fn main() !void {
    try part01();
}

fn part01() !void {
    var allocator = std.heap.page_allocator;
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const hmAllocator = gpa.allocator();

    const contents = try utils.get_file_contents(allocator, "../data/day03_input.txt");
    defer allocator.free(contents);

    var houseCount: i64 = 1;
    var housesVisited = std.StringHashMap(u16).init(hmAllocator);
    defer housesVisited.deinit();
    var posX: i64 = 0;
    var posY: i64 = 0;

    for (contents) |char| {
        std.debug.print("{c}\n", .{char});
        if (char == '^') {
            posY -= 1;
        } else if (char == '>') {
            posX += 1;
        } else if (char == 'v') {
            posY += 1;
        } else if (char == '<') {
            posX -= 1;
        }

        var buffer: [10]u8 = undefined;
        const posKey = try std.fmt.bufPrint(&buffer, "{d}-{d}", .{ posX, posY });
        if (housesVisited.get(posKey)) |value| {
            try housesVisited.put(posKey, value + 1);
        } else {
            try housesVisited.put(posKey, 1);
            houseCount += 1;
        }
    }

    std.debug.print("Houses found: {d}\n", .{houseCount});
}

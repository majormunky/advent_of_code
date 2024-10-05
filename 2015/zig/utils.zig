const std = @import("std");

pub fn get_file_contents(allocator: std.mem.Allocator, path: []const u8) ![]u8 {
    // Open the file for reading
    const file = try std.fs.cwd().openFile(path, .{});

    // Read the contents of the file into a buffer
    const contents = try file.readToEndAlloc(allocator, 20000);
    defer file.close();
    return contents;
}

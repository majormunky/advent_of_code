function file_exists(file)
  local f = io.open(file, "rb") -- Open the file passed as an arg
  if f then f:close() end       -- If the file isn't null, close it
  return f ~= nil               -- Then return true if file existed
end

function lines_from(file)
  if not file_exists(file) then return {} end    -- Ensure we have a file to read
  local lines = {}                               -- Setup a table to hold our lines
  for line in io.lines(file) do                  -- Loop over each line in the file
    lines[#lines + 1] = line                     -- Set our line in the table
  end
  return lines
end

function day01_part01()
    local file = "data/day01_input.txt"
    local lines = lines_from(file)
    local current_count = 0
    local largest_count = 0

    for line_num, line in pairs(lines)
    do
        if line == "" then                                      -- If our line is empty, it means we are done checking that elf
            if current_count > largest_count then               -- Check to see if this elf has more than our current largest
                largest_count = current_count                   -- If so, set this new elf as the current largest
            end
            current_count = 0                                   -- Reset count for the next elf
        else 
            current_count = current_count + tonumber(line)      -- Keep counting how many the current elf has
        end
    end

    -- Answer: 69795
    print(largest_count)
end

day01_part01()
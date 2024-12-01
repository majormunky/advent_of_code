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


function collect_values_from_elves()
    local file = "../data/day01_input.txt"
    local lines = lines_from(file)
    local current_count = 0
    local all_elves = {}

    for line_num, line in pairs(lines)
    do
        if line == "" then                                      -- If our line is empty, it means we are done checking that elf
            all_elves[#all_elves + 1] = current_count
            current_count = 0                                   -- Reset count for the next elf
        else
            current_count = current_count + tonumber(line)      -- Keep counting how many the current elf has
        end
    end

    return all_elves
end



function day01_part01()
    local elf_values = collect_values_from_elves()

    table.sort(elf_values)

    print(elf_values[#elf_values])
end


function day01_part02()
    local elf_values = collect_values_from_elves()
    table.sort(elf_values)

    local answer = elf_values[#elf_values] + elf_values[#elf_values - 1] + elf_values[#elf_values - 2]
    print(answer)
end

day01_part02()

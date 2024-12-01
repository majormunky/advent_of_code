import common
import sys


test_data = [
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i"
]

def parse_instruction(line):
    parts = line.split(" ")
    if len(parts) == 3:
        value = None
        try:
            value = int(parts[0])
        except ValueError:
            value = parts[0]
        return {
            "type": "ASSIGN",
            "completed": False,
            "data": {
                "key": parts[2],
                "value": value
            }
        }
    elif len(parts) == 4:
        return {
            "type": parts[0],
            "completed": False,
            "data": {
                "from": parts[1],
                "to": parts[-1]
            }
        }
    else:
        if parts[1] in ["AND", "OR"]:
            return {
                "type": parts[1],
                "completed": False,
                "data": {
                    "left": parts[0],
                    "right": parts[2],
                    "to": parts[-1]
                }
            }
        else:
            return {
                "type": parts[1],
                "completed": False,
                "data": {
                    "value": parts[0],
                    "amount": int(parts[2]),
                    "to": parts[-1]
                }
            }


def process(inst, data):
    if inst["type"] == "ASSIGN":
        key = inst["data"]["key"]
        value = inst["data"]["value"]
        data[key] = value
    elif inst["type"] == "AND":
        left_key = inst["data"]["left"]
        right_key = inst["data"]["right"]
        target = inst["data"]["to"]
        left = data[left_key]
        right = data[right_key]
        data[target] = left & right
    elif inst["type"] == "OR":
        left_key = inst["data"]["left"]
        right_key = inst["data"]["right"]
        target = inst["data"]["to"]
        left = data[left_key]
        right = data[right_key]
        data[target] = left | right
    elif inst["type"] == "LSHIFT":
        value_key = inst["data"]["value"]
        value = data[value_key]
        target_key = inst["data"]["to"]
        data[target_key] = value << inst["data"]["amount"]
    elif inst["type"] == "RSHIFT":
        value_key = inst["data"]["value"]
        value = data[value_key]
        target_key = inst["data"]["to"]
        data[target_key] = value >> inst["data"]["amount"]
    elif inst["type"] == "NOT":
        from_key = inst["data"]["from"]
        to_key = inst["data"]["to"]
        data[to_key] = ~data[from_key]
    return data

def get_key(key, data):
    print(data)
    value = data[key]
    print(value)
    if value < 0:
        value += 65536
    return value

# We can't just process the instructions one by one as some inputs aren't
# ready until we read instructions further on
def part01():
    data = {}
    lines = common.get_file_contents("data/day7_input.txt")
    queued = []
    instructions = []
    for row in lines:
        inst = parse_instruction(row)
        instructions.append(inst)
        # try:
        #     inst = parse_instruction(row)
        # except ValueError:
        #     print(row)
        #     sys.exit(1)
        # print(inst)
        # try:
        #     data = process(inst, data)
        # except KeyError:
        #     queued.append(inst)
    # working = True
    # while working:
    #     found = False
    #     for inst in queued:
    #         if inst["completed"] is False:
    #             try:
    #                 data = process(inst, data)
    #                 inst["completed"] = True
    #                 found = True
    #             except:
    #                 pass
    #     if found:
    #         working = False
    #         break

    # print(get_key('a', data))

    for i in instructions:
        print(i)


def part02():
    pass


def main():
    part01()


if __name__ == "__main__":
    main()

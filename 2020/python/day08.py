import pprint
import sys
import common
from dataclasses import dataclass, field


data = common.get_file_contents("data/day8_input.txt")


@dataclass
class ProgramState:
    index: int = 0
    program_length: int = 0
    acc: int = 0
    valid: bool = True
    visited: list[int] = field(default_factory=list)

    def process_instruction(self, i):
        inst_type = i["type"]
        
        if inst_type == "nop":
            self.index += 1
        elif inst_type == "acc":
            if i["direction"] == "plus":
                self.acc += i["amount"]
            else:
                self.acc -= i["amount"]
            self.index += 1
        elif inst_type == "jmp":            
            if i["direction"] == "plus":
                self.index += i["amount"]
            else:
                self.index -= i["amount"]

    def copy(self):
        new_copy = ProgramState()
        new_copy.index = self.index
        new_copy.program_length = self.program_length
        new_copy.acc = self.acc
        new_copy.visited = self.visited.copy()

        return new_copy


    def validate(self):
        if self.index in self.visited:
            return False
        return True


test_lines = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6"
]


def parse_instruction(line):
    parts = line.split(" ")
    amount_parts = list(parts[1])
    plus_or_minus = "plus"

    if amount_parts[0] == "-":
        plus_or_minus = "minus"

    amount_parts.pop(0)
    amount = "".join(amount_parts)
    
    return {
        "type": parts[0],
        "direction": plus_or_minus,
        "amount": int(amount)
    }


def part1():
    accumulator = 0
    index = 0

    visited_indexes = []

    while True:
        if index in visited_indexes:
            break

        visited_indexes.append(index)
        
        try:
            line = data[index]
        except IndexError:
            print("Index: ", index)
            break
        
        inst = parse_instruction(line)

        inst_type = inst["type"]

        if inst_type == "nop":
            index += 1
        elif inst_type == "acc":
            if inst["direction"] == "plus":
                accumulator += inst["amount"]
            else:
                accumulator -= inst["amount"]
            index += 1
        elif inst_type == "jmp":            
            if inst["direction"] == "plus":
                index += inst["amount"]
            else:
                index -= inst["amount"]

        
    return accumulator


def part2():
    program_data = test_lines
    
    print("Running Part 2")
    state = ProgramState()
    state.program_length = len(program_data)

    state_list = [state]
    active_state = None

    potential_winners = []

    while True:
        print("top of while loop")
        if len(state_list) == 0:
            print("State List Empty")
            break
        
        if active_state is None:
            print("Getting new active state")
            active_state = state_list.pop()

        if active_state.validate() == False:
            # infinite loop
            print("Infinite Loop, discarding")
            active_state.valid = False
            print(active_state)
            active_state = None
            continue
            
        try:
            line = program_data[active_state.index]
        except IndexError:
            print("Index Error")
            if active_state.index == active_state.program_length + 1:
                print("Found Answer:", active_state.acc)
                print("State Length:", len(state_list))
                print(active_state)
                potential_winners.append(active_state)
                active_state = None
                continue
            else:
                print("Not the answer")
                print("State Length:", len(state_list))
                print(active_state)                
                active_state = None
                continue

        active_state.visited.append(active_state.index)

        inst = parse_instruction(line)
        print("Processing Instruction: ", inst)

        if inst["type"] in ["nop", "jmp"]:
            print("Creating state copy")
            state_copy = active_state.copy()

            if inst["type"] == "nop":
                new_instruction = {
                    "type": "jmp",
                    "direction": inst["direction"],
                    "amount": inst["amount"]
                }
                state_copy.process_instruction(new_instruction)
                active_state.process_instruction(inst)
                
            else:
                new_instruction = {
                    "type": "nop",
                    "direction": inst["direction"],
                    "amount": inst["amount"]
                }
                state_copy.process_instruction(new_instruction)
                active_state.process_instruction(inst)

            state_list.append(state_copy)
        else:
            active_state.process_instruction(inst)
    print("Potential Winners:", len(potential_winners))


def main():
    # part1_answer = part1()
    part2_answer = part2()

    #print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}") # 1540 too high


if __name__ == "__main__":
    main()

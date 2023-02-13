import time
import sys
from common import get_file_contents


class Monkey:
    def __init__(self, lines, trainer):
        self.trainer = trainer
        self.name = self.parse_name(lines[0])
        self.holding_items = self.get_starting_item_list(lines[1])
        self.operation_val = None
        self.operation_type = None
        self.item_test_val = None
        self.item_test = self.build_test_func(lines[3])
        self.passes_test_next_monkey = self.get_monkey_num(lines[4])
        self.fails_test_next_monkey = self.get_monkey_num(lines[5])
        self.inspection_count = 0
        self.output = []

    def parse_name(self, line):
        """
        Get the name out of the line that includes the name
        """
        parts = line.split(" ")
        return parts[1].replace(":", "").strip()

    def perform_operation(self, val):
        """
        Performs the specific operation configured for this monkey
        """
        if self.operation_type == "increases":
            return self.operation_val + val
        if self.operation_type == "multiplied":
            if self.operation_val == "old":
                return self.operation_val * self.operation_val
            return self.operation_val * val
        print("Unknown operation type")
        return False

    def get_starting_item_list(self, line):
        """
        Takes in the line that has our starting items,
        and returns a list with just those items as ints
        """
        result = []
        parts = line.split(":")
        for item in parts[1].split(","):
            result.append(int(item))
        return result

    def catch_item(self, item):
        self.holding_items.append(item)

    def build_test_func(self, line):
        parts = line.split(" ")
        self.item_test_val = int(parts[-1])

        def new_func(x):
            return x % self.item_test_val == 0
        return new_func

    def build_operation(self, line):
        parts = line.split(" ")
        if parts[-1] == "old":
            self.operation_val = parts[-1]
        else:
            self.operation_val = int(parts[-1])
        # Remember what operation we have to do later
        self.operation_type = parts[-2]

    def get_monkey_num(self, line):
        parts = line.split(" ")
        return parts[-1]

    def process_items(self):
        # this will be a list of actions that we need to do
        result = []

        # list of messages
        # self.output = []
        # self.output.append(f"Monkey: {self.name}")

        # we will be modifying the list of held items
        # so we want to make a copy of them when we process them
        current_items = list(self.holding_items)
        for item in current_items:
            # count how many times we process an item
            self.inspection_count += 1
            # self.output.append(f"  Monkey inspects an item with a worry level of {item}.")

            # each monkey has a different operation it takes on the held item
            # the result of that sets our worry level
            worry_level = self.perform_operation(item)

            if worry_level is False:
                print("Worry level is false, stopping!")
                sys.exit(1)
            # self.output.append(f"    Worry level is {self.operation_type} by {self.operation_val} to {worry_level}")

            # if we are in part 1, part of the process reduces our worry level
            if self.trainer.test_name == "p1":
                worry_level = worry_level // 3
                # self.output.append(f"    Monkey gets bored with item. Worry level is divided by 3 to {worry_level}.")

            # each monkey has a different test that it does with the worry level of the item
            # depending on the result of that test, we send the item to a different monkey
            passes_test = self.item_test(worry_level)
            if passes_test:
                # self.output.append(f"    Current worry level is divisible by {self.item_test_val}.")
                # self.output.append(f"    Item with worry level {worry_level} is thrown to monkey {self.passes_test_next_monkey}.")
                # self.trainer.send_item_to_monkey(worry_level, self.passes_test_next_monkey)
                result.append((worry_level, self.passes_test_next_monkey),)
            else:
                # self.output.append(f"    Current worry level is not divisible by {self.item_test_val}.")
                # self.output.append(f"    Item with worry level {worry_level} is thrown to monkey {self.fails_test_next_monkey}.")
                # self.trainer.send_item_to_monkey(worry_level, self.fails_test_next_monkey)
                result.append((worry_level, self.fails_test_next_monkey),)

            # remove the item from the monkey
            self.holding_items.remove(item)
        return result

    def has_items(self):
        return len(self.holding_items) > 0


class MonkeyTrainer:
    def __init__(self, lines, test_name):
        self.test_name = test_name
        self.monkeys = {}
        self.build_monkeys(lines)
        print(f"Trainer built {len(self.monkeys.keys())} monkeys")

    def get_chunks(self, lines):
        result = []
        monkey = []
        for line in lines:
            if line == "":
                result.append(monkey)
                monkey = []
                continue
            monkey.append(line)
        if len(monkey):
            result.append(monkey)
        return result

    def send_item_to_monkey(self, item, monkey_name):
        self.monkeys[monkey_name].catch_item(item)
        
    def build_monkeys(self, lines):
        chunks = self.get_chunks(lines)
        for chunk in chunks:
            monkey = Monkey(chunk, self)
            self.monkeys[monkey.name] = monkey

    def process_monkey(self, key):
        tic = time.perf_counter()
        item_count = len(self.monkeys[key].holding_items)
        process_results = self.monkeys[key].process_items()

        for item in process_results:
            self.send_item_to_monkey(item[0], item[1])
        toc = time.perf_counter()
        time_taken = toc - tic
        return time_taken, item_count

    def run(self, round_limit):
        ROUND_LIMIT = round_limit
        round_count = 0
        sub_count = 0
        sub_limit = 100
        if sub_limit > round_limit:
            sub_limit = round_limit
        while True:
            round_count += 1
            sub_count += 1
            time_taken = None
            result_count = None
            for i in range(len(self.monkeys.keys())):
                key = str(i)
                time_taken, result_count = self.process_monkey(key)

            if sub_count == sub_limit:
                print("Process Time: ", round(time_taken, 4))
                print("Result Count: ", result_count)
                sub_count = 0
                print("Round Count:", round_count)

            if round_count == ROUND_LIMIT:
                break
                
        counts = []
        for name, monkey in self.monkeys.items():
            counts.append(monkey.inspection_count)

        counts = sorted(counts, reverse=True)
        return counts


def get_answer_from_count_list(count_list):
    return count_list[0] * count_list[1]
    

def p1():
    lines = get_file_contents("data/day11_input.txt")
    trainer = MonkeyTrainer(lines, "p1")
    answer_list = trainer.run(20)
    # Answer: 110888
    print("Answer: ", get_answer_from_count_list(answer_list))

    
def p2():
    # lines = get_file_contents("data/day11_input.txt")
    lines = get_file_contents("data/day11_test.input")
    trainer = MonkeyTrainer(lines, "p2")
    answer_list = trainer.run(1000)
    print("Answer: ", answer_list)


def main():
    p2()


if __name__ == "__main__":
    main()


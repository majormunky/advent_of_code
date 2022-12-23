from common import get_file_contents


class Monkey:
    def __init__(self, lines, trainer):
        self.trainer = trainer
        self.name = self.get_name(lines[0])
        self.holding_items = self.get_starting_item_list(lines[1])
        self.operation_val = None
        self.operation_type = None
        self.operation = self.build_operation(lines[2])
        self.item_test_val = None
        self.item_test = self.build_test_func(lines[3])
        self.passes_test_next_monkey = self.get_monkey_num(lines[4])
        self.fails_test_next_monkey = self.get_monkey_num(lines[5])
        self.inspection_count = 0
        self.output = []

    def get_name(self, line):
        parts = line.split(" ")
        return parts[1].replace(":", "").strip()
        
    def get_starting_item_list(self, line):
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
        self.operation_val_type = None
        if parts[-1] == "old":
            self.operation_val = parts[-1]
        else:
            self.operation_val = int(parts[-1])
        operation = parts[-2]

        def add_operation(held_item):
            return held_item + self.operation_val

        def multi_operation(held_item):
            if self.operation_val == "old":
                return held_item * held_item
            return held_item * self.operation_val

        if operation == "+":
            self.operation_type = "increases"
            return add_operation
        elif operation == "*":
            self.operation_type = "multiplied"
            return multi_operation
        else:
            print("Unknown operation type")
    
    def get_monkey_num(self, line):
        parts = line.split(" ")
        return parts[-1]

    def process_items(self):
        # this will be a list of actions that we need to do
        result = []

        # list of messages
        self.output = []
        self.output.append(f"Monkey: {self.name}")

        # we will be modifying the list of held items
        # so we want to make a copy of them when we process them
        current_items = list(self.holding_items)
        for item in current_items:
            # count how many times we process an item
            self.inspection_count += 1
            self.output.append(f"  Monkey inspects an item with a worry level of {item}.")

            # each monkey has a different operation it takes on the held item
            # the result of that sets our worry level
            worry_level = self.operation(item)
            self.output.append(f"    Worry level is {self.operation_type} by {self.operation_val} to {worry_level}")

            # if we are in part 1, part of the process reduces our worry level
            if self.trainer.test_name == "p1":
                worry_level = worry_level // 3
                self.output.append(f"    Monkey gets bored with item. Worry level is divided by 3 to {worry_level}.")

            # each monkey has a different test that it does with the worry level of the item
            # depending on the result of that test, we send the item to a different monkey
            passes_test = self.item_test(worry_level)
            if passes_test:
                self.output.append(f"    Current worry level is divisible by {self.item_test_val}.")
                self.output.append(f"    Item with worry level {worry_level} is thrown to monkey {self.passes_test_next_monkey}.")
                # self.trainer.send_item_to_monkey(worry_level, self.passes_test_next_monkey)
                result.append((worry_level, self.passes_test_next_monkey),)
            else:
                self.output.append(f"    Current worry level is not divisible by {self.item_test_val}.")
                self.output.append(f"    Item with worry level {worry_level} is thrown to monkey {self.fails_test_next_monkey}.")
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

    def run(self, round_limit):
        ROUND_LIMIT = round_limit
        round_count = 0
        while True:
            round_count += 1
            for i in range(len(self.monkeys.keys())):
                key = str(i)
                process_results = self.monkeys[key].process_items()
                for item in process_results:
                    self.send_item_to_monkey(item[0], item[1])
            if round_count >= ROUND_LIMIT:
                break

            if round_count % 100 == 0:
                print("Round Count:", round_count)

        # too low: 14448
        # too low: 15312
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
    lines = get_file_contents("data/day11_test.input")
    trainer = MonkeyTrainer(lines, "p2")
    answer_list = trainer.run(1000)
    print("Answer: ", answer)


def main():
    p1()


if __name__ == "__main__":
    main()


import os
import math
import common


def get_chunks(lines):
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


class Monkey:
    def __init__(self, lines, trainer):
        self.name = self.build_name(lines[0])
        self.trainer = trainer
        self.item_list = self.get_starting_item_list(lines[1])
        self.operation_val = None
        self.operation_type = None
        self.item_test_val = None
        self.item_test = self.build_test_func(lines[3])
        self.next_monkey = {
            "passes": self.get_monkey_number(lines[4]),
            "fails": self.get_monkey_number(lines[5]),
        }
        self.inspection_count = 0
        self.build_operation(lines[2])

    def build_name(self, line):
        parts = line.split(" ")
        return parts[1].replace(":", "").strip()

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

    def get_monkey_number(self, line):
        parts = line.split(" ")
        return parts[-1]

    def build_operation(self, line):
        # Operation: new = old * 19
        parts = line.split(" ")
        if parts[-1] == "old":
            self.operation_val = parts[-1]
        else:
            self.operation_val = int(parts[-1])
        # Remember what operation we have to do later
        if parts[-2] == "*":
            self.operation_type = "multiplied"
        else:
            self.operation_type = "increases"

    def perform_operation(self, val) -> int:
        if self.operation_type == "increases":
            if self.operation_val == "old":
                return val + val
            else:
                return self.operation_val + val
        elif self.operation_type == "multiplied":
            if self.operation_val == "old":
                return val * val
            else:
                return self.operation_val * val
        return 0

    def build_test_func(self, line):
        parts = line.split(" ")
        self.item_test_val = int(parts[-1])

        def new_func(x):
            return x % self.item_test_val == 0

        return new_func

    def process_fast(self, modulo_number):
        result = []
        current_items = list(self.item_list)
        for item in current_items:
            self.inspection_count += 1

            worry_level = self.perform_operation(item)
            worry_level = worry_level % modulo_number

            test_val = self.item_test(worry_level)

            test_result = {"monkey": None, "item": None}
            if test_val:
                test_result["monkey"] = self.next_monkey["passes"]
                test_result["item"] = worry_level
            else:
                test_result["monkey"] = self.next_monkey["fails"]
                test_result["item"] = worry_level

            result.append(test_result)
            self.item_list.remove(item)
        return result

    def process(self):
        result = []
        current_items = list(self.item_list)
        for item in current_items:
            self.inspection_count += 1
            worry_level = self.perform_operation(item)

            if self.trainer.perform_worry_reduction:
                worry_level = worry_level // 3

            test_val = self.item_test(worry_level)

            test_result = {"monkey": None, "item": None}
            if test_val:
                test_result["monkey"] = self.next_monkey["passes"]
                test_result["item"] = worry_level
            else:
                test_result["monkey"] = self.next_monkey["fails"]
                test_result["item"] = worry_level
            result.append(test_result)
            self.item_list.remove(item)
        return result

    def catch_item(self, val):
        self.item_list.append(val)


class MonkeyTrainer:
    def __init__(self, chunks, perform_worry_reduction):
        self.monkeys = {}
        self.perform_worry_reduction = perform_worry_reduction
        self.build_monkeys(chunks)
        self.all_monkey_modulo = self.calculate_monkey_modulo()
        print("Monkey Modulo", self.all_monkey_modulo)

    def build_monkeys(self, chunk_list):
        for chunk in chunk_list:
            monkey = Monkey(chunk, self)
            self.monkeys[monkey.name] = monkey
        print(f"Built {len(self.monkeys)} monkeys")

    def calculate_monkey_modulo(self):
        result = 0
        items = []

        for _, monkey in self.monkeys.items():
            items.append(monkey.item_test_val)
        return math.prod(items)

    def perform_round(self):
        for monkey_name, monkey in self.monkeys.items():
            results = monkey.process()

            for result in results:
                self.monkeys[result["monkey"]].catch_item(result["item"])

    def perform_round_fast(self):
        for monkey_name, monkey in self.monkeys.items():
            results = monkey.process_fast(self.all_monkey_modulo)

            for result in results:
                self.monkeys[result["monkey"]].catch_item(result["item"])

    def output_monkey_values(self):
        for monkey_name, monkey in self.monkeys.items():
            monkey_items = ""
            for item in monkey.item_list:
                monkey_items += f"{item} "
            print(f"{monkey_name}: {monkey_items}")

    def output_monkey_inspection_counts(self):
        for monkey_name, monkey in self.monkeys.items():
            print(
                f"Monkey {monkey_name} inspected items {monkey.inspection_count} times"
            )
        print()

    def get_monkey_business_amount(self):
        values = []
        for monkey_name, monkey in self.monkeys.items():
            values.append(monkey.inspection_count)
        values.sort()
        return values[-1] * values[-2]

    def run(self, rounds, fast_version=False):
        round_count = 0
        for i in range(rounds):
            if fast_version:
                self.perform_round_fast()
            else:
                self.perform_round()
            round_count += 1

            if round_count == 1:
                print(f"== After round {round_count} == ")
                self.output_monkey_inspection_counts()
            elif round_count == 20:
                print(f"== After round {round_count} == ")
                self.output_monkey_inspection_counts()
            elif round_count % 1000 == 0:
                print(f"== After round {round_count} == ")
                self.output_monkey_inspection_counts()


def part1():
    real_file = os.path.join("..", "data", "day11_input.txt")
    lines = common.get_file_contents(real_file)

    chunks = get_chunks(lines)
    trainer = MonkeyTrainer(chunks, True)
    trainer.run(20)
    return trainer.get_monkey_business_amount()


def part2():
    real_file = os.path.join("..", "data", "day11_input.txt")
    lines = common.get_file_contents(real_file)

    chunks = get_chunks(lines)
    trainer = MonkeyTrainer(chunks, False)
    trainer.run(10000, True)
    return trainer.get_monkey_business_amount()


if __name__ == "__main__":
    part1()
    part2()

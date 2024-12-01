import os
import common


def extract_date(line):
    parts = line.split("]")
    return parts[0].replace("[", "")


def extract_guard_info(line):
    parts = line.split("]")
    return parts[-1].strip()


def output_schedule(data):
    output = "Date\tID\tMinute\n"
    output += "\t\t" + "0" * 10
    output += "1" * 10
    output += "2" * 10
    output += "3" * 10
    output += "4" * 10
    output += "5" * 10
    output += "\n\t\t"
    for _ in range(6):
        for i in range(10):
            output += f"{i}"

    output += "\n"

    for date, rows in data.items():
        output += date.replace("1518-", "") + "\n"
    print(output)


def part1():
    real_file = os.path.join("..", "data", "day04_input.txt")
    data = common.get_file_contents(real_file)

    # lines = [
    #     "[1518-11-01 00:00] Guard #10 begins shift",
    #     "[1518-11-01 00:05] falls asleep",
    #     "[1518-11-01 00:25] wakes up",
    #     "[1518-11-01 00:30] falls asleep",
    #     "[1518-11-01 00:55] wakes up",
    #     "[1518-11-01 23:58] Guard #99 begins shift",
    #     "[1518-11-02 00:40] falls asleep",
    #     "[1518-11-02 00:50] wakes up",
    #     "[1518-11-03 00:05] Guard #10 begins shift",
    #     "[1518-11-03 00:24] falls asleep",
    #     "[1518-11-03 00:29] wakes up",
    #     "[1518-11-04 00:02] Guard #99 begins shift",
    #     "[1518-11-04 00:36] falls asleep",
    #     "[1518-11-04 00:46] wakes up",
    #     "[1518-11-05 00:03] Guard #99 begins shift",
    #     "[1518-11-05 00:45] falls asleep",
    #     "[1518-11-05 00:55] wakes up"
    # ]
    day_data = {}

    for line in data:
        line_datetime = extract_date(line)
        line_date, line_time = line_datetime.split(" ")

        guard_info = extract_guard_info(line)

        if line_date not in day_data.keys():
            day_data[line_date] = []
        day_data[line_date].append({"time": line_time, "guard": guard_info})

    output_schedule(day_data)

    # for k, v in day_data.items():
    #     print(k)
    #     for item in v:
    #         print(item)
    #     print("--")



def main():
    part1()



if __name__ == "__main__":
    main()

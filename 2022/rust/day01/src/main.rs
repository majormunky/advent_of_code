use std::env;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

// taken from: https://doc.rust-lang.org/stable/rust-by-example/std_misc/file/read_lines.html
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>> where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn main() {
    let args = get_args();

    match args {
        Err(why) => println!("{:?}", why),
        Ok(which_part) => {
            match which_part.as_str() {
                "part1" => {
                    let answer = part1();
                    println!("Part 1: {}", answer);
                },
                "part2" => {
                    let answer = part2();
                    println!("Part 2: {}", answer);
                },
                _ => {
                    println!("Unknown Arg! -> {:?}", which_part);
                }
            }
        }
    }
}

fn get_args() -> Result<String, &'static str> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        return Err("not enough arguments");
    }
    Ok(args[1].clone())
}


fn part2() -> u32 {
    let filename = "day01_data.txt";
    let mut data_list: Vec<u32> = Vec::new();
    let mut current_calories = 0;

    if let Ok(lines) = read_lines(filename) {
        for line in lines {
            if let Ok(the_line) = line {
                let line_value: LineValue = get_line_value(&the_line);
                match line_value {
                    LineValue::BlankLine => {
                        data_list.push(current_calories);
                        current_calories = 0;
                    },
                    LineValue::CalorieAmount(cal_amount) => {
                        current_calories += cal_amount;
                    }
                }
            }
        }
    }

    data_list.sort();
    let mut result = 0;
    let result_size = data_list.len();
    result += data_list[result_size - 1];
    result += data_list[result_size - 2];
    result += data_list[result_size - 3];

    result
}


enum LineValue {
    BlankLine,
    CalorieAmount(u32)
}


fn get_line_value(line: &str) -> LineValue {
    let trimmed_line = line.trim();

    if trimmed_line.is_empty() {
        return LineValue::BlankLine;
    }
    let calorie: u32 = trimmed_line.parse().expect("Not a number");
    LineValue::CalorieAmount(calorie)
}


fn part1() -> u32 {
    let filename = "day01_data.txt";
    let mut max_calories = 0;
    let mut current_calories = 0;

    if let Ok(lines) = read_lines(filename) {
        for line in lines {
            if let Ok(the_line) = line {
                let line_value: LineValue = get_line_value(&the_line);
                match line_value {
                    LineValue::BlankLine => {
                        if current_calories > max_calories {
                            max_calories = current_calories;
                        }
                        current_calories = 0;
                    },
                    LineValue::CalorieAmount(cal_amount) => {
                        current_calories += cal_amount;
                    }
                }
            }
        }
    }

    max_calories
}

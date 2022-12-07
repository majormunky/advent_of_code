use std::fs;
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



    10
}


fn part1() -> u32 {
    let filename = "day01_data.txt";
    let mut max_calories = 0;
    let mut current_calories = 0;

    if let Ok(lines) = read_lines(filename) {
        for line in lines {
            if let Ok(the_line) = line {
                let trimmed_line = the_line.trim();

                // if our line is empty
                if trimmed_line.is_empty() {
                    // it means we need to get our current count
                    // and check if its larger than our max
                    if current_calories > max_calories {
                        // and if so, set it as the new max
                        max_calories = current_calories;
                    }

                    // reset the current count
                    current_calories = 0;

                    // skip the rest of this loop
                    continue;
                }

                // if we are here, it means we have some data on the line
                // convert the line as a string to an integer
                let calorie: u32 = trimmed_line.parse().expect("Not a number");

                // and add it to our current count
                current_calories += calorie;
            }
        }
    }

    max_calories
}

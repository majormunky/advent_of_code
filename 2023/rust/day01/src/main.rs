use std::env;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


// taken from: https://doc.rust-lang.org/stable/rust-by-example/std_misc/file/read_lines.html
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>> where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}


const TEST_STRINGS:[&str; 4] = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
];


fn get_args() -> Result<String, &'static str> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        return Err("not enough arguments");
    }
    Ok(args[1].clone())
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
                    println!("Unknown Part: -> {:?}", which_part)
                }    
            }
        }
    }
}


fn part1() -> u32 {
    let filename = "day01_input.txt";
    if let Ok(lines) = read_lines(filename) {
        for line in lines {
            println!("{:?}", line);
        }
    }

    42
}


fn part2() -> u32 {
    42
}


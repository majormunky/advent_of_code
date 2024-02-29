use std::env;
use std::collections::HashSet;
use std::fs::read_to_string;


fn get_args() -> Result<String, &'static str> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        return Err("not enough arguments");
    }
    Ok(args[1].clone())
}


fn build_set_from_string(s: &String) -> HashSet<String> {
    let mut result = HashSet::new();

    for c in s.chars() {
        result.insert(c.to_string());
    }

    result
}


fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}


fn part1() -> usize {
    let lines = read_lines("day03_input.txt");

    let alphabet: Vec<char> = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".chars().collect();

    let mut total: usize = 0;

    for line in lines {
        let line_length = line.len();
        let half_size = line_length / 2;
        let first_part = &line[0..half_size].to_string();
        let second_part = &line[half_size..line_length].to_string();

        let first_set = build_set_from_string(&first_part);
        let second_set = build_set_from_string(&second_part);

        let mut diff = Vec::new();

        for x in first_set.intersection(&second_set) {
            diff.push(x.to_string());
        }

        let diff_char: char = diff[0].chars().next().expect("string is empty");

        let mut value: usize = 0;

        if let Some(letter_value) = alphabet.iter().position(|&x| x == diff_char) {
            value = letter_value + 1;
        }

        total += value;
    }

    total
}


fn part2() -> i32 {
    42
}


fn get_test_lines() -> Vec<String> {
    let mut result = Vec::new();

    result.push("vJrwpWtwJgWrhcsFMMfFFhFp".to_string());
    result.push("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL".to_string());
    result.push("PmmdzqPrVvPwwTWBwg".to_string());
    result.push("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn".to_string());
    result.push("ttgJtRGJQctTZtZT".to_string());
    result.push("CrZsJsPPZsGzwwsLwLmpwMDw".to_string());

    result
}


fn main() {
    let args = get_args();

    match args {
        Err(why) => println!("{:?}", why),
        Ok(which_part) => {
            match which_part.as_str() {
                "part1" => {
                    let answer = part1();
                    println!("Part 1: {answer}");
                },
                "part2" => {
                    let answer = part2();
                    println!("Part 2: {answer}");
                },
                _ => println!("Unknown part: {which_part}")    
            }
        }
    }
}

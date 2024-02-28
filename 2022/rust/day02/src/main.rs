use std::fs::read_to_string;
use std::env;


#[derive(PartialEq)]
enum Hand {
    Rock,
    Paper,
    Scissors
}


fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}


fn translate_letter_to_hand(letter: &str) -> Hand {
    match letter {
        "A" | "X" => Hand::Rock,
        "B" | "Y" => Hand::Paper,
        "C" | "Z" => Hand::Scissors,
        _ => panic!()
    }
}


fn score_game(first: Hand, second: Hand) -> i32 {
    // A Rock, B Paper, C Scissors
    // X Rock, Y Paper, Z Scissors
    // score 1 Rock, 2 Paper, 3 Scissors
    // score 0 lost, 3 draw, 6 win
    let mut result: i32 = 0;

    if first == Hand::Rock {
        if second == Hand::Rock {
            result += 3;
            result += 1;
        } else if second == Hand::Paper {
            result += 6;
            result += 2;
        } else if second == Hand::Scissors {
            result += 3;
        }
    } else if first == Hand::Paper {
        if second == Hand::Paper {
            result += 3;
            result += 2;
        } else if second == Hand::Scissors {
            result += 6;
            result += 3;
        } else if second == Hand::Rock {
            result += 1;
        }
    } else if first == Hand::Scissors {
        if second == Hand::Rock {
            result += 6;
            result += 1;
        } else if second == Hand::Scissors {
            result += 3;
            result += 3;
        } else if second == Hand::Paper {
            result += 2;
        }
    }
    
    result
}


fn get_args() -> Result<String, &'static str> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        return Err("not enough arguments");
    }
    Ok(args[1].clone())
}


fn part1() -> i32 {
    let filename = "day02_data.txt";
    let lines = read_lines(filename);
    let mut total_score: i32 = 0;

    for line in lines {
        let parts = line.split(" ");
        let collection = parts.collect::<Vec<&str>>();

        let opponent: Hand = translate_letter_to_hand(collection[0]);
        let mine: Hand = translate_letter_to_hand(collection[1]);
        
        let score: i32 = score_game(opponent, mine);

        total_score += score;
    }

    total_score
}


fn part2() -> i32 {
    42
}


fn main() {
    let args = get_args();

    match args {
        Err(why) => println!("{:?}", why),
        Ok(which_part) => {
            match which_part.as_str() {
                "part1" => {
                    let answer = part1();
                    println!("Part 1: {answer}")
                },
                "part2" => {
                    let answer = part2();
                    println!("Part 2: {answer}")
                },
                _ => {
                    println!("Unknown Arg! -> {:?}", which_part);
                }
            }
        }
    }
}

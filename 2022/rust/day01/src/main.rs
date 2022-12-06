use std::fs;

fn main() {
    let filename = "day01_data.txt";
    let contents = fs::read_to_string(filename)
        .expect("Should have been able to read the file");
    let line_iter = contents.split("\n");
    let lines = line_iter.collect::<Vec<&str>>();
    let mut max_calories = 0;
    let mut current_calories = 0;

    for line in &lines {
        // Take our line and trim off any line endings
        let trimmed_line = line.trim();

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

    println!("Total Calories: {}", max_calories);
}

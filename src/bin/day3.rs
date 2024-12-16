use regex::Regex;
use std::fs;

fn main() {
    let data = fs::read_to_string("data/3.in").expect("Unable to read file");
    let op_re = Regex::new(r"mul\(\d+,\d+\)|do\(\)|don't\(\)").unwrap();
    let num_re = Regex::new(r"\d+").unwrap();
    let mut p1 = 0;
    let mut p2 = 0;
    let mut active = true;
    for op in op_re.find_iter(&data) {
        match op.as_str() {
            "do()" => active = true,
            "don't()" => active = false,
            _ => {
                let mut prod = 1;
                for num in num_re.find_iter(op.as_str()) {
                    prod *= num.as_str().parse::<i64>().unwrap();
                }
                p1 += prod;
                if active {
                    p2 += prod;
                }
            }
        }
    }
    println!("{}", p1);
    println!("{}", p2);
}

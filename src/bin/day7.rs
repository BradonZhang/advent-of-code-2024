use regex::Regex;
use std::fs;

fn can_reach_helper(target: i64, operands: &Vec<i64>, curr: i64, index: usize) -> bool {
    if curr > target {
        return false;
    }
    if index >= operands.len() {
        return target == curr;
    }
    let operand = operands[index];
    return can_reach_helper(target, operands, curr + operand, index + 1)
        || can_reach_helper(target, operands, curr * operand, index + 1);
}

fn can_reach(target: i64, operands: &Vec<i64>) -> bool {
    return can_reach_helper(target, operands, operands[0], 1);
}

fn can_reach2_helper(target: i64, operands: &Vec<i64>, curr: i64, index: usize) -> bool {
    if curr > target {
        return false;
    }
    if index >= operands.len() {
        return target == curr;
    }
    let operand = operands[index];
    return can_reach2_helper(target, operands, curr + operand, index + 1)
        || can_reach2_helper(target, operands, curr * operand, index + 1)
        || {
            can_reach2_helper(
                target,
                operands,
                format!("{}{}", curr, operand).parse::<i64>().unwrap(),
                index + 1,
            )
        };
    // return [
    //     curr + operand,
    //     curr * operand,
    //     format!("{}{}", curr, operand).parse::<i64>().unwrap(),
    // ]
    // .iter()
    // .any(|next| can_reach2_helper(target, operands, *next, index + 1));
}

fn can_reach2(target: i64, operands: &Vec<i64>) -> bool {
    return can_reach2_helper(target, operands, operands[0], 1);
}

fn main() {
    let data = fs::read_to_string("data/7.in").expect("Unable to read file");

    let num_re = Regex::new("\\d+").unwrap();
    let eqs: Vec<_> = data
        .trim()
        .split('\n')
        .map(|line| {
            let mut nums = num_re
                .find_iter(line)
                .map(|num| num.as_str().parse::<i64>().unwrap());
            let target = nums.next().unwrap();
            let operands: Vec<_> = nums.collect();
            return (target, operands);
        })
        .collect();

    let p1: i64 = eqs
        .iter()
        .cloned()
        .map(|(target, operands)| can_reach(target, &operands) as i64 * target)
        .sum();
    println!("{}", p1);

    let p2: i64 = eqs
        .iter()
        .cloned()
        .map(|(target, operands)| can_reach2(target, &operands) as i64 * target)
        .sum();
    println!("{}", p2);
}

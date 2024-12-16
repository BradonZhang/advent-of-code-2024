use std::{collections::HashMap, fs};

fn main() {
    let data = fs::read_to_string("data/1.in").expect("Unable to read file");
    let nums: Vec<i64> = data.split_whitespace().map(|s| s.parse::<i64>().unwrap()).collect();
    // let pairs: Vec<(i64, i64)> = data.trim().split('\n').map(parse_line).collect();
    // for pair in pairs {
    //     println!("{:?}", pair);
    // }
    let mut left: Vec<i64> = nums.clone().into_iter().enumerate().filter(|&(i, _)| i % 2 == 0).map(|(_, s)| s).collect();
    left.sort();
    let mut right: Vec<i64> = nums.into_iter().enumerate().filter(|&(i, _)| i % 2 == 1).map(|(_, s)| s).collect();
    right.sort();
    let mut p1 = 0;
    let n = left.len();
    let mut mem: HashMap<i64, i64> = HashMap::new();
    for i in 0..n {
        p1 += (left[i] - right[i]).abs();
        *mem.entry(right[i]).or_insert(0) += 1;
    }
    println!("{}", p1);
    let mut p2 = 0;
    for num in left {
        p2 += num * mem.get(&num).unwrap_or(&0);
    }
    println!("{}", p2);
    // let mut p2 = 0;
    // let mut j = 0;
    // for i in 0..n {
    //     while j < n && right[j] <= left[i] {
    //         if right[j] == left[i] {
    //             p2 += left[i];
    //         }
    //         j += 1;
    //     }
    //     if j >= n {
    //         break;
    //     }
    // }
    // println!("{}", p2);
}

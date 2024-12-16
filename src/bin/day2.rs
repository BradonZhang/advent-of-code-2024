use std::fs;

fn parse_line(line: &str) -> Vec<i64> {
    let nums: Vec<i64> = line
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    return nums;
}

fn main() {
    let data = fs::read_to_string("data/2.in").expect("Unable to read file");
    let reports: Vec<Vec<i64>> = data.trim().split('\n').map(parse_line).collect();

    let mut p1 = 0;
    let mut p2 = 0;
    for report in reports {
        let increasing = report[1] > report[0];
        let mut good = true;
        for i in 1..report.len() {
            let curr = report[i];
            let prev = report[i - 1];
            if curr == prev || ((curr > prev) != increasing || (curr - prev).abs() > 3) {
                good = false;
                break;
            }
        }
        if good {
            p1 += 1;
            p2 += 1;
        } else {
            let report_ = report;
            for i in 0..report_.len() {
                let mut good = true;
                let mut report = report_.clone();
                report.remove(i);
                let increasing = report[1] > report[0];
                for i in 1..report.len() {
                    let curr = report[i];
                    let prev = report[i - 1];
                    if curr == prev || ((curr > prev) != increasing || (curr - prev).abs() > 3) {
                        good = false;
                        break;
                    }
                }
                if good {
                    p2 += 1;
                    break;
                }
            }
        }
    }
    println!("{}", p1);
    println!("{}", p2);
}

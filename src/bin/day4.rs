use std::fs;

fn main() {
    let data = fs::read_to_string("data/4.in").expect("Unable to read file");
    let grid: Vec<Vec<char>> = data
        .trim()
        .split_whitespace()
        .map(|line| line.chars().collect())
        .collect();
    let m = grid.len();
    let n = grid[0].len();
    let key = vec!['X', 'M', 'A', 'S'];
    let ds: Vec<i64> = vec![-1, 0, 1];
    let mut p1 = 0;
    let mut p2 = 0;
    for i in 0..m {
        for j in 0..n {
            if grid[i][j] == 'X' {
                for di in &ds {
                    for dj in &ds {
                        if *di == 0 && *dj == 0 {
                            continue;
                        }
                        let mut found = true;
                        for d in 1..4 {
                            let i1 = (i as i64) + di * (d as i64);
                            let j1 = (j as i64) + dj * (d as i64);
                            if i1 < 0
                                || i1 >= (m as i64)
                                || j1 < 0
                                || j1 >= (n as i64)
                                || grid[i1 as usize][j1 as usize] != key[d]
                            {
                                found = false;
                                break;
                            }
                        }
                        if found {
                            p1 += 1;
                        }
                    }
                }
            }
            if grid[i][j] == 'A' {
                if i == 0 || i == m - 1 || j == 0 || j == n - 1 {
                    continue;
                }
                let a = grid[i - 1][j - 1];
                let b = grid[i - 1][j + 1];
                let c = grid[i + 1][j + 1];
                let d = grid[i + 1][j - 1];
                match (a, b, c, d) {
                    ('M', 'M', 'S', 'S')
                    | ('S', 'M', 'M', 'S')
                    | ('S', 'S', 'M', 'M')
                    | ('M', 'S', 'S', 'M') => p2 += 1,
                    _ => {}
                }
            }
        }
    }
    println!("{}", p1);
    println!("{}", p2);
}

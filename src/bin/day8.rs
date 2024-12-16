use gcd::Gcd;
use std::{collections::{HashSet, HashMap},fs};

fn main() {
    let data = fs::read_to_string("data/8.in").expect("Unable to read file");
    let grid: Vec<Vec<_>> = data
        .trim()
        .split_whitespace()
        .map(|line| line.chars().collect())
        .collect();
    let m = grid.len();
    let n = grid[0].len();
    let mut nodes = HashMap::<char, Vec<(i64, i64)>>::new();
    for i in 0..m {
        for j in 0..n {
            if grid[i][j] != '.' {
                nodes.entry(grid[i][j]).or_insert(Vec::new()).push((i as i64, j as i64));
            }
        }
    }
    let mut antinodes1 = HashSet::<(i64, i64)>::new();
    let mut antinodes2 = HashSet::<(i64, i64)>::new();
    for locs in nodes.values().cloned() {
        for i in 0..locs.len() {
            for j in 0..locs.len() {
                if i == j {
                    continue;
                }
                let (r0, c0) = locs[i];
                let (r1, c1) = locs[j];
                let (dr, dc) = (r1 - r0, c1 - c0);
                let (r2, c2) = (r1 + dr, c1 + dc);
                if 0 <= r2 && r2 < m as i64 && 0 <= c2 && c2 < n as i64 {
                    antinodes1.insert((r2, c2));
                }
                let gcd = (dr.abs() as usize).gcd(dc.abs() as usize);
                let mut r = r0 + dr / gcd as i64;
                let mut c = c0 + dc / gcd as i64;
                while 0 <= r && r < m as i64 && 0 <= c && c < n as i64 {
                    antinodes2.insert((r, c));
                    r += dr / gcd as i64;
                    c += dc / gcd as i64;
                }
            }
        }
    }

    let p1 = antinodes1.len();
    println!("{}", p1);

    let p2 = antinodes2.len();
    println!("{}", p2);
}

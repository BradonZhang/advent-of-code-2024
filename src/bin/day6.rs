use std::{collections::HashSet, fs};

fn main() {
    let data = fs::read_to_string("data/6.in").expect("Unable to read file");
    let grid: Vec<Vec<_>> = data
        .trim()
        .split_whitespace()
        .map(|line| line.chars().collect())
        .collect();

    let m = grid.len() as i64;
    let n = grid[0].len() as i64;
    let caret = data.find('^').unwrap() as i64;
    let x0 = caret % (n + 1);
    let y0 = caret / (n + 1);
    let dirs = [(1i64, 0i64), (0, 1), (-1, 0), (0, -1)];

    let sim = |bx: i64, by: i64| {
        let mut seen1 = HashSet::<(i64, i64)>::new();
        if (bx, by) == (x0, y0) {
            return Some(seen1);
        }

        let mut x = x0;
        let mut y = y0;
        let mut d = 3;

        let mut seen2 = HashSet::<(i64, i64, usize)>::new();
        seen1.insert((x, y));
        seen2.insert((x, y, d));

        loop {
            let (dx, dy) = dirs[d];
            let x1 = x + dx;
            let y1 = y + dy;
            if x1 < 0 || x1 >= n || y1 < 0 || y1 >= m {
                return Some(seen1);
            }
            if grid[y1 as usize][x1 as usize] == '#' || (x1, y1) == (bx, by) {
                d = (d + 1) % 4;
            } else {
                x = x1;
                y = y1;
                let key = (x, y, d);
                if seen2.contains(&key) {
                    return None;
                }
                seen1.insert((x, y));
                seen2.insert((x, y, d));
            }
        }
    };

    let seen = sim(-1, -1).unwrap();
    let p1 = seen.len();
    println!("{}", p1);

    let p2: usize = seen
        .iter()
        .map(|(bx, by)| match sim(*bx, *by) {
            Some(_) => 0,
            None => 1,
        })
        .sum();
    println!("{}", p2);
}

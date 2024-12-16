use std::{
    collections::{HashMap, HashSet, VecDeque},
    fs,
};

fn main() {
    let data = fs::read_to_string("data/5.in").expect("Unable to read file");

    let (rules_text, updates_text) = data.trim().split_once("\n\n").unwrap();
    let rules: Vec<(i64, i64)> = rules_text
        .split('\n')
        .map(|line| match line.split_once('|') {
            Some((a, b)) => (a.parse::<i64>().unwrap(), b.parse::<i64>().unwrap()),
            None => panic!(),
        })
        .collect();
    let mut deps = HashMap::<i64, HashSet<i64>>::new();
    for (a, b) in rules {
        deps.entry(a).or_insert(HashSet::new());
        deps.entry(b).or_insert(HashSet::new()).insert(a);
    }

    let updates: Vec<Vec<i64>> = updates_text
        .split('\n')
        .map(|line| line.split(',').map(|num| num.parse().unwrap()).collect())
        .collect();

    let mut p1 = 0;
    let mut p2 = 0;
    for update in updates {
        let update_set: HashSet<i64> = HashSet::from_iter(update.iter().copied());
        let mut todo = update_set.clone();
        for num in update.iter().copied() {
            match deps.get(&num) {
                Some(num_deps) => {
                    if todo.intersection(&num_deps).count() > 0 {
                        break;
                    }
                },
                None => {},
            }
            todo.remove(&num);
        }
        if todo.len() == 0 {
            p1 += update[update.len() / 2];
        } else {
            let mut minideps: HashMap<i64, HashSet<i64>> = HashMap::new();
            let mut leaves: VecDeque<i64> = VecDeque::new();
            for num in update.iter().copied() {
                let num_deps = HashSet::<i64>::from_iter(deps.get(&num).unwrap().intersection(&update_set).map(|s| *s));
                if num_deps.is_empty() {
                    leaves.push_back(num);
                } else {
                    minideps.insert(num, num_deps);
                }
            }
            let mut order: Vec<i64> = Vec::new();
            while !leaves.is_empty() {
                let leaf = leaves.pop_front().unwrap();
                order.push(leaf);
                let keys: Vec<i64> = minideps.keys().cloned().collect();
                for key in keys {
                    minideps.entry(key).and_modify(|key_deps| {
                        key_deps.remove(&leaf);
                    });
                    if minideps.get(&key).unwrap().is_empty() {
                        minideps.remove(&key);
                        leaves.push_back(key);
                    }
                }
            }
            p2 += order[order.len() / 2];
        }
    }
    println!("{}", p1);
    println!("{}", p2);
}

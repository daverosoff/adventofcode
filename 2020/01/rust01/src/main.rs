use std::env;
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let args: Vec<String> = env::args().collect();
    println!("{:?}", args);
    //println!("Hello, world!");
    let query = &args[1];
    let filename = &args[2];
    println!("In file {}", filename);

    let mut f = File::open(filename).expect("File not found");

    let mut contents = String::new();
    f.read_to_string(&mut contents)
        .expect("Something went wrong reading the file");

    println!("With text:\n{}", contents);
}

use std::collections::{HashMap, HashSet};
use std::fs;
use std::io;

// Function to generate a report of file sizes on a given path and its subdirectories.
fn get_file_sizes(path: &str) -> HashMap<String, u64> {
    let mut file_sizes = HashMap::new();

    for entry in fs::read_dir(path).unwrap() {
        let entry = entry.unwrap();
        let file_path = entry.path().to_str().unwrap();

        if fs::metadata(&file_path).is_ok() {
            let size = fs::metadata(&file_path).unwrap().len::<u64>();

            // Check if the file path is a directory
            if fs::read_dir(file_path).is_err() {
                *file_sizes.entry(file_path.to_str().unwrap().to_string()).or_insert(0) += size;
            }
        } else {
            println!("Failed to get size for: {}", file_path);
        }
    }

    file_sizes
}

// Function to find unique words in a given text.
fn find_unique_words(text: &str) -> HashSet<String> {
    let words = text.split_whitespace()
                      .map(|s| s.to_lowercase())
                      .filter(|&s| !s.is_empty())
                      .collect::<HashSet<_>>();

    words
}

// Function to compress a string by replacing repeated characters with the count of repetitions.
fn compress_string(input: &str) -> String {
    let mut compressed = String::new();
    let mut char_count = 1;

    for i in 1..input.len() {
        if input.chars().nth(i).unwrap() == input.chars().nth(i - 1).unwrap() {
            char_count += 1;
        } else {
            compressed.push_str(&format!("{}{}", char_count, input.chars().nth(i - 1).unwrap()));
            char_count = 1;
        }
    }

    compressed.push_str(&format!("{}", char_count));
    compressed
}

// Function to decompress a string by replacing repeated characters with the original character repeated that many times.
fn decompress_string(compressed: &str) -> String {
    let mut decompressed = String::new();

    for i in 0..compressed.len() {
        if i + 1 < compressed.len() && compressed.chars().nth(i).unwrap() == compressed.chars().nth(i + 1).unwrap() {
            decompressed.push_str(&compressed.chars().nth(i).unwrap().to_string().repeat(compressed.chars().nth(i + 1).unwrap() as usize));
        } else {
            decompressed.push(compressed.chars().nth(i).unwrap());
        }
    }

    decompressed
}

fn main() {
    let path = "/path/to/your/files";

    // Print file sizes for the given path and its subdirectories.
    println!("File Sizes:");
    for (file_path, size) in get_file_sizes(path).into_iter() {
        println!("{}: {}", file_path, size);
    }

    // Find unique words in a text.
    let text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.";
    let unique_words = find_unique_words(text);
    println!("Unique Words:");
    for word in unique_words {
        println!("{}", word);
    }

    // Compress and decompress strings.
    let input_string = "aaaabbbccc";
    let compressed_str = compress_string(input_string);
    println!("Compressed String: {}", compressed_str);

    let decompressed_str = decompress_string(compressed_str);
    println!("Decompressed String: {}", decompressed_str);
}

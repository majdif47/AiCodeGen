// Create a simple data structure to store books
struct Book {
    title: String,
    author: String,
    publication_year: i32,
}

impl Book {
    // Function to add a new book to the library
    fn new(title: &str, author: &str, year: i32) -> Book {
        Book {
            title: title.to_string(),
            author: author.to_string(),
            publication_year: year,
        }
    }

    // Function to print a book's details
    fn print_book(&self) {
        println!("Title: {}", self.title);
        println!("Author: {}", self.author);
        println!("Publication Year: {}", self.publication_year);
    }
}

// Create a library with some books
fn main() {
    let mut library = Vec::new();

    // Add some books to the library
    library.push(Book::new("1984", "George Orwell", 1949));
    library.push(Book::new("To Kill a Mockingbird", "Harper Lee", 1960));
    library.push(Book::new("The Great Gatsby", "F. Scott Fitzgerald", 1925));

    // Print each book's details
    for i in 0..library.len() {
        let book = &library[i];
        println!("Book {}:".to_string());
        book.print_book();
        println!();
    }

    // Search for a specific book by title
    for i in 0..library.len() {
        if library[i].title.contains("Orwell") {
            println!("Found the book '1984' in the library:");
            library[i].print_book();
            println!();
        }
    }
}

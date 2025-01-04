// File: todo_app.rs

use std::collections::{HashSet, VecDeque};

struct TodoApp {
    tasks: HashSet<String>,
    completed_tasks: HashSet<String>,
    queue: VecDeque<String>,
}

impl TodoApp {
    fn new() -> Self {
        TodoApp {
            tasks: HashSet::new(),
            completed_tasks: HashSet::new(),
            queue: VecDeque::new(),
        }
    }

    fn add_task(&mut self, task: String) {
        if !self.tasks.contains(&task) {
            self.tasks.insert(task);
            println!("Task added: {}", task);
        } else {
            println!("Task already exists.");
        }
    }

    fn complete_task(&mut self, task: String) -> bool {
        if let Some(index) = self.queue.iter().position(|t| t == &task) {
            self.completed_tasks.insert(task.clone());
            self.tasks.remove(&task);
            self.queue.remove(index);
            println!("Task completed: {}", task);

            true
        } else {
            false
        }
    }

    fn add_to_queue(&mut self, task: String) {
        if !self.tasks.contains(&task) && !self.completed_tasks.contains(&task) {
            self.queue.push_back(task.clone());
            println!("Task added to queue: {}", task);
        } else {
            println!("Task already exists.");
        }
    }

    fn view_tasks(&self) {
        let mut tasks = String::new();
        for t in &self.tasks {
            tasks += t + ", ";
        }
        tasks.pop();
        println!("Open Tasks: {}", tasks);

        let mut completed_tasks = String::new();
        for t in &self.completed_tasks {
            completed_tasks += t + ", ";
        }
        completed_tasks.pop();
        println!("Completed Tasks: {}", completed_tasks);
    }
}

fn main() {
    let mut todo_app = TodoApp::new();

    todo_app.add_task("Buy milk".to_string());
    todo_app.add_task("Walk the dog".to_string());
    todo_app.add_to_queue("Call John".to_string());

    println!("Queue: {}", todo_app.queue.iter().collect::<Vec<_>>().join(", "));
    println!("Tasks: ");

    todo_app.view_tasks();

    todo_app.complete_task("Buy milk".to_string());
    todo_app.complete_task("Walk the dog".to_string());

    todo_app.view_tasks();
}

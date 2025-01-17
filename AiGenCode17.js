// Create a class for a todo list
class TodoList {
  constructor() {
    this.tasks = [];
  }

  // Method to add new task
  addTask(task) {
    this.tasks.push({ description: task, completed: false });
  }

  // Method to complete task
  completeTask(index) {
    if (index >= 0 && index < this.tasks.length) {
      this.tasks[index].completed = true;
    }
  }

  // Method to view all tasks
  viewTasks() {
    return this.tasks.map((task, index) => 
      `Task ${index + 1}: ${task.description} - Completed: ${task.completed}`);
  }

  // Method to delete task
  deleteTask(index) {
    if (index >= 0 && index < this.tasks.length) {
      this.tasks.splice(index, 1);
    }
  }
}

// Create a new todo list instance
const todoList = new TodoList();

// Add some sample tasks
todoList.addTask('Buy milk');
todoList.addTask('Finish project');
todoList.addTask('Learn JavaScript');

// View all tasks
console.log(todoList.viewTasks());

// Complete the second task
todoList.completeTask(1);

// View all tasks again
console.log(todoList.viewTasks());

// Delete the first task
todoList.deleteTask(0);

// View all tasks again
console.log(todoList.viewTasks());

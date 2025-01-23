import datetime
import sqlite3
from colorama import init, Fore, Back, Style

# Initialize Colorama
init()

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                due_date DATE
            )
        ''')
        self.conn.commit()

    def add_task(self, title, description, due_date):
        try:
            self.cursor.execute("INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)", 
                                (title, description, due_date))
            self.conn.commit()
            print(f"Task added successfully: {title}")
        except sqlite3.Error as e:
            print(f"Error adding task: {e}")

    def view_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        rows = self.cursor.fetchall()
        for row in rows:
            print(Fore.GREEN + f"ID: {row[0]} | Title: {row[1]} | Description: {row[2]} | Due Date: {row[3]}" + Style.RESET_ALL)

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Task deleted successfully with ID: {task_id}")
        else:
            print(f"No task found with ID: {task_id}")

    def update_task(self, task_id, title=None, description=None, due_date=None):
        self.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = self.cursor.fetchone()
        if row is not None:
            if title:
                row = row[:1] + (title,) + row[2:]
            if description:
                row = row[:3] + (description,) + row[4:]
            if due_date:
                row = row[:5] + (due_date,) + row[6:]
            self.cursor.execute("UPDATE tasks SET title = ?, description = ?, due_date = ? WHERE id = ?", 
                                (*row, title or None, description or None, due_date or None))
            self.conn.commit()
            print(f"Task updated successfully with ID: {task_id}")
        else:
            print(f"No task found with ID: {task_id}")


def main():
    db_name = 'tasks.db'
    db = Database(db_name)

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            db.add_task(title, description, due_date)
        elif choice == '2':
            db.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            db.delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new task title (press enter to skip): ")
            description = input("Enter new task description (press enter to skip): ")
            due_date = input("Enter new task due date (YYYY-MM-DD) (press enter to skip): ")
            db.update_task(task_id, title or None, description or None, due_date or None)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

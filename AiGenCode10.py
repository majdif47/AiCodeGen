import datetime
import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack()

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.display_tasks_label = tk.Label(self.root, text="Tasks:")
        self.display_tasks_label.pack()

        self.tasks_listbox = tk.Listbox(self.root)
        self.tasks_listbox.pack()
        self.update_tasks_list()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.display_tasks_list()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            index = self.tasks_listbox.curselection()[0]
            del self.tasks[index]
            self.display_tasks_list()
        except IndexError:
            messagebox.showerror("Error", "Select a task to delete")

    def display_tasks_list(self):
        for widget in self.tasks_listbox.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            tk.Label(self.tasks_listbox, text=f"{i+1}. {task}").pack()

    def update_tasks_list(self):
        self.display_tasks_list()
        self.root.after(1000, self.update_tasks_list)

def main():
    root = tk.Tk()
    root.title("Todo List App")
    TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

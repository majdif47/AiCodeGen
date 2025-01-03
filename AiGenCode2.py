import datetime
from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    name: str
    description: str
    deadline: datetime.date
    priority: int

def get_today_date():
    return datetime.date.today()

def create_task(name: str, description: str, deadline: datetime.date):
    task = Task(name=name, description=description, deadline=deadline, priority=1)
    print(f"Task created: {task.name} - Deadline: {task.deadline}")
    return task

def list_tasks(tasks: List[Task]):
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task.deadline < get_today_date() else "Due"
        print(f"{i}. Name: {task.name} - Status: {status}")

def update_task_status(task_name: str, new_status: str):
    tasks = [
        Task(name="Buy Milk", description="Buy milk from grocery store", deadline=get_today_date(), priority=1),
        Task(name="Finish Project", description="Finish project by end of week", deadline=datetime.date(2024, 3, 15), priority=2)
    ]
    task_to_update = next((task for task in tasks if task.name == task_name), None)

    if task_to_update:
        if new_status.lower() == "completed":
            print(f"Task {task_name} is completed.")
        elif new_status.lower() == "due":
            print(f"Task {task_name} has been marked due.")
        else:
            print("Invalid status. Please use 'Completed' or 'Due'.")
    else:
        print("Task not found.")

def main():
    tasks = []
    while True:
        print("\n1. Create Task\n2. List Tasks\n3. Update Task Status\n4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            deadline = datetime.datetime.strptime(input("Enter deadline (YYYY-MM-DD): "), "%Y-%m-%d").date()
            tasks.append(create_task(name, description, deadline))
            
        elif choice == "2":
            list_tasks(tasks)
            
        elif choice == "3":
            name = input("Enter task name: ")
            new_status = input("Enter new status (Completed/Due): ")
            update_task_status(name, new_status)
            
        elif choice == "4":
            break
            
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()

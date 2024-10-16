import json
import argparse

# Dummy credentials
USERNAME = "testuser"
PASSWORD = "password123"

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"ID: {self.id}, Title: {self.title}, Status: {status}"

task_list = []

def login():
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")
    
    if username_input == USERNAME and password_input == PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Exiting...")
        return False

def add_task(task_id, title):
    task = Task(task_id, title)
    task_list.append(task)

def view_tasks():
    if not task_list:
        print("No tasks available.")
        return
    for task in task_list:
        print(task)

def delete_task(task_id):
    global task_list
    task_list = [task for task in task_list if task.id != task_id]

def complete_task(task_id):
    for task in task_list:
        if task.id == task_id:
            task.completed = True
            break

def save_tasks():
    tasks_data = [{"id": task.id, "title": task.title, "completed": task.completed} for task in task_list]
    with open('tasks.json', 'w') as file:
        json.dump(tasks_data, file, indent=4)

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks_data = json.load(file)
            for task in tasks_data:
                task_list.append(Task(task['id'], task['title'], task['completed']))
    except FileNotFoundError:
        pass

def main():
    if not login():
        return  # Exit if login fails
    load_tasks()

    while True:
        print("\nAvailable actions: add, view, delete, complete, exit")
        action = input("Enter action: ")

        if action == 'add':
            title = input("Enter task title: ")
            add_task(len(task_list) + 1, title)  # Auto-incrementing task ID
            save_tasks()
            print(f"Task added: {title}")
        elif action == 'view':
            view_tasks()
        elif action == 'delete':
            task_id_input = input("Enter task ID to delete: ")
            try:
                task_id = int(task_id_input)  # Convert to int
                delete_task(task_id)
                save_tasks()
                print(f"Task ID {task_id} deleted.")
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif action == 'complete':
            task_id_input = input("Enter task ID to complete: ")
            try:
                task_id = int(task_id_input)  # Convert to int
                complete_task(task_id)
                save_tasks()
                print(f"Task ID {task_id} marked as complete.")
            except ValueError:
                print("Invalid task ID. Please enter a number.")
        elif action == 'exit':
            save_tasks()
            print("Exiting the application.")
            break  # Exit the loop
        else:
            print("Invalid command. Please try again.")

if __name__ == '__main__':
    main()

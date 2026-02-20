import json
import argparse
import os
import hashlib
from exceptions import (
    TaskManagerError,
    UserAlreadyExistsError,
    UserNotFoundError,
    InvalidPasswordError,
    TaskNotFoundError,
    InvalidInputError
)

class TaskManager:

    def __init__(self, users_file, session_file, tasks_folder):
        self.users_file = users_file
        self.session_file = session_file
        self.tasks_folder = tasks_folder
 
#Password hashing 
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


#loading and saving  the users in user.json
    def load_users(self):
        if not os.path.exists(self.users_file):
            return {}
        with open(self.users_file, "r") as f:
            return json.load(f)

    def save_users(self, users):
        with open(self.users_file, "w") as f:
            json.dump(users, f, indent=4)


##REGISTERING THE USER 
    def register_user(self, username, password):
        users = self.load_users()

        if username in users:
            raise UserAlreadyExistsError("User already exists.")

        users[username] = {
            "password": self.hash_password(password)
        }

        self.save_users(users) 

        self.login_user(username, password)
#login 
    def login_user(self, username, password):
            users = self.load_users()

            if username not in users:
                raise UserNotFoundError("User is not there!!.")

            if users[username]["password"] != self.hash_password(password):
                raise InvalidPasswordError("Incorrect password.")

            with open(self.session_file, "w") as f:
                json.dump({"current_user": username}, f)

##fetching the login user 
    def get_current_user(self):
        if not os.path.exists(self.session_file):
            raise InvalidInputError("You must login first.")

        with open(self.session_file, "r") as f:
            session = json.load(f)

        user = session.get("current_user")

        if not user:
            raise InvalidInputError("You must login first.")

        return user
    
##logout 
    def logout_user(self):
            if not os.path.exists(self.session_file):
                raise InvalidInputError("No user logged in!!")

            with open(self.session_file, "w") as f:
                json.dump({"current_user": None}, f)

##Geting the User 
    def get_user_file(self):
        user = self.get_current_user()

        if not os.path.exists(self.tasks_folder):
            os.makedirs(self.tasks_folder)

        return os.path.join(self.tasks_folder, f"{user}.json") 


##CRUD operations 
    def load_tasks(self):
        file_path = self.get_user_file()

        if not os.path.exists(file_path):
            return []

        with open(file_path, "r") as f:
            return json.load(f)

    def save_tasks(self, tasks):
        file_path = self.get_user_file()

        with open(file_path, "w") as f:
            json.dump(tasks, f, indent=4)

    def update_task(self, task_no, name=None, time=None, priority=None, due=None, status=None):
        tasks = self.load_tasks()

        if 1 <= task_no <= len(tasks):
            task = tasks[task_no - 1]

            if name:
                task["name"] = name
            if time:
                task["time"] = time
            if priority is not None:
                task["priority"] = priority
            if due:
                task["due"] = due
            if status:
                task["status"] = status

            self.save_tasks(tasks)
        else:
            raise TaskNotFoundError("Task not found.")

    def add_task(self, name, time, priority, due):
        tasks = self.load_tasks()

        tasks.append({
            "name": name,
            "time": time,
            "priority": priority,
            "due": due,
            "status": "pending"
        })

        self.save_tasks(tasks)

    def delete_task(self, task_no):
        tasks = self.load_tasks()

        if 1 <= task_no <= len(tasks):
            removed_task = tasks.pop(task_no - 1)
            self.save_tasks(tasks)
            return removed_task   
        else:
            raise TaskNotFoundError("Task not found.")
        
    def show_tasks(self, status=None, priority=None, due=None):
        tasks = self.load_tasks()

        filtered_tasks = tasks

        if status:
            filtered_tasks = [t for t in filtered_tasks if t["status"] == status]

        if priority is not None:
            filtered_tasks = [t for t in filtered_tasks if t["priority"] == priority]

        if due:
            filtered_tasks = [t for t in filtered_tasks if t["due"] == due]

        if not filtered_tasks:
            raise TaskNotFoundError("No matching tasks found.")

        return filtered_tasks

def main():

    manager = TaskManager(
        users_file="users.json",
        session_file="session.json",
        tasks_folder="tasks"
    )

    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Register
    register_parser = subparsers.add_parser("register")
    register_parser.add_argument("username")
    register_parser.add_argument("password")

    # Login
    login_parser = subparsers.add_parser("login")
    login_parser.add_argument("username")
    login_parser.add_argument("password")

    # Add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("name")
    add_parser.add_argument("--time", required=True)
    add_parser.add_argument("--priority", type=int, choices=[1,2,3], required=True)
    add_parser.add_argument("--due", required=True)

    # List
    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--status", choices=["pending", "completed"])
    list_parser.add_argument("--priority", type=int, choices=[1,2,3])
    list_parser.add_argument("--due")

    # Delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("task_no", type=int)

    # Update
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("task_no", type=int)
    update_parser.add_argument("--name")
    update_parser.add_argument("--time")
    update_parser.add_argument("--priority", type=int, choices=[1,2,3])
    update_parser.add_argument("--due")
    update_parser.add_argument("--status", choices=["pending", "completed"])

    # Logout
    subparsers.add_parser("logout")

    args = parser.parse_args()

    try:
        if args.command == "register":
            manager.register_user(args.username, args.password)
            print(f"User registered successfully! Welcome {args.username}!")

        elif args.command == "login":
            manager.login_user(args.username, args.password)
            print(f"Welcome {args.username}!")

        elif args.command == "add":
            manager.add_task(args.name, args.time, args.priority, args.due)
            print("Task added successfully!")

        elif args.command == "list":
            tasks = manager.show_tasks(args.status, args.priority, args.due)

            for i, task in enumerate(tasks, start=1):
                print(
                    f"{i}. {task['name']} | "
                    f"Time: {task['time']} | "
                    f"Priority: {task['priority']} | "
                    f"Due: {task['due']} | "
                    f"Status: {task['status']}"
                )

        elif args.command == "delete":
            deleted = manager.delete_task(args.task_no)
            print(f"Deleted task: {deleted}")

        elif args.command == "update":
            if not any([args.name, args.time, args.priority, args.due, args.status]):
                raise InvalidInputError("Provide at least one field to update.")

            manager.update_task(
                args.task_no,
                args.name,
                args.time,
                args.priority,
                args.due,
                args.status
            )
            print("Task updated successfully!")

        elif args.command == "logout":
            manager.logout_user()
            print("Logged out successfully!")

    except TaskManagerError as e:
        print(f"Error: {e}")

        


if __name__ == "__main__":
    main()

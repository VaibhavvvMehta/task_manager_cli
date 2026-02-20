# Task Manager CLI Application

A comprehensive command-line task management system built with Python, featuring user authentication, task CRUD operations, and advanced filtering capabilities.

## Features

- 🔐 **User Authentication**: Secure user registration and login with password hashing
- 📝 **Task Management**: Create, update, delete, and view tasks
- 🔍 **Advanced Filtering**: Filter tasks by status, priority, and due date
- 👤 **Multi-User Support**: Each user has their own isolated task list
- 🛡️ **Error Handling**: Comprehensive error handling with custom exceptions
- 💾 **Data Persistence**: JSON-based storage for users and tasks
- ✅ **Unit Tested**: Full test coverage with pytest

## Installation

1. **Clone or download the project files**
2. **Install dependencies**:
   ```bash
   pip install pytest  # For running tests (optional)
   ```
3. **Navigate to the project directory**:
   ```bash
   cd /path/to/task-manager
   ```

## Project Structure

```
task-manager/
├── task_manager.py      # Main application file
├── exceptions.py        # Custom exception classes
├── README.md           # This file
├── test/
│   └── test_task_manager.py  # Unit tests
├── users.json          # User data (created automatically)
├── session.json        # Current session data (created automatically)
└── tasks/              # User task files (created automatically)
    ├── alice.json
    ├── bob.json
    └── ...
```

## Usage

### Basic Command Structure
```bash
python3 task_manager.py <command> [arguments] [options]
```

---

## Commands Reference

### 1. **register** - Register a New User

**Syntax:**
```bash
python3 task_manager.py register <username> <password>
```

**Examples:**
```bash
# Register a new user named 'alice' with password 'password123'
python3 task_manager.py register alice password123

# Register user 'john' with password 'securepass456'
python3 task_manager.py register john securepass456
```

**Output:**
```
User registered successfully! Welcome alice!
```

**Errors:**
```bash
# Trying to register an existing user
python3 task_manager.py register alice password123
# Output: Error: User already exists.
```

---

### 2. **login** - Login to Your Account

**Syntax:**
```bash
python3 task_manager.py login <username> <password>
```

**Examples:**
```bash
# Login as alice
python3 task_manager.py login alice password123

# Login as john
python3 task_manager.py login john securepass456
```

**Output:**
```
Welcome alice!
```

**Errors:**
```bash
# Wrong password
python3 task_manager.py login alice wrongpassword
# Output: Error: Incorrect password.

# Non-existent user
python3 task_manager.py login nonuser password
# Output: Error: User not found.
```

---

### 3. **add** - Add a New Task

**Syntax:**
```bash
python3 task_manager.py add "<task_name>" --time "<time_estimate>" --priority <1|2|3> --due "<due_date>"
```

**Parameters:**
- `task_name`: Task description (use quotes if it contains spaces)
- `--time`: Time estimate (required)
- `--priority`: Priority level: 1 (High), 2 (Medium), 3 (Low) (required)
- `--due`: Due date in YYYY-MM-DD format (required)

**Examples:**
```bash
# Add a high-priority morning exercise task
python3 task_manager.py add "Morning Exercise" --time "6:00 AM" --priority 1 --due "2026-02-20"

# Add a medium-priority grocery shopping task
python3 task_manager.py add "Buy Groceries" --time "2 hours" --priority 2 --due "2026-02-21"

# Add a low-priority entertainment task
python3 task_manager.py add "Watch Movie" --time "3 hours" --priority 3 --due "2026-02-23"

# Add a work-related task
python3 task_manager.py add "Finish Project Report" --time "4 hours" --priority 1 --due "2026-02-22"
```

**Output:**
```
Task added successfully!
```

**Errors:**
```bash
# Not logged in
python3 task_manager.py add "Task" --time "1 hour" --priority 1 --due "2026-02-25"
# Output: Error: You must login first.

# Missing required parameters
python3 task_manager.py add "Task" --time "1 hour"
# Output: error: the following arguments are required: --priority, --due

# Invalid priority
python3 task_manager.py add "Task" --time "1 hour" --priority 5 --due "2026-02-25"
# Output: error: argument --priority: invalid choice: '5' (choose from 1, 2, 3)
```

---

### 4. **list** - View Tasks

**Syntax:**
```bash
python3 task_manager.py list [--status <pending|completed>] [--priority <1|2|3>] [--due <date>]
```

**Examples:**

#### List All Tasks:
```bash
python3 task_manager.py list
```
**Output:**
```
1. Morning Exercise | Time: 6:00 AM | Priority: 1 | Due: 2026-02-20 | Status: pending
2. Buy Groceries | Time: 2 hours | Priority: 2 | Due: 2026-02-21 | Status: pending
3. Watch Movie | Time: 3 hours | Priority: 3 | Due: 2026-02-23 | Status: completed
```

#### Filter by Status:
```bash
# Show only pending tasks
python3 task_manager.py list --status pending

# Show only completed tasks
python3 task_manager.py list --status completed
```

#### Filter by Priority:
```bash
# Show high-priority tasks (priority 1)
python3 task_manager.py list --priority 1

# Show medium-priority tasks (priority 2)
python3 task_manager.py list --priority 2

# Show low-priority tasks (priority 3)
python3 task_manager.py list --priority 3
```

#### Filter by Due Date:
```bash
# Show tasks due on specific date
python3 task_manager.py list --due "2026-02-20"
```

#### Combine Filters:
```bash
# Show pending high-priority tasks
python3 task_manager.py list --status pending --priority 1

# Show completed tasks due on specific date
python3 task_manager.py list --status completed --due "2026-02-20"
```

**Errors:**
```bash
# Not logged in
python3 task_manager.py list
# Output: Error: You must login first.

# No tasks found
python3 task_manager.py list --status completed
# Output: Error: No matching tasks found.

# No tasks at all
python3 task_manager.py list
# Output: Error: No matching tasks found.
```

---

### 5. **update** - Update an Existing Task

**Syntax:**
```bash
python3 task_manager.py update <task_number> [--name "<new_name>"] [--time "<new_time>"] [--priority <1|2|3>] [--due "<new_date>"] [--status <pending|completed>]
```

**Examples:**

#### Update Task Status:
```bash
# Mark task 1 as completed
python3 task_manager.py update 1 --status completed

# Mark task 2 as pending
python3 task_manager.py update 2 --status pending
```

#### Update Task Name:
```bash
# Change task name
python3 task_manager.py update 2 --name "Buy Organic Groceries"
```

#### Update Multiple Fields:
```bash
# Update name, priority, and status
python3 task_manager.py update 2 --name "Updated Task" --priority 1 --status completed

# Update time and due date
python3 task_manager.py update 3 --time "5 hours" --due "2026-02-25"
```

#### Update Priority:
```bash
# Change priority to high
python3 task_manager.py update 2 --priority 1

# Change priority to low
python3 task_manager.py update 3 --priority 3
```

**Output:**
```
Task updated successfully!
```

**Errors:**
```bash
# Invalid task number
python3 task_manager.py update 99 --status completed
# Output: Error: Task not found.

# No fields to update
python3 task_manager.py update 1
# Output: Error: Provide at least one field to update.

# Invalid status value
python3 task_manager.py update 1 --status invalid_status
# Output: error: argument --status: invalid choice: 'invalid_status' (choose from pending, completed)
```

---

### 6. **delete** - Delete a Task

**Syntax:**
```bash
python3 task_manager.py delete <task_number>
```

**Examples:**
```bash
# Delete task number 3
python3 task_manager.py delete 3

# Delete task number 1
python3 task_manager.py delete 1
```

**Output:**
```
Deleted task: {'name': 'Watch Movie', 'time': '3 hours', 'priority': 3, 'due': '2026-02-23', 'status': 'pending'}
```

**Errors:**
```bash
# Invalid task number
python3 task_manager.py delete 99
# Output: Error: Task not found.

# Not logged in
python3 task_manager.py delete 1
# Output: Error: You must login first.
```

---

### 7. **logout** - Logout Current User

**Syntax:**
```bash
python3 task_manager.py logout
```

**Examples:**
```bash
# Logout current user
python3 task_manager.py logout
```

**Output:**
```
Logged out successfully!
```

---

## Complete Workflow Example

Here's a complete example showing how to use the task manager:

```bash
# 1. Register a new user
python3 task_manager.py register alice password123
# Output: User registered successfully! Welcome alice!

# 2. Add some tasks
python3 task_manager.py add "Morning Workout" --time "1 hour" --priority 1 --due "2026-02-20"
# Output: Task added successfully!

python3 task_manager.py add "Buy Groceries" --time "2 hours" --priority 2 --due "2026-02-21"
# Output: Task added successfully!

python3 task_manager.py add "Watch Netflix" --time "2 hours" --priority 3 --due "2026-02-22"
# Output: Task added successfully!

# 3. List all tasks
python3 task_manager.py list
# Output:
# 1. Morning Workout | Time: 1 hour | Priority: 1 | Due: 2026-02-20 | Status: pending
# 2. Buy Groceries | Time: 2 hours | Priority: 2 | Due: 2026-02-21 | Status: pending
# 3. Watch Netflix | Time: 2 hours | Priority: 3 | Due: 2026-02-22 | Status: pending

# 4. Complete the first task
python3 task_manager.py update 1 --status completed
# Output: Task updated successfully!

# 5. List only high-priority tasks
python3 task_manager.py list --priority 1
# Output:
# 1. Morning Workout | Time: 1 hour | Priority: 1 | Due: 2026-02-20 | Status: completed

# 6. Update task details
python3 task_manager.py update 2 --name "Buy Organic Groceries" --priority 1
# Output: Task updated successfully!

# 7. Delete a task
python3 task_manager.py delete 3
# Output: Deleted task: {'name': 'Watch Netflix', 'time': '2 hours', 'priority': 3, 'due': '2026-02-22', 'status': 'pending'}

# 8. List remaining tasks
python3 task_manager.py list
# Output:
# 1. Morning Workout | Time: 1 hour | Priority: 1 | Due: 2026-02-20 | Status: completed
# 2. Buy Organic Groceries | Time: 2 hours | Priority: 1 | Due: 2026-02-21 | Status: pending

# 9. Logout
python3 task_manager.py logout
# Output: Logged out successfully!
```

## Multi-User Example

```bash
# Register multiple users
python3 task_manager.py register alice password123
python3 task_manager.py register bob securepass456

# Alice's session
python3 task_manager.py login alice password123
python3 task_manager.py add "Alice's Task" --time "1 hour" --priority 1 --due "2026-02-20"
python3 task_manager.py logout

# Bob's session
python3 task_manager.py login bob securepass456
python3 task_manager.py add "Bob's Task" --time "2 hours" --priority 2 --due "2026-02-21"
python3 task_manager.py list
# Bob will only see his own tasks

python3 task_manager.py logout
```

## Error Handling

The application provides comprehensive error handling for various scenarios:

### Authentication Errors:
- **Wrong Password**: `Error: Incorrect password.`
- **User Not Found**: `Error: User not found.`
- **User Already Exists**: `Error: User already exists.`
- **Not Logged In**: `Error: You must login first.`

### Task Errors:
- **Task Not Found**: `Error: Task not found.`
- **No Matching Tasks**: `Error: No matching tasks found.`
- **Missing Parameters**: Detailed argparse error messages

### Input Validation:
- **Invalid Priority**: Must be 1, 2, or 3
- **Invalid Status**: Must be 'pending' or 'completed'
- **Missing Required Fields**: Clear error messages for required parameters

## Testing

Run the comprehensive test suite:

```bash
# Install pytest if not already installed
pip install pytest

# Run all tests
python3 -m pytest test/test_task_manager.py -v

# Run specific test
python3 -m pytest test/test_task_manager.py::test_register_user -v

# Run with coverage (if pytest-cov is installed)
python3 -m pytest test/test_task_manager.py --cov=task_manager
```

## Technical Details

### Security Features:
- **Password Hashing**: Uses SHA-256 for secure password storage
- **User Isolation**: Each user's tasks are stored in separate files
- **Session Management**: Secure session handling with file-based storage

### Data Storage:
- **users.json**: Stores user credentials (with hashed passwords)
- **session.json**: Stores current session information
- **tasks/{username}.json**: Individual task files for each user

### Dependencies:
- **Built-in Python modules**: `json`, `os`, `hashlib`, `argparse`
- **Testing**: `pytest` (optional, for running tests)

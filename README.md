# 📋 Task Manager CLI

> A command-line task manager built with Python — with AI-powered task decomposition via OpenAI.

**Homework Project 1** for the course *Master Developing with AI*.

---

## ✨ Features

- **Add, list, complete and remove tasks** from the terminal
- **AI-powered task splitting** — describe a complex task and GPT breaks it into subtasks automatically
- **Persistent storage** — tasks are saved to `tasks.json` and restored on startup
- **Unit tested** — core logic covered with `unittest`

---

## 📁 Project Structure

```
task-manage-py/
├── main.py               # CLI entry point and menu loop
├── task_manager.py        # Task and TaskManager classes (CRUD + persistence)
├── ai_service.py          # OpenAI integration for subtask generation
├── test_task_manager.py   # Unit tests for TaskManager
├── tasks.json             # Auto-generated task storage (created at runtime)
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** (uses `match/case` syntax)
- An **OpenAI API key** (only required for AI features)

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/task-manage-py.git
cd task-manage-py
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=sk-your-api-key-here
```

> **Note:** The `.env` file is loaded automatically by `python-dotenv`. Never commit this file to version control.

### 5. Run the application

```bash
python main.py
```

---

## 🧪 Running Tests

Tests are written with Python's built-in `unittest` framework:

```bash
python -m unittest test_task_manager -v
```

**Test coverage includes:**

| Test | Description |
|------|-------------|
| `test_load_tasks_with_valid_data` | Loads tasks from a valid JSON file |
| `test_load_tasks_sets_next_id_correctly` | Ensures `next_id` = max(id) + 1 |
| `test_load_tasks_with_empty_list` | Handles an empty task list |
| `test_load_tasks_file_not_found` | Gracefully handles missing file |
| `test_load_tasks_preserves_completed_status` | Preserves the completed flag |
| `test_load_tasks_creates_task_instances` | Verifies `Task` instances are created |
| `test_load_tasks_invalid_json_raises_exception` | Raises error on malformed JSON |

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `openai` | OpenAI API client for AI-powered subtask generation |
| `python-dotenv` | Loads environment variables from `.env` |
| `requests` | HTTP library (general purpose) |

Full dependency list: [`requirements.txt`](requirements.txt)

---

## 🎮 Usage

```
Task Manager
0. Create Simple Task using AI
1. Add Task
2. List Tasks
3. Mark Task as Completed
4. Remove Task
5. Exit
```

**Example — AI subtask generation:**

```
Enter your choice: 0
Enter the description of the task: Build a REST API with authentication
Subtasks created by AI:
1. Set up project structure and dependencies
2. Create database models for users
3. Implement JWT authentication
4. Build CRUD endpoints
5. Add input validation and error handling
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

-----

# CLI To-Do List Manager

A simple and fast command-line application for managing your daily tasks. This project is built using modern Python tooling with `uv` for project and dependency management.

-----

## Features

  * **Interactive Menu**: No need to remember commands; just choose from the on-screen menu.
  * **View Tasks**: See a clean, formatted list of your pending and completed tasks.
  * **Add & Delete Tasks**: Quickly add new tasks or remove old ones.
  * **Mark as Done**: Easily update a task's status to "done".
  * **Data Persistence**: Your tasks are saved locally in a `tasks.json` file.

-----

## Prerequisites

  * Python 3.8+
  * `uv` installed on your system. (Follow the installation guide [here](https://github.com/astral-sh/uv)).

-----

## Setup

1.  **Clone the repository** to your local machine:

    ```bash
    git clone <your-repository-url>
    ```

2.  **Navigate into the project directory**:

    ```bash
    cd <repository-name>
    ```

3.  **Create a virtual environment and install dependencies** using `uv`. This command reads the `pyproject.toml` and `uv.lock` files to create a consistent environment.

    ```bash
    uv pip sync
    ```

-----

## Usage

All commands are run from the terminal within the project directory. Make sure your virtual environment is activated.

#### **To view all tasks:**

This is the default action if no command is given.

```bash
uv run main.py
```

You will be greeted with an interactive menu. Simply type the number corresponding to your desired action and press Enter.

```
Welcome to your Interactive To-Do List

--- Menu ---
1. View Tasks
2. Add Task
3. Delete Task
4. Mark Task as Done
5. Exit
Enter your choice (1-5):
```

## Project Structure

```
.
├── main.py
├── pyproject.toml
├── README.md
├── tasks.json
└── uv.lock
```

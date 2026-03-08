# to-do_list_manager
A simple command-line to-do list manager written in Python.

This project was built to practice core programming concepts such as functions, loops, input validation, and file persistence using JSON.

## Features
- Add new tasks
- View all tasks
- Mark tasks as complete
- Delete tasks
- Persistant storage using a JSON file
- simple command-line interface

## How It Works

Tasks are stored as dictionaries inside a Python list.

Each task contains:
- ```task```: the task description
- ```done```: a boolean indicating completion status

#### Example Structure:
```
  [
    {"task": "Study biology", "done": false}, 
    {"task": "Finish Python project", "done": true}
  ]
```

The program automatically loads tasks from 
```
tasks.json
```
when it starts and saves them when the users exits.


## How to Run

1. Make sure Python is installed.
2. Download or clone this repository.
3. Run the program from the terminal:
```
python program.py
```

## Menu Options
    1) Add task
    2) View tasks
    3) Complete task
    4) Delete task
    5) Save and Exit
### Files
    tasks.json
Stores all tasks so they persist between program runs.

## Concepts Practiced
  - Functions and modular program design
  - Lists and dictionaries
  - Input validation
  - Error handling (try/except)
  - File handling
  - JSON serialization
  - CLI application structure

## Concepts to Add (Future Improvements)

- This project will continue to evolve as more programming concepts are learned.
- Planned concepts and improvements include:
- Refactoring duplicated code
- Helper functions for input validation
- Automatic saving after task updates
- Task IDs instead of list indexes
- Task priorities
- Due dates
- Sorting and filtering tasks
- Search functionality
- Code organization improvements
- Unit testing
- Logging

### Author
  [Muhammad Ayan Atif](github.com/MuAyan)

import os
import json

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print("1) Add task")
    print("2) View tasks")
    print("3) Complete task")
    print("4) Delete task")
    print("5) Save and Exit")
    choice = input("Select an option: ")
    return choice

def add_task(tasks):
    name = input("Task:" ).strip()
    while not name:
        print("Task must have a description.")
        name = input("Task:" ).strip()
    new_dict = {"task": name, "done": False}
    tasks.append(new_dict)
    print("Task Successfully added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    for index, task in enumerate(tasks, start=1):
        if task["done"]:
            print(f"{index}) [X] {task['task']}")
        else:
            print(f"{index}) [ ] {task['task']}")

def complete_task(tasks):
    if tasks:
        view_tasks(tasks)
        while True:
            try:
                numb = int(input("Which task would you like to complete?"))
                clear()
                if numb < 1 or numb > len(tasks):
                    view_tasks(tasks)
                    print("Task must be a valid task number.")
                else:
                    break
            except ValueError:
                clear()
                view_tasks(tasks)
                print("Invalid input, try again")   
        if not tasks[numb - 1]["done"]:
            tasks[numb - 1]["done"] = True
            clear()
            print(f"{tasks[numb - 1]['task']} is now complete.")
        else:
            clear()
            print("Task is already complete.")
    else:
        clear()
        print("You don't have any tasks.")


def delete_task(tasks):
    if tasks:
        view_tasks(tasks)
        while True:
            try:
                numb = int(input("Which task would you like to remove?"))
                clear()
                if numb < 1 or numb > len(tasks):
                    view_tasks(tasks)
                    print("Task must be a valid task number.")
                else:
                    break
            except ValueError:
                clear()
                view_tasks(tasks)
                print("Invalid input, try again")
        clear()
        print(f"{tasks[numb - 1]['task']} has been removed.")
        tasks.pop(numb - 1)
    else:
        clear()
        print("You don't have any tasks.")

def save_and_exit(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
    input("Tasks saved successfully, press enter to leave: ")

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

    

def main():
    tasks = load_tasks()
    while True:
        choice = menu()
        clear()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_and_exit(tasks)
            break
        else:
            print("Invalid choice.")




if __name__ == "__main__":
    main()



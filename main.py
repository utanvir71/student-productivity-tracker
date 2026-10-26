
# Student Name: ISLAM MD TANVIRUL | Student ID: 23013062

# ========== Project: Student Productivity Tracker ============

# Import modules for terminal control and the loading animation.
import subprocess
import platform
import time


# Clear the terminal and optionally wait for user confirmation.
def clear_terminal(print_prompt=True):
    if print_prompt:
        time.sleep(2)
        input("\n\n\t\t\t\t---Press Enter to go to the main menu---")
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear")


# Display a loading animation when the application starts.
def loading_screen():
    print("\n\n\n\n\t\t\t\tLOADING", end="")
    for i in range(10):
        print(" * ", end="", flush=True)
        time.sleep(.5)
    print("\n\n\n\n")


# Store tasks, unique subjects, and the permitted priority levels.
tasks = []
subjects = set()
PRIORITIES = ("low", "medium", "high")


# Validate the estimated study hours entered by the user.
def get_hours():
    while True:
        hours_text = input("\t\t\t\tEstimate study time in hours (q to exit): ").strip().lower()
        if hours_text == "q":
            return "q"
        if hours_text.count(".") <= 1 and hours_text.replace(".", "", 1).isdigit():
            hours = float(hours_text)
            if hours > 0:
                return hours
        print("\t\t\t\tInvalid number. Enter a positive number.")


# Collect task details, validate input, and add the task to the list.
def add_task():
    while True:
        title = input("\t\t\t\tEnter task name (q to exit): ").strip()
        if title == 'q':
            clear_terminal()
            return
        if title == "":
            print("\t\t\t\tTask name cannot be emptly.")
            continue
        break

    while True:
        subject = input("\t\t\t\tEnter subject (q to exit): ").strip().title()
        if subject.lower() == 'q':
            clear_terminal()
            return
        if subject == "":
            print("\t\t\t\tsubjects cannot be emptty.")
            continue
        break

    while True:
        priority = input("\t\t\t\tEnter priority (low/medium/high) (q to exit): ").strip().lower()
        if priority == 'q':
            clear_terminal()
            return
        if priority not in PRIORITIES:
            print("\t\t\t\tinvalid priority. ")
            continue
        break

    hours = get_hours()
    if hours == 'q':
        clear_terminal()
        return

    task = {
        "title": title,
        "subject": subject,
        "priority": priority.title(),
        "hours": hours,
        "completed": False
    }

    tasks.append(task)
    subjects.add(subject)
    print("\t\t\t\tTask added successfully!")
    clear_terminal()


# Display all tasks with their details and completion status.
def view_tasks(clear_after=True):
    if len(tasks) == 0:
        print("\t\t\t\tNo tasks avaialbe.")
        if clear_after:
            clear_terminal()
        return

    print("\n\t\t\t\t--- All Tasks ---")
    for number, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f""""\t\t\t\t{number}. {task['title']}
        \n\t\t\t\t   Subject: {task['subject']}
        \n\t\t\t\t   Priority: {task['priority']}
        \n\t\t\t\t   Hours: {task['hours']:.1f}
        \n\t\t\t\t   Status: {status}\n\n""")

    if clear_after:
        clear_terminal()


# Allow the user to select a task and mark it as completed.
def mark_task_completed():
    if len(tasks) == 0:
        print("\t\t\t\tNo tasks available.")
        clear_terminal()
        return

    view_tasks(False)
    while True:
        number = input("\t\t\t\tEnter task number to complete (q to exit): ")
        if number == 'q':
            break
        if not number.isdigit():
            print("\t\t\t\tEnter a valid positive whole number.")
            continue

        index = int(number) - 1
        if index < 0 or index >= len(tasks):
            print("\t\t\t\tTask number does not exist")
            continue
        elif tasks[index]["completed"]:
            print("\t\t\t\tTask already marked as completed.")
            continue
        else:
            tasks[index]["completed"] = True
            print("\t\t\t\ttask marked as completed!")
            break

    clear_terminal()


# Search task titles and subjects using a case-insensitive keyword.
def search_task():
    keyword = input("Enter search keyword: ").strip().lower()
    if keyword == "":
        print("\t\t\t\tSearch keyward cannot be empty.")
        clear_terminal()
        return

    found = False
    for task in tasks:
        if keyword in task["title"].lower() or keyword in task["subject"].lower():
            print(f"""\t\t\t\tTitle: {task['title']}
            \n\t\t\t\tSubject: {task['subject']}
            \n\t\t\t\tPriority: {task['priority']}\n""")
            found = True

    if not found:
        print("\t\t\t\tNo matching tasks found.")

    clear_terminal()


# Calculate and display task totals, pending tasks, study hours, and subjects.
def show_summary():
    total = len(tasks)
    completed = 0
    total_hours = 0.0

    for task in tasks:
        total_hours += task["hours"]
        if task["completed"]:
            completed += 1

    pending = total - completed

    print("\n\n\n\n\t\t\t\t--- Producitvity Summury ----")
    print("\t\t\t\tTotal tasks: ", total)
    print("\t\t\t\tPending tasks: ", pending)
    print(f"\t\t\t\tEstimated study hours: {total_hours:.1f}")

    if subjects:
        print("\t\t\t\tsubjects: ", ", ".join(sorted(subjects)))
    else:
        print("\t\t\t\tsubjects: None")

    clear_terminal()


# Run the main menu and direct the user to the selected feature.
def main():
    clear_terminal(False)
    loading_screen()
    clear_terminal(False)

    while True:
        print("\n\n\n\n\t\t\t\t==== STUDENT PRODUCTIVUTY TRACKER ====")
        print("\t\t\t\t1. Add a task")
        print("\t\t\t\t2. View all task")
        print("\t\t\t\t3. Mark a task as completed")
        print("\t\t\t\t4. Search tasks")
        print("\t\t\t\t5. View productivity summary")
        print("\t\t\t\t6. Exit\n\n")

        choice = input("\t\t\t\tEnter you choice: ").strip()
        clear_terminal(False)
        print("\n\n\n\n")

        if choice == "1":
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_completed()
        elif choice == '4':
            search_task()
        elif choice == "5":
            show_summary()
        elif choice == "6":
            clear_terminal(False)
            print("\n\n\n\n\n\n\n\n\t\t\t\tGoodbye! good luck with your studies.\n\n\n\n\n\n\n")
            break
        else:
            print("\t\t\t\tInvalid choice. please select 1-6.")


# Start the application.
main()

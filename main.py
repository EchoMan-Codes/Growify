# Growify - Personal Learning Dashboard

import csv
from datetime import datetime
import os

from helpers import Task, UserProfile, clear_screen
from storage import load_data, restore_tasks, save_data

# ---- Data Storage----
tasks = []
study_sessions = []
total_xp = 0
profile = None

# ---- Main Menu ----
def show_menu():
    """Displays the main menu options to the user"""
    clear_screen()
    print("\n╭──────────────────────────────────────────────────╮")
    print("│               GrowthOS - Main Menu               │")
    print("├──────────────────────────────────────────────────┤")
    print("│                                                  │")
    print("│  [1] Add Task          [5] Add Study Session     │")
    print("│  [2] View Tasks        [6] View Study Sessions   │")
    print("│  [3] Complete Task     [7] View Dashboard        │")
    print("│  [4] Delete Task       [8] Export CSV Report     │")
    print("│  [9] Edit Profile      [0] Exit                  │")
    print("╰──────────────────────────────────────────────────╯\n")


# ---- Add Task ----
def add_task():
    """Ask the user for task details and add it to the tasks list."""
    print("\n📝 Add New Task")
    print("─────────────────────────")

    name = input("➤ Task name: ").strip()

    if not name:
        print('[!] Task name cannot be empty.')
        return

    difficulty = input("➤ Difficulty (easy, medium, hard): ").strip().lower()

    if difficulty not in ['easy', 'medium', 'hard']:
        print('[!] Invalid difficulty. Using "easy" as default.')
        difficulty = 'easy'

    task = Task(name, difficulty)
    tasks.append(task)

    print(f'\n[+] Task "{task.name} added! ({task.difficulty.capitalize()} - {task.xp} XP)')


# ---- View Tasks ----
def view_tasks():
    """Display all tasks with their index number."""
    print("\n📋 Your Tasks")
    print("─────────────────────────")

    if not tasks:
        print('  No tasks yet. Add one from the menu.')
        return
    
    for index, task in enumerate(tasks, start = 1):
        print(f'   {index}.{task}')

    print(f'\n   Total: {len(tasks)} taks(s)')


# ---- Complete Task ----
def complete_task():
    """Mark a task as completed and award XP."""
    global total_xp

    print("\n✅ Complete a Task")
    print("─────────────────────────")

    if not tasks:
        print('  No tasks to complete.')
        return
    
    # Show tasks so user can pick one
    view_tasks()

    choice = input("\n➤ Enter task number to complete: ").strip()

    # Validate: is it a number?
    if not choice.isdigit():
        print('[!] Please enter a valid number.')
        return
    
    index = int(choice) - 1    # Convert to 0-based index

    # Validate: is it in range?
    if index < 0 or index >= len(tasks):
        print('[!] Invalid task number.')
        return
    
    task = tasks[index]

    # Validate: is it already done?
    if task.completed:
        print(f'[!] "{task.name}" is already completed.')
        return
    
    task.completed = True
    total_xp += task.xp

    print(f'\n[+] "{task.name}" completed! + {task.xp} XP earned!')
    print(f'     Total XP: {total_xp}')


# ---- Delete Task ----
def delete_task():
    """Remove a task from the tasks list permanently."""
    global total_xp

    print("\n🗑️  Delete a Task")
    print("─────────────────────────")

    if not tasks:
        print('No tasks to delete.')
        return
    
    view_tasks()

    choice = input("\n➤ Enter task number to delete: ").strip()

    if not choice.isdigit():
        print('[!] Please enter a valid number.')
        return
    
    index = int(choice) - 1

    if index < 0 or index >= len(tasks):
        print('[!] Invalid task number.')
        return
    
    task = tasks.pop(index)
    
    # If deleted task was completed, remove its xp
    if task.completed:
        total_xp -= task.xp

    print(f'\n[-] Task "{task.name}" deleted.' )


# ---- Study Session ----
def add_study_session():
    """Ask the user for study session details and save it."""
    print("\n⏱️  Add Study Session")
    print("─────────────────────────")

    subject = input('➤ Subject (e.g., Python, Math): ').strip()

    if not subject:
        print('[!] Subject cannot be empty.')
        return
    
    hours_input = input("➤ Hours studied: ").strip()

    # Validate hours studied
    try:
        hours  = float(hours_input)
    except ValueError:
        print('[!] Hours must be greater than 0.')
        return
    
    # Date: use today if user presses Enter
    date_input = input("➤ Date (YYYY-MM-DD) or press Enter for today: ").strip()

    if date_input:
        date = date_input
    else:
        date = datetime.now().strftime('%Y-%m-%d')

    # Store as a dictionary
    session = {
        'subject': subject,
        'hours': hours,
        'date': date,
    }

    study_sessions.append(session)

    print(f'\n[+] Study session added: {subject} | {hours}h | {date}')


# ---- View Study Sessions ----
def view_study_session():
    """Displays all study sessions and total hours"""
    print("\n📚 Your Study Sessions")
    print("─────────────────────────")

    if not study_sessions:
        print('  No study sessions yet. Add one from the menu.')
        return
    
    total_hours = 0

    for index, session in enumerate(study_sessions, start = 1):
        sub = session['subject']
        hrs = session['hours']
        dt = session['date']
        print(f'   {index}. {sub} | {hrs}h | {dt}')
        total_hours += hrs
    
    print(f'\n   Total hours: {len(study_sessions)} session(s) | {total_hours}s studied')

def print_box_line(text):
    """Helper to print a padded line inside the dashboard box."""
    print(f"│ {text}".ljust(51) + "│")

# ---- View Dashboard ----
def view_dashboard():
    """Displays the full dashboard summary."""
    print("\n╭──────────────────────────────────────────────────╮")
    print("│                    DASHBOARD                     │")
    print("├──────────────────────────────────────────────────┤")

    # User info
    level = profile.get_level(total_xp)
    xp_target = level * UserProfile.XP_PER_LEVEL
    xp_progress = total_xp % UserProfile.XP_PER_LEVEL
    
    # Calculate bar length (20 chars total)
    bar_length = int((xp_progress / UserProfile.XP_PER_LEVEL) * 20)
    bar = "#" * bar_length + "-" * (20 - bar_length)

    print_box_line(f"User:  {profile.name}")
    print_box_line(f"Level: {level}")
    print_box_line(f"XP:    {total_xp} / {xp_target} [{bar}]")
    print_box_line("")

    # Task stats
    completed_count = 0
    for task in tasks:
        if task.completed:
            completed_count += 1

    print_box_line(f"Tasks:     {completed_count} completed / {len(tasks)} total")

    # Study stats
    total_hours = 0
    for session in study_sessions:
        total_hours += session['hours']

    print_box_line(f"Studying:  {total_hours}h across {len(study_sessions)} session(s)")
    print("╰──────────────────────────────────────────────────╯")


# ---- CSV Report ----
def export_csv_report():
    """Export tasks and study sessions to a CSV file."""
    report_file = os.path.join("data", "report.csv")
    try:
        os.makedirs("data", exist_ok=True)
        with open(report_file, "w", newline="") as file:
            writer = csv.writer(file)

        # Section 1: Tasks
            writer.writerow(["=== TASKS ==="])
            writer.writerow(["Name", "Difficulty", "Status", "XP", "Date Created"])

            for task in tasks:
                status = "Completed" if task.completed else "Pending"
                writer.writerow([
                    task.name,
                    task.difficulty.capitalize(),
                    status,
                    task.xp,
                    task.date_created,
                ])

            # Blank row between sections
            writer.writerow([])

            # Section 2: Study Sessions
            writer.writerow(["=== STUDY SESSIONS ==="])
            writer.writerow(["Subject", "Hours", "Date"])

            for session in study_sessions:
                writer.writerow([
                    session["subject"],
                    session["hours"],
                    session["date"],
                ])

            # Blank row then summary
            writer.writerow([])
            writer.writerow(["=== SUMMARY ==="])

            level = profile.get_level(total_xp)
            completed_count = sum(1 for t in tasks if t.completed)
            total_hours = sum(s["hours"] for s in study_sessions)

            writer.writerow(["Total XP", total_xp])
            writer.writerow(["Level", level])
            writer.writerow(["Tasks Completed", f"{completed_count}/{len(tasks)}"])
            writer.writerow(["Total Study Hours", total_hours])

        print(f"\n[+] CSV report exported to: {report_file}")
    except (IOError, OSError) as error:
        print(f'\n[!] Could not export CSV: {error}')


# ---- Edit Profile ----
def edit_profile():
    """Allow the user to change their profile name."""
    print("\n👤 Edit Profile")
    print("─────────────────────────")
    
    new_name = input(f"➤ Enter new name (Current: {profile.name}): ").strip()
    
    if new_name:
        profile.name = new_name
        print(f"\n[+] Name updated to '{profile.name}'!")
    else:
        print("\n[!] Name cannot be empty. No changes made.")


# ---- Handle Choices ----
def handle_choices(choice):
    """Process the user's menu selection."""
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        add_study_session()
    elif choice == "6":
        view_study_session()
    elif choice == "7":
        view_dashboard()
    elif choice == "8":
        export_csv_report()
    elif choice == "9":
        edit_profile()
    elif choice == "0":
        save_data(profile, tasks, study_sessions, total_xp)
        print("\nGoodbye! Keep growing!")
        return False
    else:
        print("\n[!] Invalid choice. Please enter a number from 0 to 9.")

    input("\nPress Enter to continue...")
    return True


# ---- Main Program ----
def main():
    """Main function that runs the Growify application."""
    global profile, tasks, study_sessions, total_xp

    clear_screen()
    print("╭──────────────────────────────────────────────────╮")
    print("│               Welcome to GrowthOS                │")
    print("│         Your Personal Learning Dashboard         │")
    print("╰──────────────────────────────────────────────────╯")

    saved = load_data()

    if saved:
        profile = UserProfile(saved['profile']['name'])
        tasks = restore_tasks(saved['tasks'])
        study_sessions = saved['study_sessions']
        total_xp = saved['total_xp']
        print(f"\n✨ Welcome back, {profile.name}!")
        print(f"   Level {profile.get_level(total_xp)} | {total_xp} XP | {len(tasks)} task(s)")
    else:
        name = input("\n➤ Enter your name: ").strip()

        if not name:
            name = 'Echo'
        profile = UserProfile(name)
    
        print(f"\n✨ Hello, {profile.name}! Let's grow today.")

    input("\nPress Enter to start...")

    running = True

    try:
        while running:
            show_menu()
            choice = input("➤ Choice: ")
            running = handle_choices(choice)
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user (Ctrl+C). Saving data and exiting...")
        save_data(profile, tasks, study_sessions, total_xp)

if __name__ == '__main__':
    main()